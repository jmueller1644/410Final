import re
from cStringIO import StringIO
from stemming.porter2 import stem
import string
import numpy as np

from sklearn import svm
from sklearn.multiclass import OneVsOneClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import HashingVectorizer

from sklearn.pipeline import Pipeline



def normalize_text(text):
    return string.join([stem(w) for w in filter(lambda x: (x in string.printable) and (not (x in string.punctuation)), text.lower()).split(" ")]," ")

class OffLineSKLearner:
    __pipeline=None
    def __init__(self, pipe):
        self.__pipeline=pipe
        
    def predict(self, doc):
        return self.__pipeline.predict([normalize_text(doc)])[0]
    
    def train( self,docs,classifications ):
        raise NotImplementedError( "This is an offline learner" )
    
class OnLineSKLearner:
    __transformers=None
    __classifier=None
    def __init__(self, t, c, docs, targets):
        self.__transformers=t
        self.__classifier=c
        toFit=docs
        for trans in self.__transformers:
            toFit=trans.fit_transform(toFit)
        self.__classifier.partial_fit(toFit, targets, np.array([0, 1, 2]))
        
    def transform(self, docs):
        d=[normalize_text(i) for i in docs]
        for t in self.__transformers:
            d=t.transform(d)
        return d
        
    def predict(self, doc):
        return self.__classifier.predict(self.transform([doc]))[0]
    
    def train( self,docs,classifications ):
        self.__classifier.partial_fit(self.transform(docs),np.array(classifications))

def learnPipe(cat1,cat2,cat3,feature_type,learner_type):
    clf=None
    if learner_type=="svm":
        clf=svm.SVC(verbose=True)
    elif learner_type=="svm_ava":
        clf=OneVsOneClassifier(svm.SVC(verbose=True))
    elif learner_type=="knn":
        clf=KNeighborsClassifier(weights='distance')
    else:
        raise NameError('Not a valid learner')

    if feature_type=="tfidf":
        text_clf = Pipeline([('vect', CountVectorizer()),
                            ('tfidf', TfidfTransformer()),
                            ('clf', clf)])
    elif feature_type=="tf":
        text_clf = Pipeline([('vect', CountVectorizer()),
                            ('tfidf', TfidfTransformer(use_idf=False)),
                            ('clf', clf)])
    elif feature_type=="bw":
        text_clf = Pipeline([('vect', CountVectorizer()),
                            ('clf', clf)])
    elif feature_type=="hashing":
        text_clf = Pipeline([('vect', HashingVectorizer(decode_error='ignore', n_features=2 ** 17, non_negative=True)),
                            ('clf', clf)])
    else:
        raise NameError('Not a valid learner')

    targets=[]
    for t in cat1:
        targets.append(0)
    for t in cat2:
        targets.append(1)
    for t in cat3:
        targets.append(2)
    text_clf.fit(cat1+cat2+cat3, np.array(targets))
    return OffLineSKLearner(text_clf)

def learnOnlineLearner(cat1,cat2,cat3,feature_type,learner_type):
    clf=None
    if learner_type=="sgd":
        clf=linear_model.SGDClassifier()
    elif learner_type=="multinomial_nb":
        clf=MultinomialNB(alpha=0.01)
    elif learner_type=="passive_aggresive":
        clf=linear_model.PassiveAggressiveClassifier()
    elif learner_type=="perceptron":
        clf=linear_model.Perceptron()
    else:
        raise NameError('Not a valid learner')

    if feature_type=="tfidf":
        transformers=[CountVectorizer(), TfidfTransformer()]
    elif feature_type=="tf":
        transformers=[CountVectorizer(), TfidfTransformer(use_idf=False)]
    elif feature_type=="bw":
        transformers=[CountVectorizer()]
    elif feature_type=="hashing":
        transformers = [HashingVectorizer(decode_error='ignore', n_features=2 ** 17, non_negative=True)]
    else:
        raise NameError('Not a valid learner')

    targets=[]
    for t in cat1:
        targets.append(0)
    for t in cat2:
        targets.append(1)
    for t in cat3:
        targets.append(2)
    return OnLineSKLearner(transformers,clf,cat1+cat2+cat3,np.array(targets))
