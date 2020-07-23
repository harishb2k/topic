import tensorflow as tf

# We can calculate differentiation of a matrix using "matrix calculus"
# https://explained.ai/matrix-calculus/
#
# Matrix Calculus defines some rules to make operations easy e.g. vector W and vector B multiplication can be calculated
# with pre-defined formula:
# Δy/Δw = diag(b)
# Δy/Δb = diag(w)

# ------------------------------------- Scalar expansion ---------------------------------------------------------------
# Scalar expansion
# Y = W + T
#       where "W" is a vector and "T" is a scalar
#
# Δy/Δw = Iw
# Δy/Δt = w
#
# Sample: w = [ 1.8517164 , -0.19331335] and t=11.0
# Δy/Δw = [11. 11.]
# Δy/Δt = 1.658403  which is sum(w)

w = tf.Variable(tf.random.normal((1, 2)), name='w')
t = tf.Variable(11.0)
print("\nW & T")
print(w)
print(t)

with tf.GradientTape(persistent=True) as tape:
    y = w * t

[dl_dw, dl_dt] = tape.gradient(y, [w, t])
print("\ndy_dw & dy_dt")
print(dl_dw)
print(dl_dt)
print("\n\n End - Scalar expansion \n\n")

# Given below is example Element-wise operations on vectors

w = tf.Variable(tf.random.normal((1, 2)), name='w')
b = tf.Variable(tf.random.normal((1, 2)), name='b')
print("\nW & B")
print(w)
print(b)

with tf.GradientTape(persistent=True) as tape:
    y = w * b

[dl_dw, dl_db] = tape.gradient(y, [w, b])
print("\ndy_dw & dy_db")
print(dl_dw)  # expect diag(b)
print(dl_db)  # expect diag(b)
print("\n\n End - Element-wise operations on vectors \n\n")
