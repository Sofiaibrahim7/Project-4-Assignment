from graphics import Canvas
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """
    Erase objects that overlap with the eraser.
    Any blue cell that comes into contact with the eraser turns white.
    """
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    # Define eraser's boundaries
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find overlapping objects
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    # Change color of overlapping cells (except eraser itself) to white
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Create a grid of blue rectangles (cells)
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    # Wait for click to place the eraser
    canvas.wait_for_click()
    start_x, start_y = canvas.get_last_click()

    # Create the eraser (a pink rectangle)
    eraser = canvas.create_rectangle(
        start_x,
        start_y,
        start_x + ERASER_SIZE,
        start_y + ERASER_SIZE,
        'pink'
    )

    # Move eraser with mouse and erase overlapping blue cells
    try:
        while True:
            mouse_x = canvas.get_mouse_x()
            mouse_y = canvas.get_mouse_y()
            canvas.moveto(eraser, mouse_x, mouse_y)
            erase_objects(canvas, eraser)
            time.sleep(0.05)
    except:
        print("Canvas closed. Exiting program.")

# Required to run the program
if __name__ == '__main__':
    main()
