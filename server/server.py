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
        urls = [str(url) for url in json.loads(self.get_argument('sites'))]
        response = requests.get(urls[0])
        doc = pq(response.content)

        #doc is pyQuery object and response.content is a string containg html of the url
        self.write({"firstPage": response.content})

#says what file to open based on the url paths
application = tornado.web.Application(handlers=[
    (r"/urls", URLHandler)],
    static_path=os.path.join(os.path.dirname(__file__), '.'),
    debug=True
)

if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()