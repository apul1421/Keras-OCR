import matplotlib.pyplot as plt
import keras_ocr

def convert_image_to_text(image_path):
    # Load the recognizer model
    pipeline = keras_ocr.pipeline.Pipeline()

    # Read the input image
    image = keras_ocr.tools.read(image_path)

    # Perform OCR on the image
    predictions = pipeline.recognize([image])

    # Extract the text from the predictions
    text = ""
    for prediction in predictions[0]:
        text += prediction[0] + " "

    return text.strip()

# Path to the image file
image_path = "path/to/your/image.jpg"

# Convert the image to text
result_text = convert_image_to_text(image_path)

# Print the extracted text
print(result_text)
