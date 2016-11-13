# Hello World app for TensorFlow

import tensorflow as tf

# define the graph
M1 = tf.constant([[3., 3.]])
M2 = tf.constant([[2.], [2.]])
M3 = tf.matmul(M1, M2) # symbolic: no calculation yet, all happens at once outside of Python (in GPU, on network, etc)

# start a session to compute the graph
with tf.Session() as sess: # runs on GPU first
    #with tf.device("/gpu:1"): # explicitly choose if you have multiple GPUs
    #with tf.device("grpc://host:2222"): # explicitly choose host with running TensorFlow server
    result = sess.run(M3)
    print(result) # [[12.]]

state = tf.Variable(0, name='counter')  # maintains state along Session
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)    # again symbolic
init_op = tf.initialize_all_variables() # makes operator; does not run anything yet

with tf.Session() as sess:
    sess.run(init_op)           # run init vars
    print(sess.run(state))      # run creates state
    for _ in range(3):
        print(sess.run(update)) # run graph for updates

# to allow setting inputs for each flow, use placeholders:
#x = tf.placeholder(tf.float32, [None, 784]) # placeholder = input
#sess.run(x, feed_dict={x: mnist.test.images})
