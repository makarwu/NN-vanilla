## Simple digit classification from Scratch

### Problem statement

The dataset we're working with is the MNIST handwritten digits dataset, commonly used for instructive ML and computer vision projects. It contains 28x28 grayscale images of handwritten digits that look like this:

Our network will have three layers total: an input layer and two layers with parameters. Because the input layer has no parameters, this network would be referred to as a two-layer neural network.

The input layer has 784 nodes, corresponding to each of the 784 pixels in the 28x28 input image. Each pixel has a value between 0 and 255, with 0 being black and 255 being white. It's common to normalize these values getting all values between 0 and 1, here by simply dividing by 255 before feeding them in the network.

The second layer, or hidden layer, could have any amount of nodes, but we've made it really simple here with just 10 nodes. The value of each of these nodes is calculated based on weights and biases applied to the value of the 784 nodes in the input layer. After this calculation, a ReLU activation is applied to all nodes in the layer.

The output layer also has 10 nodes, corresponding to each of the output classes (digits 0 to 9). The value of each of these nodes will again be calculated from weights and biases applied to the value of the 10 nodes in the hidden layer, with a softmax activation applied to them to get the final output.

![alt text](./img/Bildschirmfoto%202024-12-09%20um%2012.08.44.png)

The process of taking an image input and running through the neural network to get a prediction is called **forward propagation**. The prediction that is made from a given image depends on the **weights and biases, or parameters**, of the network.
