from xml.etree.cElementTree import iterparse


class PageParser:

    def __init__(self):
        self.pages = dict()

    def add_pages(self):
        for elem, event in iterparse('pages.xml', events=('start', 'end')):
            if event == 'start':
                if elem.tag == 'pageviews':
                    views = 0
            elif event == 'end':
                if elem.tag == 'continue':
                    self._continue = elem.attrib['gapcontinue']
                elif elem.tag == 'pvip':
                    views += int(elem.text)
                elif elem.tag == 'page':
                    page = {'id': int(elem.attrib['pageid']),
                            'size': int(elem.attrib['length']),
                            'views': views}
                    self.pages[page['id']] = page