import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'modules')))
import page_parser


class TestParser(unittest.TestCase):

    def setUp(self):
        with open('pages.xml', 'w') as xml:
            xml.write(sample_xml)
        self.parser = page_parser.PageParser()
        self.parser.add_pages()

    def tearDown(self):
        os.remove('../modules/pages.xml')
        del self.parser

    def test_add_continue(self):
        self.assertTrue(self.parser._continue == '!!!')

    def test_parsing(self):
        expected = {5878274: {'size': 84, 'views': 166},
                    3632887: {'size': 1242, 'views': 123}}
        actual = self.parser.pages
        self.assertEqual(expected, actual)


sample_xml = """<?xml version="1.0"?>
<api batchcomplete="">
<continue pvipcontinue="!!!" continue="gapcontinue||" />
<query>
<pages>
<page pageid="5878274" pagelanguagedir="ltr" touched="2017-05-11T07:54:10Z" lastrevid="732538600" length="84">
<pageviews>
<pvip date="2017-03-26" xml:space="preserve">82</pvip>
<pvip date="2017-03-27" xml:space="preserve">55</pvip>
<pvip date="2017-03-28" xml:space="preserve">29</pvip>
</pageviews>
</page>
<page pageid="3632887" pagelanguage="en" touched="2017-05-19T01:50:45Z" lastrevid="780817488" length="1242">
<pageviews><pvip date="2017-03-26" xml:space="preserve">123</pvip>
</pageviews></page></pages></query>
</api>
"""

if __name__ == '__main__':
    unittest.main(verbosity=2)
