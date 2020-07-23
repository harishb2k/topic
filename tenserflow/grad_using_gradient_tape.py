import tensorflow as tf

# Scalar expansion
# Y = x + z
#       x is a vector
#       z is a scalar
w = tf.Variable(tf.random.normal((1, 2)), name='w')
t = tf.Variable(11.0)
print("\nW & T")
print(w)
print(t)

with tf.GradientTape(persistent=True) as tape:
    # y with_respect_to_w = It  (expect a identity matrix of t)
    # y with_respect_to_t = w   (expect a sum of w)
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
