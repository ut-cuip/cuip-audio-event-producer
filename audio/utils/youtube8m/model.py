import tensorflow as tf


# Workaround for num_epochs issue.
def set_up_init_ops(variables):
    init_op_list = []
    for variable in list(variables):
        if "train_input" in variable.name:
            init_op_list.append(tf.assign(variable, 1))
            variables.remove(variable)
    init_op_list.append(tf.variables_initializer(variables))
    return init_op_list


def load_model(sess, checkpoint_path):
    meta_graph_location = checkpoint_path + '.meta'

    saver = tf.train.import_meta_graph(
        meta_graph_location, clear_devices=True, import_scope='m2'
    )

    saver.restore(sess, checkpoint_path)

    sess.run(
        set_up_init_ops(tf.get_collection_ref(tf.GraphKeys.LOCAL_VARIABLES))
    )
