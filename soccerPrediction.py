import preprocessor
import logisticRegression
import evaluator


def main():
    print 'Accuracies'
    print 'k\tBinary \tMulticlass'
    for k in range(3,7):
        # 2 class classification
        X_train, y_train = preprocessor.get_binary_train_features(k)
        mlr_model = logisticRegression.perform_binary_logistic_regression(X_train, y_train)

        X_test, y_test = preprocessor.get_binary_test_features(k)
        pred_y = mlr_model.predict(X_test)

        binary_accuracy = evaluator.calculate_accuracy(y_test, pred_y)
        binary_accuracy = round(binary_accuracy, 2)

        #Classification with 3 classes
        X_train, y_train = preprocessor.get_multiclass_train_features(k)
        mlr_model = logisticRegression.perform_multiclass_logistic_regression(X_train, y_train)

        X_test, y_test = preprocessor.get_multiclass_test_features(k)
        pred_y = mlr_model.predict(X_test)

        multiclass_accuracy = evaluator.calculate_accuracy(y_test, pred_y)
        multiclass_accuracy = round(multiclass_accuracy, 2)
        print str(k) + '\t' + str(binary_accuracy) + '     \t' + str(multiclass_accuracy)

main()

