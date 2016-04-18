import preprocessor
import logisticRegression


def main():
    X_train, y_train = preprocessor.get_features('train')
    mlr_model = logisticRegression.perform_logistic_regression(X_train, y_train)

    X_test, y_test = preprocessor.get_features('test')
    pred_probabilities = mlr_model.predict_proba(X_test)
    classes = mlr_model.classes_
    pred_y_test = []

    for p in pred_probabilities:
        class_index = get_class_index(p)
        pred_y_test.append(classes[class_index])

    t = 0
    for i in range(len(y_test)):
        if y_test[i] == pred_y_test[i]:
            t += 1

    print t
    print len(y_test)
    print float(t)/float(len(y_test))


def get_class_index(p):

    max_value = 0.0
    max_index = 0
    for i in range(0, len(p)):
        value = p[i]
        if value > max_value:
            value = max_value
            max_index = i
    return max_index


main()

