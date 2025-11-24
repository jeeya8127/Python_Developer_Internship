import os
from PIL import Image

INPUT_FOLDER = 'images_to_resize'
OUTPUT_FOLDER = 'resized_images'
TARGET_SIZE = (800, 600)

def resize_images_in_batch(input_dir, output_dir, size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        if os.path.isdir(input_path):
            continue

        try:
            img = Image.open(input_path)

            if img.mode != 'RGB':
                img = img.convert('RGB')

            resized_img = img.resize(size)

            output_path_jpg = os.path.splitext(output_path)[0] + '.jpg'
            resized_img.save(output_path_jpg, 'JPEG', quality=95)

            print(f"Resized and saved: {filename}")

        except IOError:
            print(f"Skipping non-image file: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
    
    if os.listdir(INPUT_FOLDER):
        resize_images_in_batch(INPUT_FOLDER, OUTPUT_FOLDER, TARGET_SIZE)
    else:
        print(f"'{INPUT_FOLDER}' is empty. Add images to process.")