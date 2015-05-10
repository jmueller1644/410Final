from lxml import html
from pyquery import PyQuery as pq
import os
import math
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from stemming.porter2 import stem
import string
from sklearn import svm
from learningAlgorithm import ToVS
from learningAlgorithm import learn
from learningAlgorithm import predict
import pickle

def scrapeFile(path):
    with open(path,"rb") as f:
            return pq(html.fromstring(unicode(f.read(),errors='ignore'))).remove("script").remove("style")

def scrapeFolder(rootdir,f):
    result=[]
    for folder, subs, files in os.walk(rootdir):
        for filename in files:
            #print(os.path.join(folder, filename))
            result.append(ToVS(f(os.path.join(folder, filename))))
    return result

def WordCount(docs):
    words=dict()
    total=0
    for d in docs:
        for w in d.keys():
            if(words.has_key(w)):
                words[w]+=d[w]
            else:
                words[w]=d[w]
            total+=d[w]
    for w in words.keys():
        words[w]=words[w]*1.0/total
    return words

def WordCountM(docSet):
    total=0
    words=dict()
    for docs in docSet:
        for d in docs:
            for w in d.keys():
                if(words.has_key(w)):
                    words[w]+=d[w]
                else:
                    words[w]=d[w]
                total+=d[w]
    for w in words.keys():
        words[w]=words[w]*1.0/total
    return words
def scrapeMain(path):
    return scrapeFile(path)(".main").text()

def scrapeWeb(path):
    return scrapeFile(path).text()

def scrapePDF(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return unicode(str,errors="ignore")
    
def SortByDivision(ss,cs):
    items=ss.items()
    return sorted(ss.items(),key=lambda item: (-1.0*item[1]/cs[item[0]], item[0]))

def PrintMostDistinguishingFeatures(ss,cs):
    print("--------------------------")
    for i in range(100):
        print(ss[i][0], ss[i][1],ss[i][1]/cs[ss[i][0]])
    print("--------------------------")

def compareVals(key):
    return hWC[key]/tWC[key],wWC[key]/tWC[key],pWC[key]/tWC[key]
    
    
# print 1
# hS=scrapeFolder("../410project/www.huffingtonpost.com", scrapeMain)
# print 2
# wS=scrapeFolder("../410project/www.w3schools.com", scrapeMain)
# print 3
# wS=wS+scrapeFolder("../410project/pdfTutorial", scrapePDF)
# print 4
# wS=wS+scrapeFolder("../410project/otherTutorial", scrapeWeb)
# print 5
# pickle.dump([hS, wS, pS], open('data.p', 'wb'))

if __name__ == '__main__':
    pickle_file = open('data.p', 'rb')
    arr = pickle.load(pickle_file)
    hS = arr[0]
    wS = arr[1]
    pS = arr[2]
    pickle_file.close()

    print("Scrape - Finished")
    hWC=WordCount(hS)
    wWC=WordCount(wS)
    pWC=WordCount(pS)
    print("Partial Count - Finished")
    tWC=WordCountM([hS, wS, pS])
    print("Finished")
    hB=SortByDivision(hWC,tWC)
    wB=SortByDivision(wWC,tWC)
    pB=SortByDivision(pWC,tWC)
    print("Huffington:")
    PrintMostDistinguishingFeatures(hB,tWC)
    print("W3School:")
    PrintMostDistinguishingFeatures(wB,tWC)
    print("Research:")
    PrintMostDistinguishingFeatures(pB,tWC)

    print 'STARTING MODEL CREATION'
    model_file =  open('knn_model.p', 'wb')
    pickle.dump(learn(hS,wS,pS), model_file)
    model_file.close()
