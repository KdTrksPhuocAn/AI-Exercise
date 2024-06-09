# Write a function to evaluate a classification model


def evaluate_classification_model(tp, fp, fn):

    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print('Precision:', precision)
    print('Recall: ', recall)
    print('F1-score: ', f1_score)


print('Example 1:')
evaluate_classification_model(2, 3, 4)
print('Example 2:')
evaluate_classification_model('a', 3, 4)
print('Example 3:')
evaluate_classification_model(2, 'a', 4)
print('Example 4:')
evaluate_classification_model(2, 3, 'a')
print('Example 5:')
evaluate_classification_model(2, 3, 0)
print('Example 6:')
evaluate_classification_model(2.1, 3, 0)
