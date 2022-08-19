# -*- coding: utf-8 -*-
from readability import Document
import html2text
import markdown
import re

"""
这是一个提取正文的类

"""
def get_markdown_images(text):
    """
    从markdown中提取图片

    :param text:
    :return:
    """
    image_arr = re.findall(r'(?:!\[(.*?)\]\((.*?)\))', text)  # 提最述与rul
    # print("image_arr", image_arr)
    return image_arr

class tkitReadability:
    """
    一个正文提取类，优化提取流程
    >>> tkitＲeadability()

    """

    def __init__(self):
        pass

    def html2text(self, html,
                  ignore_links=True,
                  bypass_tables=True,  # 用 HTML 格式而不是 Markdown 语法来格式化表格。
                  ignore_images=False,
                  images_to_alt=False,
                  images_as_html=False,
                  images_with_size=True,
                  ignore_emphasis=True
                  ):
        """从html中提取正文
        继承自  https://pypi.org/project/html2text/
        更多参数
        https://github.com/Alir3z4/html2text/blob/master/docs/usage.md



        >>> html2text(html,
                  ignore_links=True,
                  bypass_tables=False,
                  ignore_images=True,
                  images_to_alt=True)


        """
        # response = requests.get(url)
        # logging.info(response.text)
        # html = request.urlopen(url)

        # logging.info(html)

        doc = Document(html)
        # doc = Document(html)
        # logging.info(doc.title())
        try:
            html = doc.summary(True)
        except:
            return ''
        #   logging.info(doc.get_clean_html())
        # t =html2text.html2text(html)
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = ignore_links
        text_maker.bypass_tables = bypass_tables
        text_maker.ignore_images = ignore_images
        text_maker.images_to_alt = images_to_alt
        text_maker.images_as_html = images_as_html
        text_maker.images_with_size = images_with_size
        text_maker.google_doc = True
        text_maker.single_line_break = False  # 在块元素之后使用单个换行符而不是两个。
        text_maker.ignore_emphasis = ignore_emphasis
        text_maker.body_width = False  # 是否自动折行
        # html = function_to_get_some_html()
        text = text_maker.handle(html)
        # text=self.remove_HTML_tag('img',text)
        # print(text)
        return text

    def html2markdown(self, html,
                  ignore_links=True,
                  bypass_tables=True,  # 用 HTML 格式而不是 Markdown 语法来格式化表格。
                  ignore_images=False,
                  images_to_alt=False,
                  images_as_html=False,
                  images_with_size=True,
                  ignore_emphasis=True, **kwargs):
        """从html中提取正文
        继承自  https://pypi.org/project/html2text/
        更多参数
        https://github.com/Alir3z4/html2text/blob/master/docs/usage.md



        >>>


        """
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = ignore_links
        text_maker.bypass_tables = bypass_tables
        text_maker.ignore_images = ignore_images
        text_maker.images_to_alt = images_to_alt
        text_maker.images_as_html = images_as_html
        text_maker.images_with_size = images_with_size
        text_maker.google_doc = True
        text_maker.single_line_break = False  # 在块元素之后使用单个换行符而不是两个。
        text_maker.ignore_emphasis = ignore_emphasis
        text_maker.body_width = False  # 是否自动折行
        # html = function_to_get_some_html()
        text = text_maker.handle(html)
        # return self.html2text(**kwargs)
        return text

    def markdown2Html(self, text, **kwargs):
        """
        将markdown转换为html

        """
        return markdown.markdown(text)

    def remove_HTML_tag(self, tag, string):
        """删除特定的标签

        # 删除掉图片
        >>> tag ='img'
        >>> string ='''              '''



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
        s = re_doctype.sub('', s)
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

    def remove_word_wrap(self, html):
        """删除多余的换行

        """
        nt = re.sub('[\n]+', '\n', html)
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


if __name__ == '__main__':
    html = """

            <div class="full-component-wrapper">

                    <div class="component component--text-image image-position--right" data-id="45290" data-type="c_sideimagetext_ttt">
          <div class="text-image--component-wrapper twb-container">
            <div class="text-image--content-wrapper row">


                      <div class="text-image--image col-12 col-xl-7 order-2 order-xl-3">

                    <div class="field field--name-field-c-image field--type-entity-reference field--label-hidden field__item">   
                     <picture>
                          <source srcset="/sites/default/files/styles/ttt_image_690/public/2021-07/border-collie.webp?itok=1oyChjVg 2x" media="all and (min-width: 1140px)" type="image/webp">
                      <source srcset="/sites/default/files/styles/ttt_image_930/public/2021-07/border-collie.webp?itok=QxWrubxE 1x" media="all and (min-width: 992px)" type="image/webp">
                      <source srcset="/sites/default/files/styles/ttt_image_690/public/2021-07/border-collie.webp?itok=1oyChjVg 1x" media="all and (min-width: 768px)" type="image/webp">
                      <source srcset="/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.webp?itok=jhilnwqZ 1x" media="all and (min-width: 576px)" type="image/webp">
                      <source srcset="/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.webp?itok=jhilnwqZ 1x" type="image/webp">
                      <source srcset="/sites/default/files/styles/ttt_image_690/public/2021-07/border-collie.jpg?itok=1oyChjVg 2x" media="all and (min-width: 1140px)" type="image/jpeg">
                      <source srcset="/sites/default/files/styles/ttt_image_930/public/2021-07/border-collie.jpg?itok=QxWrubxE 1x" media="all and (min-width: 992px)" type="image/jpeg">
                      <source srcset="/sites/default/files/styles/ttt_image_690/public/2021-07/border-collie.jpg?itok=1oyChjVg 1x" media="all and (min-width: 768px)" type="image/jpeg">
                      <source srcset="/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ 1x" media="all and (min-width: 576px)" type="image/jpeg">
                      <source srcset="/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ 1x" type="image/jpeg">
                          <img src="/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ" alt="Border Collie" typeof="foaf:Image" loading="lazy">

          </picture>

        </div>

                </div>
        <img src="/sites/default/files/styles/ttt_image_510/public/2021-07/border-collie.jpg?itok=jhilnwqZ" alt="Border Collie" typeof="foaf:Image" loading="lazy">
                <div class="text-image--text-wrapper col-12 col-xl-5 order-3 order-xl-2">

                  <div class="text-image--text">

                    <div class="clearfix text-formatted field field--name-field-c-sideimagetext-summary field--type-text-long field--label-hidden field__item"><h2>Pet Card</h2>

        <ul>
            <li><strong>Living Considerations:</strong> Not hypoallergenic, suitable for apartment living, good with older children</li>
            <li><strong>Size:</strong> Medium</li>
            <li><strong>Height:</strong> Males - 48 to 56 centimetres at the withers, Females - 45 to 53 centimetres at the withers</li>
            <li><strong>Weight:</strong> Males -13 to 20 kilograms, Females - 12 to 19 kilograms</li>
            <li><strong>Coat:</strong> Medium/Long</li>
            <li><strong>Energy:</strong> High</li>
            <li><strong>Colour:</strong> All colours or colour combinations</li>
            <li><strong>Activities:</strong> Agility, Conformation, Herding, Obedience, Rally Obedience, Tracking</li>
            <li><strong>Indoor/Outdoor:</strong> Both</li>
        </ul>
        </div>

                  </div>

                          </div>
                  </div>
          </div>
        </div>





              </div>


    """
    Readability = tkitReadability()
    content = Readability.html2text(html)
    print(content)
    # 输出为html
    print(Readability.markdown2Html(content))
