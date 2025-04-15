# Eraser Assignment

This program creates a canvas where you can erase blue cells using a pink eraser. The canvas consists of a grid of blue rectangles, and any cell that overlaps with the eraser turns white.

## Features
- **Canvas**: A grid of blue cells created dynamically.
- **Eraser**: A pink rectangle that moves with the mouse.
- **Erasing Action**: Blue cells turn white when they come into contact with the eraser.

## Constants
- `CANVAS_WIDTH`: Width of the canvas (400 pixels).
- `CANVAS_HEIGHT`: Height of the canvas (400 pixels).
- `CELL_SIZE`: Size of each grid cell (40 pixels).
- `ERASER_SIZE`: Size of the eraser (20 pixels, adjustable).

## How to Run the Program

1. Ensure you have Python installed on your system.
2. Make sure the `graphics.py` library is available.
3. Save the code in a Python file (e.g., `eraser_assignment.py`).
4. Run the script using the following command:

   ```bash
   python eraser_assignment.py

Click anywhere on the canvas to place the eraser and use it to erase blue cells by moving it around.

Example Output
A grid of blue cells is displayed on the canvas.

A pink eraser is placed at the position of the mouse click.

The pink eraser can be moved, and overlapping blue cells turn white.

Customization
You can customize the following constants in the code:

ERASER_SIZE: Change the size of the eraser (e.g., 40, 60, etc.).

CELL_SIZE: Adjust the size of the grid cells.

Troubleshooting
If the program crashes when closing the canvas, it's due to the canvas being closed while the program is still running. A try-except block can handle this gracefully.

License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### Key sections in the README:
1. **Introduction**: A brief description of what the program does.
2. **Features**: Highlights the main features of the program.
3. **Constants**: Explains the constants used in the code.
4. **How to Run**: Instructions on how to run the Python program.
5. **Customization**: Details on how users can customize the code for different experiences.
6. **Troubleshooting**: Common issues and solutions.
7. **License**: You can add a license if necessary.

---

### 📝 Instructions:
- Simply copy and paste this content into a `.md` file and name it `README.md` in your project folder.
- You can later add more details or modify the sections as per your needs!
