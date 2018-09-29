# from filecmp import cmp
from html.parser import HTMLParser

class HtmlParseUtil(HTMLParser) :

    # def handle_starttag(self, tag, attrs):
    #     # super().handle_starttag(tag, attrs)
    #     if tag == 'a':
    #         print("Encountered a start tag:", tag)
    #         # print(_attr('href',attrs))
    #         for item in attrs:
    #             if item[0] == 'href':
    #                 print('href:'+item[1])
    #     else:
    #         if tag == 'img':
    #             print("Encountered a start tag:", tag)
    #             for item in attrs:
    #                 if item[0] == 'src':
    #                     print('src:'+item[1])

    def handle_data(self, data):
        # super().handle_data(data)
        if self.lasttag == 'p':
            print('ppp--->'+data.strip())
        if self.lasttag == 'a':
            print('aaa--->'+data.strip())