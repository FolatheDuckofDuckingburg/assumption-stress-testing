"""AST-RI RI-02: provenance-preserving candidate extraction."""

from .extractor import (
    ClaimCandidate,
    EquationCandidate,
    ExtractionResult,
    extract_candidates,
)

__all__ = [
    "ClaimCandidate",
    "EquationCandidate",
    "ExtractionResult",
    "extract_candidates",
]
