import pickle
from inputReading import get_url_text

models=dict();
for p in [#"bw_knn_model.p","bw_svm_ava_model.p","bw_svm_model.p",
          #"tf_knn_model.p","tf_svm_ava_model.p","tf_svm_model.p",
          #"tfidf_knn_model.p","tfidf_svm_ava_model.p","tfidf_svm_model.p",
            "tfidf_sgd_model.p","tfidf_perceptron_model.p","tfidf_multinomial_nb_model.p"]:
    with open(p,"rb") as f:
        models[p]=pickle.load(f)
def compareLearners(url):
    text=get_url_text(url)
    for (n,m) in models.items():
        print n, m.predict(text);

