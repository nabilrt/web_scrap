import scrapy

class TrueSpider(scrapy.Spider):
    name='truecar'

    def start_requests(self):
        url=['https://www.imdb.com/search/title/?genres=Thriller&ref_=nv_sr_srsg_0']

        for u in url:
            yield scrapy.Request(u, callback=self.parse) 


    def parse(self,response):
        all_names=response.css('div.lister-item')

        for element in all_names:
            movie_data={
            'movie_name':element.css('h3.lister-item-header a::text').get(),
            'genre':element.css('span.genre::text').get()
            }
            print(movie_data)
            yield movie_data    



