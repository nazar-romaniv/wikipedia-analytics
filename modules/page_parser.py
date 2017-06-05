from xml.etree.cElementTree import iterparse


class PageParser:

    def __init__(self):
        self.pages = dict()
        self._continue = ''

    def add_pages(self):
        end = True
        for event, elem in iterparse('pages.xml', events=('start', 'end')):
            if event == 'start':
                if elem.tag == 'pageviews':
                    views = 0
            elif event == 'end':
                if elem.tag == 'continue':
                    end = False
                    self._continue = elem.attrib['pvipcontinue']
                elif elem.tag == 'pvip':
                    views += int(elem.text)
                elif elem.tag == 'page':
                    if elem.attrib['title'] == self._continue.replace('_', ' '):
                        return self._continue
                    page_id = int(elem.attrib['pageid'])
                    page = {'size': int(elem.attrib['length']),
                            'views': views}
                    self.pages[page_id] = page
        if end:
            print('End')
            return False
        else:
            print('Not end')