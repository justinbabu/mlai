from dataset_costants import TABLE_DICT
import os
import os.path
PATH_TO_LABELS = os.path.join(os.getcwd(),'data','object-detection.pbtxt')
BMP_IMAGE_TEST_TO_PATH = os.path.join(os.getcwd(),'test')

NUM_CLASSES = 1

PATHS_TO_TEST_IMAGE = [
    'test/test1.PNG',
    'test/test2.PNG',
    'test/test3.PNG',
    'test/test4.PNG',
    'test/test5.PNG',
    'test/test6.PNG',
    'test/test7.PNG'
]

PATHS_TO_CKPTS = [
    # 'data/',
    # 'C:/Users/giova/Documents/PycharmProjects/TableTrainNet/trained_models/model__rcnn_inception_momentum_optimizer_1batch/frozen/frozen_inference_graph.pb',
    # 'C:/Users/giova/Documents/PycharmProjects/TableTrainNet/trained_models/model__rcnn_inception_adam_1/frozen/frozen_inference_graph.pb',
    # 'C:/Users/giova/Documents/PycharmProjects/TableTrainNet/trained_models/model__rcnn_inception_adam_2/frozen/frozen_inference_graph.pb',
    # 'C:/Users/giova/Documents/PycharmProjects/TableTrainNet/trained_models/model__rcnn_inception_adam_3/frozen/frozen_inference_graph.pb',
    # 'C:/Users/giova/Documents/PycharmProjects/TableTrainNet/trained_models/model__rcnn_inception_momentum_1/frozen/frozen_inference_graph.pb',
    # 'C:/Users/giova/Documents/PycharmProjects/TableTrainNet/trained_models/model__rcnn_inception_momentum_10k_jpg/frozen/frozen_inference_graph.pb',
    # 'C:/Users/giova/Documents/PycharmProjects/TableTrainNet/trained_models/model__rcnn_inception_momentum_optimizer_1batch/frozen/frozen_inference_graph.pb'
    '/content/mlai/trained_models/model__rcnn_inception_adam_4/frozen/frozen_inference_graph.pb'
]

TEST_SCORES = [0.2, 0.4, 0.6, 0.8]

MAX_NUM_BOXES = 10
