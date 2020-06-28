import cv2             # this is for opencv which our program uses to process the image that we're running color detection on
import numpy as np
import pandas as pd    # use pandas to read csv file which contains our color library
import argparse        # this is the argument parser which allows us to take the image path from the command line
import os

# User Inputs - have the user verify that they have their image saved
while True:
    image_check = input("Please verify that you've downloaded your image to the repo folder (YES or NO): ") # output: string
    if image_check == "YES":
 #       leave = input("Thank you for verifying, please type 'control + C' to exit the program. Then type 'python color_detection.py -i [type image name here]' in the command line to run color detection on your selected jpeg: ")
        break
    else:
        print("Please download your image to the project repo folder!")   # we leveraged this from our shopping cart project!

# Creating argument parser to take image path from command line 
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")      # this allows us to input the name of the image within the command line
args = vars(ap.parse_args())
img_path = args['image']

img = cv2.imread(img_path)    # reading the image with opencv

# Declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0          # starting point is zero 

index=["color","color_name","hex","R","G","B"]                # assigning names to each column
csv = pd.read_csv('colors.csv', names=index, header=None)     # reading csv file that contains our library of colors with pandas

# Function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):                                         
    minimum = 10000
    for i in range(len(csv)):                                 # utilize all contents in csv file 
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))       # formula to calculate distance to tell user which color listed in the csv file a selected pixel is closest to
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]                # utilize pandas loc method to select row by index (as shown in line 28) from pandas dataframes
    return cname                                           # returning color name for chosen value

# Function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):        
    if event == cv2.EVENT_LBUTTONDBLCLK:          # detect double click of mouse and calculate rgb values along with the x,y position of a selected pixel
        global b,g,r,xpos,ypos, clicked
        clicked = True                            # if double click criteria is met, code will continue to run
        xpos = x                                  # defines x coordinate of mouse
        ypos = y                                  # defines y coordinate of mouse 
        b,g,r = img[y,x]
        b = int(b)                                # converts value of "b" to an integer 
        g = int(g)                                # converts value of "g" to an integer 
        r = int(r)                                # converts value of "r" to an integer 
       
cv2.namedWindow('image')                        # open window to display image
cv2.setMouseCallback('image',draw_function)     # display mouse on new window which displays the image

while(1):

    cv2.imshow("image",img)                    # draw the image on the window 
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)                      # puts a rectangle on the image

        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)            # creates string of text that displays color name and RGB value in our new window
        
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)        # gets color name to draw text on the window and specify formatting

        if(r+g+b>=600):                                                         # if the color is too light, text will display in black instead of white
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    # Exit loop    
    if cv2.waitKey(20) & 0xFF ==27:          # hit esacpe key to exit
        break
    
cv2.destroyAllWindows()
