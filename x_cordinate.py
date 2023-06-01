import operator
import keras_ocr

def sort_by_x_coordinate(prediction):
    return prediction[1][0][0]

def convert_image_to_text(image_path):
    # Load the recognizer model
    pipeline = keras_ocr.pipeline.Pipeline()

    # Read the input image
    image = keras_ocr.tools.read(image_path)

    # Perform OCR on the image
    predictions = pipeline.recognize([image])

    # Sort the predictions based on x-coordinate
    sorted_predictions = sorted(predictions[0], key=sort_by_x_coordinate)

    # Extract the text and bounding box coordinates from the sorted predictions
    text = " ".join([prediction[0] for prediction in sorted_predictions])
    boxes = [prediction[1] for prediction in sorted_predictions]

    return text, boxes

# Path to the image file
image_path = "path/to/your/image.jpg"

# Convert the image to text and get the bounding box coordinates
result_text, result_boxes = convert_image_to_text(image_path)

# Print the extracted text
print(result_text)

# Print the bounding box coordinates
for box in result_boxes:
    print(box)
