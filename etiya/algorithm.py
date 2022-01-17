import pandas as pd
import numpy as np
import pickle
import sqlite3
from sqlite3 import Error
import time
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_score, accuracy_score, recall_score
import sys
import os


# def create_data(file):
#      df = pd.read_excel(file)
#      return df['text'].tolist(), df['label'].tolist()

def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("db.sqlite3")
    except Error as e:
        print(e)

    return conn

def select_all_data(conn):
    """
    Query all rows in the table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT text,label FROM crud_data")

    rows = cur.fetchall()
    text_list = []
    label_list = []
    for sublist in rows:
        for val in sublist:
            if val.startswith('Confirmation'):
                label_list.append(val)
            else:
                text_list.append(val)
    print(text_list)
    print(label_list)
    return text_list, label_list

# def test():
#     print("bu bir test")

#feature extraction - creating a tf-idf matrix
def tfidf(data, ma = 0.6, mi = 0.0001):
    print(data)
    print("data")
    tfidf_vectorize = TfidfVectorizer()
    tfidf_data = tfidf_vectorize.fit_transform(data)
    return tfidf_data, tfidf_vectorize


#SVM classifier
def test_SVM(x_train, x_test, y_train, y_test):
    SVM = SVC(kernel = 'linear', probability=True)
    SVMClassifier = SVM.fit(x_train, y_train)
    predictions = SVMClassifier.predict(x_test)
    a = accuracy_score(y_test, predictions)
    p = precision_score(y_test, predictions, average = 'weighted')
    r = recall_score(y_test, predictions, average = 'weighted')
    return SVMClassifier, a, p, r



def dump_model(model, file_output):
    pickle.dump(model, open(file_output, 'wb'))

def load_model(file_input):
    return pickle.load(open(file_input, 'rb'))
		
# GET DATA
# file = "test_data.xlsx"
# text, label = create_data(file)
# print(text,label)
def start():
    conn = create_connection()
    text, label = select_all_data(conn)
    # TRAIN
    training, vectorizer = tfidf(text)
    print(training, vectorizer)
    import warnings
    warnings.filterwarnings('ignore')

    x_train, x_test, y_train, y_test = train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    print(model,accuracy, precision, recall)
    dump_model(model, 'model.pickle')
    dump_model(vectorizer, 'vectorizer.pickle')
    return "train completed"

# PREDICTION
def prediction(user_text):
    model = load_model('model.pickle')
    vectorizer = load_model('vectorizer.pickle')
    res = vectorizer.transform([user_text])
    result = model.predict_proba(res).tolist()
    return result
