"""Deterministic candidate extraction from supplied theoretical-physics text.

This module does not fetch papers, infer scientific truth, or validate arguments.
It identifies text spans that merit human review and preserves exact offsets.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import re
from typing import Iterable


_CLAIM_CUES = re.compile(
    r"\b(?:we show|we prove|we derive|we establish|we find|we obtain|"
    r"our results? (?:show|demonstrate|indicate)|it follows that|"
    r"this implies|therefore|theorem\s+\d|proposition\s+\d|"
    r"corollary\s+\d|is given by|can be written as)\b",
    re.IGNORECASE,
)

# Longest/specific environments first. The outermost full match is retained.
_EQUATION_PATTERN = re.compile(
    r"(?P<environment>\\begin\{(?P<envname>equation\*?|align\*?|"
    r"gather\*?|multline\*?|eqnarray\*?)\}.*?\\end\{(?P=envname)\})"
    r"|(?P<display>\\\[.*?\\\])"
    r"|(?P<dollar>\$\$.*?\$\$)"
    r"|(?P<paren>\\\(.*?\\\))",
    re.DOTALL,
)


@dataclass(frozen=True, slots=True)
class ClaimCandidate:
    claim_id: str
    source_id: str
    text: str
    locator: str
    start_offset: int
    end_offset: int
    line_start: int
    line_end: int
    extraction_method: str = "deterministic_sentence_cue"
    review_status: str = "unreviewed"
    epistemic_status: str = "unclassified_candidate"


@dataclass(frozen=True, slots=True)
class EquationCandidate:
    equation_id: str
    source_id: str
    latex: str
    locator: str
    start_offset: int
    end_offset: int
    line_start: int
    line_end: int
    delimiter: str
    extraction_method: str = "latex_delimiter_scan"
    review_status: str = "unreviewed"
    transcription_status: str = "not_verified"


@dataclass(frozen=True, slots=True)
class ExtractionResult:
    source_id: str
    document_sha256: str
    character_count: int
    line_count: int
    claims: tuple[ClaimCandidate, ...]
    equations: tuple[EquationCandidate, ...]

    def to_dict(self) -> dict:
        """Return a JSON-serializable representation."""
        return {
            "source_id": self.source_id,
            "document_sha256": self.document_sha256,
            "character_count": self.character_count,
            "line_count": self.line_count,
            "claims": [asdict(item) for item in self.claims],
            "equations": [asdict(item) for item in self.equations],
        }


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _stable_id(prefix: str, source_id: str, text: str, start: int) -> str:
    payload = f"{source_id}\0{start}\0{text}".encode("utf-8")
    return f"{prefix}_{hashlib.sha256(payload).hexdigest()[:16]}"


def _sentence_spans(text: str) -> Iterable[tuple[int, int, str]]:
    """Yield conservative sentence spans without normalizing source text."""
    # Sentence punctuation followed by whitespace and a likely sentence start.
    boundary = re.compile(r"(?<=[.!?])(?:[\"')\]]*)\s+(?=[A-Z0-9\\])")
    start = 0
    for match in boundary.finditer(text):
        end = match.start()
        candidate = text[start:end].strip()
        if candidate:
            left = start + len(text[start:end]) - len(text[start:end].lstrip())
            right = start + len(text[start:end].rstrip())
            yield left, right, text[left:right]
        start = match.end()
    tail = text[start:]
    candidate = tail.strip()
    if candidate:
        left = start + len(tail) - len(tail.lstrip())
        right = start + len(tail.rstrip())
        yield left, right, text[left:right]


def extract_candidates(text: str, source_id: str) -> ExtractionResult:
    """Extract candidate claims/equations from caller-supplied plain text.

    Offsets are zero-based, end-exclusive Python character offsets into the
    exact input string. Line numbers are one-based. No PDF/OCR conversion is
    performed here; the caller must retain any upstream page mapping.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not source_id or not source_id.strip():
        raise ValueError("source_id must be a non-empty stable source identifier.")
    if not text.strip():
        raise ValueError("text must not be empty.")

    claims: list[ClaimCandidate] = []
    for start, end, sentence in _sentence_spans(text):
        if not _CLAIM_CUES.search(sentence):
            continue
        claims.append(ClaimCandidate(
            claim_id=_stable_id("clm", source_id, sentence, start),
            source_id=source_id,
            text=sentence,
            locator=f"lines { _line_number(text, start) }-{ _line_number(text, end) }",
            start_offset=start,
            end_offset=end,
            line_start=_line_number(text, start),
            line_end=_line_number(text, end),
        ))

    equations: list[EquationCandidate] = []
    for match in _EQUATION_PATTERN.finditer(text):
        raw = match.group(0)
        if match.group("environment"):
            delimiter = f"environment:{match.group('envname')}"
        elif match.group("display"):
            delimiter = r"\[...\]"
        elif match.group("dollar"):
            delimiter = "$$...$$"
        else:
            delimiter = r"\(...\)"
        start, end = match.span()
        equations.append(EquationCandidate(
            equation_id=_stable_id("eq", source_id, raw, start),
            source_id=source_id,
            latex=raw,
            locator=f"lines { _line_number(text, start) }-{ _line_number(text, end) }",
            start_offset=start,
            end_offset=end,
            line_start=_line_number(text, start),
            line_end=_line_number(text, end),
            delimiter=delimiter,
        ))

    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return ExtractionResult(
        source_id=source_id,
        document_sha256=digest,
        character_count=len(text),
        line_count=text.count("\n") + 1,
        claims=tuple(claims),
        equations=tuple(equations),
    )
