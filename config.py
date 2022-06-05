import os



NET_NAME = 'resnet_v1_50' #

FIXED_BLOCKS = False

WEIGHT_DECAY = 0.00001

num_classes = 3

global_pool = True #resnet做分类时需要设置成True

train_path = os.path.join(r'F:\learning\interpretation\Tensorflow-Resnet-Image-Classification-master\UCMerced_LandUse\1', 'train')
test1_path = os.path.join(r'F:\learning\interpretation\Tensorflow-Resnet-Image-Classification-master\UCMerced_LandUse\1', 'test1')
test2_path = os.path.join(r'F:\learning\interpretation\Tensorflow-Resnet-Image-Classification-master\UCMerced_LandUse\1', 'test2')
cache_path = os.path.join(r'F:\learning\interpretation\Tensorflow-Resnet-Image-Classification-master\UCMerced_LandUse\1', 'cache')
cache_rebuild = True
batch_size = 16

val_batch_size = 16
# image_height = 224
# image_width = 224
image_height = 256
image_width = 256
image_channels = 3

num_iters = 70000

decay_iters = 50000

lr = [0.001, 0.0001]

beta1 = 0.9

beta2 = 0.999

momentum = 0.9

save_stp = 1

batch_norm_scale = True

batch_norm_epsilon = 1e-5

batch_norm_decay = 0.997
