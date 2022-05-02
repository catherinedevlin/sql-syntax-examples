import scrapy


def is_wanted(sql):
    if len(sql) < 10:
        return False
    if "..." in sql:
        return False
    return True


class PostgresqlSpider(scrapy.Spider):
    name = "postgresql"

    start_urls = [
        "https://www.postgresql.org/docs/current/",
    ]

    def parse(self, response):
        self.log(f"Scraping {response.url}")

        for snippet in response.css("pre.programlisting::text"):
            txt = snippet.get()
            if is_wanted(txt):
                yield {"sql": snippet.get(), "source": response.url}

        for chapter_url in response.css(
            "span.chapter a::attr(href), span.sect1 a::attr(href)"
        ).getall():
            chapter_link = response.urljoin(chapter_url)
            yield scrapy.Request(chapter_link, callback=self.parse)
