# Web Scraper using Scrapy Framework
import scrapy
from scrapy.crawler import CrawlerProcess
import csv

# Creating Spider Class
class ShadowFoxSpider(scrapy.Spider):

    name = "shadowfox_spider"

    # Website to scrape
    start_urls = [
        "https://www.shadowfox.org.in/"
    ]

    # Parsing webpage content
    def parse(self, response):

        scraped_data = []

        print("Website Title :")
        title = response.css("title::text").get()
        print(title)
        scraped_data.append([title])

        print("\nHeadings Found :")

        # Extracting headings from webpage
        headings = response.css("h1::text, h2::text, h3::text").getall()

        for heading in headings:

            clean_heading = heading.strip()

            if clean_heading:
                print(clean_heading)

                scraped_data.append([clean_heading])

        # Saving scraped data into CSV file
        with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(["Headings"])

            writer.writerows(scraped_data)

        print("\nData saved into scraped_data.csv")

# Running the Scrapy spider
process = CrawlerProcess()

process.crawl(ShadowFoxSpider)

process.start()