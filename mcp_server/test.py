import unittest
from pathlib import Path
from mcp_server.services.parser_service import ParserService

class TestParserService(unittest.TestCase):
    def setUp(self):
        self.parser = ParserService()
        self.test_data_dir = Path(__file__).parent / "test_data"
        self.test_data_dir.mkdir(exist_ok=True)

    def tearDown(self):
        for item in self.test_data_dir.iterdir():
            item.unlink()
        self.test_data_dir.rmdir()

    def test_parse_txt_file_no_rank(self):
        # Step 2: Write a test to confirm the bug.
        # The test will parse a sample text file where a title has no rank
        # and assert that the returned rank is `[]`.
        content = """test_id | Test Platform
No Rank Title"""
        test_file = self.test_data_dir / "test.txt"
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(content)

        titles_by_id, _ = self.parser.parse_txt_file(test_file)
        self.assertEqual(titles_by_id["test_id"]["No Rank Title"]["ranks"], [])

if __name__ == '__main__':
    unittest.main()
