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
