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
        category = int(get_dict['category'][0])
        model.train([get_url_text(get_dict['site'][0])],[category]);
        self.write({"results": "done"})

class SaveHandler(tornado.web.RequestHandler):
    def get(self):
        with open(model_file_name, 'wb') as f:
            pickle.dump(model, f)
        
        self.write({"results": "done"})

class URLHandler(tornado.web.RequestHandler):
    def post(self):
        urls = filter(lambda u: str(u) != 'None', [str(url) for url in json.loads(self.get_argument('sites'))])
        inner_texts = []
        for url in urls:
            print url
            inner_texts.append(get_url_text(url))
        
        predictions = [model.predict(text) for text in inner_texts]
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
