import os
import random
import numpy as np
from PIL import Image, ImageEnhance
base_path = "C://Users//masip//Documents//Erasmus//Subjects//DeepL//bugNIST//BugNIST_DATA//train"
def load_images_from_folder(folder):
    """ Load all images from a folder into a list along with filenames and adjust brightness. """
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = Image.open(img_path).convert('L')  # Convert to grayscale
        if img is not None:
            # Adjust brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.5)  # Increase brightness by 50%
            images.append((img, img_path))
            filenames.append(filename)
    return images, filenames

def create_mixture(image_lists, filenames_lists, output_size=(64, 64)):
    """ Create a mixture using max pixel value blending of 3-5 images and return contributing image paths. """
    num_images = random.randint(3,5)  # Choose 3, 4, or 5 images randomly
    chosen_indices = random.sample(range(len(image_lists)), num_images)
    selected_images = [image_lists[i][0] for i in chosen_indices]
    contributing_paths = [image_lists[i][1] for i in chosen_indices]

    # Resize images
    resized_images = [img.resize(output_size) for img in selected_images]

    # Initialize a numpy array for max blending
    max_image_array = np.zeros((output_size[0], output_size[1]), dtype=np.uint8)

    # Apply max blending
    for img in resized_images:
        image_array = np.array(img, dtype=np.uint8)
        max_image_array = np.maximum(max_image_array, image_array)

    # Convert back to image
    result_image = Image.fromarray(max_image_array, mode='L')
    return result_image, contributing_paths

def main():
    
    output_base = "output_directory"  # Define the base output directory
    if not os.path.exists(output_base):
        os.makedirs(output_base)

    bug_types = ['AC', 'BC', 'BF', 'BL', 'BP', 'CF', 'GH', 'MA', 'ML', 'PP', 'SL', 'WO']
    all_images = []

    # Load images and filenames for each bug type
    for bug in bug_types:
        folder_path = os.path.join(base_path, bug)
        images, _ = load_images_from_folder(folder_path)
        all_images.extend(images)

    # Generate mixed images
    num_mixed_images = 10  # Number of mixed images to create
    for i in range(num_mixed_images):
        mixed_image, contributors = create_mixture(all_images, all_images)
        mixed_image_folder = os.path.join(output_base, f"mixed_image_{i}")
        os.makedirs(mixed_image_folder, exist_ok=True)

        # Save mixed image
        mixed_image.save(os.path.join(mixed_image_folder, 'mixed_image.png'))

        # Copy contributing images into the folder
        for path in contributors:
            original_image_name = os.path.basename(path)
            original_image = Image.open(path)
            original_image.save(os.path.join(mixed_image_folder, original_image_name))

        print(f"Folder created: {mixed_image_folder} with contributing images.")



main()
