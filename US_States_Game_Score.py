# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:49:41 2022

@author: wajee
"""



import turtle
from turtle import Screen, Turtle
import time
#import importlib


#importlib.reload(turtle)

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score=0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()
    
    
    def update_score(self):
        
        self.write(f"Score : {self.score}/50",align="center",font=("Arial",24,"normal"))
        
    def game_over(self):
        
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",24,"normal"))
        
    def increase_score(self):
        
        self.score +=1
        self.clear()
        self.update_score()
    