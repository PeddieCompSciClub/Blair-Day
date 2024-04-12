from encodings import utf_8
from bs4 import BeautifulSoup as bs
import requests

# https://www.thepythoncode.com/article/extract-weather-data-python
file = open("weather.txt", "w", encoding="utf-8")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"


def get_weather_data(url):
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    session.headers["Accept-Language"] = LANGUAGE
    session.headers["Content-Language"] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")

    result = {}
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    result["temp_now"] = soup.find("span", attrs={"id": "wob_tm"}).text
    result["weather_img"] = "https:" + soup.find("img", attrs={"id": "wob_tci"})["src"]
    result["humidity"] = soup.find("span", attrs={"id": "wob_hm"}).text
    result["wind"] = soup.find("span", attrs={"id": "wob_ws"}).text
    return result


if __name__ == "__main__":
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather+Hightstown+NJ"
    import argparse

    parser = argparse.ArgumentParser(
        description="Quick Script for Extracting Weather data using Google Weather"
    )
    parser.add_argument(
        "region",
        nargs="?",
        help="""Region to get weather for, must be available region.
                                        Default is your current location determined by your IP Address""",
        default="",
    )
    # parse arguments
    args = parser.parse_args()
    region = args.region
    URL += region
    # get data
    data = get_weather_data(URL)
    file.write(f"{data['temp_now']}\u2109\n")
    file.write(f"{data['weather_now']}\n")
    file.write(f"Humidity: {data['humidity']}\n")
    file.write(f"Wind: {data['wind']}")
    open('weather.png', 'wb').write(requests.get(data["weather_img"], allow_redirects=True).content)

    file.close()

#debugging:
print(__file__)
