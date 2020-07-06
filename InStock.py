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
        #need to append as we write data to file because of this for loop
        #print(key.replace('[','').replace(']','').replace('"','').replace('{','').replace('}',''))
        writeMe(key.replace('[','').replace(']','').replace('"','').replace('{','').replace('}','') + '\n', outFile)
    

# the below writeDict command is only needed once to write the cleaned html to a text file
writeDict('banana.txt', 'banana_split.txt')

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

def writePostLookup(lookupName, filename, newFileName):
    focusFile = open(newFileName, 'w')
    keysnew = open(filename, 'r')
    #lookupName = 'colorgroup'
    lineStart = lookup(lookupName, filename)
    #print(lineStart,'0i')
    lineEnd = len(open(filename).readlines())
    count = 0
    for line in keysnew:
        if count >= lineStart and count <= lineEnd:
            count += 1
            focusFile.write(line)
        else:
            count += 1

    keysnew.close()
    focusFile.close()

# the below writePostLookup gets all text after the phrase colorgroup
writePostLookup('colorgroup', 'banana_split.txt', 'peeled_banana.txt')


with open('peeled_banana.txt', 'r') as f:
    color = ['white']
    for line in f:
        print(line)
        if line.startswith('colors'):
            for i in range(8):
                    print(next(f))
        #for word in line.strip().split(':'):
        #    if word in color:
                #print(word)
    #elif line.startswith('sizedimension'):
        #print(line)
    #elif line.startswith('instock'):
        #print(line)