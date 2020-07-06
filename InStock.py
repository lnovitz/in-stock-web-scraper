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

#inputFile = open('banana.txt', 'r') #read in the html 

#create a dict cleaned up with split method
def writeDict(readFile, outFile):
    elementdict = {}
    inputFile = open(readFile, 'r')
    for line in inputFile:
        strings = line.lower().split(",") #split based on commas
        for element in strings:
            elementSplit = element.split() #split based on spaces
            elementdict[element] = elementSplit
    inputFile.close()

    for key in elementdict.keys():
        writeMe(key.replace('"','').replace('{','').replace('}','') + '\n\n\n', outFile)
    

# the below writeDict command is only needed once to write the cleaned html to a text file
#writeDict('banana.txt', 'elementdictkeylist2.txt')

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
focusFile = open('colorgroup.txt', 'a')
keysnew = open('elementdictkeylist.txt', 'r')
lineEnd = len(open('elementdictkeylist.txt').readlines())

def writePostLookup():
    count = 0
    for line in keysnew:
        if count >= lineStart and count <= lineEnd:
            count += 1
            focusFile.write(line)
        else:
            count += 1

    keysnew.close()
    focusFile.close()