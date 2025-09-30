# ZhihuPostSpider
原理
-------------------
##### 知乎的文章页面的网址（或统一资源定位符，url）都是“https://zhuanlan/zhihu.com/p/XXX” 这种形式。不同文章的“XXX”编号不同。不过知乎这网站有个略坑之处，就是文章不连号。有些号码对应的url是没有内容的，如果访问会返回404错误。比如“https://zhuanlan/zhihu.com/p/1” 就是个不存在的网址。所有有文章内容的编号，只有知乎的服务器自己清楚。所以只能辛苦一下计算机挨个遍历过去。遇到404程序会抛出urllib.error.HTTPError错误，用try-except语句捕捉。
使用
-------------------
##### 用fiddler抓个包，把请求头里的user-agent复制到代码里header字典的第一行“user-agent”后面的XXX里，再登录一下知乎，抓一下GET请求https://www.zhihu.com/ 的包，把里面的cookie复制到“cookie”后面的XXX里。
##### 找个高匿代理（比如西刺免费代理网站）。ProxyHandler类的构造函数的参数是一个字典，键是代理的类型，比如HTTP，HTTPS或SOCKS4/5；值是IP地址以及冒号加端口号，填入就行了。
