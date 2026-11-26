"""AST-RI RI-01: local bibliographic source registry."""

from .models import Source, SourceType, SourceValidationError
from .providers import (
    ArxivProvider,
    CrossrefProvider,
    ProviderError,
    ProviderRecord,
    compare_provider_records,
)
from .registry import (
    DuplicateSourceError,
    SourceNotFoundError,
    SourceRegistry,
)

__all__ = [
    "ArxivProvider",
    "CrossrefProvider",
    "DuplicateSourceError",
    "ProviderError",
    "ProviderRecord",
    "Source",
    "SourceNotFoundError",
    "SourceRegistry",
    "SourceType",
    "SourceValidationError",
    "compare_provider_records",
]
