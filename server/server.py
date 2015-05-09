import tornado.escape
import tornado.ioloop
import tornado.web
import json
import os
import requests
from pyquery import PyQuery as pq
PORT = 8888

class URLHandler(tornado.web.RequestHandler):
    def post(self):
        urls = filter(lambda u: str(u) != 'None', [str(url) for url in json.loads(self.get_argument('sites'))])
        contents = [requests.get(url).content for url in urls]
        pyq_docs = [pq(content).remove("script").remove("style") for content in contents]
        inner_texts = [doc("body").text() for doc in pyq_docs]
        self.write({"linkTexts": inner_texts})

#says what file to open based on the url paths
application = tornado.web.Application(handlers=[
    (r"/urls", URLHandler)],
    static_path=os.path.join(os.path.dirname(__file__), '.'),
    debug=True
)

if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()