#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: lnovitz
"""
import requests 
from lxml import html

#define URL
# https://bananarepublic.gap.com/browse/product.do?pid=548041&bvstate=pg:2/ct:r#pdp-page-content

def grabWebLink():
    webLink= input('Enter the webpage you want to scrape: ')
    return webLink

# getting the data 
def getHTML(webLink):
    page = requests.get(webLink)
    tree = html.fromstring(page.content)
    treeOutput = tree.xpath("//html//text()")
    return str(treeOutput) #get html output as a string

def writeHTML(treeOutput):
    output = open('banana.txt', 'w') #write html to a text file
    output.write(treeOutput)
    output.close()

# writeHTML(getHTML(grabWebLink())) # this command is only needed once to write the html to a text file

inputFile = open('banana.txt', 'r') #read in the html 
stockCount = 0
greater10count = 0
i = 0
for x in inputFile:
    print(len(x)) #442 thousand elements in x!
    strings = 0
    dicts = 0
    for element in x:
        if type(element) == str:
            strings += 1
        elif type(element) == dict:
            dicts += 1
        else: 
            print(type(element))
    print('strings',strings, 'dicts',dicts)
    #if x.lower().find('instock') != -1:
        #print(x + '\n\n\n\n--------------------------\n')
    #    stockCount += 1
    #elif len(x) > 10:
    #    greater10count += 1

print(stockCount, greater10count)

inputFile.close()

    