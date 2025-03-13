## Joy Recorder

_Joy Recorder_ is a simple Python script webcam recorder that is coded with OpenCV.

This Recorder supports preview of the default webcam, recording, changing the file format and the fps.

This project is established for Computer Vision lecture in 2025 1st semester assignment.

### Main Function
- Preview webcam video
- Record current webcam video
- Change the save format of the video
- Change the frame rate of the video

### How to Use
<img src="https://raw.githubusercontent.com/fallingflow/JoyRecorder/refs/heads/main/screenshots/preview.PNG">

- Initial Screen
    - Shows the default information about current FPS and file format

<img src="https://raw.githubusercontent.com/fallingflow/JoyRecorder/refs/heads/main/screenshots/setting.PNG">

- Changing settings
    - Press ',' or '.' to change the current FPS (',' for decreasing, '.' for increasing)
    - Press 'f' to change the file format

<img src="https://raw.githubusercontent.com/fallingflow/JoyRecorder/refs/heads/main/screenshots/recording.PNG">

- Recording
    - Press space bar to start recording
    - Display the current recording status in red text

### Supported Format
| Feature     | Description    |
|-------------|----------------|
| FPS         | 10, 20, **30** |
| File format | .avi, **.mp4** |
(bold means default value)