__author__ = 'Vaibhav'

import pandas as pd
import os
import csv
import pickle

from sklearn import svm
from sklearn import preprocessing

global test_data
global train_labels

def process_data():
    dir = os.getcwd() + '/data'
    filenames = os.listdir(dir)

    data = []
    labels = []
    for filename in filenames:
        with open(os.path.join(dir, filename), 'rb') as csvfile:
            reader = csv.reader(csvfile)
            reader.next()
            for row in reader:
                l = list()
                l.append(row[1])
                l.append(row[2])
                l.append(row[3])
                l.append(row[4])
                l.append(row[5])
                l.append(row[13])
                l.append(row[14])
                l.append(row[17])
                l.append(row[18])
                l.append(row[6])
                data.append(l)
                labels.append(list(row[6]))
    test_data = pd.DataFrame(data, columns=('Div','HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HC', 'AC','FTR'))

    pickle.dump(test_data, open('train_data.txt', 'w'))

    return test_data


def generate_features(test_data):

    feature_vector=[['Div','Team','Home Goals','Away Goals','Home Goals Against','Away Goals Against', 'Shorts on Target Ratio','Corners']]
    all_teams=test_data['HomeTeam'].unique()

    for team in all_teams:
        all_rows=test_data[test_data['HomeTeam']==team or test_data['AwayTeam']==team]
        for div in xrange(1,39):
            if(all_rows['Div']=div)



def main():
    global test_data
    global train_labels
    test_data=process_data()
    final_features= generate_features(test_data)