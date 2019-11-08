import time
import json
from urllib import request
from urllib import parse
from lxml import etree
from urllib import error
from http import cookiejar

def zhihu_post_spider():
    """
    爬取知乎文章所在页面，并分析赞数
    :return: None
    """
    header = {"User-Agent": "xxx",
              "Cookie":  "XXX"
             }
    proxy_handler = request.ProxyHandler({"socks4/5": "XXX.XXX.XX.XXX:XXXXX"})
    cookie_jar = cookiejar.CookieJar()
    cookie_handler = request.HTTPCookieProcessor(cookie_jar)
    opener = request.build_opener(proxy_handler, cookie_handler)
    request.install_opener(opener)
    dict_result = {}
    start_time = time.time()
    print("起始时间：", time.asctime(time.localtime(time.time())))
    for num in range(50000000, 50000010):
        switch = 1
        try:
            url = "https://zhuanlan.zhihu.com/p/" + str(num)
            rqo = request.Request(url, headers=header)
            rp = request.urlopen(rqo)
        except error.HTTPError:
            switch = 0
        if switch == 1:
            rp_htmldom = etree.HTML(rp.read())
            list_match = rp_htmldom.xpath("//button[@class=\"Button VoteButton VoteButton--up\"]/@aria-label")
            print(url)
            print(list_match)
            if list_match != []:        #知乎被建议修改的文章不显示赞数，但是html里面仍有内容，这种情况需要排除
                num_agree = (list_match[0].split())[1]
                list_keys = list(dict_result.keys())
                try:
                    dict_result[num_agree] += 1
                except KeyError:
                    dict_result[num_agree] = 1
    print(dict_result)
    end_time = time.time()
    print("结束时间为：", time.asctime(time.localtime(time.time())))
    workin_time = end_time - start_time
    print("工作时长为：", workin_time)


if __name__ == "__main__":
    zhihu_post_spider()
