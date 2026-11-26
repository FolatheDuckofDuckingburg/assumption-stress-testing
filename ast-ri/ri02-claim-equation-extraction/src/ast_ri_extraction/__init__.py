"""AST-RI RI-02: provenance-preserving candidate extraction and records."""

from .assumptions import AssumptionKind, AssumptionRecord
from .extractor import (
    ClaimCandidate,
    EquationCandidate,
    ExtractionResult,
    extract_candidates,
)

__all__ = [
    "AssumptionKind",
    "AssumptionRecord",
    "ClaimCandidate",
    "EquationCandidate",
    "ExtractionResult",
    "extract_candidates",
]
