from sklearn import linear_model


def perform_logistic_regression(x, y):
    lr = linear_model.LogisticRegression(multi_class='multinomial', solver='lbfgs')
    model = lr.fit(x, y)
    return model
