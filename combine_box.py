import numpy as np
from operator import itemgetter

def combine_boxes_to_lines(boxes, max_gap):
    # Sort the boxes by their y-coordinate
    sorted_boxes = sorted(boxes, key=itemgetter(1))
    
    lines = []
    current_line = []
    previous_box = None
    
    for box in sorted_boxes:
        if previous_box is None:
            current_line.append(box)
        else:
            gap = box[1] - (previous_box[1] + previous_box[3])
            
            if gap <= max_gap:
                current_line.append(box)
            else:
                lines.append(current_line)
                current_line = [box]
        
        previous_box = box
    
    lines.append(current_line)
    
    return lines

def combine_lines_to_paragraphs(lines, max_line_gap):
    paragraphs = []
    current_paragraph = []
    previous_line = None
    
    for line in lines:
        if previous_line is None:
            current_paragraph.extend(line)
        else:
            gap = line[0][1] - (previous_line[-1][1] + previous_line[-1][3])
            
            if gap <= max_line_gap:
                current_paragraph.extend(line)
            else:
                paragraphs.append(current_paragraph)
                current_paragraph = line
        
        previous_line = line
    
    paragraphs.append(current_paragraph)
    
    return paragraphs

# Example usage
# Assume 'word_boxes' is a list of word bounding boxes in the format [x, y, width, height]

# Combining word boxes into lines
max_line_gap = 10  # Maximum allowed gap between word boxes in a line
lines = combine_boxes_to_lines(word_boxes, max_line_gap)

# Combining lines into paragraphs
max_paragraph_gap = 50  # Maximum allowed gap between lines in a paragraph
paragraphs = combine_lines_to_paragraphs(lines, max_paragraph_gap)

# Printing the paragraphs
for paragraph in paragraphs:
    print("Paragraph:")
    for line in paragraph:
        print("Line:", line)
        
       
'''In the code above, we define two functions: combine_boxes_to_lines and combine_lines_to_paragraphs. The combine_boxes_to_lines function takes a list of word bounding boxes (boxes) and a maximum allowed gap between word boxes in a line (max_gap). It sorts the boxes by their y-coordinate, iterates through them, and combines boxes that are close together vertically into lines. The result is a list of lines.

The combine_lines_to_paragraphs function takes a list of lines (lines) and a maximum allowed gap between lines in a paragraph (max_line_gap). It iterates through the lines and combines lines that are close together vertically into paragraphs. The result is a list of paragraphs.

To use these functions, you need to pass in your list of word bounding boxes (word_boxes) and specify the maximum allowed gaps (max_line_gap and max_paragraph_gap). The resulting lines and paragraphs are then available for further processing or printing.

Note that the code assumes that the word bounding boxes are represented as lists of [x, y, width, height] where x and y represent the top-left coordinates of the box, and width and height represent the dimensions of the box. Adjust the code accordingly if your bounding boxes are represented differently.
'''

