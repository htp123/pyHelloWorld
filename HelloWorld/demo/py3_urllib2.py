import urllib.request
import urllib.parse
# from htmlParseUtil import HtmlParseUtil
from bs4 import BeautifulSoup
from soupParseUtil import find_all
from soupParseUtil import blogParser
from soupParseUtil import analyzeBlog

url = 'http://www.cnblogs.com/mvc/AggSite/PostList.aspx'
result = urllib.request.urlopen(url).read()
# print(len(result))
# print(result)
html = result.decode('utf-8')
# print(html)

# 解析html

# 1.自带的HTMLParser
# parser = HtmlParseUtil()
# parser.feed(html)

# 2.BeautifulSoup
soup = BeautifulSoup(html)
# print(soup.prettify())

# 结果写进文件
# file = open('test.html', mode='w+',encoding='utf-8')
# file.write(soup.prettify())
# file.close()

# 调用find_all()
# print(find_all(soup, 'a', 'gray'))

# 调用解析函数
url = 'http://www.cnblogs.com/mvc/AggSite/PostList.aspx'
result = blogParser(url)
for item in result:
    # print(item)
    detail = analyzeBlog(item)
    for col in detail:
        print(col)




