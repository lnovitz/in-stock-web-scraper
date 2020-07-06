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

def writeMe(inputText, filename):
    output = open(filename, 'a') #write html to a text file
    output.write(inputText)
    output.close()

def appendHTML(treeOutput):
    output = open('banana-split.txt', 'a') #write html to a text file
    output.write(treeOutput)
    output.close()

# writeMe(getHTML(grabWebLink()), 'banana-new-try.txt') # this command is only needed once to write the html to a text file

inputFile = open('banana.txt', 'r') #read in the html 

startIndex = 0
instockIndexes = []
elements = 0
elementSplit = []
elementdict = {}
for line in inputFile:
    strings = line.lower().split(",")
    print(type(strings))
    for element in strings:
        find = element.find('instock', startIndex) #index to search will increase for every element
        x = 0
        elementSplit = element.split()
        elementdict[element] = elementSplit
        elements += 1
        for x in range(5):
            instockIndexes.append(find)
            #print(element[find])
            startIndex = find + 1
            x += 1
#print(elements,len(instockIndexes), len(elementdict))

inputFile.close()
#for key in elementdict.keys():
#    writeMe(key.replace('"','').replace('{','').replace('}','') + '\n\n\n', 'elementdictkeylist.txt')
#writeMe(str(elementdict.keys()), 'elementdictkeys.txt')

#keyFile = open('elementdictkeylist.txt', 'r') #read in the html 

        #get
        #print(line) #index to search will increase for every element
#print(find)

def lookup(lookupText, filename):
    keyFile = open(filename, 'r')
    lookup_list = []
    with keyFile as f:
        for num, line in enumerate(f, 0):
            if lookupText in line:
                #print('found at line:', num)
                lookup_list.append(num)
    keyFile.close()
    if len(lookup_list) == 1:
        return lookup_list[0]
    else:
        return lookup_list

lineStart = lookup('colorgroup', 'elementdictkeylist.txt')
print(lineStart)
#keyFile = open('elementdictkeylist.txt', 'r')
focusFile = open('colorgroup.txt', 'a')

keysnew = open('elementdictkeylist.txt', 'r')
lineEnd = len(open('elementdictkeylist.txt').readlines())
print(keysnew)  
print(lineEnd)

keysnew.close()