import numpy as np
import matplotlib.pyplot as plt


def generate_img_index(index, reloaded_model):
    noise = np.random.normal(0, 1, (1,))
    label = np.array([[index]])
    return reloaded_model.predict([noise, label])[0]


def save_img(image, output_path):
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.grid(False)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()