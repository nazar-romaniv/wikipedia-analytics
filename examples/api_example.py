import requests

#fetching data from main page example
def get_page_data(title):
    params = {
        "action": "query",
        "prop": "revisions|info",
        "rvprop": "content",
        "titles": title,
        "rvlimit": "1",
        "format": "json",
    }

    endpoint = "https://en.wikipedia.org/w/api.php"

    resp = requests.get(endpoint, params=params)

    print resp.text


if __name__ == "__main__":
    get_page_data("Main_Page")
