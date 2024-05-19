# Face Detection and Video Recording

This project was a test of OpenCV to detect faces in real-time from a webcam, automatically record a video when a face is detected. Additionally, it saves screenshots of frames where faces are detected.

## Features

- Real-time face detection using **Haar Cascades**.
- Display the video feed with rectangles around detected faces.
- Save screenshots of frames with detected faces.
- Display the count of detected faces on the video feed.
- Record the video feed to a file.

## Requirements

- Python
- OpenCV

## Installation

1. Install Python.
2. Install OpenCV using pip:
    ```sh
    pip install opencv-python
    ```

## Usage

1. Clone this repository or download the script.
2. Run the script:
    ```sh
    python face_detection.py
    ```
3. To stop the script, press the 'q' key.

## Output

- The video feed is saved to a file named `output.avi` in the same directory as the script.
- Snapshots of frames with detected faces are saved as PNG files with filenames like `snapshot_YYYYMMDD_HHMMSS.png`.

