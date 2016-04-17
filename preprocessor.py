import pandas as pd
import os
import csv
from collections import defaultdict
k = 4


def process_data():
    dir = os.getcwd() + '/data'
    filenames = os.listdir(dir)

    data = []
    labels = []
    features = []
    class_labels = []
    for filename in filenames:
        ht_match_count = defaultdict(lambda: 0)
        at_match_count = defaultdict(lambda: 0)
        with open(os.path.join(dir, filename), 'rb') as csvfile:
            reader = csv.reader(csvfile)
            reader.next()
            for row in reader:
                home_team = row[2]
                away_team = row[3]
                ht_match_count[home_team] += 1
                at_match_count[away_team] += 1
                l = [home_team, away_team, row[4], row[5], row[13], row[14], row[17], row[18], ht_match_count[home_team]
                    ,at_match_count[away_team], row[6]]
                data.append(l)
                # labels.append(list(row[6]))
        data = pd.DataFrame(data, columns=('HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HC', 'AC', 'HTMN', 'ATMN', 'FTR'))
        # print data
        home_goals, home_corners, home_st, away_goals, away_corners, away_st = create_dictionaries(data)
        features, class_labels = create_features(home_goals, home_corners, home_st, away_goals, away_corners, away_st, data, features, class_labels)

    return features, class_labels


def create_dictionaries(data):
    home_goals = defaultdict(lambda: [])
    home_corners = defaultdict(lambda: [])
    home_st = defaultdict(lambda: [])
    away_goals = defaultdict(lambda: [])
    away_corners = defaultdict(lambda: [])
    away_st = defaultdict(lambda: [])

    for index, row in data.iterrows():
        home_goals[row['HomeTeam']].append(int(row['FTHG']))
        away_goals[row['AwayTeam']].append(int(row['FTAG']))
        home_corners[row['HomeTeam']].append(int(row['HC']))
        away_corners[row['AwayTeam']].append(int(row['AC']))
        home_st[row['HomeTeam']].append(int(row['HST']))
        away_st[row['AwayTeam']].append(int(row['AST']))

    return home_goals, home_corners, home_st, away_goals, away_corners, away_st


def create_features(home_goals, home_corners, home_st, away_goals, away_corners, away_st, data, features, class_labels):
    for index, row in data.iterrows():
        home_match_no = row['HTMN']
        away_match_no = row['ATMN']
        result = row['FTR']
        if home_match_no <= k or away_match_no <= k:
            continue

        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        home_g_avg = 0
        away_g_avg = 0
        home_c_avg = 0
        away_c_avg = 0
        home_st_avg = 0
        away_st_avg = 0

        for i in range(home_match_no - k - 1, home_match_no - 1):
            home_g_avg += home_goals[home_team][i] / k
            home_c_avg += home_corners[home_team][i] / k
            home_st_avg += home_st[home_team][i] / k

        for i in range(away_match_no - k - 1, away_match_no - 1):
            away_g_avg += away_goals[away_team][i] / k
            away_c_avg += away_corners[away_team][i] / k
            away_st_avg += away_st[away_team][i] / k

        l = [home_g_avg - away_g_avg, home_c_avg - away_c_avg, home_st_avg - away_st_avg]
        features.append(l)
        class_labels.append(result)

    return features, class_labels





