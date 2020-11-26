# -*- coding: utf-8 -*-
from readability import Document
import html2text
import re
"""
这是一个提取正文的类

"""

class tkitＲeadability:
    """
    一个正文提取类，优化提取流程
    >>> tkitＲeadability()
    
    """
    def __init__(self):
        pass
    def html2text(self,html):
        """从html中提取正文

        >>> html2text(html)


        """
        # response = requests.get(url)
        # logging.info(response.text)
        # html = request.urlopen(url)

        # logging.info(html)

        doc = Document(html)
        # doc = Document(html)
        # logging.info(doc.title())
        try:
          html= doc.summary(True)
        except:
          return ''
        #   logging.info(doc.get_clean_html())
        # t =html2text.html2text(html)
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        text_maker.bypass_tables = False
        text_maker.ignore_images = True
        text_maker.images_to_alt = True
        # html = function_to_get_some_html()
        text = text_maker.handle(html)
        # text=self.remove_HTML_tag('img',text)
        # print(text)
        return text
    def remove_HTML_tag(self,tag, string):
        """删除特定的标签

        # 删除掉图片
        >>> tag ='img'
        >>> string ='''
          萌照镇楼。\n

          <img data-rawwidth="1393" data-rawheight="1104"
          src="https://pic3.zhimg.com/50/63f68657ef2e5c22fef8b982a141cfd0_hd.jpg"
          class="origin_image zh-lightbox-thumb" width="1393" data-
          original="https://pic3.zhimg.com/63f68657ef2e5c22fef8b982a141cfd0_r.jpg"/>

          母犬发情期的主要特征：

          '''

        >>> remove_HTML_tag(tag, string)

        """
        string = re.sub(r"<\b(" + tag + r")\b[^>]*>", r"", string)
        return re.sub(r"<\/\b(" + tag + r")\b[^>]*>", r"", string)
    def filter_tags(self, htmlstr):
        """清理掉html代码

        >>> filter_tags(htmlstr)


        """
        re_doctype = re.compile('<![DOCTYPE|doctype].*>')
        re_nav = re.compile('<nav.+</nav>')
        re_cdata = re.compile('//<!\[CDATA\[.*//\]\]>', re.DOTALL)
        re_script = re.compile(
            '<\s*script[^>]*>.*?<\s*/\s*script\s*>', re.DOTALL | re.I)
        re_style = re.compile(
            '<\s*style[^>]*>.*?<\s*/\s*style\s*>', re.DOTALL | re.I)
        re_textarea = re.compile(
            '<\s*textarea[^>]*>.*?<\s*/\s*textarea\s*>', re.DOTALL | re.I)
        re_br = re.compile('<br\s*?/?>')
        re_h = re.compile('</?\w+.*?>', re.DOTALL)
        re_comment = re.compile('<!--.*?-->', re.DOTALL)
        re_space = re.compile(' +')
        s = re_cdata.sub('', htmlstr)
        s = re_doctype.sub('',s)
        s = re_nav.sub('', s)
        s = re_script.sub('', s)
        s = re_style.sub('', s)
        s = re_textarea.sub('', s)
        s = re_br.sub('', s)
        s = re_h.sub('', s)
        s = re_comment.sub('', s)
        s = re.sub('\\t', '', s)
        s = re_space.sub(' ', s)
        s = self.replaceCharEntity(s)
        return s
    def remove_word_wrap(self,html):
        """删除多余的换行

        """
        nt =  re.sub('[\n]+', '\n', html)
        return nt
    def clear(self, string):
        """清理多余空格

        清理多余的换行空格等

        >>> clear('这里似乎内\t容不给')

        """

        # return string.strip()
        # for line in string.readlines():
        # string = re.sub('[\n]+', '\n', string)
        string = string.replace('\n', '').replace(
            '\n\n', '\n').replace('\r\n', '\n').replace('   ', '\n')
        # string = string.replace('\n\n', ' ').replace('\n', '')
        string = re.sub(' +', ' ', string)
        return string