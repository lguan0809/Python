import unittest
from pathlib import Path


class TestGenerateTakeoutSkill(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill_path = Path(__file__).parent.parent / "skills" / "generate_takeout" / "SKILL.md"
        assert cls.skill_path.exists(), f"SKILL.md not found at {cls.skill_path}"
        cls.text = cls.skill_path.read_text(encoding="utf-8")

    def test_title_present(self):
        self.assertIn("Skill: generate_takeout_notes", self.text)

    def test_python_grammar_section(self):
        self.assertTrue(
            "Python Grammar" in self.text or "Python Grammar (detailed)" in self.text,
            "Python Grammar section missing",
        )

    def test_behavior_steps_present(self):
        self.assertIn("Behavior / Steps the agent must follow", self.text)

    def test_contributing_check(self):
        # skill should require checking CONTRIBUTING.md
        self.assertIn("CONTRIBUTING.md", self.text)

    def test_algorithm_requirements(self):
        # ensure algorithm detail requirements are present
        self.assertIn("recurrence", self.text.lower())
        self.assertIn("memoization", self.text.lower())
        self.assertIn("iterative", self.text.lower())


if __name__ == "__main__":
    unittest.main()
