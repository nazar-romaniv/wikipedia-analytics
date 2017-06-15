import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'modules')))
from top import Top
from page_parser import views_top, PageParser


class TestParser(unittest.TestCase):

    def setUp(self):
        try:
            os.mkdir('modules')
        except OSError:
            pass
        with open('modules/pages.xml', 'w') as xml:
            xml.write(sample_xml)
        self.parser = PageParser()
        self.parser.add_pages()

    def tearDown(self):
        os.remove('modules/pages.xml')
        os.rmdir('modules')
        del self.parser
        views_top._clear((0, 0))

    def test_add_continue(self):
        self.assertTrue(self.parser._continue == '!!!')

    def test_parsing(self):
        new_top = Top('views')
        new_top.add(166, 5878274)
        new_top.add(123, 3632887)
        new_top.display()
        views_top.display()
        self.assertTrue(new_top == views_top)


sample_xml = """<?xml version="1.0"?>
<api batchcomplete="">
<continue gapcontinue="!!!" continue="gapcontinue||" />
<query>
<pages>
<page pageid="5878274" title="aaa" pagelanguagedir="ltr" touched="2017-05-11T07:54:10Z" lastrevid="732538600" length="84">
<pageviews>
<pvip date="2017-03-26" xml:space="preserve">82</pvip>
<pvip date="2017-03-27" xml:space="preserve">55</pvip>
<pvip date="2017-03-28" xml:space="preserve">29</pvip>
</pageviews>
</page>
<page pageid="3632887" title="bbb" pagelanguage="en" touched="2017-05-19T01:50:45Z" lastrevid="780817488" length="1242">
<pageviews><pvip date="2017-03-26" xml:space="preserve">123</pvip>
</pageviews></page></pages></query>
</api>
"""


if __name__ == '__main__':
    unittest.main(verbosity=2)
