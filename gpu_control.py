import tensorflow as tf

print("TensorFlow GPU kullanılabilir mi: ", tf.test.is_gpu_available())
print("Kullanılan GPU: ", tf.test.gpu_device_name())
print("TensorFlow sürümü: ", tf.__version__)


