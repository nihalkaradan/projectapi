
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import operator
import sqlite3
import numpy as np
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import os
import statistics

from flask_restful import Resource,Api
app = Flask(__name__)
app.secret_key='nihal'

DATABASE='/home/nihalkaradan/mysite/data.db'
"""class City(Resource):
	def get(self):
		connection=sqlite3.connect(DATABASE)
		cursor=connection.cursor()
		query="SELECT CITY2,SUM(PASSENGERSTOCITY2) FROM test GROUP BY CITY2 ;"
		result=cursor.execute(query)
		#print (result.fetchall())
		z={}
		for k,v in result.fetchall():
			z[k]=v

		return z

		connection.close()"""
def convert_data():
    connection=sqlite3.connect(os.path.abspath('/home/nihalkaradan/mysite/data.db'))
    cursor=connection.cursor()
    query="CREATE TABLE IF NOT EXISTS updata (territory text,city1 real,city2 text,unique(territory,city1,city2));"
    cursor.execute(query)
    query="SELECT CITY1,CITY2 FROM test WHERE CITY2!=0 AND CITY1!=0 ;"
    result=cursor.execute(query)
    dicto={}
    labelp=[]
    i=1
    for k,v in result.fetchall():
        if k in dicto:

            labelp.append(v)
        else:
            dicto[k]=i
            i=i+1

            labelp.append(v)



    query="CREATE TABLE IF NOT EXISTS updata (territory real,city1 real,city2 text,unique(territory,city1,city2));"
    cursor.execute(query)
    X=[]
    zero=[]

    query="SELECT 0,CITY1,CITY2 FROM test WHERE CITY2!=0 AND CITY1!=0 ;"
    result=cursor.execute(query)

    for row in result.fetchall():
        X.append(dicto[row[1]])
        zero.append(row[0])

    kr=[]
    xz= preprocessing.scale(X)

    i=0
    for i in range(len(xz)):
        p=[zero[i],xz[i]]
        kr.append(p)
        i=i+1
    clf=GaussianNB()
    dictlabel={}
    intlabel=[]
    j=1
    for a in labelp:
        if a in dictlabel:
            intlabel.append(dictlabel[a])

        else:
            dictlabel[a]=j
            intlabel.append(dictlabel[a])
            j=j+1

    clf.fit(kr,intlabel)
    dictfin={}
    proba=clf.predict_proba(kr)





    connection.close()
    print("Preprocessed data \n")
    print(kr)
    print("Probability of each label")
    print(proba[0])
    from sklearn.model_selection import train_test_split
    """X_train, X_test, y_train, y_test = train_test_split(kr, intlabel, test_size=0.4, random_state=1)
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred = gnb.predict(X_test)
    from sklearn import metrics
    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)"""


"""def convert_data():
    connection=sqlite3.connect(os.path.abspath('/home/nihalkaradan/mysite/data.db'))
    cursor=connection.cursor()
    query="CREATE TABLE IF NOT EXISTS updata (territory text,city1 real,city2 text,unique(territory,city1,city2));"
    cursor.execute(query)
    query="SELECT CITY1,CITY2 FROM test WHERE CITY2!=0 AND CITY1!=0 ;"
    result=cursor.execute(query)
    dicto={}
    labelp=[]

    i=1
    for k,v in result.fetchall():
        if  k in dicto:
            query="INSERT INTO updata VALUES(0,?,? );"
            cursor.execute(query,(dicto[k],v))
            labelp.append(v)
            continue
        else:
            dicto[k]=i
            i=i+1
            query="INSERT INTO updata VALUES(0,?,? );"
            cursor.execute(query,(dicto[k],v))
            labelp.append(v)


    query="DROP TABLE updata"

    cursor.execute(query)

    query="CREATE TABLE IF NOT EXISTS updata (territory real,city1 real,city2 text,unique(territory,city1,city2));"
    cursor.execute(query)

    p=list(map(int,dicto.values()))
    X= preprocessing.scale(p)
    q=list(dicto.keys())
    dictp = dict(zip(q, X))
    query="SELECT CITY1,CITY2 FROM test WHERE CITY2!=0 AND CITY1!=0 ;"
    result=cursor.execute(query)
    for row in result.fetchall():
        query="INSERT INTO updata VALUES(0,?,?);"
        cursor.execute(query,(dictp[row[0]],row[1]))
        connection.commit()
    query="SELECT territory,city1,city2 FROM updata;"
    x1=[]
    x2=[]
    labelp=[]
    result=cursor.execute(query)
    for row in result:
        x1.append(row[0])
        x2.append(row[1])
        labelp.append(row[2])
    kr=[]
    xz= preprocessing.scale(x2)
    i=0
    for i in range(len(x1)):
        p=[x1[i],xz[i]]
        kr.append(p)
        i=i+1
    print(kr)
    clf=GaussianNB()
    clf.fit(kr,labelp)
    print("Here goes the probability!")
    f=clf.predict_proba(kr)
    print(f.sum())
    q=list(dicto.keys())
    dictp = dict(zip(q, X))
    query="SELECT 0,CITY1,CITY2 FROM test";
    labelp = []
    result=cursor.execute(query)
    for row in result.fetchall():
        if row[1] in dictp:
            query="INSERT INTO updata VALUES(0,?,? );"
            labelp.append(row[1])
            cursor.execute(query,(dictp[k],row[2]))
    Y=labelp
    clf = GaussianNB()
    clf.fit(X, Y)
    print(clf.predict_proba(X))

    connection.close()

    #print(dictp)
    return dicto"""


class City(Resource):
    def get(self):
        connection=sqlite3.connect(os.path.abspath('/home/nihalkaradan/mysite/data.db'))
        cursor=connection.cursor()

        query="SELECT CITY2,SUM(PASSENGERSTOCITY2) FROM test GROUP BY CITY2 ;"
        result=cursor.execute(query)
        z={}

        for k,v in result.fetchall():
            z[k]=v


        print(z)
        sorted_z = sorted(z.items(), key=operator.itemgetter(0))

        connection.close()
        return z
api = Api(app)


@app.route('/nihal')
def nihal():
    connection=sqlite3.connect(os.path.abspath('/home/nihalkaradan/mysite/data.db'))
    cursor=connection.cursor()
    query="SELECT CITY2,SUM(PASSENGERSTOCITY2) FROM test GROUP BY CITY2 ;"
    result=cursor.execute(query)
    z={}

    for k,v in result.fetchall():
        z[k]=v
    connection.close()
    print(z)
    return os.path.abspath('/home/nihalkaradan/mysite/data.db')
@app.route('/')
def hello_world():
    convert_data()
    return 'Preprocessing completed !Gaussian Naive Bayes classification completed! \n '
api.add_resource(City,'/city')
