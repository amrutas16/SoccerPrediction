import pandas as pd
import os
import csv
import pickle

from sklearn import svm
from sklearn import preprocessing

global train_data
global train_labels

#Processing the initial data
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
    train_data = pd.DataFrame(data, columns=('HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HC', 'AC','FTR'))
    train_labels = pd.DataFrame(labels)
    # print train_data
    # print train_labels
    pickle.dump(train_data, open('train_data.txt', 'w'))
    pickle.dump(train_labels, open('train_labels.txt', 'w'))



    return train_data, train_labels


#generating training features

def generate_features(train_data,train_labels):
    #feature_vector=[['Team','Home Goals','Away Goals','Home Goals Against','Away Goals Against', 'Shorts on Target Ratio','Corners','Win Percentage']]

    feature_vector=[['Team','Total Goals','Total Goals Against','Shorts on Target','Corners','Win Percentage']]

    home_goals=[]
    away_goals=[]
    home_goals_against=[]
    away_goals_against=[]
    corners_1=[]
    corners_2=[]
    home_shorts_target=[]
    away_shorts_target=[]
    home_win= 0
    away_win= 0
    all_teams=train_data['HomeTeam'].unique()
    for team in all_teams:

#counting the home features
        home_rows=train_data[train_data['HomeTeam']==team]
        home_games= float(len(home_rows.index))
        home_win = float(len(home_rows[home_rows['FTR']=='H'].index))/home_games
        #print home_win
        home_goals=map(float,home_rows['FTHG'])
        home_goals_against=map(float,home_rows['FTAG'])
        home_shorts_target=map(float,home_rows['HST'])
        corners_1=map(float,home_rows['HC'])

#counting the away features
        away_rows=train_data[train_data['AwayTeam']==team]
        away_games=float(len(away_rows.index))
        away_win=float(len(away_rows[away_rows['FTR']=='A'].index))/away_games
        total_away_matches=len(away_rows.index)
        away_goals=map(int,away_rows['FTAG'])
        away_goals_against=map(int,away_rows['FTHG'])
        away_shorts_target=map(int,away_rows['AST'])
        corners_2=map(int,home_rows['AC'])

        total_games= home_games+away_games

        feature_vector.append([team,(sum(home_goals)+1.5*sum(away_goals))/total_games,(-1.5*sum(home_goals_against)-1*sum(away_goals_against))/total_games,(sum(corners_1)+sum(corners_2))/total_games,(sum(away_shorts_target)+sum(home_shorts_target))/total_games,(home_win+away_win)])
    for feature in feature_vector:
        print feature

    return feature_vector



def main():
    global train_data
    global train_labels
    train_data,train_labels=process_data()
    final_features=generate_features(train_data,train_labels)
    with open("R_data_load/aggregated_features.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(final_features)

#print(train_data['HomeTeam'])

main()