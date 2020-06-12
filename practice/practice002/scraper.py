"""Scrape yahoo news head line and save result to text.

Todo:
    * Add alert to notice result.
    * Add func to make CSV.
    * Add exception handling.
    
"""
import requests
from bs4 import BeautifulSoup
import re


class Scraper:
    def __init__(self):
        pass

    def scraper(word):
        """Scrape and make text.

            Scrape yahoo news head line by given word.
            Then save the result to text file. ("./news.txt")

        Args:
            word (str): search word for scraping.

        Returns:
            bool: If file is maked (num of results > 0), True.

        """

        url = "https://www.yahoo.co.jp/"
        arr = []

        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
        pickup_links = [elem.attrs['href'] for elem in elems]

        for pickup_link in pickup_links:
            pickup_res = requests.get(pickup_link)
            pickup_soup = BeautifulSoup(pickup_res.text, "html.parser")
            pickup_elem = pickup_soup.find("p", class_="pickupMain_detailLink")

            news_link = pickup_elem.contents[0].attrs['href']
            news_res = requests.get(news_link)
            news_soup = BeautifulSoup(news_res.text, "html.parser")
            detail_text = news_soup.find(class_=re.compile("DetailText"))

            if hasattr(detail_text, "text") and (word in detail_text.text):
                arr.append(news_soup.title.text)
                arr.append("\n")
                arr.append(news_link)
                arr.append("\n")
                arr.append(detail_text.text)
                arr.append("\n\n\n\n")

        if len(arr) == 0:
            return False
        else:
            Scraper.makeFile(arr)
            return True

    def makeFile(arr):
        """Make text file from arr.

        Args:
            arr (array of string): string arr for make text.
        Returns:
            None:

        """

        path = "news.txt"
        s = ""

        for i in arr:
            s = s + i

        with open(path, mode='w') as f:
            f.write(s)

        return None