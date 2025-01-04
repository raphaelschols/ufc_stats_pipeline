import scrapy


class UfcSpider(scrapy.Spider):
    name = "ufc_spider"
    allowed_domains = ["www.ufcstats.com"]
    start_urls = ["http://www.ufcstats.com/statistics/events/completed?page=all"]

    def parse(self, response):
        """
        Parse event data from the main event listing page and trigger fighter data requests.
        """

        # Loop through each event row on the page
        for event in response.css("tr.b-statistics__table-row"):
                            
                event_name = event.css("a.b-link.b-link_style_black::text").get()
                event_date =  event.css("span.b-statistics__date::text").get()
                event_location =  event.css(
                    "td.b-statistics__table-col.b-statistics__table-col_style_big-top-padding::text"
                ).get()

                # Yield the event data
                yield {
                    "name": event_name,
                    "date": event_date,
                    "location": event_location
                }