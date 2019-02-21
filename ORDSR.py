import tensorflow as tf
import cv2
import numpy as np

def load_graph(frozen_graph_filename):
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def, name="ORDSR")
    return graph

if __name__ == '__main__':
    image = cv2.imread('dem.bmp', 0)
    image = image.astype(np.float32) / 255
    testInput = image[np.newaxis, ..., np.newaxis]
    scale = 3
    graph = load_graph('./model/x{}.pb'.format(scale))

    input_op = graph.get_tensor_by_name('ORDSR/input_op:0')
    output_op = graph.get_tensor_by_name('ORDSR/output_op:0')
    print('{}'.format(testInput.dtype))
    with tf.Session(graph=graph) as sess:
        SR = sess.run([output_op], feed_dict={input_op: testInput.astype(np.float)})
        cv2.imwrite('./dem_SR.bmp', SR[0][0, ...] * 255)

    print('ORDSR finished!')
