import pandas as pd
import os
import csv
import pickle
import sklearn
from collections import defaultdict


def process_data():
    dir = os.getcwd() + '/data'
    filenames = os.listdir(dir)

    data = []
    labels = []
    for filename in filenames:
        ht_match_count = defaultdict(lambda: 0)
        at_match_count = defaultdict(lambda: 0)
        with open(os.path.join(dir, filename), 'rb') as csvfile:
            reader = csv.reader(csvfile)
            reader.next()
            for row in reader:
                l = list()
                home_team = row[2]
                away_team = row[3]
                ht_match_count[home_team] += 1
                at_match_count[away_team] += 1
                l.append(row[2])
                l.append(row[3])
                l.append(row[4])
                l.append(row[5])
                l.append(row[13])
                l.append(row[14])
                l.append(row[17])
                l.append(row[18])
                l.append(ht_match_count[home_team])
                l.append(at_match_count[away_team])
                data.append(l)
                labels.append(list(row[6]))
    train_data = pd.DataFrame(data, columns=('HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HC', 'AC', 'HTMN', 'ATMN'))
    train_labels = pd.DataFrame(labels)
    # pickle.dump(train_data, open('train_data.txt', 'w'))
    # pickle.dump(train_labels, open('train_labels.txt', 'w'))
    # print train_data
    return train_data, train_labels


def create_dictionaries(data):
    goals = defaultdict(lambda: [])
    corners = defaultdict(lambda: [])
    st = defaultdict(lambda: [])

    # home_goals_list = list()
    # away_goals_list = list()
    # home_corners_list = list()
    # away_corners_list = list()
    # home_st_list = list()
    # away_st_list = list()

    for index, row in data.iterrows():
        goals[row['HomeTeam']].append(int(row['FTHG']))
        goals[row['AwayTeam']].append(int(row['FTAG']))
        corners[row['HomeTeam']].append(int(row['HC']))
        corners[row['AwayTeam']].append(int(row['AC']))
        st[row['HomeTeam']].append(int(row['HST']))
        st[row['AwayTeam']].append(int(row['AST']))

    return goals, corners, st


def create_features(goals, corners, st, data):
    k = 4

    feature_set = pd.DataFrame()
    season_no = -1
    for index, row in data.iterrows():
        if row['HTMN'] <= k or row['ATMN'] <= k:
            continue

        #get past k goals for every match season wise
        if index == 0 or (index + 1) % 380 == 0:
            season_no += 1

        home_team = row['HomeTeam']
        away_team = row['AwayTeam']


def main():
    train_data, train_labels = process_data()
    goals, corners, st = create_dictionaries(train_data)
    create_features(goals, corners, st, train_data)

main()


