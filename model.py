# -*- coding: utf-8 -*-
"""cnn_sequential for cat and robbet_data(week04_day04).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T6iz5njAa4TcQCnM-5LwhL3Vms0LZ22k

**import libraries for project:**
"""

import numpy as numpy
import pandas as pd
import os
import tensorflow as tf
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import cv2 as cv

"""**load train images dataset:**"""

train_images_path = '/content/drive/MyDrive/dataset/train-cat-rabbit'

train_dataset = tf.keras.utils.image_dataset_from_directory(
    train_images_path,
    labels='inferred',
    label_mode='binary',
    color_mode='rgb',
    image_size=(224, 224),
    batch_size=50,
    shuffle=True
)

val_images_path = '/content/drive/MyDrive/dataset/val-cat-rabbit'

val_dataset = tf.keras.utils.image_dataset_from_directory(
    val_images_path,
    labels='inferred',
    label_mode='binary',
    color_mode='rgb',
    image_size=(224, 224),
    batch_size=50,
    shuffle=False
)

"""**initialize cnn sequential model:**"""

model = tf.keras.Sequential([
      # ist convolutional layer
      tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
      tf.keras.layers.MaxPooling2D((2, 2)),

      # 2nd convolutional layer
      tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
      tf.keras.layers.MaxPooling2D((2, 2)),

      #3rd convolutional layer
      tf.keras.layers.Conv2D(128, (3,3), activation = 'relu'),
      tf.keras.layers.MaxPooling2D((2, 2)),

      # 4rd conv layer
      tf.keras.layers.Conv2D(264, (3,3), activation = 'relu'),
      tf.keras.layers.MaxPooling2D((2, 2)),

      # 5th layer conv
      tf.keras.layers.Conv2D(512, (3,3), activation= 'relu'),
      tf.keras.layers.MaxPooling2D((2, 2)),

      # Flatten the output of the convolutional layers
      tf.keras.layers.Flatten(),

      # Fully connected layer 1
      tf.keras.layers.Dense(128, activation='relu'),

      # Fully connected layer 2
      tf.keras.layers.Dense(64, activation='relu'),

      # Output layer
      tf.keras.layers.Dense(1, activation='sigmoid')
])

"""**compile your model:**"""

model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])

"""**fit the CNN Sequential model on the training dataset:**"""

model.fit(train_dataset, validation_data = val_dataset, epochs= 5)

"""**import test dataset:**"""

model.save('cat_vs_rabbit.h5')

test_images_path = '/content/drive/MyDrive/dataset/test-images'

test_dataset = tf.keras.utils.image_dataset_from_directory(
    test_images_path,
    labels='inferred',
    label_mode='binary',
    color_mode='rgb',
    image_size=(224, 224),
    batch_size=50,
    shuffle=False
)

"""**check model prediction on test dataset:**"""

#Evaluate the model on the training dataset
loss, accuracy = model.evaluate(test_dataset)
print("Training Accuracy:", accuracy)

prediction = model.predict(test_dataset)
print(prediction)

"""**test it on single image of cat:**"""

image_test = '/content/cat_image.jpg'

import numpy as np
img = tf.keras.preprocessing.image.load_img(image_test, target_size = (224, 224))
img = tf.keras.preprocessing.image.img_to_array(img)
img = np.expand_dims(img, axis=0)
prediction = model.predict(img)
print(prediction)
if prediction >= 0.5:
  print("this is a cat")
else:
  print("this is not a cat")

"""**Now predict the class throught labels:**"""

label = train_dataset.class_names[1]
print(label)
lebel = train_dataset.class_names[0]
print(lebel)

# Path to the test image
test_image_path = '/content/cat_image.jpg'

# Preprocess the test image
preprocessed_image = preprocess_image(test_image_path)

# Remove the extra dimension
preprocessed_image = np.squeeze(preprocessed_image)

# Make predictions
predictions = model.predict(np.expand_dims(preprocessed_image, axis=0))

# Convert predictions to binary form
binary_prediction = 1 if predictions[0][0] > 0.5 else 0

print("Prediction Probability:", predictions[0])
print("Binary Prediction:", binary_prediction)

model.save('/content/drive/MyDrive/Save model IT wing/cat_vs_rabbit.h5')

model.save('cat_vs_rabbit.h5')

model.save('/content/drive/MyDrive/Save model IT wing/my_model.keras')

