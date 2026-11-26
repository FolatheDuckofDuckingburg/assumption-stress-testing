"""AST-RI RI-01: local bibliographic source registry and review tools."""

from .arxiv_search import (
    ALLOWED_ARXIV_CATEGORIES,
    ArxivSearchPage,
    ArxivSearchProvider,
    ArxivSearchValidationError,
    SearchProvenance,
    build_arxiv_search_query,
)
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
from .relevance import (
    RelevanceQueueItem,
    RelevanceReview,
    RelevanceReviewStore,
    RelevanceStatus,
)

__all__ = [
    "ALLOWED_ARXIV_CATEGORIES",
    "ArxivProvider",
    "ArxivSearchPage",
    "ArxivSearchProvider",
    "ArxivSearchValidationError",
    "CrossrefProvider",
    "DuplicateSourceError",
    "ProviderError",
    "ProviderRecord",
    "RelevanceQueueItem",
    "RelevanceReview",
    "RelevanceReviewStore",
    "RelevanceStatus",
    "SearchProvenance",
    "Source",
    "SourceNotFoundError",
    "SourceRegistry",
    "SourceType",
    "SourceValidationError",
    "build_arxiv_search_query",
    "compare_provider_records",
]
