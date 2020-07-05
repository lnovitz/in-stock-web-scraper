#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: lnovitz
"""
import requests 
from lxml import html

# getting the data 
page = requests.get('https://bananarepublic.gap.com/browse/product.do?pid=548041&bvstate=pg:2/ct:r#pdp-page-content')
tree = html.fromstring(page.content)
new = tree.xpath("//html//text()") #get tree

output = open('banana.txt', 'w') #write html to a text file
output.write(str(new))

inputFile = open('banana.txt', 'r') #read in the html 
stockCount = 0
greater10count = 0
for x in inputFile:
    if x.lower().find('instock') != -1:
        #print(x + '\n\n\n\n--------------------------\n')
        stockCount += 1
    elif len(x) > 10:
        greater10count += 1


print(stockCount, greater10count)

output.close()
inputFile.close()

    