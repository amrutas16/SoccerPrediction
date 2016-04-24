def calculate_accuracy(y_test, pred_y):
    t = 0
    for i in range(len(pred_y)):
        if pred_y[i] == y_test[i]:
            t += 1

    return float(t)/float(len(y_test))