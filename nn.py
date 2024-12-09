"@makarwu - nn.ipynb all in one go"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r"./data/train.csv")

data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_, m_train = X_train.shape

def init_param():
    w1 = np.random.rand(10, 784)-0.5
    b1 = np.random.rand(10, 1)-0.5
    w2 = np.random.rand(10, 10)-0.5
    b2 = np.random.rand(10, 1)-0.5
    return w1, b1, w2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def derivative_ReLU(Z):
    return Z>0

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A

def forward_prop(w1, b1, w2, b2, X):
    z1 = w1.dot(X)+b1
    a1 = ReLU(z1)
    z2 = w2.dot(a1)+b2
    a2 = softmax(z2)
    return z1, a1, z2, a2

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def back_prop(z1, a1, z2, a2, w2, Y, X):
    one_hot_Y = one_hot(Y)
    dZ2 = a2-one_hot_Y # NOTE: shouldn't it be 2*(A2-Y)? Since the error at the final layer should be (A2-Y)^2
    dW2 = 1/m * dZ2.dot(a1.T)
    db2 = 1/m * np.sum(dZ2)
    dZ1 = w2.T.dot(dZ2) * derivative_ReLU(z1)
    dW1 = 1/m * dZ1.dot(X.T)
    db1 = 1/m * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1-alpha*dW1
    b1 = b1-alpha*db1
    W2 = W2-alpha*dW2
    b2 = b2-alpha*db2
    return W1, b1, W2, b2

def get_predictions(a2):
    return np.argmax(a2, 0)

def get_accuracy(predictions, Y):
    print(predictions, Y)
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, iterations, alpha):
    w1, b1, w2, b2 = init_param()
    for i in range(iterations):
        z1, a1, z2, a2 = forward_prop(w1, b1, w2, b2, X)
        dW1, db1, dW2, db2 = back_prop(z1, a1, z2, a2, w2, Y, X)
        w1, b1, w2, b2 = update_params(w1, b1, w2, b2, dW1, db1, dW2, db2, alpha)
        if i%10 == 0:
            print("iterations: ", i)
            print("Accuracy: ", get_accuracy(get_predictions(a2), Y))
    return w1, b1, w2, b2

if __name__ == "main":
    w1, b1, w2, b2 = gradient_descent(X_train, Y_train, 500, 0.1)

    def make_predictions(X, W1, b1, W2, b2):
        _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
        predictions = get_predictions(A2)
        return predictions
    
    def test_prediction(index, W1, b1, W2, b2):
        current_image = X_train[:, index, None]
        prediction = make_predictions(X_train[:, index, None], W1, b1, W2, b2)
        label = Y_train[index]
        print("Prediction: ", prediction)
        print("Label: ", label)

        current_image = current_image.reshape((28, 28)) * 255
        plt.gray()
        plt.imshow(current_image, interpolation='nearest')
        plt.show()
    
    test_prediction(1, w1, b1, w2, b2)