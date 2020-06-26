import cv2
import numpy as np
import pandas as pd
import argparse
import os

# User Inputs - have this user verify that they have their image saved
while True:
    image_check = input("Please verify that you've downloaded your image to the repo folder (YES or NO): ") # output: string
    if image_check == "YES":
 #       leave = input("Thank you for verifying, please type 'control + C' to exit the program. Then type 'python color_detection.py -i [type image name here]' in the command line to run color detection on your selected jpeg: ")
        break
    else:
        print("Please download your image to the project repo folder!")

#Creating argument parser to take image path from command line 
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

img = cv2.imread(img_path)    # reading the image with opencv

#declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

index=["color","color_name","hex","R","G","B"]                # assigning names to each column
csv = pd.read_csv('colors.csv', names=index, header=None)     # reading csv file that contains our library of colors with pandas

#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):                                         
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))       # formula to calculate distance to tell user which color listed in the csv file a selected pixel is closest to
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]                   # returning color name for chosen value
    return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):        # detect double click of mouse and calculate rgb values along with the x,y position of a selected pixel
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x                                  # defines x coordinate of mouse
        ypos = y                                  # defines y coordinate of mouse 
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')                        # open window to display image
cv2.setMouseCallback('image',draw_function)     

while(1):

    cv2.imshow("image",img)                    # draw the image on the window 
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)                      # puts a rectangle on the image

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)        # gets color name to draw text on the window

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
