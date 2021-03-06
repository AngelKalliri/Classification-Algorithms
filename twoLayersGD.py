# Pattern Recognition 2020: Assignment 1    |      Kalliri Angeliki     A.M. 2446 #
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPClassifier


# Classification algorithm 2b: Neural Network with 2 hidden layers & Gradient Descent (GD) #
# train_set & test_set, that are passed, keep the Y category info
def nn2_gd_algorithm(train_set, test_set, k1, k2):
    nn2_gd_metrics = []
    # Store the last column (Y category)
    y_train = train_set[:, len(train_set[0]) - 1]
    y_test = test_set[:, len(test_set[0]) - 1]

    # Delete the columns from the sets
    x_train = np.delete(train_set, len(train_set[0]) - 1, 1)
    x_test = np.delete(test_set, len(test_set[0]) - 1, 1)

    train_size = len(x_train)

    # Batch size: number of training examples used. SGD -> DG, batch size must have the size of the training set
    mlp = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(k1, k2), batch_size=train_size,
                        max_iter=500)       # epochs = 200 (max_iter)

    mlp.fit(x_train, y_train)
    y_pred = mlp.predict(x_test)

    # Compute confusion_matrix = [TP FP]
    #                            [FN TN]
    matrix = np.array(confusion_matrix(y_test, y_pred))

    # Metrics calculation
    accuracy = (matrix[0][0] + matrix[1][1]) / np.sum(matrix)
    precision = matrix[0][0] / (matrix[0][0] + matrix[0][1])    # Precision = TP / TP + FP
    recall = matrix[0][0] / (matrix[0][0] + matrix[1][0])       # Recall = TP / TP + FN
    f1score = 2 * ((precision * recall) / (precision + recall))
    nn2_gd_metrics.append(accuracy)
    nn2_gd_metrics.append(f1score)

    return nn2_gd_metrics
