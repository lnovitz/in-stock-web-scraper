#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: lnovitz
"""
# getting the data 
import requests
from lxml import html
page = requests.get('https://bananarepublic.gap.com/browse/product.do?pid=548041&bvstate=pg:2/ct:r#pdp-page-content')
tree = html.fromstring(page.content)
new = tree.xpath("//html//text()")
output = open('banana.txt', 'w')
output.write(str(new))
#<div class="swatch swatch--fixed swatch--color selected"><label class="swatch__input" for="buybox-color-swatch--White-"><input type="radio" aria-describedby="price--59" aria-disabled="false" aria-label="White " checked="" class="swatch__radio" id="buybox-color-swatch--White-" name="color-radio" value="White "><span class="swatch__image-wrapper invisible-border swatch--underlined"><img alt="White " aria-hidden="true" class="swatch__image" src="/webcontent/0018/509/832/cn18509832.jpg"></span></label></div><div class="swatch swatch--fixed swatch--color swatch--unavailable"><label class="swatch__input" for="buybox-color-swatch--Black"><input type="radio" aria-describedby="price--59" aria-disabled="true" aria-label="Black out of stock" class="swatch__radio" id="buybox-color-swatch--Black" name="color-radio" value="Black"><span class="swatch__image-wrapper invisible-border"><img alt="Black" aria-hidden="true" class="swatch__image" src="/webcontent/0018/558/894/cn18558894.jpg"><svg class="swatch__out-of-stock-indicator" viewBox="0 0 37 23"><g class="group" fill="none" fill-rule="evenodd" stroke="none" stroke-width="1"><g fill="#000000" stroke="#FFFFFF"><rect class="rectangle" height="2"></rect></g></g></svg></span></label></div>
divs = tree.xpath('//div//text()')
#print(divs[1])
stockCount = 0
greater10count = 0
for x in divs:
    if x.lower().find('white') != -1:
        #print(x + '\n\n\n\n--------------------------\n')
        stockCount += 1
    elif len(x) > 10:
        greater10count += 1
#print(stockCount, greater10count)

    
#    x = tree.xpath('//text()')
#    print(x,'\n\n\n\n')