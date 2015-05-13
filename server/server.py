import tornado.escape
import tornado.ioloop
import tornado.web
import json
import os
from pyquery import PyQuery as pq
from inputReading import get_url_text
import pickle
PORT = 8888
model = ''
model_file_name='tfidf_perceptron_model.p'

class TrainHandler(tornado.web.RequestHandler):
    def get(self):
        get_dict = self.request.arguments
        category = get_dict['category'][0]
        print category
        # urls = filter(lambda u: str(u) != 'None', [str(url) for url in json.loads(get_dict['site'][0])])
        # inner_texts = []
        # for url in urls:
        #     print url
        #     inner_texts.append(get_url_text(url))
        # pyq_docs = [pq(content).remove("script").remove("style") for content in contents]
        # inner_texts = [doc("body").text() for doc in pyq_docs]

        model.train([get_url_text(get_dict['site'][0])],[category]);
        #print predictions
        self.write({"results": "done"})

class SaveHandler(tornado.web.RequestHandler):
    def get(self):
        with open(model_file_name, 'wb') as f:
            model = pickle.dump(model, f)
        
        #print predictions
        self.write({"results": "done"})

class URLHandler(tornado.web.RequestHandler):
    def post(self):
        urls = filter(lambda u: str(u) != 'None', [str(url) for url in json.loads(self.get_argument('sites'))])
        inner_texts = []
        for url in urls:
            print url
            inner_texts.append(get_url_text(url))
        # pyq_docs = [pq(content).remove("script").remove("style") for content in contents]
        # inner_texts = [doc("body").text() for doc in pyq_docs]

        
        predictions = [model.predict(text) for text in inner_texts]
        #print predictions
        self.write({"results": predictions})

#says what file to open based on the url paths
application = tornado.web.Application(handlers=[
    (r"/urls", URLHandler),
    (r"/train", TrainHandler),
    (r"/save", SaveHandler)],
    static_path=os.path.join(os.path.dirname(__file__), '.'),
    debug=True
)

if __name__ == "__main__":
    application.listen(PORT)
    with open(model_file_name, 'rb') as f:
        model = pickle.load(f)
    tornado.ioloop.IOLoop.instance().start()
