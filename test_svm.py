import pandas as pd
import os
import csv
import pickle
from sklearn import svm

#global train_data
#global train_labels

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
                data.append(l)
                labels.append(list(row[6]))
    train_data = pd.DataFrame(data, columns=('HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HST', 'AST', 'HC', 'AC'))
    train_labels = pd.DataFrame(labels)
    # print train_data
    # print train_labels
    pickle.dump(train_data, open('train_data.txt', 'w'))
    pickle.dump(train_labels, open('train_labels.txt', 'w'))

    return train_data, train_labels





def main():
    print(process_data())


main()


