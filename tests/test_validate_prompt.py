import tempfile
import unittest
from pathlib import Path

from scripts.validate_prompt import prompt_body


class PromptBodyTests(unittest.TestCase):
    def test_extracts_text_block(self):
        self.assertEqual(prompt_body("```text\nhello\n```"), "hello")

    def test_plain_text_is_preserved(self):
        self.assertEqual(prompt_body("  hello  "), "hello")


class StoryFacingContractTests(unittest.TestCase):
    def test_story_facing_prompt_has_no_framework_label(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "prompt.md"
            path.write_text("A timed scene with a stable end frame.", encoding="utf-8")
            self.assertNotIn("STAR", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
