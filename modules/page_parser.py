from xml.etree.cElementTree import iterparse


class PageParser:

    def __init__(self):
        self.pages = dict()

    def add_pages(self):
        for event, elem in iterparse('pages.xml', events=('start', 'end')):
            if event == 'start':
                if elem.tag == 'pageviews':
                    views = 0
            elif event == 'end':
                if elem.tag == 'continue':
                    self._continue = elem.attrib['pvipcontinue'].replace('_', ' ')
                elif elem.tag == 'pvip':
                    views += int(elem.text)
                elif elem.tag == 'page':
                    if elem.attrib['title'] == self._continue:
                        return self._continue
                    page_id = int(elem.attrib['pageid'])
                    page = {'size': int(elem.attrib['length']),
                            'views': views}
                    self.pages[page_id] = page
