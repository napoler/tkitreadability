# 一个从html中提取正文的库

```python
from tkitreadability import tkitReadability
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




```

## 更新

### version:'0.0.0.4'
加入的markdown的转换为html


文档查看
https://docs.terrychan.org/tkitreadability/


## 快速上传操作
可以自动查找依赖，然后上传
```
sh upload.sh
```

