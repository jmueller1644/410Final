import tornado.escape
import tornado.ioloop
import tornado.web
import webbrowser
import json
import os
import time
PORT = 8888

#stock symbols can be downloaded from ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt

#defines what html file to open. Says to open the bar time series
class URLHandler(tornado.web.RequestHandler):
    def post(self):
        urls = self.get_argument('sites')
        print urls
        self.write({"test": 1});

#says what file to open based on the url paths
application = tornado.web.Application(handlers=[
    (r"/urls", URLHandler)],
    static_path=os.path.join(os.path.dirname(__file__), '.'),
    debug=True
)

if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()