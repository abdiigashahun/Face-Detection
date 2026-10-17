# Face Recognition Attendance System

A Python application that recognizes known faces from a live webcam and records attendance automatically in `Attendance.csv`.

The project uses OpenCV for the camera and display, `face_recognition` for face locations and face encodings, NumPy for distance comparisons, and dlib models through the `face_recognition` package.

![Face detection example](https://user-images.githubusercontent.com/28294942/166667109-d2024d8c-9aec-44ed-93f8-8f1d9b66098a.png)

## What This Project Does

1. Loads one reference image for each person from `Images_Attendance`.
2. Creates a face encoding for every reference image.
3. Opens the computer's default webcam.
4. Detects and encodes faces in each camera frame.
5. Compares camera faces with the reference encodings.
6. Draws a name around a recognized face.
7. Adds the person's name, time, and date to `Attendance.csv` once per run.

The system is intended for learning and small, controlled demonstrations. Face recognition can make mistakes, so attendance should be reviewed by a responsible person.

## Project Files

```text
Face-recognition-Attendance-System-Project/
├── AttendanceProject.py       # Main live webcam attendance application
├── main.py                    # Optional two-image face comparison demo
├── Attendance.csv             # Attendance output file
├── Images_Attendance/         # Reference face images (you create this folder)
├── requirements.txt           # Python dependencies
└── README.md                  # This guide
```

## Requirements

- Linux, macOS, or Windows
- Python 3.9 or newer
- A working webcam for the live application
- One clear image containing one visible face for every person
- Permission to use the images and camera

Python 3.12 is supported with the dependency setup in this repository. The `face_recognition_models` package is older and requires `setuptools<81`; this is already listed in `requirements.txt`.

## Installation on Linux

Open a terminal and move into the project directory. Because the directory name contains spaces, keep the quotes around the parent path:

```bash
cd "/home/abdi/Pictures/Face Detection/Face-recognition-Attendance-System-Project"
```

Check that Python is available:

```bash
python3 --version
```

Create an isolated virtual environment:

```bash
python3 -m venv .venv
```

If the `venv` module is missing on Ubuntu or Debian, install it once:

```bash
sudo apt update
sudo apt install python3-venv python3-pip
```

Activate the environment:

```bash
source .venv/bin/activate
```

After activation, the terminal normally shows `(.venv)` at the beginning of the prompt. Install all project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Confirm that the dependencies are healthy:

```bash
python -m pip check
python -c "import cv2, numpy, face_recognition; print('All imports OK')"
```

When the environment is not activated, use the project interpreter directly instead:

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python AttendanceProject.py
```

## Add Reference Face Images

Create the required folder from the project directory:

```bash
mkdir -p Images_Attendance
```

Copy one image per person into it. The filename becomes the person's name. For example:

```text
Images_Attendance/
├── Alice Johnson.jpg
├── Bob Smith.png
└── Charlie Brown.jpeg
```

Use clear, well-lit images with one face visible. Keep the person's face reasonably large and facing the camera. Avoid group photos, blurry photos, and images containing several faces.

The application removes the file extension and converts the filename to uppercase when it displays the name. For example, `Alice Johnson.jpg` is recorded as `ALICE JOHNSON`.

Supported image formats generally include `.jpg`, `.jpeg`, and `.png`.

## Prepare the Attendance File

The repository includes `Attendance.csv`. It should begin with this header:

```csv
Name,Time,Date
```

If you need to create a new empty file, run:

```bash
printf 'Name,Time,Date\n' > Attendance.csv
```

The application appends records in this format:

```csv
Name,Time,Date
ALICE JOHNSON,09:30:12,17/10/2026
```

Make a backup before deleting or editing attendance records:

```bash
cp Attendance.csv Attendance-backup.csv
```

## Run Live Attendance

From the project directory, activate the environment and run the main program:

```bash
source .venv/bin/activate
python AttendanceProject.py
```

Or run it without activation:

```bash
.venv/bin/python AttendanceProject.py
```

What you should see:

- The terminal prints the loaded image filenames.
- The terminal prints `Encoding Complete`.
- A window named `webcam` opens.
- Recognized faces receive a green rectangle and name.
- A new attendance row is written the first time a recognized person appears.

To stop the application, focus the webcam window and press **Enter**. The camera is released and the window closes.

## Run the Optional Image Demo

`main.py` compares two specific images:

```text
Images_Attendance/modi-image-for-InUth.jpg
Images_Attendance/narendra-modi.jpg
```

Place those exact files in `Images_Attendance`, or update the filenames in `main.py`. Then run:

```bash
source .venv/bin/activate
python main.py
```

The script prints the comparison result and opens two image windows. Press any key while an image window is focused to close the demo.

This file is a separate experiment; it does not write attendance records.

## Useful Commands

Run a syntax check:

```bash
python -m py_compile AttendanceProject.py main.py
```

List reference images:

```bash
find Images_Attendance -maxdepth 1 -type f -printf '%f\n' | sort
```

View the latest attendance rows:

```bash
tail -n 10 Attendance.csv
```

Deactivate the virtual environment:

```bash
deactivate
```

Reinstall the dependencies if the environment becomes damaged:

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Troubleshooting

### `can't open file 'AttendanceProject.py'`

You are in the parent directory. Move into the project directory first:

```bash
cd "/home/abdi/Pictures/Face Detection/Face-recognition-Attendance-System-Project"
```

### `ModuleNotFoundError: No module named 'cv2'`

Activate the virtual environment and install the requirements:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The import is named `cv2`, but the package to install is named `opencv-python`.

### `Please install face_recognition_models`

Make sure the command uses the project interpreter:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

The requirements include `face-recognition` and the compatible `setuptools<81` version needed by its model package.

### `FileNotFoundError: Images_Attendance`

Create the folder and add at least one valid face image:

```bash
mkdir -p Images_Attendance
```

### `list index out of range` while creating an encoding

At least one image does not contain a detectable face. Replace it with a clear image containing exactly one face.

### The webcam window is black or does not open

Check that another application is not using the camera, verify camera permissions, and test the webcam with another application. The code currently uses camera index `0`, which means the default camera.

### The wrong person is recognized

Use clearer reference images, improve lighting, keep the face near the camera, and avoid similar-looking reference images. Review the CSV because face recognition is not perfect.

### No attendance row is added

The person must match one of the reference images. Also confirm that `Attendance.csv` exists and begins with `Name,Time,Date`.

## Privacy and Responsible Use

Face images and attendance records are personal data. Store them securely, obtain consent, restrict access, and follow the privacy laws and policies that apply to your school or organization. Do not use this project as the only basis for disciplinary or other important decisions.

## Technology

- Python
- OpenCV
- `face_recognition`
- dlib
- NumPy
- CSV files
