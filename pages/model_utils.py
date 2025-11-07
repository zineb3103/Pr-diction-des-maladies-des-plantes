import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import zipfile
def setup_data_paths(base_dir):
    train_dir = os.path.join(base_dir, 'train')
    validation_dir = os.path.join(base_dir, 'valid')
    return train_dir, validation_dir

def download_and_extract_dataset(local_zip_path, extract_path):
    with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Chemin du fichier ZIP et du répertoire d'extraction
local_zip = r"C:\Users\zineb\Desktop\New Plant Diseases Dataset(Augmented).zip"
base_dir = '/tmp/New Plant Diseases Dataset(Augmented)'

# Téléchargement et extraction
download_and_extract_dataset(local_zip, base_dir)

# Utilisation des chemins des données
train_dir, validation_dir = setup_data_paths(base_dir)
# Définir les chemins des données


def create_generators(train_dir, validation_dir):
    train_datagen = ImageDataGenerator(rescale=1 / 255.0)
    validation_datagen = ImageDataGenerator(rescale=1 / 255.0)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary'
    )

    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary'
    )

    return train_generator, validation_generator


def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), input_shape=(150, 150, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.0001),
                  loss='binary_crossentropy', metrics=['acc'])
    return model


def train_model(model, train_generator, validation_generator, epochs=50):
    history = model.fit(
        train_generator,
        steps_per_epoch=100,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=50
    )
    return history


def plot_training_history(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(acc))

    plt.figure(figsize=(12, 8))
    plt.plot(epochs, acc, 'r', label='Training accuracy')
    plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 8))
    plt.plot(epochs, loss, 'r', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()


def predict_image(model, image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255.0
    prediction = model.predict(x)
    return prediction
