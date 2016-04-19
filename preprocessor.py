import pandas as pd
import os
import csv
from collections import defaultdict
k = 4


def get_features(d):
    dir = os.getcwd() + '/data/' + d
    filenames = os.listdir(dir)
   
    data = []
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

        data = pd.DataFrame(data, columns=('HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HC', 'AC', 'HTMN', 'ATMN', 'FTR'))

        home_goals, home_corners, home_st, away_goals, away_corners, away_st = create_dictionaries(data)

        if d == 'train':
            features, class_labels = create_train_features(home_goals, home_corners, home_st, away_goals, away_corners, away_st, data, features, class_labels)

        if d == 'test':
            features, class_labels = create_test_features(home_goals, home_corners, home_st, away_goals, away_corners, away_st, data, features, class_labels)

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
        if int(row['HST']) == 0:
            home_st[row['HomeTeam']].append(0)
        else:
            home_st[row['HomeTeam']].append(int(row['FTHG']) / int(row['HST']))
        if int(row['AST']) == 0:
            away_st[row['AwayTeam']].append(0)
        else:
            away_st[row['AwayTeam']].append(int(row['FTAG']) / int(row['AST']))

    return home_goals, home_corners, home_st, away_goals, away_corners, away_st


def create_test_features(home_goals, home_corners, home_st, away_goals, away_corners, away_st, data, features, class_labels):
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
            home_st_avg += (home_st[home_team][i]) / k

        for i in range(away_match_no - k - 1, away_match_no - 1):
            away_g_avg += away_goals[away_team][i] / k
            away_c_avg += away_corners[away_team][i] / k
            away_st_avg += away_st[away_team][i] / k

        if home_st_avg == 0:
            h = 0.0
        else:
            h = home_g_avg/home_st_avg

        if away_st_avg == 0:
            a = 0.0
        else:
            a = away_g_avg/away_st_avg

        l = [home_g_avg - away_g_avg, home_c_avg - away_c_avg, h - a]
        features.append(l)
        class_labels.append(result)

    return features, class_labels


def create_train_features(home_goals, home_corners, home_st, away_goals, away_corners, away_st, data, features, class_labels):
    for index, row in data.iterrows():
        # home_match_no = row['HTMN']
        # away_match_no = row['ATMN']
        result = row['FTR']
        # if home_match_no <= k or away_match_no <= k:
        #     continue

        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        hg = int(row['FTHG'])
        ag = int(row['FTAG'])
        hc = int(row['HC'])
        ac = int(row['AC'])
        hst = int(row['HST'])
        ast = int(row['AST'])

        # home_g_avg = 0
        # away_g_avg = 0
        # home_c_avg = 0
        # away_c_avg = 0
        # home_st_avg = 0
        # away_st_avg = 0

        # for i in range(home_match_no - k - 1, home_match_no - 1):
        #     home_g_avg += home_goals[home_team][i] / k
        #     home_c_avg += home_corners[home_team][i] / k
        #     home_st_avg += home_st[home_team][i] / k
        #
        # for i in range(away_match_no - k - 1, away_match_no - 1):
        #     away_g_avg += away_goals[away_team][i] / k
        #     away_c_avg += away_corners[away_team][i] / k
        #     away_st_avg += away_st[away_team][i] / k

        if hst == 0:
            h = 0.0
        else:
            h = hg/hst

        if ast == 0:
            a = 0.0
        else:
            a = ag/ast

        l = [hg - ag, hc - ac, h - a]
        features.append(l)
        class_labels.append(result)

    return features, class_labels



