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
		allH5s = sel.xpath('//h5')
		
		for p in allPs:
			item = TextItem()
			item['text'] = p.xpath('text()').extract()
			yield item   
		for a in allAs:
			item = TextItem()
			item['text'] = a.xpath('text()').extract()
			yield item
		for h1 in allH1s:
			item = TextItem()
			item['text'] = h1.xpath('text()').extract()
			yield item
		for h5 in allH5s:
			item = TextItem()
			item['text'] = h5.xpath('text()').extract()
			yield item
