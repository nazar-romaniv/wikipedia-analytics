from xml.etree.cElementTree import iterparse, ParseError
import top

views_top = top.Top("views")
size_top = top.Top("size")



class PageParser:

    def __init__(self):
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
                            size_top.add(int(elem.attrib['length']), page_id)
                            views_top.add(views, page_id)
                        except KeyError:
                            views_top.add(views, page_id)
                        except UnboundLocalError:
                            pass
               
            except ParseError as e:
                print e.message

        if end:
            print('End')
            return False
        elif gap:
            print 'Gap!!!!!!!!!!!!!!!!!!!!!'
            return self._continue


parser = PageParser()

