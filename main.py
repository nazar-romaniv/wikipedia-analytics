from modules.request_handler import request_handler
from modules.page_parser import parser, views_top, size_top
import os


def save_results(*tops):
    for item in tops:
        with open('results_%s.txt' % item.param, 'w') as f:
            f.write(item.display())


def main():
    try:
        while True:
            request_handler.new_read()
            next_page = parser.add_pages()
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

