# color-ID-app

# About

This app detects colors in an image and returns the name of a color to the user. 

Program repo: https://github.com/amynordrum/color-ID-app

# Install

Clone or download from project repo site (see above).

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

cd color-id-app 

# Setup 

Download the jpeg you wish to analyze. 

Save the jpeg to the repository folder (for example: color-id-app)

Please note: You don't need to set up a virtual environment to run this program.

You will need three packages to run this app: pandas, numpy, and open-cv. For your convenience, these packages are stored in the requirements.txt file in the repo. To install them, use this command: 

pip install -r requirements.txt

# Usage

To run the program:

python color_detection.py -i [add image file name here]

(for example: python color-detection.py -i examplepic.jpg)

Running the program will open a new window which will display your selected picture. 

Double click a specific pixel or spot on the image in the new window to identify the color.

To end the program, hit the "esc" key. 

# Authors 

Pearl Verma and Amy Nordrum

# Acknowledgements

https://data-flair.training/blogs/project-in-python-colour-detection/?fbclid=IwAR26aLHto_8XRbDRpvLMUPh4RcQ0EA8m1MivpCRtMY0EPsTmp8MUdwJM688


