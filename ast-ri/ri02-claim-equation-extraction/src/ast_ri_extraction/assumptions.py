"""Human-authored assumption records with explicit/inferred provenance."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
import hashlib


class AssumptionKind(str, Enum):
    EXPLICIT = "explicit"
    INFERRED = "inferred"


@dataclass(frozen=True, slots=True)
class AssumptionRecord:
    """A reviewable assumption linked to source evidence and affected claims.

    This record is authored by a researcher, not generated automatically.
    "Explicit" means the cited passage states the assumption; it does not
    establish that the assumption is justified or physically correct.
    """

    assumption_id: str
    source_id: str
    statement: str
    kind: AssumptionKind
    locator: str
    evidence_quote: str
    rationale: str
    affected_claim_ids: tuple[str, ...] = ()
    review_status: str = "unreviewed"

    @classmethod
    def create(
        cls,
        *,
        source_id: str,
        statement: str,
        kind: AssumptionKind,
        locator: str,
        evidence_quote: str,
        rationale: str = "",
        affected_claim_ids: tuple[str, ...] = (),
    ) -> "AssumptionRecord":
        if not source_id or not source_id.strip():
            raise ValueError("source_id must be a non-empty stable source identifier.")
        statement = statement.strip()
        locator = locator.strip()
        evidence_quote = evidence_quote.strip()
        rationale = rationale.strip()
        if not statement:
            raise ValueError("Assumption statement is required.")
        if not locator:
            raise ValueError("A source locator is required.")
        if not evidence_quote:
            raise ValueError("An evidence quote is required.")
        try:
            normalized_kind = AssumptionKind(kind)
        except ValueError as exc:
            raise ValueError(f"Unsupported assumption kind: {kind!r}") from exc
        if normalized_kind is AssumptionKind.INFERRED and not rationale:
            raise ValueError("Inferred assumptions require an explicit rationale.")
        if any(not claim_id.strip() for claim_id in affected_claim_ids):
            raise ValueError("Affected claim identifiers must be non-empty.")
        payload = (
            f"{source_id}\0{statement}\0{normalized_kind.value}\0"
            f"{locator}\0{evidence_quote}"
        ).encode("utf-8")
        assumption_id = "asm_" + hashlib.sha256(payload).hexdigest()[:16]
        return cls(
            assumption_id=assumption_id,
            source_id=source_id,
            statement=statement,
            kind=normalized_kind,
            locator=locator,
            evidence_quote=evidence_quote,
            rationale=rationale,
            affected_claim_ids=tuple(affected_claim_ids),
        )

    def to_dict(self) -> dict:
        data = asdict(self)
        data["kind"] = self.kind.value
        return data
