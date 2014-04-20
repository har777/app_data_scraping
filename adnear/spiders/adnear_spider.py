from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from adnear.items import AdnearItem
import numpy as np
from scrapy.http import Request

class MySpider(CrawlSpider):



     #Logic for parsing given file
    file = open("/home/rage/Desktop/set_of_comma_seperated_app_names.txt", "r")
    for apps in file:
        print apps
    app = apps.split(",")
    #Removing Duplicates

    global i
    i = 0
    global j
    j = 0
    final_app = list(set(app))
    global final_app2
    final_app2 = [s.lower() for s in final_app]
    final_app2 = [s[2:-1] for s in final_app2]
    name = "adnear_spider"
    allowed_domains = ["appexplorer.com"]
    start_urls = ["http://www.appexplorer.com/?so=&q="+final_app[0].replace(" ","+").replace("'","").replace("Android","").replace("iOS","")]
    #+final_app[0].replace(" ","+").replace("'","").replace("Android","")

    rules = (Rule (SgmlLinkExtractor(allow=("/?so=&q=.*","/a/*","/?q=&pg={\d+:\d+\}&dev=",))
    , callback="parse_items", follow= True),
    )



    def parse_items(self, response):
        res = Selector(response)
        items = []
        item = AdnearItem()

        #item["title"] = map(unicode.strip, res.xpath('//title/text()').extract())
        #item["text"] = res.xpath('//div[@itemprop="articleBody"]/p/text()').extract()
        title = res.xpath('//span[@id="id_appsh_ti"]/text()').extract()
        print title
        global j
        j = j + 1
        global i
        print j

        def match(title):
            for s in final_app2:
                if (title[0].encode('utf-8').replace("?","").replace("  ","").lower()) in s:
                    return True
                else:
                    return False

        #u_to_str = (title[0].encode('utf-8'))
        if(title and match(title)):

            #final_app.remove(title[0])
            print "success"
            print " "
            print " "
            print " "
            print " "
            print " "
            #Didnt find region data. Will search more sources.
            i = i + 1
            #Not extracting data for some reason. Have to recheck.
            rating = res.xpath('//span[@id="app_rtg"]/text()').extract()
            #item["rating"] = rating
            #item["rating_number"]
            item["title"] = title
            #Categories Like Entertainment, Medical, etc can have a big impact on targetting the ad
            categories = res.xpath('//span[@class="cl_appsh_cat"]/a/text()').extract()
            #last part of categories below contain developer name. We need to remove that for categories Item
            categories = categories[:-1]
            item["category"] = categories

            #I'm not very sure on the dynamics of pricing on targetted ad's. But I know people who wont buy apps even for a small price regardless of how good it is.
            #Inclined to add it.
            price = res.xpath('//span[@id="id_appsh_pr"]/b/text()').extract()
            item["pricing"] = price

            #Rank in its particular category.
            #Something wrong with the xpath. Will work on it.
            rank = res.xpath('//span[@class="cl_appsh_cat"]/text()').extract()
            item["rank"] = rank
            yield Request("http://www.appexplorer.com/?so=&q=" + final_app2[i].replace(" ","+").replace("'","").replace("Android",""))
            yield item
        #items.append(item)

