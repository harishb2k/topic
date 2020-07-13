import tensorflow as tf

tf.compat.v1.disable_eager_execution()

# We need a placeholder first - this is a constant
# A placeholder is a actual var
# Why can't i use a normal python var "y"
#       Tensorflow needs to create a execution graph. So it needs a place to store a value
#       of y in the graph
y = tf.compat.v1.placeholder("float")

# Why this is a var not placeholder?
#   Tensorflow will update only during optimization.
#   For example if you have weights in [(x * W) + B] then you will have to create W and B as Variable
#   Tensorflow will update value fo W and B in each iteration.
x = tf.compat.v1.Variable([1.0], name="x")

init = tf.compat.v1.global_variables_initializer()

# This is out model - tenserflow will try to solve this equation
y_model = tf.multiply(x, x) + 4

# Optimizer graph
opt = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.001)
error = tf.square(y - y_model)
train = opt.minimize(error)

with tf.compat.v1.Session() as session:
    session.run(init)
    for step in range(100):
        session.run(train, feed_dict={y: 13})
        x_value = session.run(x)
        print("Predicted model: {a:.3f}x ".format(a=x_value[0]))
