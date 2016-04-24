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
    dir = os.getcwd() + '/finaltest'
    filenames = os.listdir(dir)

    data = []
    labels = []
    for filename in filenames:
        with open(os.path.join(dir, filename), 'rb') as csvfile:
            reader = csv.reader(csvfile)
            reader.next()
            for row in reader:
                l = list()
                l.append(row[0])
                l.append(row[2])
                l.append(row[3])
                l.append(row[4])
                l.append(row[5])
                l.append(row[13])
                l.append(row[14])
                l.append(row[17])
                l.append(row[18])
                data.append(l)
                labels.append(list(row[6]))
    test_data = pd.DataFrame(data, columns=('Div','HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HC', 'AC'))

    pickle.dump(test_data, open('test_data.txt', 'w'))
    print "You are Here"
    return test_data


def generate_features(test_data):
    print "You are here"
    #feature_vector=[['Home Goals','Away Goals','Home Goals Against','Away Goals Against','Corners']]
    feature_vector=[['Total Goals','Total Goals Against','Shorts on Target','Corners']]

    all_teams=test_data['HomeTeam'].unique()

    for team in all_teams:
        print team
    print len(all_teams)

    for team in all_teams:
        #print "You are Here 3"
        all_rows = test_data[(test_data['HomeTeam']==team) | (test_data['AwayTeam']==team)]
        #print(all_rows)
        div=1
        while(div<38):
            row=all_rows[all_rows['Div']==str(div)]
            if row.empty:
                feature_vector.append(feature_vector[div-1])
                div=div+1
                continue
            print row
            for index,row in row.iterrows():
                print div
                #print row
                if team in row['HomeTeam']:
                    home_goals=float(row['FTHG'])
                    print home_goals
                    away_goals=0.0
                    home_goals_against=float(row['FTAG'])
                    away_goals_against=0.0
                    home_shorts_target=float(row['HST'])
                    corners_1=float(row['HC'])

                    if(div==1):

                        feature_vector.append([home_goals+away_goals,-1.5*home_goals_against-away_goals_against,home_shorts_target,corners_1])
                        div=div+1
                    else:
                        temp_vector=[home_goals + away_goals,-1.5*home_goals_against-away_goals_against,home_shorts_target,corners_1]
                        c=[x+y for x,y in zip(feature_vector[div-1],temp_vector)]
                        c=[x/float(div) for x in c]
                        #c.append(team)
                        feature_vector.append(c)
                        div=div+1
                else:
                    home_goals=0.0
                    away_goals=float(row['FTAG'])
                    home_goals_against=0.0
                    away_goals_against=float(row['FTHG'])
                    away_shorts_target=float(row['AST'])
                    corners_1=float(row['AC'])

                    if(div==1):
                        feature_vector.append([home_goals+1.5*away_goals,-1.5*home_goals_against-1*away_goals_against,away_shorts_target,corners_1])
                        div=div+1
                    else:
                        temp_vector=[home_goals+1.5*away_goals,-1.5*home_goals_against-1*away_goals_against,away_shorts_target,corners_1]
                        c=[x+y for x,y in zip(feature_vector[div-1],temp_vector)]
                        c=[x/float(div) for x in c]
                        #c.append(team)
                        feature_vector.append(c)
                        div=div+1
    for feature in feature_vector:
        print feature

    return feature_vector



def main():
    global test_data
    global train_labels
    test_data=process_data()
    print(test_data)
    final_features= generate_features(test_data)
    with open("test/test_features.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(final_features)

main()