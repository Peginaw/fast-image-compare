# Fast Image Compare
I'm tired of having to load a dozen images as layers into Photoshop or GIMP and then painstakingly turn layers on and off to compare them, so I made this tool to quickly flip back and forth between variations of an image. The idea came from behind-the-scenes videos of traditional cartoon animators flipping their physical paper frames to see the motion as they worked.

## Requirements:
- Python 3
 - PyQt5 (for the graphical interface)

## Installation
1. Download the zip file or Clone this project to your computer.
```bash
git clone https://github.com/Peginaw/fast-image-compare/
```
1. If not already installed, install PyQt5 (Update pip first)
```bash
pip install --upgrade pip
pip install PyQt5
```
## How to Use
Run the main.py file found in the root folder.

Select a base reference image to compare the rest against.

Select another image for comparison.

Flip back and forth as needed.

Use the 'Next' and 'Prev' buttons to switch to other pictures in the same directory for comparison, while keeping the base image the same.

The 'Refresh' button does two things. It updates the size of the images to fill the screen after resizing the window, and it checks for new images in the directory.
