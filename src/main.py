import argparse
from crawler import Crawler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="doc", add_help=True)
    parser.add_argument(
        "--domains",
        "-d",
        type=str,
        help="comma-separated domain names to crawl",
    )
    parser.add_argument("--crawl", "-c", action="store_true", help="crawl the domain")

    args = parser.parse_args()

    if args.domains:
        domains = args.domains.split(",")
    else:
        file = open("domains.txt", "r")
        domains = file.read().splitlines()

    if args.crawl:
        crawler = Crawler(domains)
        crawler.crawl()
