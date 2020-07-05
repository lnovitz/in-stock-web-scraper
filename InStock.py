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
    output = open('banana-new.txt', 'w') #write html to a text file
    output.write(treeOutput)
    output.close()

# writeHTML(getHTML(grabWebLink())) # this command is only needed once to write the html to a text file

inputFile = open('banana.txt', 'r') #read in the html 

isStrings = 0
notStrings = 0
for x in inputFile:
    print(type(x))
    print(len(x)) #442 thousand elements in x!
    for element in x:
        if type(element) == str:
            isStrings += 1
        else:
            notStrings += 1
    print(isStrings, notStrings)

inputFile.close()

    