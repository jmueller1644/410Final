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
                words[w]+=d[w];
            else:
                words[w]=d[w];
            total+=d[w];
    for w in words.keys():
        words[w]=words[w]*1.0/total
    return words;
def WordCountM(docSet):
    total=0;
    words=dict()
    for docs in docSet:
        for d in docs:
            for w in d.keys():
                if(words.has_key(w)):
                    words[w]+=d[w];
                else:
                    words[w]=d[w];
                total+=d[w];
    for w in words.keys():
        words[w]=words[w]*1.0/total
    return words;
def scrapeWeb(path):
    return scrapeFile(path)(".main").text();
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
    items=ss.items();
    return sorted(ss.items(),key=lambda item: (-1.0*item[1]/cs[item[0]], item[0]))

def PrintMostDistinguishingFeatures(ss,cs):
    print("--------------------------")
    for i in range(100):
        print(ss[i][0], ss[i][1],ss[i][1]/cs[ss[i][0]])
    print("--------------------------")
    
    
hS=scrapeFolder("C:/Users/Gaston/Desktop/CS410Final/410project/www.huffingtonpost.com",scrapeWeb)
wS=scrapeFolder("C:/Users/Gaston/Desktop/CS410Final/410project/www.w3schools.com",scrapeWeb)
pS=scrapeFolder("C:/Users/Gaston/Desktop/research",scrapePDF)
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

def compareVals(key):
    return hWC[key]/tWC[key],wWC[key]/tWC[key],pWC[key]/tWC[key]
