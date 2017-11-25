from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Conv2D, Flatten, Activation, MaxPooling2D, Dropout
from keras.utils import plot_model
from keras.callbacks import History, TerminateOnNaN, TensorBoard, CSVLogger

IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300

def train():
    model = Sequential()

    model.add(Conv2D(64, (3, 3), input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3)))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3), input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    # model.add(Conv2D(32, (3, 3), input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3)))
    # model.add(Activation('relu'))
    # model.add(Conv2D(32, (3, 3), input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3)))
    # model.add(Activation('relu'))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    # model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(2048))
    model.add(Activation('sigmoid'))
    model.add(Dense(57))
    model.add(Activation('sigmoid'))

    model.compile(
        loss='categorical_crossentropy',
        optimizer=RMSprop(),
        metrics=['accuracy']
    )

    model.fit_generator(
        ImageDataGenerator(rescale=1. / 255).flow_from_directory(
            directory='images',
            target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
            batch_size=20
        ),
        # validation_data=ImageDataGenerator(rescale=1. / 255).flow_from_directory(
        #     directory='test',
        #     target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        #     batch_size=16
        # ),
        # validation_steps=2,
        epochs=20,
        steps_per_epoch=57000 // 16,
        verbose=2,
        callbacks=[
            TerminateOnNaN(),
            # TensorBoard(log_dir='./logs', write_images=True),
            # CSVLogger('./logs/log.txt', append = False)
        ]
    )

    model.save('model.h5')
    # plot_model(model, 'model.png', show_shapes=True)

if __name__ == '__main__':
    train()


