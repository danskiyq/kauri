import requests
import html_to_json


def get_json_response(url: str):
    response = requests.get(url,
                            timeout=1)
    response.raise_for_status()
    return html_to_json.convert_html.convert(response.text)


if __name__ == '__main__':
    link = 'https://kauri.one/'
    print(get_json_response(link))
