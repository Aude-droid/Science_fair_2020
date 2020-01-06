#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: Aude

This Is My Science Fair Project. This program can calculate the area of any black and white shape.
I used Python to make my program because its free and easy to learn

"""

#This gets the image tool in the library
from PIL import Image 

#this opens my picture file
MyPicture = Image.open("/Users/Philippe/Documents/Aude_science_fair_2020/Square.png")

#this is the number or columns and row divisions
divisions = 1000

#this is the size of the paper
paperwidth = 10.0
paperheight = 10.0

columnpaper = paperwidth/divisions
rowpaper =paperheight/divisions

#this is the area of one paper cell
cellpaperarea = columnpaper * rowpaper

#this divides the picture into rows and columns and keeps only the whole number
#no remainders allowed!
columnwidth = MyPicture.size[0]//divisions
rowheight = MyPicture.size[1]//divisions

#this counts the number of black cells
cellcounter = 0

#this cuts the picture into columns
for col in range(divisions):
    #this cuts the columns into rows
    for row in range(divisions):
        cell = (col*columnwidth,row*rowheight,((col+1)*columnwidth)-1,((row+1)*rowheight)-1)
        #this creates a picture of the cell
        cellpicture = MyPicture.crop(cell)
       
        value = []
        #this gets all the colors in the cell
        pixels = cellpicture.getdata()
        
        #this makes the average color in the cell
        for pixel in pixels:
            value.append(pixel[0])
            cellcolor = sum(value)/len(value)
        
        #If the average color is black then the counter is added 1
        if cellcolor == 0:
            #new_cellcol = list([(0,0,0)]) * (cellpicture.size[0] * cellpicture.size[1])
            #cellpicture.putdata(new_cellcol)
            cellcounter = cellcounter+1
        # If the average color is not black then the cell is colored white. This step is not important to measure area
        else:
            new_cellcol = list([(255,255,255)]) * (cellpicture.size[0] * cellpicture.size[1])
            cellpicture.putdata(new_cellcol)
        
        #The colored  cell is pasted to the original picture
        MyPicture.paste(cellpicture,(col*columnwidth,row*rowheight))
 
#this shows my picture with the new colors       
MyPicture.show()

#this calculates the total area with the number of black cells and the area of one cell
totalarea = cellcounter * cellpaperarea 

#this displays results
print ("Total number of cells: "+ str(divisions * divisions))
print ("Total number of black cells: "+ str(cellcounter))
print ("Total area is: "+ str(totalarea))
