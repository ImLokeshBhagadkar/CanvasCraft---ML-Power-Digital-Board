# CanvasCraft---ML-Power-Digital-Board
# CanvasCraft - ML Powered Digital Board

## Overview

CanvasCraft is an advanced desktop application that leverages the MediaPipe library to detect hand movements and create a virtual canvas for users to interact with using a virtual pointer. This AI-powered digital whiteboard provides a seamless, hands-free drawing and writing experience, ideal for educational and professional settings.

## Features

- **Hand Tracking:** Uses the MediaPipe library to detect hand movements and finger positions.
- **Drawing Mode:** Allows users to draw on a digital canvas using their finger as a virtual pen.
- **Selection Mode:** Enables switching between different drawing tools and colors.
- **Eraser Tool:** Provides an option to erase parts of the drawing with a virtual eraser.
- **Multiple Colors:** Supports drawing in multiple colors, including black, red, blue, and green.
- **Local Execution:** Runs entirely on the user's local device for enhanced performance and reliability.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** 
  - OpenCV
  - MediaPipe
  - NumPy

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/CanvasCraft.git
   cd CanvasCraft
   ```

2. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   ```sh
   python main.py
   ```

## Usage

1. **Launching the Application:**
   - Run the `main.py` script to start the application.
   - The webcam will activate and the hand tracking system will initialize.

2. **Drawing on the Canvas:**
   - Use your index finger to draw on the virtual canvas.
   - Raise both your index and middle fingers to switch to selection mode.

3. **Changing Colors and Tools:**
   - Use the virtual toolbar at the top of the screen to select different colors and the eraser.

4. **Saving Your Work:**
   - The current implementation does not support saving. Future updates will include save functionality.

## Acknowledgments

We would like to express our deepest appreciation to all those who provided us the possibility to complete this project. A special gratitude we give to our project guide, Prof. S. A. Bachwani, for his valuable guidance, inspiration, and encouragement. We also extend our sincere thanks to Prof. C. V. Andhare, Head of the Department of Computer Engineering, and Dr. P. M. Khodke, Principal of Government College of Engineering Yavatmal, for their support.

## Future Scope

- **Save/Load Functionality:** Allow users to save their work and load previous sessions.
- **Enhanced Gesture Recognition:** Incorporate more complex gestures for additional commands.
- **Cloud Integration:** Optional cloud storage for collaborative work.
- **Multi-user Support:** Enable multiple users to collaborate on the same canvas in real-time.

## References

- MediaPipe: [https://google.github.io/mediapipe/](https://google.github.io/mediapipe/)
- OpenCV: [https://opencv.org/](https://opencv.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any queries or contributions, please contact bhagadkar99@gmail.com.

Happy Drawing!
