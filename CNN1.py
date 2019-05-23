# Genre classification using CNN

# first we have to import a dataset of the extracted frames and also optimize it according to our needs accordingly using keras
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.25,
                                   zoom_range = 0.25,
                                   horizontal_flip = True,
                                   rotation_range = 0.1)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('/Users/dhruvchandel/Desktop/trailer/DATASET(CNN1)/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'sparse')

test_set = test_datagen.flow_from_directory('/Users/dhruvchandel/Desktop/trailer/DATASET(CNN1)/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'sparse')

# Now preparing a CNN model for the same dataset
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# initialising the CNN

classifier = Sequential()

classifier.add(Convolution2D(50,3,3,input_shape = (64,64,3) , activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

classifier.add(Flatten())

classifier.add(Dense(output_dim = 128 , activation = 'LeakyReLU'))
classifier.add(Dense(output_dim = 128 , activation = 'LeakyReLU'))
classifier.add(Dense(output_dim = 12 , activation = 'softmax'))

classifier.compile(optimizer = 'nadam' , loss = 'sparse_categorical_crossentropy'  , metrics = ['accuracy'])

#classifier.summary()



classifier.fit_generator(training_set,
                         samples_per_epoch = 4452,
                         nb_epoch = 25,
                         validation_data = test_set,
                         nb_val_samples = 1110)