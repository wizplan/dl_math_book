import tensorflow as tf

sess = tf.Session()

a = tf.constant([2, 1])
print(sess.run(a))

b = tf.constant([3, 2, 1])
print(sess.run(b))

A = tf.constant([[2, 4, 1], [6, 3, 5]])
print(sess.run(A))