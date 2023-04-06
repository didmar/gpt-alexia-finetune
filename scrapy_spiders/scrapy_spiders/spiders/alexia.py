from pathlib import Path
import scrapy


class AlexiaSpider(scrapy.Spider):
    name = 'alexia'
    allowed_domains = ['www.alexia.fr']
    # start_urls = ['http://www.alexia.fr/']
    start_urls = ["https://www.alexia.fr/questions/397109/le-cir-pour-le-renouvellement-du-titre-de-sejour-conjoint-de-francais.htm"]

    # def start_requests(self):
    #     urls = [
    #         # 'https://www.alexia.fr/questions/396649/bracelet-anti-rapprochement.htm',
    #         # 'https://www.alexia.fr/questions/396747/regroupement-familial-prefecture.htm',
    #         'https://www.alexia.fr/questions/396855/mon-pere-est-cede-en-2017.htm',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sujet = '\n'.join(response.xpath('//*[@id="nvf_table_sujet_content"]/text()').extract())

        answers = []
        nvf_post_conts = response.xpath('.//div[@class="nvf_post_cont"]')
        for nvf_post_cont in nvf_post_conts:
            avocat_name = nvf_post_cont.xpath('.//a[@class="author_avocat"]/@title').extract_first()
            if not avocat_name:
                continue
            answer = '\n'.join(nvf_post_cont.xpath('.//div[@class="nvf_post_cont_message"]/text()').extract())
            is_best = bool(nvf_post_cont.xpath('.//div[@class="ggroboto"]'))
            answers.append({'avocat_name': avocat_name, 'answer': answer, 'is_best': is_best})
        
        if answers:
            yield {'url': response.url, 'question': sujet, 'answers': answers}

        for url in response.xpath('//a[@class="customlinktitle"]/@href').extract():
            if url.startswith('https://www.alexia.fr/questions'):
                yield scrapy.Request(url, callback=self.parse)

        # import ipdb
        # ipdb.set_trace()

        # filename = response.url.split("/")[-1]
        # Path(filename).write_bytes(response.body)
        # self.log(f'Saved file {filename}')
