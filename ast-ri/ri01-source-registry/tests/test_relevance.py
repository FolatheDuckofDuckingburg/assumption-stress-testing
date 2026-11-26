import tempfile
import unittest
from pathlib import Path

from ast_ri_source_registry import Source, SourceRegistry
from ast_ri_source_registry.relevance import RelevanceReviewStore, RelevanceStatus


class RelevanceReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = Path(self.temp_dir.name) / "registry.sqlite3"
        self.registry = SourceRegistry(self.database)
        self.source = self.registry.add_source(Source(
            title="A theoretical physics paper",
            authors=("A. Author",),
            arxiv_id="2301.01234",
        ))
        self.reviews = RelevanceReviewStore(self.registry)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_unreviewed_sources_default_to_uncertain_queue(self):
        queue = self.reviews.list_queue(self.registry)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue[0].status, RelevanceStatus.UNCERTAIN)
        self.assertIsNone(queue[0].assessor)

    def test_review_changes_queue_and_history_is_preserved(self):
        first = self.reviews.record_review(
            self.source.source_id, RelevanceStatus.IN_SCOPE,
            "The work develops a quantum-gravity model.", "human-reviewer-1"
        )
        second = self.reviews.record_review(
            self.source.source_id, RelevanceStatus.UNCERTAIN,
            "Scope requires checking the paper's central results.", "human-reviewer-1"
        )
        self.assertNotEqual(first.reviewed_at, "")
        self.assertEqual(self.reviews.current_review(self.source.source_id), second)
        self.assertEqual(len(self.reviews.list_queue(self.registry)), 1)
        self.assertEqual(
            self.reviews.list_queue(self.registry, status=RelevanceStatus.IN_SCOPE), []
        )

    def test_review_requires_rationale_and_assessor(self):
        with self.assertRaises(ValueError):
            self.reviews.record_review(
                self.source.source_id, RelevanceStatus.IN_SCOPE, " ", "reviewer"
            )
        with self.assertRaises(ValueError):
            self.reviews.record_review(
                self.source.source_id, RelevanceStatus.IN_SCOPE, "Reason", " "
            )


if __name__ == "__main__":
    unittest.main()
