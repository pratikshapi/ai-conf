import cv2
import pytesseract
import os

# Path to the frames directory
frames_path = 'frames/'
# List all files in the directory
image_files = [f for f in os.listdir(frames_path) if os.path.isfile(os.path.join(frames_path, f))]

# print(image_files)

# Initialize an empty dictionary to hold the text from each image
extracted_texts = {}

for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(frames_path, image_file)
    
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Failed to load {image_file}. Skipping...")
        continue

    # Convert the image to gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply OCR on the gray image
    text = pytesseract.image_to_string(gray_image)
    
    # Store the extracted text in the dictionary, using the image file name as the key
    extracted_texts[image_file] = text

# Optionally, print the extracted text for each image
for image_file, text in extracted_texts.items():
    # print(f"Text from {image_file}:")
    print(text)
    # print("-" * 50)
