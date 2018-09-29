from bs4 import BeautifulSoup
import re


soup = BeautifulSoup(open('test.html', mode='r', encoding='utf-8'))
# print(soup.prettify())

# *******
# 1.四大对象（Tag,NavigableString,BeautifulSoup,Comment）
# *******

# print(type(soup.div))
# print(soup.name)
# print(soup.div.attrs)
# print(soup.a.get('href'))
# print(soup.a.string)

# ******
# 2.遍历文档树
# ******

# print(soup.body)
# 直接子节点 contents children
# print(soup.body.contents)
# count = 0
# for child in soup.body.children:
#     count = count + 1
#     # print(str(count) + ':' + child)  #该行无法运行
#     print(str(count))
#     print(child)

# 子孙节点 descendants 节点内容
# count = 0
# for child in soup.descendants:
#     count = count + 1
#     print('count:' + str(count))
#     # print(child)
#     content = str(child.string).strip()
#     if len(content) > 0:
#         print(content)

# 多节点内容 strings , stripped_strings
# for string in soup.strings:
#     print(repr(string))

# for string in soup.stripped_strings:
#     # repr:返回对象的String形式
#     print(repr(string))

# 父节点
# p = soup.p
# print(p.parent.name)
# content = soup.head.title.string
# print(content.parent.name)

# 全部父节点
# content = soup.head.title.string
# for parent in content.parents:
#     print(parent.name)

# 兄弟节点
# print(soup.p.next_sibling)
# 空白

# print(soup.p.prev_sibling)
# none

# print(soup.p.next_sibling.next_sibling)

# 全部兄弟节点
# count = 0
# for sibling in soup.p.next_siblings:
#     count = count + 1
#     print(str(count))
#     print(repr(sibling))

# 前后节点，针对所有节点，不分层次关系
# print(soup.head)
# print(soup.head.next_element.next_element)
# print(soup.head.previous_element)

# 所有前后节点 .next_elements  .previous_elements
# for element in soup.a.next_elements:
#     print(repr(element))

# 3. 搜索文档树
# find_all
# name: 字符串 正则 列表 true  方法
# print(soup.find_all('a'))

# for tag in soup.find_all(re.compile("^d")):
#     print(tag.attrs)

# print(soup.find_all(['a', 'img']))

# for tag in soup.find_all(True):
#     if tag.name == 'a':
#         print(tag.get('href'))

# keyword text limit recursive
