from xml.etree.cElementTree import iterparse, ParseError


class PageParser:

    def __init__(self):
        self.pages = dict()
        self._continue = ''

    def add_pages(self):
        end = True
        gap = False
        for event, elem in iterparse('modules/pages.xml', events=('start', 'end')):
            try:
                if event == 'start':
                    if elem.tag == 'pageviews':
                        views = 0
                elif event == 'end':
                    if elem.tag == 'continue':
                        end = False
                        try:
                            self._continue = elem.attrib['pvipcontinue']
                        except KeyError:
                            self._continue = elem.attrib['gapcontinue']
                            gap = True
                    elif elem.tag == 'pvip':
                        try:
                            views += int(elem.text)
                        except TypeError:
                            pass
                    elif elem.tag == 'page':
                        if elem.attrib['title'] == self._continue.replace('_', ' '):
                            return self._continue
                        page_id = int(elem.attrib['pageid'])
                        try:
                            page = {
                                'size': int(elem.attrib['length']),
                                'views': views
                                }
                        except UnboundLocalError:
                            page = {
                                'size': int(elem.attrib['length']),
                                'views': 0
                                }
                        self.pages[page_id] = page
            except ParseError as e:
                print e.message

        if end:
            print('End')
            return False
        elif gap:
            return self._continue
