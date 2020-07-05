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

def appendHTML(treeOutput):
    output = open('banana-split.txt', 'a') #write html to a text file
    output.write(treeOutput)
    output.close()

# writeHTML(getHTML(grabWebLink())) # this command is only needed once to write the html to a text file

inputFile = open('banana.txt', 'r') #read in the html 
#inputFile = list(inputFile)

startIndex = 0
newInput = []
for line in inputFile:
    strings = line.split(",")
    for element in strings:
        startIndex += 1
print(startIndex)

inputFile.close()

    