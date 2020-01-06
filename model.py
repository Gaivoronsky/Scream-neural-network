from keras.applications.vgg19 import VGG19, preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing import image
import numpy as np



train_dir = 'train'
val_dir = 'val'

img_width, img_height = 224, 224
input_shape = (img_width, img_height, 3)
epochs = 5
batch_size = 1
nb_train_samples = 100
nb_validation_samples = 40
nb_test_samples = 1

def train_and_check_model():
    vgg19 = VGG19(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    vgg19.trainable = False

    model = Sequential()
    model.add(vgg19)
    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.summary()

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    datagen = ImageDataGenerator(rescale=1. / 255)


    train_generator = datagen.flow_from_directory(
        train_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    val_generator = datagen.flow_from_directory(
        val_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=val_generator,
        validation_steps=nb_validation_samples // batch_size)

    model.save('audio_model.h5')

    plt.plot(history.history['accuracy'],
             label='Доля верных ответов на обучающем наборе')
    plt.plot(history.history['val_accuracy'],
             label='Доля верных ответов на проверочном наборе')
    plt.xlabel('Эпоха обучения')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()


def predicting_model(name_img):
    model = load_model('audio_model.h5')

    img = image.load_img(name_img,
                         target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    result = model.predict(x)

    return result







