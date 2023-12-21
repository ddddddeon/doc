import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Crawler:
    def __init__(self, domains):
        self.domains = domains
        self.visited = set()

    def sanitize_url(self, url):
        if url in self.visited:
            return None

        if not re.match(r"http(s)?://[a-zA-Z0-9]", url):
            return self.sanitize_url(f"https://{url}")

        for domain in self.domains:
            if domain in url:
                return url

        return None

    def scrape(self, url):
        url = self.sanitize_url(url)
        if not url:
            return

        response = requests.get(url)
        self.visited.add(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # do the stuff
            print(f"{len(self.visited)} - {soup.title.text}")
            # print(soup.get_text())

            links = soup.find_all("a")
            for link in links:
                href = link.get("href")
                if href:
                    absolute_url = urljoin(url, href)
                    self.scrape(absolute_url)

    def crawl(self):
        for domain in self.domains:
            first = len(self.visited)
            print(f"* Crawling domain: {domain}")
            self.scrape(domain)
            print(f"* Crawled {len(self.visited) - first} pages")
        print(f"* Crawled {len(self.visited)} pages total")
