from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from amazon.items import AmazonItem
from scrapy.selector import Selector
from scrapy.http.request import Request
#from scrapy.selector import HtmlXPathSelector
import re
count=0
class MySpider(CrawlSpider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = ["http://www.amazon.com/s/ref=sr_nr_n_0?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011%2Cn%3A158592011&bbn=158591011&ie=UTF8&qid=1403264414&rnid=158591011","http://www.amazon.com/s/ref=amb_link_364193142_12?ie=UTF8&bbn=154606011&rh=i%3Adigital-text%2Cn%3A133140011%2Cn%3A!133141011%2Cn%3A154606011%2Cn%3A157325011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=left-1&pf_rd_r=11FA19RN5B32JD172YZY&pf_rd_t=101&pf_rd_p=1713014242&pf_rd_i=5613016011",
    "http://www.amazon.com/s/ref=amb_link_364193142_12?ie=UTF8&bbn=154606011&rh=i%3Adigital-text%2Cn%3A133140011%2Cn%3A!133141011%2Cn%3A154606011%2Cn%3A157325011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=left-1&pf_rd_r=11FA19RN5B32JD172YZY&pf_rd_t=101&pf_rd_p=1713014242&pf_rd_i=5613016011",
    "http://www.amazon.com/s/ref=sr_nr_n_0?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011%2Cp_n_date%3A1249102011%2Cn%3A158592011&bbn=158591011&ie=UTF8&qid=1403524388&rnid=158591011",
    "http://www.amazon.com/s/ref=lp_158597011_nr_n_1?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A158597011%2Cn%3A158610011&bbn=158597011&ie=UTF8&qid=1403524700&rnid=158597011",
    "http://www.amazon.com/s/ref=sr_nr_n_0?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A158597011%2Cn%3A158610011%2Cn%3A158611011&bbn=158610011&ie=UTF8&qid=1403524709&rnid=158610011",
    "http://www.amazon.com/s/ref=sr_nr_n_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A158597011%2Cn%3A158610011%2Cn%3A158617011&bbn=158610011&ie=UTF8&qid=1403524709&rnid=158610011",
    "http://www.amazon.com/s/ref=lp_157305011_nr_n_0?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&bbn=157305011&ie=UTF8&qid=1403524801&rnid=157305011",
    "http://www.amazon.com/s/ref=lp_156699011_nr_n_0?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156699011%2Cn%3A156700011&bbn=156699011&ie=UTF8&qid=1403524945&rnid=156699011",
    "http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156699011%2Cn%3A156700011&page=2&bbn=156699011&ie=UTF8&qid=1403524952",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156699011%2Cn%3A156700011&page=3&bbn=156699011&ie=UTF8&qid=1403524979",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=3&ie=UTF8&qid=1403525049",
    "http://www.amazon.com/s/ref=sr_pg_4?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=4&ie=UTF8&qid=1403525055",
    "http://www.amazon.com/Rescue-Ell-Donsaii-story-11-ebook/dp/B00K6UC3WC/ref=sr_1_75?s=digital-text&ie=UTF8&qid=1403525082&sr=1-75",
    "http://www.amazon.com/s/ref=sr_pg_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=6&ie=UTF8&qid=1403525082",
    "http://www.amazon.com/s/ref=sr_pg_8?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=8&ie=UTF8&qid=1403525112",
    "http://www.amazon.com/s/ref=sr_pg_9?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=9&ie=UTF8&qid=1403525129",
    "http://www.amazon.com/s/ref=sr_pg_10?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=10&ie=UTF8&qid=1403525142",
    "http://www.amazon.com/s/ref=sr_pg_12?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=12&ie=UTF8&qid=1403525180",
    "http://www.amazon.com/s/ref=sr_pg_13?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158591011&page=13&ie=UTF8&qid=1403525194",
    "http://www.amazon.com/s/ref=sr_pg_12?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157028011%2Cn%3A157051011&page=12&bbn=157028011&ie=UTF8&qid=1403530100",
    "http://www.amazon.com/s/ref=lp_156576011_nr_n_12?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&bbn=156576011&ie=UTF8&qid=1403530237&rnid=156576011",
    "http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=2&bbn=156576011&ie=UTF8&qid=1403530252",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=3&bbn=156576011&ie=UTF8&qid=1403530271",
    "http://www.amazon.com/s/ref=sr_pg_5?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=5&bbn=156576011&ie=UTF8&qid=1403530301",
    "http://www.amazon.com/s/ref=sr_pg_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=6&bbn=156576011&ie=UTF8&qid=1403530312",
    "http://www.amazon.com/s/ref=sr_pg_7?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=7&bbn=156576011&ie=UTF8&qid=1403530323",
    "http://www.amazon.com/s/ref=sr_pg_8?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=8&bbn=156576011&ie=UTF8&qid=1403530334",
    "http://www.amazon.com/s/ref=sr_pg_9?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=9&bbn=156576011&ie=UTF8&qid=1403530345",
    "http://www.amazon.com/s/ref=sr_pg_10?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=10&bbn=156576011&ie=UTF8&qid=1403530356",
    "http://www.amazon.com/s/ref=sr_pg_11?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=11&bbn=156576011&ie=UTF8&qid=1403530371",
    "http://www.amazon.com/s/ref=sr_pg_12?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=12&bbn=156576011&ie=UTF8&qid=1403530383",
    "http://www.amazon.com/s/ref=sr_pg_13?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156576011%2Cn%3A156680011&page=13&bbn=156576011&ie=UTF8&qid=1403530394",
    "http://www.amazon.com/s/ref=lp_668010011_nr_n_0?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&bbn=668010011&ie=UTF8&qid=1403530511&rnid=668010011",
    "http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=2&bbn=668010011&ie=UTF8&qid=1403530529",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=3&bbn=668010011&ie=UTF8&qid=1403530544",
    "http://www.amazon.com/s/ref=sr_pg_4?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=4&bbn=668010011&ie=UTF8&qid=1403530557",
    "http://www.amazon.com/s/ref=sr_pg_5?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=5&bbn=668010011&ie=UTF8&qid=1403530567",
    "http://www.amazon.com/s/ref=sr_pg_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=6&bbn=668010011&ie=UTF8&qid=1403530577",
    "http://www.amazon.com/s/ref=sr_pg_7?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=7&bbn=668010011&ie=UTF8&qid=1403530588",
    "http://www.amazon.com/s/ref=sr_pg_8?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=8&bbn=668010011&ie=UTF8&qid=1403530599",
    "http://www.amazon.com/s/ref=sr_pg_9?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=9&bbn=668010011&ie=UTF8&qid=1403530608",
    "http://www.amazon.com/s/ref=sr_pg_10?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=10&bbn=668010011&ie=UTF8&qid=1403530623",
    "http://www.amazon.com/s/ref=sr_pg_11?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=11&bbn=668010011&ie=UTF8&qid=1403530634",
    "http://www.amazon.com/s/ref=sr_pg_12?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=12&bbn=668010011&ie=UTF8&qid=1403530647",
    "http://www.amazon.com/s/ref=sr_pg_13?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=13&bbn=668010011&ie=UTF8&qid=1403530660",
    "http://www.amazon.com/s/ref=sr_pg_14?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=14&bbn=668010011&ie=UTF8&qid=1403530670",
    "http://www.amazon.com/s/ref=sr_pg_15?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011&page=15&bbn=668010011&ie=UTF8&qid=1403530679",
    "http://www.amazon.com/s/ref=sr_nr_n_8?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&bbn=158576011&ie=UTF8&qid=1403530529&rnid=158576011",
    "http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=2&bbn=158576011&ie=UTF8&qid=1403530748",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=3&bbn=158576011&ie=UTF8&qid=1403530765",
    "http://www.amazon.com/s/ref=sr_pg_4?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=4&bbn=158576011&ie=UTF8&qid=1403530779",
    "http://www.amazon.com/s/ref=sr_pg_5?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=5&bbn=158576011&ie=UTF8&qid=1403530787",
    "http://www.amazon.com/s/ref=sr_pg_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=6&bbn=158576011&ie=UTF8&qid=1403530799",
    "http://www.amazon.com/s/ref=sr_pg_7?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=7&bbn=158576011&ie=UTF8&qid=1403530811",
    "http://www.amazon.com/s/ref=sr_pg_8?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=8&bbn=158576011&ie=UTF8&qid=1403530820",
    "http://www.amazon.com/s/ref=sr_pg_9?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=9&bbn=158576011&ie=UTF8&qid=1403530830",
    "http://www.amazon.com/s/ref=sr_pg_10?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=10&bbn=158576011&ie=UTF8&qid=1403530841",
    "http://www.amazon.com/s/ref=sr_pg_12?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=12&bbn=158576011&ie=UTF8&qid=1403530885",
    "http://www.amazon.com/s/ref=sr_pg_13?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=13&bbn=158576011&ie=UTF8&qid=1403530895",
    "http://www.amazon.com/s/ref=sr_pg_14?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=14&bbn=158576011&ie=UTF8&qid=1403530904",
    "http://www.amazon.com/s/ref=sr_pg_15?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=15&bbn=158576011&ie=UTF8&qid=1403530921",
    "http://www.amazon.com/s/ref=sr_pg_16?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=16&bbn=158576011&ie=UTF8&qid=1403530931",
    "http://www.amazon.com/s/ref=sr_pg_18?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=18&bbn=158576011&ie=UTF8&qid=1403530955",
    "http://www.amazon.com/s/ref=sr_pg_19?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=19&bbn=158576011&ie=UTF8&qid=1403531079",
    "http://www.amazon.com/s/ref=sr_pg_20?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A668010011%2Cn%3A158576011%2Cn%3A169457011&page=20&bbn=158576011&ie=UTF8&qid=1403531090",
    "http://www.amazon.com/s/ref=lp_157305011_nr_n_0?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&bbn=157305011&ie=UTF8&qid=1403531206&rnid=157305011",
    "http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=2&bbn=157305011&ie=UTF8&qid=1403531215",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=3&bbn=157305011&ie=UTF8&qid=1403531227",
    "http://www.amazon.com/s/ref=sr_pg_4?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=4&bbn=157305011&ie=UTF8&qid=1403531235",
    "http://www.amazon.com/s/ref=sr_pg_5?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=5&bbn=157305011&ie=UTF8&qid=1403531244",
    "http://www.amazon.com/s/ref=sr_pg_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=6&bbn=157305011&ie=UTF8&qid=1403531258",
    "http://www.amazon.com/s/ref=sr_pg_7?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=7&bbn=157305011&ie=UTF8&qid=1403531269",
    "http://www.amazon.com/s/ref=sr_pg_8?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=8&bbn=157305011&ie=UTF8&qid=1403531282",
    "http://www.amazon.com/s/ref=sr_pg_9?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=9&bbn=157305011&ie=UTF8&qid=1403531290",
    "http://www.amazon.com/s/ref=sr_pg_10?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=10&bbn=157305011&ie=UTF8&qid=1403531299",
    "http://www.amazon.com/s/ref=sr_pg_11?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A157305011%2Cn%3A6361460011&page=11&bbn=157305011&ie=UTF8&qid=1403531309",
    "http://www.amazon.com/s/ref=lp_159936011_nr_n_1?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A159936011%2Cn%3A159938011&bbn=159936011&ie=UTF8&qid=1403531673&rnid=159936011",
    "http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A159936011%2Cn%3A159938011&page=2&bbn=159936011&ie=UTF8&qid=1403531678",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A159936011%2Cn%3A159938011&page=3&bbn=159936011&ie=UTF8&qid=1403531693",
    "http://www.amazon.com/s/ref=sr_pg_4?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A159936011%2Cn%3A159938011&page=4&bbn=159936011&ie=UTF8&qid=1403531702",
    "http://www.amazon.com/s/ref=sr_pg_5?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A159936011%2Cn%3A159938011&page=5&bbn=159936011&ie=UTF8&qid=1403531714",
    "http://www.amazon.com/s/ref=sr_pg_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A159936011%2Cn%3A159938011&page=6&bbn=159936011&ie=UTF8&qid=1403531723",
    "http://www.amazon.com/s/ref=lp_156116011_nr_n_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&bbn=156116011&ie=UTF8&qid=1403531758&rnid=156116011",
    "http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=2&bbn=156116011&ie=UTF8&qid=1403531773",
    "http://www.amazon.com/s/ref=sr_pg_3?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=3&bbn=156116011&ie=UTF8&qid=1403531785",
    "http://www.amazon.com/s/ref=sr_pg_4?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=4&bbn=156116011&ie=UTF8&qid=1403531800",
    "http://www.amazon.com/s/ref=sr_pg_5?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=5&bbn=156116011&ie=UTF8&qid=1403531811",
    "http://www.amazon.com/s/ref=sr_pg_6?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=6&bbn=156116011&ie=UTF8&qid=1403531821",
    "http://www.amazon.com/s/ref=sr_pg_7?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=7&bbn=156116011&ie=UTF8&qid=1403531830",
    "http://www.amazon.com/s/ref=sr_pg_8?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=8&bbn=156116011&ie=UTF8&qid=1403531838",
    "http://www.amazon.com/s/ref=sr_pg_9?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=9&bbn=156116011&ie=UTF8&qid=1403531850",
    "http://www.amazon.com/s/ref=sr_pg_10?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=10&bbn=156116011&ie=UTF8&qid=1403531859",
    "http://www.amazon.com/s/ref=sr_pg_11?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=11&bbn=156116011&ie=UTF8&qid=1403531870",
    "http://www.amazon.com/s/ref=sr_pg_12?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=12&bbn=156116011&ie=UTF8&qid=1403531883",
    "http://www.amazon.com/s/ref=sr_pg_13?rh=n%3A133140011%2Cn%3A%21133141011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156140011&page=13&bbn=156116011&ie=UTF8&qid=1403531893"
    ]

    def parse(self, response):
        print 'inside'
        hxs = Selector(response)
        items = hxs.xpath('//*[@id="resultsCol"]').re(r'\/dp\/B00.*digital-text')
        items=list(set(items))
        print items
        for item in items:
            #link = item.extract()
            item="http://www.amazon.com"+item
            yield Request(url=item,callback=self.parse_category)

    def parse_category(self, response):
        sel = Selector(response)
        url=response.url
        item = AmazonItem()
        items = []
        print 'inside'
        item ["title"] = ''.join(sel.css('#btAsinTitle::text').extract())
        print 'url:',response.url
        item["digitalprice"] = ''.join(sel.css('.digitalListPrice>.listprice::text').extract())
        item["digitalprice"]=re.sub('\s+','',item["digitalprice"])
        item["listprice"] = ''.join(sel.css('.listPrice::text').extract())
        item["listprice"]=re.sub('\s+','',item["listprice"])
        item["kindleprice"] = ''.join(sel.css('.priceLarge::text').extract())
        item["kindleprice"]=re.sub('\s+','',item["kindleprice"])
        item["reviews"]=''.join(sel.css('#divsinglecolumnminwidth > div:nth-child(34) > span > span > a::text').extract())
        item["reviews"]=re.sub('\s+','',item["reviews"])
        item["author"]=''.join(sel.css('span.contributorNameTrigger a::text').extract())
        item["author"]=re.sub('\s+','',item["author"])
        item["reviews"] = ''.join([i for i in item["reviews"] if i.isdigit()])
        item["ratings"]=''.join(sel.css('.buying .crAvgStars a span::attr("title")').extract())


        print items

       #if item["digitalprice"] != None and item["listprice"] != None and item["kindleprice"] != None and item["reviews"] != None:
        items.append(item)
        global count
        count=count+1
        print 'Count:',count
        return items
