import numpy as np

from math import sqrt

CLASS_INDEX = 0


class KNN(object):

    def __init__(self, k, data_set):
        self.k = k
        self.data_set = data_set
        self.data_set_len = len(self.data_set)

    @staticmethod
    def euclidean_distance(v1, v2):
        """
        Function to calculate the Euclidean distance between 2 vectors.

        :param v1: The first vector.
        :param v2: The second vector.
        :return: A floating number denoting the Euclidean distance between 2 vectors.
        """
        distance = 0

        # Calculate distance (a1 - b1) ^ 2 + (a2 -b2) ^ 2 + ... + (an - bn) ^ 2
        for i in range(len(v1)):
            distance += pow(v1(i) - v2(i), 2)

        # Return the square root of that distance
        return sqrt(distance)

    def predict(self, trained_data, sample_data_point):
        # Get K nearest neighbors for the sample data point
        return 1.0

    def evaluate(self):
        """
        Evaluate the accuracy of the model using the K-fold cross validation.

        :return: The accuracy as a floating point integer.
        """
        correct_count = 0
        for i in range(self.data_set_len):

            # Leave one piece of data out
            sample_data_for_testing = self.data_set[i]

            # Take the rest of the data for training
            trained_data = np.concatenate((self.data_set[:i], self.data_set[(i + 1):]))

            # Predict
            predicted_class = self.predict()

            # Check the predicted class and adjust the correct count
            if predicted_class == sample_data_for_testing[0]:
                correct_count = correct_count + 1

        return correct_count / self.data_set_len
