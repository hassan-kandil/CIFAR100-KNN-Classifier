import numpy as np

class KNearestNeighbor(object):
    #http://cs231n.github.io/classification/
    def __init__(self):
        pass

    def train(self,X, y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        # the nearest neighbor classifier simply remembers all the training data
        self.data = X
        self.labels = y

    def predict(self,X,k,l='L2'):
        """ X is N x D where each row is an example we wish to predict label for """
        num_test = X.shape[0]
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype = self.labels.dtype)
        # loop over all test rows
        for i in xrange(num_test):
            # find the nearest training example to the i'th test example
            if l == 'L1':
                # using the L1 distance (sum of absolute value differences)
                distances = np.sum(np.abs(self.data - X[i,:]), axis = 1)
            else:
                distances = np.sqrt(np.sum(np.square(self.data - X[i,:]), axis = 1))
            
            kdistances = distances.argsort()[:k]
            #print (kdistances)
            labelscount = np.zeros((20,))
         #   knnlabels = self.labels[kdistances] #sort the distances and store the labels of the k nearest cells
       #     knncount = np.bincount(knnlabels) #get the count of the labels (count of each superclass)
            for t in kdistances:
                nlabel = self.labels[t]
                labelscount[nlabel] += 1
            Ypred[i] = np.argmax(labelscount) # predict the label using the label of the class with the highest count
    
        return Ypred