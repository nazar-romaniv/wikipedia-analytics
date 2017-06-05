from modules import request_handler
from modules import page_parser
from modules import top


def main():
    view_top = top.Top('views')
    size_top = top.Top('size')
    parser = page_parser.PageParser()
    requests = request_handler.RequestHandler()

    while True:
        requests.new_read()
        next_page = parser.add_pages()
        if next_page is False:
            print('Done')
            break
        print(next_page)
        requests.params['gapfrom'] = next_page

main()
