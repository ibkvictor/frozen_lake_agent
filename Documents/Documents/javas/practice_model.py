# dataset
# build model
# train model
# test model

import tensorflow as tf
import pandas as pd
import numpy as np 
import numpy.random as rg
import os
import sys
import tensorflow.keras.datasets.mnist as mnist
sys.path.append("/Users/user/Documents/Documents/javas/neural-networks-and-deep-learning-master/src")

import mnist_loader
test_data, validation_data, training_data = mnist_loader.load_data_wrapper()

class Network:
    def __init__(self, sizes):
        self.sizes = sizes
        self.layers = len(sizes)
        self.biases = [rg.rand(x,1) for x in sizes[:-1]]
        # print (self.weights)
        self.weights = [np.random.randn(y,x) for x, y in zip(sizes[:-1],sizes[1:])]
        # print (self.biases)
        # self.feature = None
        # self.label = None

    def sigmoid(self,z):
        d = 1/1+exp(-z)
        return d

    def exp (self, n):
        e = 2.7182818285
        return e ** n

    def feedforward (self,a):
        for w,b in zip(self.weights, self.biases):
            a = (np.dot(a,w) + b)
            a = sigmoid(a)
        return a

    def SGD(self, train_data, mini_batch_size, epochs, eta, test_data = None):
        train_data = list(train_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)
        n = len(train_data)

        for j in range(epochs):
            np.random.shuffle(train_data)
            batch = [train_data[k:k+mini_batch_size] for k in range(0,n,mini_batch_size)]

            for mini_batch in batch:
                self.update_mini_batch(batch,eta)
            
            if test_data:
                print ("epochs {0}, {1}/{2}").format(j,self.evaluate(test_data),eta)
            else:
                print ("epochs complete {0}").format(j)

    def update_mini_batch(self, batch, eta):
        nabla_w = [np.zeros(np.shape(w)) for w in self.weights ]
        nabla_b = [np.zeros(np.shape(b)) for b in self.biases ]

        for x,y in batch:
            delta_nabla_w, delta_nabla_b = self.backpropagate(x,y)
        
        nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
        nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        self.weights = [w-(eta/len(batch))*nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(batch))*nb for b, nb in zip(self.biases, nabla_b)]
        return (self.weights, self.biases)

    def backpropagate(self, x,y):
        nabla_w = [np.zeros(self.weights) for x in self.weights]
        nabla_b = [np.zeros(self.biases) for x in self.biases]

        activation = x
        activation = [x]
        zs = [] # for the z values
        # do a feed_forward
        for w,b in zip(self.weights, self.biases):
            z = np.dot(w,activation)+b
            zs.append(z)
            activation.append(sigmoid(z))
            

        delta = self.cost_derivative(self.activation[-1],y) * self.sigmoid_prime(zs[-1])
        self.biases[-1] = delta
        self.weights = np.dot(delta, self.activation[-2].transpose)

        for l in range(2, self.layers):
            z = zs[-l]
            sp = self.sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1],delta) * sp
            self.biases[-1] = delta
            self.weights = np.dot(delta, self.activation[-l-1].transpose)
        
    def sigmoid_prime(self,y):
        y = (1-y)*(y)
        return y

    def evaluate(self,train_data):
        evaluation = [np.argmax(self.feedforward(x),y) for x,y in train_data]
        return sum(int( x == y) for x, y in evaluation)

    def cost_derivative (self, output_activation, y):
        c = output_activation - y
        return c

net = Network ([784,30,10])
net.SGD(training_data, 30,10,3.0,test_data=None )
# mnist.load_data(path='mnist.npz')

# biases = [3,6]
# biases = np.reshape(biases, (1,2))
# weight = [1,2,1,1,2,1]
# weight = np.reshape(weight, (3,2))
# y = 3
# activation = y
# activation = [y]
# for a,b in zip(weight,biases):
#     z = np.dot(activation,a) + b
#     activation.append(z)

# print(np.dot(([2],[3],[5],[6]),[4]))