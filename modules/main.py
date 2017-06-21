from modules.request_handler import request_handler
from modules.page_parser import parser, views_top, size_top
import os


def save_results(*tops):
    for item in tops:
        with open('results_%s.txt' % item.param, 'w') as f:
            f.write(item.display())
for item in [(10420293, 38679890),
             (25247887, 10318332),
             (44662181, 372541),
             (44076335, 299593),
             (20238168, 247687),
             (45056190, 23330),
             (241267, 22410),
             (37125755, 22189),
             (25143203, 20011),
             (18938265, 18083),
            ]:
    views_top.add(item[1], item[0])

for item in [(27193010, 22663),
             (27690256, 18642),
             (7135302, 17191),
             (2281433, 15794),
             (2281489, 14028),
             (18938265, 13524),
             (12844930, 13419),
             (28789972, 13291),
             (2012940, 13174),
             (28798622, 13062),
            ]:
    size_top.add(item[1], item[0])

request_handler.params['gapfrom'] = '152'


def main():
    try:
        while True:
            request_handler.new_read()
            next_page = parser.add_pages()
            if next_page is False:
                print 'Done'
                break
            print next_page
            request_handler.params['gapfrom'] = next_page

        save_results(views_top, size_top)
    finally:
        views_top.display()
        size_top.display()
        os.remove('modules/pages.xml')

if __name__ == '__main__':
    main()

