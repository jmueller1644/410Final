import tornado.escape
import tornado.ioloop
import tornado.web
import json
import os
from pyquery import PyQuery as pq
from inputReading import get_url_text
import pickle
PORT = 8888

class URLHandler(tornado.web.RequestHandler):
    def post(self):
        urls = filter(lambda u: str(u) != 'None', [str(url) for url in json.loads(self.get_argument('sites'))])
        inner_texts = []
        for url in urls:
            print url
            inner_texts.append(get_url_text(url))
        # pyq_docs = [pq(content).remove("script").remove("style") for content in contents]
        # inner_texts = [doc("body").text() for doc in pyq_docs]

        model_file = open('tfidf_sgd_model.p', 'rb')
        model = pickle.load(model_file)
        predictions = [model.predict(text) for text in inner_texts]
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
