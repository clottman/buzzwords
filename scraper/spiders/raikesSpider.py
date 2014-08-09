from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scraper.items import TextItem
from scrapy.utils.response import get_base_url
import urlparse

class raikesSpider(BaseSpider):
	name = "raikes"
	allowed_domains = ["raikes.unl.edu"]
	start_urls = ["http://raikes.unl.edu"]

	def getText(self, list):
		allItems = []
		for element in list:
			item = TextItem()
			item['text'] = element.xpath('text()').extract()
			allItems.append(item)
		return allItems

	def parse(self, response):
		base_url = get_base_url(response)
		sel = Selector(response)
		sites = sel.xpath('//a')
		items = []
		
		for relativeUrl in sel.xpath('//a/@href').extract():
			wholeUrl = urlparse.urljoin(base_url, relativeUrl)

			# prevents the "meh i'm not unicode" error on pages that don't need processed anyways
			ignoreWords = ['video', 'mp4', 'jpg', 'pdf']
			makeRequest = True
			for word in ignoreWords:
				if word in wholeUrl:
					makeRequest = False
			if makeRequest:
				yield Request(wholeUrl, callback=self.parse)
			
		allPs = sel.xpath('//p')
		allAs = sel.xpath('//a')
		allH1s = sel.xpath('//h1')
		allH2s = sel.xpath('//h2')
		allH3s = sel.xpath('//h3')
		allH4s = sel.xpath('//h4')
		allH5s = sel.xpath('//h5')
		allLis = sel.xpath('//li')
		allSpans = sel.xpath('//span')
		allBlockquotes = sel.xpath('//blockquote')
		
		# elements used to analyze old website
		for item in self.getText(allPs):
			yield item
		for item in self.getText(allAs):
			yield item
		for item in self.getText(allH1s):
			yield item
		for item in self.getText(allH5s):
			yield item

		# added to reflect new website's markup
		for item in self.getText(allH2s):
			yield item
		for item in self.getText(allH3s):
			yield item
		for item in self.getText(allH4s):
			yield item
		for item in self.getText(allLis):
			yield item
		for item in self.getText(allSpans):
			yield item
		for item in self.getText(allBlockquotes):
			yield item