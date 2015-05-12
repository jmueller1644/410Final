import re
from cStringIO import StringIO
from stemming.porter2 import stem
import string
import numpy as np

from sklearn import svm
from sklearn.multiclass import OneVsOneClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.pipeline import Pipeline

def learn(cat1,cat2,cat3,feature_type,learner_type):
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
    return text_clf

def predict(learner,doc):
    return learner.predict(doc)
