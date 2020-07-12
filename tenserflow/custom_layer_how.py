import tensorflow as tf
from tensorflow import keras


class Linear(keras.layers.Layer):
    def __init__(self, units=32, input_dim=32):
        super(Linear, self).__init__()

        # We should have weights as random - for this case using simple var to debug
        r = tf.constant([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]])
        self.w = tf.Variable(
            initial_value=r,
            trainable=True,
        )

        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(units,)), trainable=True
        )

    def call(self, inputs, **kwargs):
        print("Input")
        print(inputs)
        print("W")
        print(self.w)
        print("B")
        print(self.b)
        return tf.matmul(inputs, self.w) + self.b


# Training input - our input has 2 features i.e. we have 2 var input
# Example - 2 feature for house cost will be "area", "no of bedrooms"
#
# Sample 1 - [1.0, 1.0] is first sample e.g. area=1.0, no_of_bedroom=2
# Sample 2 - [2.0, 2.0] is first sample e.g. area=2.0, no_of_bedroom=2
# Sample 3 - [3.0, 3.0] is first sample e.g. area=2.0, no_of_bedroom=3
training_input = tf.constant([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])

# First param  = units      -> this is 3 in this case i.e. no of samples
# Second param = input_dim  -> "no of features" or "no of dimension" in our input. Here it is 2 (area, no of bedrooms)
linear_layer = Linear(3, 2)

# This will call our "call" function
y = linear_layer(training_input)

# What is done in "call method"
# [1. 1.]         [1., 1., 1.]                         [3. 3. 3.]
# [2. 2.]   *     [2., 2., 2.]  + "B"     =            [6. 6. 6.]
# [3. 3.]                                              [9. 9. 9.]

print(y)
