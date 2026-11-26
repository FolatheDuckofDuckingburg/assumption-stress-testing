import hashlib
import unittest

from ast_ri_extraction import extract_candidates


class ExtractionTests(unittest.TestCase):
    def test_claim_candidates_preserve_exact_sentence_and_locator(self):
        text = (
            "We consider a spacetime with metric g.\n"
            "We show that the solution is unique under the stated boundary conditions.\n"
            "This paragraph describes the setup."
        )
        result = extract_candidates(text, "src_example")
        self.assertEqual(len(result.claims), 1)
        claim = result.claims[0]
        self.assertEqual(
            claim.text,
            "We show that the solution is unique under the stated boundary conditions."
        )
        self.assertEqual(claim.line_start, 2)
        self.assertEqual(claim.review_status, "unreviewed")
        self.assertEqual(claim.epistemic_status, "unclassified_candidate")
        self.assertEqual(text[claim.start_offset:claim.end_offset], claim.text)

    def test_equations_preserve_latex_and_offsets(self):
        text = (
            "The field equation is\n"
            r"\[ G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T_{\mu\nu} \]"
            "\nwhich we use below."
        )
        result = extract_candidates(text, "src_gr")
        self.assertEqual(len(result.equations), 1)
        equation = result.equations[0]
        self.assertEqual(equation.latex, r"\[ G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T_{\mu\nu} \]")
        self.assertEqual(text[equation.start_offset:equation.end_offset], equation.latex)
        self.assertEqual(equation.line_start, 2)
        self.assertEqual(equation.transcription_status, "not_verified")

    def test_supports_equation_environment_and_inline_math(self):
        text = (
            r"Inline relation \( E = mc^2 \)."
            "\n"
            r"\begin{equation}a^2+b^2=c^2\end{equation}"
        )
        result = extract_candidates(text, "src_math")
        self.assertEqual(len(result.equations), 2)
        self.assertEqual(result.equations[0].delimiter, r"\(...\)")
        self.assertEqual(result.equations[1].delimiter, "environment:equation")

    def test_hash_is_of_exact_input(self):
        text = "A source passage."
        result = extract_candidates(text, "src_hash")
        self.assertEqual(
            result.document_sha256,
            hashlib.sha256(text.encode("utf-8")).hexdigest()
        )

    def test_rejects_empty_text_and_missing_source(self):
        with self.assertRaises(ValueError):
            extract_candidates("  ", "src")
        with self.assertRaises(ValueError):
            extract_candidates("A sentence.", " ")

    def test_offsets_are_stable_and_end_exclusive(self):
        text = "We prove a result.\n"
        first = extract_candidates(text, "src")
        second = extract_candidates(text, "src")
        self.assertEqual(first.claims[0].claim_id, second.claims[0].claim_id)
        claim = first.claims[0]
        self.assertEqual(text[claim.start_offset:claim.end_offset], claim.text)
        self.assertGreater(claim.end_offset, claim.start_offset)


if __name__ == "__main__":
    unittest.main()
