from datetime import datetime

import requests
import selectorlib
import time

# the url that will be scraped
URL = "https://programmer100.pythonanywhere.com"


# gather intell/ data from the url
def scrape_url(url):
    response = requests.get(url)
    text_response = response.text
    return text_response


# extracts the data from the yaml file that is connected to the css id
def extract_text(text_response):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(text_response)["temp"]
    return value


def extracted_data(extract):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    file_path = "temp_data.txt"
    with open(file_path, 'a+') as file:
        line = f"{now},{extract}\n"
        file.write(line)


if __name__ == "__main__":
    while True:
        scrape_source = scrape_url(URL)
        extract = extract_text(scrape_source)
        extracted_data(extract)
        time.sleep(2)
