from lxml import html
from pyquery import PyQuery as pq
import os
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from stemming.porter2 import stem
import string

def scrapeFile(path):
    with open(path,"rb") as f:
            return pq(html.fromstring(unicode(f.read(),errors='ignore'))).remove("script").remove("style")

def scrapeFolder(rootdir,f,transform):
    result=[]
    for folder, subs, files in os.walk(rootdir):
        for filename in files:
            #print(os.path.join(folder, filename))
            result.append(transform(f(os.path.join(folder, filename))))
    return result

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
