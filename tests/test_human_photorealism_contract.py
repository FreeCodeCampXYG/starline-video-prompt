import unittest
from pathlib import Path


class HumanPhotorealismContractTests(unittest.TestCase):
    def test_contract_covers_identity_and_safety_boundaries(self):
        contract = Path("references/human-photorealism-contract.md").read_text(encoding="utf-8")
        self.assertIn("成年角色", contract)
        self.assertIn("不得模仿明星", contract)
        self.assertIn("资产图", contract)
        self.assertIn("剧情抓拍", contract)


if __name__ == "__main__":
    unittest.main()
