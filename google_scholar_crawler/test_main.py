import unittest
from main import parse_citation_count


class CitationParsingTests(unittest.TestCase):
    def test_selects_total_instead_of_recent_citations_or_h_index(self):
        document = '''<td class="gsc_rsb_std">999</td>
        <table id="gsc_rsb_st"><tr><td>Citations</td>
        <td class="gsc_rsb_std">1,234</td><td class="gsc_rsb_std">125</td></tr>
        <tr><td>h-index</td><td class="gsc_rsb_std">9</td></tr></table>'''
        self.assertEqual(parse_citation_count(document), 1234)

    def test_zero_is_a_valid_total(self):
        self.assertEqual(parse_citation_count(
            '<table id="gsc_rsb_st"><td class="gsc_rsb_std">0</td></table>'), 0)

    def test_challenge_page_and_invalid_data_do_not_become_zero(self):
        for document in [
            '<html>Our systems have detected unusual traffic</html>',
            '<table id="gsc_rsb_st"><td class="gsc_rsb_std">Unavailable</td></table>',
        ]:
            with self.subTest(document=document), self.assertRaises(ValueError):
                parse_citation_count(document)


if __name__ == "__main__":
    unittest.main()
