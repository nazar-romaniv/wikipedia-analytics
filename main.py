from modules import request_handler
from modules import page_parser
from modules import top
import os


def save_results(*tops):
    for item in tops:
        with open('results_%s.txt' % item.param, 'w') as f:
            f.write(item.display())


def main():
    try:
        views_top = top.Top('views')
        size_top = top.Top('size')
        parser = page_parser.PageParser()
        requests = request_handler.RequestHandler()

        while True:
            requests.new_read()
            next_page = parser.add_pages()
            for page_id in parser.pages:
                views_top.add(parser.pages[page_id], page_id)
                size_top.add(parser.pages[page_id], page_id)
            parser.pages.clear()
            if next_page is False:
                print 'Done'
                break
            print next_page
            requests.params['gapfrom'] = next_page

        save_results(views_top, size_top)
    finally:
        views_top.display()
        size_top.display()
        os.remove('modules/pages.xml')

if __name__ == '__main__':
    main()
