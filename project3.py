# CPS121 Project 3
# Written: <November 13th 2026> <Ann Howard> <Ann.Howard@gordon.edu>
# 
# <Include description of program here>
## Makes a collage of pictures with different desired effects on certain photos
# Change each occurrence of "_" in the list below to be "Y" or "N" to indicate
# whether or not the given transformation is implemented in your program.
#
#   Can be done using just getPixels()
#   _ Altering colors of the image
#   _ Grayscale
#   _ Making darker or lighter
#   _ Sepia-toned
#   _ Posterized
#   Need nested loops
#   _ Mirrorizing
#   _ Edge detection5
#   _ Chromakey (change background)
#   _ Blurring
#   Need nested loops and alter size or shape
#   _ Rotation
#   _ Cropping
#   _ Shifting
#   Other transformations
#   _ <description of transformation>
#   _ <description of transformation>
#   _ <description of transformation>
# ============================================================================

import GCPictureTools as gpt
import pygame as pg
import os, sys
import math
import traceback

# ============================================================================
# ================ Start making changes after this comment ===================
# ============================================================================

# ---- SUPPORTING FUNCTIONS SHOULD GO HERE ----

def createCollage():
    """Create a collage.
 
    Returns 
    -------
    Picture
        the collage.
    """
    # create "canvas" on which to make a collage.  You may exchange the
    # width and height values if you prefer a landscape orientation.
    collage = gpt.Picture(950, 700)

    # ---- YOUR CODE TO BUILD THE COLLAGE GOES HERE ----
    # Notice that this is **inside** the createCollage() function.  Because
    # createCollage() should be a "one-and-only-one-thing" function, you
    # should use supporting functions to do transformations, etc.  These
    # supporting functions should be defined below, after the code for this
    # function.
                

    pic1 = gpt.Picture('fenceflowers.jpg')
    pic2 = gpt.Picture('pinkandyellowsmallflowers.jpg')
    pic3 = gpt.Picture('stonebridge.jpg')
    pic4 = gpt.Picture('streamwithflowers.jpg')
    pic5 = gpt.Picture('vintage flowers.jpg')
    pic6 = gpt.Picture('winniethepooh.jpg')

    pic1.copyInto(collage, 193, 25)
    pic_post = gpt.Picture('fenceflowers.jpg')
    posterize(pic_post)
    pic_post.copyInto(collage, 193, 520)
    pic11 = gpt.Picture('fenceflowers.jpg')
    decreaseRed(pic11)
    pic11.copyInto(collage, 757, 190)
    pic2_edge = gpt.Picture('pinkandyellowsmallflowers.jpg')
    pic2_edge = edgeDetect(pic2, 20)
    blend_pic2 = blend(pic2_edge, pic5, 0.7)
    blend_pic2.copyInto(collage, 381, 25)
    newpic2 = gpt.Picture('pinkandyellowsmallflowers.jpg')
    decreaseRed(newpic2)
    newpic2.copyInto(collage, 381, 520)
    pic2.copyInto(collage, 569, 190)
    pic3.copyInto(collage, 381, 190)
    pic3_mirror = gpt.Picture('stonebridge.jpg')
    mirrorHorizontal(pic3_mirror)
    pic3_mirror.copyInto(collage, 757, 25)
    pic3_edge = gpt.Picture('stonebridge.jpg')
    pic3_edge = edgeDetect(pic3_edge, 40)
    blend_pic3 = blend(pic2, pic3_edge, 0.5)
    blend_pic3.copyInto(collage, 5, 355)
    pic4.copyInto(collage, 5, 25)
    pic4_post = gpt.Picture('streamwithflowers.jpg')
    posterize(pic4_post)
    pic4_post.copyInto(collage, 757, 520)
    pic41 = gpt.Picture('streamwithflowers.jpg')
    blend_pic41 = blend(pic41, pic1, 0.5)
    blend_pic41.copyInto(collage, 569, 520)
    newpic4 = gpt.Picture('streamwithflowers.jpg')
    newpic4 = cropIt(newpic4, 187, 145)
    newpic4.copyInto(collage, 193, 355)
    pic_post5 = gpt.Picture('vintage flowers.jpg') 
    posterize(pic_post5)
    pic_post5.copyInto(collage, 5, 190)
    pic5.copyInto(collage, 569, 355)
    blend_pic5 = gpt.Picture('vintage flowers.jpg')
    blend_pic5 = blend(blend_pic5, pic2_edge, 0.4)
    blend_pic5.copyInto(collage, 757, 355)
    decreaseRed(pic6)
    pic6 = rotate90R(pic6)
    pic6.copyInto(collage, 193, 190)
    pic61 = gpt.Picture('winniethepooh.jpg')
    pic61 = rotate90L(pic61)
    pic61.copyInto(collage, 381 ,355)
    newpic62 = gpt.Picture('winniethepooh.jpg')
    newpic62 = rotate90R(newpic62)
    newpic62.copyInto(collage, 569, 25)
    newpic63 = gpt.Picture('winniethepooh.jpg')
    newpic63 = rotate90L(newpic63)
    newpic63.copyInto(collage, 5, 520)
    return collage


def decreaseRed(pic):
    """
    Purpose:
        Reduce the color red in each pixel by value between 0 and 1
    Arguements:
        pic (Picture): image being changed
    Returns:
        Nothing
    Raises:
        Nothing
    """
    for x in range (0, pic.getWidth()):
        for y in range (0,pic.getHeight()):
            pixel = pic.getPixel(x,y)
            pixel.setRed(pixel.getRed()*0.8)


def posterize(pic):
    """
    Purpose:
        Reduce color resolution of picture 4 levels
    Arguements:
        pic (Picture): image being posterized
    Returns:
        Nothing
    Raises:
        Nothing
    """
    for x in range (0,pic.getWidth()):
        for y in range (0,pic.getHeight()):
            p = pic.getPixel(x,y)
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            # checks and sets red values based off of rules
            if red < 50:
                p.setRed(40)
            if red > 49 and red < 110:
                p.setRed(98)
            if red > 109 and red < 180:
                p.setRed(150)
            if red > 179 and red <256:
                p.setRed(223)
            # checks and sets green values based off of rules
            if green < 50:
                p.setGreen(40)
            if green > 49 and green < 110:
                p.setGreen(98)
            if green > 109 and green < 180:
                p.setGreen(150)
            if green > 179 and green <256:
                p.setGreen(223)
            # checks and sets blue values based off of rules
            if blue < 50:
                p.setBlue(40)
            if blue > 49 and blue < 110:
                p.setBlue(98)
            if blue > 109 and blue < 180:
                p.setBlue(150)
            if blue > 179 and blue <256:
                p.setBlue(223)


def edgeDetect(pic, threshold):
    """
    Purpose:
        Make a new line drawing picture from orginal and return it 
    Arguements:
        pic (Picture): orignal picture
        threshold (number): the difference of numeric margin between two neighboring pixels
    Returns:
        bwPic : a new black and white picture
    Raises:
        Nothing
    """
    bwPic = gpt.Picture(pic)
    for x in range (0, pic.getWidth()-1):
        for y in range (0,pic.getHeight()-1):
            here = pic.getPixel(x,y)
            down = pic.getPixel(x,y+1)
            right = pic.getPixel(x+1, y)
            hereLum = (here.getRed() + here.getGreen() + here.getBlue())/3
            downLum = (down.getRed() + down.getGreen() + down.getBlue())/3
            rightLum = (right.getRed() + right.getGreen() + right.getBlue())/3
            if abs(hereLum-downLum)>10 and abs(hereLum-rightLum)>10:
                bwPic.setColor(x, y, (0,0,0))
            if abs(hereLum-downLum)<=10 and abs(hereLum-rightLum)<=10:
                bwPic.setColor(x,y,(255,255,255))
    return bwPic

def blend(pic7, pic8, alpha):
    """
    Purpose:
        Puts two pictures together by averaging each pair of matching pixels
    Arguements:
        pic7 (Picture): first picture
        pic8 (Picture): second picture
        alpha (float): how much of each pic to use from 0.0 to 1.0
    Returns:
        outPic: new picture with blend of pic7 and pic8
    Raises:
        Nothing
    """
    width = min(pic7.getWidth(), pic8.getWidth())
    height = min(pic7.getHeight(), pic8.getHeight())
    outPic = gpt.Picture(width, height)
    for x in range (0, width):
        for y in range (0, height):
            pix1 = pic7.getPixel(x,y)
            pix2 = pic8.getPixel(x,y)
            r = alpha * pix1.getRed() + (1 - alpha) * pix2.getRed()
            g = alpha * pix1.getGreen() + (1 - alpha) * pix2.getGreen()
            b = alpha * pix1.getBlue() + (1 - alpha) * pix2.getBlue()
            outPic.setColor(x,y,(r,g,b))
    return outPic
    

def mirrorHorizontal(pic):
    """
    Purpose:
        Copies the top half of picture onto bottom half
    Arguements:
        pic (Picture): the picture being mirrored
    Returns:
        Nothing
    Raises:
        Nothing
    """
    mirrorPoint = int(pic.getHeight () /2)
    height = pic.getHeight()
    for x in range (0, pic.getWidth()):
        for y in range (0, mirrorPoint):
            topPixel = pic.getPixel(x,y)
            bottomPixel = pic.getPixel(x,height-y-1)
            color = topPixel.getColor()
            bottomPixel.setColor(color)

def rotate90R(pic):
    """
    Purpose:
        Turns the picture 90 degrees to the right
    Arguements:
        pic (Picture): the picture being rotated
    Returns:
        pic: new picture of orginal picture rotated
    Raises:
        Nothing
    """
    width = pic.getWidth()
    height = pic.getHeight()
    Newpic = gpt.Picture(height, width)
    for col in range (0, width):
        for row in range (0, height):
            color = pic.getColor(col, row)
            Newpic.setColor(height-1-row, col, color)
    return Newpic

def rotate90L(pic):
    """
    Purpose:
        Turns the picture 90 degrees to the left
    Arguements:
        pic (Picture): the picture being rotated
    Returns:
        pic: new picture of orginal picture rotated
    Raises:
        Nothing
    """
    width = pic.getWidth()
    height = pic.getHeight()
    Newpic = gpt.Picture(height, width)
    for col in range(0, width):
        for row in range(0, height):
            color = pic.getColor(col, row)
            Newpic.setColor(row, width-1-col, color)
    return Newpic

def cropIt(pic, newWidth, newHeight):
    """
    Purpose:
        Makes a new picture with the center of the orginial picture.
        Picture cropped to the given width and height
    Arguements:
        pic: the orginal Picture that is going to be cropped
        newWdith: the width of the cropped picture
        newHeight: the height of the cropped picture
    Returns:
        A new Picture of size newWidth x newHeight, keeping the center of the picture
    Raises:
        Nothing
    """
    startX = ((pic.getWidth() - newWidth) // 2)
    startY = ((pic.getHeight() - newHeight) // 2)
    canvas = gpt.Picture(newWidth, newHeight)
    for x in range (0, newWidth):
        for y in range(0, newHeight):
            color = pic.getColor(x + startX, y + startY)
            canvas.setColor(x, y, color)
    return canvas


    # ---- YOUR CODE TO BUILD THE Webpage with the COLLAGE GOES HERE ----

def createDocType():
    """Return standard html5 DOCTYPE string"""
    return '<!DOCTYPE html>\n'

def startHTML():
    """Return html start tag"""
    return '<html>\n\n'

def endHTML():
    """Return html end tag"""
    return '</html>\n'

def startHead():
    """Return head start tag"""
    return '<head>\n\n'

def endHead():
    """Return head end tag"""
    return '</head>\n'

def startTitle():
    """Return title start tag"""
    return '<title>\n\n'

def endTitle():
    """Return title end tag"""
    return '</title>\n'

def startHead1():
    """Return h1 start tag"""
    return '<h1>\n\n'

def endHead1():
    """Return h1 end tag"""
    return '</h1>\n'

def startParagraph():
    """Return p start tag"""
    return '<p>\n\n'
    
def endParagraph():
    """Return p end tag"""
    return '</p>\n\n'

def startBody():
    """Return body start tag"""
    return '<body>\n\n'

def endBody():
    """Return body end tag"""
    return '</body>\n\n'

def createImage(imgfile, alttext):
    """Returns image element.

    Args:
        imgfile (str): Image file name.
        alttext (str): Alt text for image.
    """
    return f'<img src="{imgfile}" alt="{alttext}" />'

 

def createWebPage(imageFile, webPageFile):
    """Create web page that contains the collage.
    Parameter: imageFile - the image file name 
    Parameter: webPageFile - the filename of the output web page 
    Returns
    -------
    nothing
    """
    htmlFile = open(webPageFile, "wt")
    htmlFile.write(createDocType())
    htmlFile.write(startHTML())
    htmlFile.write(startHead())
    htmlFile.write(startTitle())
    htmlFile.write("Ann's Cottage Core")
    htmlFile.write(endTitle())
    htmlFile.write(endHead())
    htmlFile.write(startBody())
    htmlFile.write(startHead1())
    htmlFile.write("Welcome to Ann's Cottage Core Collage")
    htmlFile.write(endHead1())
    htmlFile.write(startParagraph())
    htmlFile.write('Hello! My name is Ann. I love looking at Pinterest boards and seeing different aesthetics. '
    'Hope you enjoy my take on the whimsical wildlife!')
    htmlFile.write(endParagraph())
    htmlFile.write(createImage(imageFile, alttext="Picture of Cottage Core Collage"))
    htmlFile.write(endBody())
    htmlFile.write(endHTML())
    htmlFile.close()   


# ============================================================================
# ============== Do NOT make any changes below this comment ==================
# ============================================================================

if __name__ == '__main__':

    # first command line argument, if any, is name of image file for output
    # second command line argument, if any, is name of the output html file name
    collageFile = None
    htmlFileName = "AnnHowardCottageCoreCollage.html"  #Default name

    if len(sys.argv) > 1:
        collageFile = sys.argv[1]
    if len(sys.argv) > 2:
        htmlFileName = sys.argv[2]    

    # temporarily set media path to project directory
    scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))

    # create the collage
    
    collage = createCollage()
    #collage.display()

    try:
        # either show collage on screen or write it to file
        if collageFile is None:
            collage.display()
            input('Press Enter to quit...')
        else:
            print(f'Saving collage to {collageFile}')
            collage.save(collageFile)
            createWebPage(collageFile, htmlFileName)
    except:
        print('Could not show or save picture')

