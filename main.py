# This file was created by: Vincent Temperino

# IMPORTS
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

'''
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [text-boxes](https://chat.openai.com/c/c6c9204a-de77-45e9-877f-58e0c6bbb889)
* [scrolling]https://chat.openai.com/c/5089dd3c-9339-43db-ab9b-204542651bdb
'''

import os
from settings import *
import sys
import time
import math
from sprites import *
from tkinter import *
from time import *
pg.init()
import numpy as np


# Setting up a bunch of different variables that are needed globablly through the script
started = False
screen = pg.display.set_mode((WIDTH, HEIGHT))
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img_folder")
sound_folder = os.path.join(game_folder, "sound_folder")
font = pg.font.Font(None, 50)
text = font.render("Decision Analysis App", True, TEXTC )
jpic = os.path.join(img_folder, "judgepic.png")
mouseclick = os.path.join(sound_folder,"mouseclick.wav")
jimage = pg.image.load(jpic)
jrect = jimage.get_rect(center=(WIDTH/2,300))
text_rect = text.get_rect(center=(WIDTH//2,80))
toplayer = Solids(0,0,800,200,0,0,PURPLE)
loadingimg = pg.image.load(os.path.join(img_folder,"loadingimg.png"))
loadrect = loadingimg.get_rect(center=(WIDTH/2,HEIGHT/2))
angle = 0

arrayofdata = {}
# These are the categories that the data will be categorized in
categoriesofdata = ["Education","Political Bias","Risk Aversion","Agreeableness","Empathy","Judgement"]


# CHARACTERISTIC COUNTS
givenvalues = []
alldata = []
TOTALAPPROVAL  = 0
totaladded = 0


# Runnning loop through whole process
class Run:
    def __init__(self):
        pg.mixer.init()
        pg.display.update()
        pg.display.set_caption("Decision Analysis App")
        self.clock = pg.time.Clock()
        self.running = True
        
    def new(self):
        self.analyzed = False
        self.all_sprites = pg.sprite.Group()

all_lines = pg.sprite.Group()


class SortingScreen:
    def __init__(self):
        screen.fill(BCKG)


#Allows to create textbox instance inside of a function or table
class TextBox:
    def __init__(self,x,y,w,h,text):
        self.rect = pg.Rect(x,y,w,h)
        self.text = text
        


# Gives results of all values both inputted and generated
class giveResults:

    def __init__(self):
        calculated = False
        gottendata = False

        givendata = [] # This table is for data given by the player (the 1-100 ranking)
        screen.fill(BCKG)
        if gottendata == False:
            for x in categoriesofdata:
                currentamt = 0
                for y in alldata:
                    datavalue = y[categoriesofdata.index(x)]
                    currentamt += int(datavalue)
                givendata.insert(categoriesofdata.index(x),currentamt)



        gottendata = True
        offsetamt = 15000
        ## ALGORITHYM

        if calculated == False:

            addtotal = 0

            for v in range(0,5):
                addtotal += (150*100*(givenvalues[v]*0.01))

            totaladded = addtotal - offsetamt
            totalapp = 0

            for x in categoriesofdata:
                
                percentamt = givenvalues[categoriesofdata.index(x)] * .001 
                amtinfluence = givendata[categoriesofdata.index(x)] * percentamt 
                totalapp += amtinfluence

            




            # Finding ratio of approval to total possible approval (finding %)
            TOTALAPPROVAL = totalapp
            TOTALAPPROVAL = TOTALAPPROVAL / totaladded



            amtofline = 645*TOTALAPPROVAL
            amtofline2 = 700 - amtofline
            line2 = pg.Rect(50,100,amtofline,20) # Creating large line with green on top
            pg.draw.rect(screen,GREEN,line2)
            line3 = pg.Rect(50+amtofline,100,amtofline2,20)
            pg.draw.rect(screen,pg.Color("black"),line3)
            fontrn = pg.font.Font(None, 20)
            resultslabel = font.render("Results", True, (0,0,0),)
            # Creating the label to display above green/red bars
            resultsbox = pg.Rect(30,35,100,50)
            screen.blit(resultslabel,resultsbox)
            percentscaled = round(TOTALAPPROVAL*100)
            percentl = font.render((str(percentscaled) + "% : Total Approval"),True,(0,0,0))
            prcbox = percentl.get_rect(center=(amtofline+50,145))
            screen.blit(percentl,prcbox)
            text_boxes = [
            ]

            for x in categoriesofdata:
                amtdone = givendata[categoriesofdata.index(x)]
                totalallowed = addtotal / len(categoriesofdata)
                percentforcat = (amtdone/totalallowed) * 10
                #calculating total amount of percent in approval and how to draw on line
                pfc = font.render((str(percentforcat) + "% : " + str(x)) , True, (0,0,0))
                pxlmovedown = 180 + (70 * int(categoriesofdata.index(x)))
                pfc2 = ((700 * (percentforcat * 0.01)) - 88)
                a = TextBox(50,int(pxlmovedown),pfc2,10, str(x))
                text_boxes.insert(categoriesofdata.index(x),a)
            
            for box in text_boxes:
                newone = pg.Rect(box.rect.x,box.rect.y,700,box.rect.h)
                pg.draw.rect(screen,RED,newone)
                pg.draw.rect(screen,GREEN,box.rect)
                dfont = pg.font.Font(None,5)
                dtext = font.render(box.text, True, (0,0,0))
                screen.blit(dtext, box.rect)




class generateData:

    def __init__(self,a):
        alldata.clear()
        end = False
        for i in range(0,a):
            arrayofdata = []
            
            for r in range(0,len(categoriesofdata)):

                rdata = random.randint(1,100)
                nameofcat = categoriesofdata[r]
                arrayofdata.insert(r-1,rdata) # inserting the data into the array
                alldata.insert(i-1,arrayofdata)
                if r >= a:
                    break
        screen.fill((0,0,0))
        puton = 0
        for l in range(len(alldata)):
            font = pg.font.Font(None, 15)
            textlfont = pg.font.Font(None,2) # setting font size
            for cat in range(len(categoriesofdata)):
                #generating data and putting on screen 
                textbox = pg.Rect(50+(120*cat),40+(40*l),100,5)
                textl = font.render(str(categoriesofdata[cat] + ": " + str(alldata[l][cat])),True,(255,255,255))
                screen.blit(textl,textbox)

            puton = l



'''
START ENDS
'''

class Sprite():
    def __init__(self):
        '''
        '''


# Setting more final variables and the run loop
r = Run()
button_color = GREEN

input_text = ""
sortt = False
slidermark = 0
gotvalues = False
pg.mixer.init(
)
mclickersound = pg.mixer.Sound(mouseclick)

while r.running:
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mclickersound.play()
        if event.type == pg.MOUSEBUTTONDOWN and started == False:
            if button_rect.collidepoint(event.pos):
           
                started = True
                generateData(150)
        elif event.type== pg.MOUSEBUTTONDOWN and started == True and sortt == False:
            SortingScreen()
            sortt = True

            spinspeed = 0.02 # How fast you want the circle to spin
                
            rotated_load = pg.transform.rotate(loadingimg, math.degrees(angle))
            rotated_rect = rotated_load.get_rect(center=loadrect.center)
            screen.blit(rotated_load, rotated_rect.topleft)

            angle += spinspeed # Calculating new angle for next spin




    pg.display.flip()
    r.new()
    amtdata = 150
    scrollspeed = 20
    dragging = False

    personalityc = 0



    if not started:
        buttonfont = pg.font.Font(None, 30)
        buttontext = font.render("generate", True, (0,0,0))
        button_rect = pg.Rect(50,HEIGHT-100,150,50)
        bt_rect = text.get_rect(center = button_rect.center)
        screen.fill(WHITE)
        button_color = GREEN
        pg.draw.rect(screen, button_color,button_rect)
        screen.blit(text, text_rect)
        screen.blit(buttontext,button_rect)
        screen.blit(jimage,jrect)

        keys = pg.key.get_pressed()
    elif started and sortt == False:
        buttonfont = pg.font.Font(None, 30)
        buttontext = font.render("   next", True, WHITE)
        bt_rect = text.get_rect(center = button_rect.center)
        button_color = GREEN
        pg.draw.rect(screen, button_color,button_rect)
        screen.blit(buttontext,button_rect)
    elif started and sortt and gotvalues == False:
        for i in categoriesofdata:
            window = Tk() # Using Tkinter
            window.title("Input Box") # Allows us to get easy data from user
            window.geometry('1000x1000') # Sets shape
            label1 = Label(window,text =str(i) + " (0-100)", fg = 'blue',font=('Arial',12))
            label1.grid(row=0+(1*categoriesofdata.index(i)),column =0,padx=5,pady=10)
            textbox1 = Entry(window,fg='blue',font=('Arial',12))
            textbox1.grid(row=0,column=1)
        
            infolabel = Label(window, text = "100 most important, 1 least", fg = "black",font = ('Arial',9))
            infolabel.grid(row=0,column=2)
            # infolabel.grid(row=12,column=0,padx=5,pady= 10)
            data = StringVar() # setting data variable

            def myFunction():
                message = textbox1.get()
                if message:
                    givenvalues.insert(categoriesofdata.index(i),int(message))
                    window.destroy()

            button1=Button(window,command=myFunction,text='Save',fg='blue',font=('Arial',12))
            button1.grid(row=7,column=1,sticky=W)

            
            if i == "Judgement":
                gotvalues = True

       


            window.mainloop()
    elif started and sortt and gotvalues:
        giveResults()
            



pg.quit()