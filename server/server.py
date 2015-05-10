import tornado.escape
import tornado.ioloop
import tornado.web
import json
import os
import requests
from pyquery import PyQuery as pq
from learningAlgorithm import predict
import urllib2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import pickle
PORT = 8888

PDF = 'application/pdf'
HTML = 'text/html'

def is_pdf(url):
    if PDF in requests.get(url, verify=False).headers['content-type']:
        return True

def pdf_from_url_to_txt(url):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Open the url provided as an argument to the function and read the content
    f = urllib2.urlopen(urllib2.Request(url)).read()
    # Cast to StringIO object
    fp = StringIO(f)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp,
                                  pagenos,
                                  maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

class URLHandler(tornado.web.RequestHandler):
    def post(self):
        urls = filter(lambda u: str(u) != 'None', [str(url) for url in json.loads(self.get_argument('sites'))])
        inner_texts = []
        for url in urls:
            print url
            if is_pdf(url):
                inner_texts.append(pdf_from_url_to_txt(url))
            else:
                pq_doc = pq(requests.get(url, verify=False).content).remove("style")
                inner_texts.append(pq_doc("body").text())
        # pyq_docs = [pq(content).remove("script").remove("style") for content in contents]
        # inner_texts = [doc("body").text() for doc in pyq_docs]

        model_file = open('knn_model.p', 'rb')
        model = pickle.load(model_file)
        predictions = [predict(model, text) for text in inner_texts]
        #print predictions
        self.write({"results": predictions})

#says what file to open based on the url paths
application = tornado.web.Application(handlers=[
    (r"/urls", URLHandler)],
    static_path=os.path.join(os.path.dirname(__file__), '.'),
    debug=True
)

if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()