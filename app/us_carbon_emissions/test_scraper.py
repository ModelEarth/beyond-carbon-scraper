import unittest
import app.us_carbon_emissions.scraper

class TextCleanerFunction(unittest.TestCase):
    def test_cleaner_removes_newlines(self):
        got = app.us_carbon_emissions.scraper.clean_text("abc\ndef")
        self.assertEqual(got, "abc def")
    def test_cleaner_replaces_nbsp_with_space(self):
        got = app.us_carbon_emissions.scraper.clean_text("abc def")
        self.assertEqual(got, "abc def")
    def test_cleaner_converts_to_float(self):
        got = app.us_carbon_emissions.scraper.clean_text("1.234")
        self.assertEqual(got, 1.234)
    def test_cleaner_converts_to_int(self):
        got = app.us_carbon_emissions.scraper.clean_text("100")
        self.assertEqual(got, 100)
    def test_chunk_function(self):
        got = list(app.us_carbon_emissions.scraper.chunks(["1","2","3","4","5","6"],2))
        self.assertEqual(len(got), 3)
        self.assertEqual(got[0],["1","2"])
        self.assertEqual(got[1],["3","4"])
        self.assertEqual(got[2],["5","6"])
