# -*- coding: utf-8 -*-
import scrapy


class SuumoHousingSpider(scrapy.Spider):
    name = 'suumo_housing'
    allowed_domains = ['suumo.jp']
    start_urls = [
        'https://suumo.jp/chintai/__JJ_FR301FC001_arz1030z2bsz1040z2tcz10401303z2tcz10401304.html']

    def parse(self, response):
        listings = response.xpath('//*[@class="cassetteitem"]')
        for listing in listings:

            # initial block
            title = listing.xpath(
                './/*[@class="cassetteitem_content-title"]/text()').extract_first()
            area = listing.xpath(
                './/*[@class="cassetteitem_detail-col1"]/text()').extract_first()
            distances = listing.xpath(
                './/*[@class="cassetteitem_detail-col2"]/div/text()').extract()
            building_age = listing.xpath(
                './/*[@class="cassetteitem_detail-col3"]/div[1]/text()').extract_first()
            stories_tall = listing.xpath(
                './/*[@class="cassetteitem_detail-col3"]/div[2]/text()').extract_first()

            # int for number of listings
            number_of_listings = len(listing.xpath(
                './/*[@class="js-cassette_link"]'))

            # listing information
            for i in range(0, number_of_listings):
                raw_floor = listing.xpath(
                    './/*[@class="js-cassette_link"]/td[3]/text()').extract()
                floor = (str(raw_floor[0])).strip()

                raw_price = listing.xpath(
                    './/span[@class="cassetteitem_price cassetteitem_price--rent"]/span/text()').extract()
                price = raw_price[i]

                raw_administrative_cost = listing.xpath(
                    './/span[@class="cassetteitem_price cassetteitem_price--administration"]/text()').extract()
                administrative_cost = raw_administrative_cost[i]

                raw_deposit = listing.xpath(
                    './/span[@class="cassetteitem_price cassetteitem_price--deposit"]/text()').extract()
                deposit = raw_deposit[i]

                raw_gratuity = listing.xpath(
                    './/span[@class="cassetteitem_price cassetteitem_price--gratuity"]/text()').extract()
                gratuity = raw_gratuity[i]

                raw_rooms = listing.xpath(
                    './/span[@class="cassetteitem_madori"]/text()').extract()
                rooms = raw_rooms[i]

                raw_sqmeters = listing.xpath(
                    './/span[@class="cassetteitem_menseki"]/text()').extract()
                sqmeters = raw_sqmeters[i]

                links = listing.xpath(
                    './/*[@class="ui-text--midium ui-text--bold"]/a/@href').extract()

                raw_absolutelinks = []

                for link in links:
                    raw_absolutelinks.append(response.urljoin(link))
                absolutelink = raw_absolutelinks[i]

                yield {'Listing Title': title,
                       'Area': area,
                       'Distances to Railway Stations': distances,
                       'Building Age': building_age,
                       'Stories Tall': stories_tall,
                       'Floor': floor,
                       'Price': price,
                       'Administrative Costs': administrative_cost,
                       'Deposit': deposit,
                       'Gratuity': gratuity,
                       'Rooms': rooms,
                       'Square Meters': sqmeters,
                       'Links to Listing': absolutelink}
