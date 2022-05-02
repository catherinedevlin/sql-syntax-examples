# sql-syntax-examples
SQL query syntax scraped from database docs, plus the scraper

Currently scraping from 

- https://www.postgresql.org/docs/current/

To re-scrape

    cd scrape_docs 
    scrapy crawl postgresql -O postgresql.json
    