import unittest

from ast_ri_extraction.assumptions import AssumptionKind, AssumptionRecord


class AssumptionRecordTests(unittest.TestCase):
    def test_explicit_assumption_requires_source_evidence(self):
        record = AssumptionRecord.create(
            source_id="src_gr",
            statement="The spacetime is asymptotically flat.",
            kind=AssumptionKind.EXPLICIT,
            locator="Section 2, paragraph 1",
            evidence_quote="We assume asymptotic flatness.",
            affected_claim_ids=("clm_123",),
        )
        self.assertEqual(record.kind, AssumptionKind.EXPLICIT)
        self.assertEqual(record.review_status, "unreviewed")
        self.assertEqual(record.affected_claim_ids, ("clm_123",))
        self.assertEqual(record.to_dict()["kind"], "explicit")

    def test_inferred_assumption_requires_rationale(self):
        with self.assertRaises(ValueError):
            AssumptionRecord.create(
                source_id="src_gr",
                statement="A smoothness condition is used.",
                kind=AssumptionKind.INFERRED,
                locator="Equation 4",
                evidence_quote="The derivative is taken twice.",
            )

    def test_inferred_assumption_records_why_it_was_inferred(self):
        record = AssumptionRecord.create(
            source_id="src_gr",
            statement="The field is assumed differentiable in this derivation.",
            kind=AssumptionKind.INFERRED,
            locator="Page 3, paragraph 2",
            evidence_quote="Taking the second derivative gives...",
            rationale="The displayed operation requires differentiability, but the paper does not state it as a separate assumption.",
        )
        self.assertEqual(record.kind, AssumptionKind.INFERRED)
        self.assertIn("does not state", record.rationale)

    def test_missing_locator_or_quote_is_rejected(self):
        base = dict(
            source_id="src",
            statement="A condition.",
            kind=AssumptionKind.EXPLICIT,
            locator="Section 1",
            evidence_quote="We assume a condition.",
        )
        with self.assertRaises(ValueError):
            AssumptionRecord.create(**{**base, "locator": " "})
        with self.assertRaises(ValueError):
            AssumptionRecord.create(**{**base, "evidence_quote": " "})

    def test_ids_are_deterministic(self):
        args = dict(
            source_id="src",
            statement="Metric compatibility holds.",
            kind=AssumptionKind.EXPLICIT,
            locator="Equation 2",
            evidence_quote="We impose metric compatibility.",
        )
        self.assertEqual(
            AssumptionRecord.create(**args).assumption_id,
            AssumptionRecord.create(**args).assumption_id,
        )


if __name__ == "__main__":
    unittest.main()
