# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:36:17 2022

@author: wajee
"""

MAP_PATH = "map_path"
STATES_PATH = "csv file path"  #Absolute or relative

import pandas as pd
import turtle
from turtle import Screen, Turtle
import importlib
importlib.reload(turtle)

from US_States_Game_Score import Score


data = pd.read_csv(STATES_PATH)

timmy = Turtle()
timmy.hideturtle()
screen = Screen()
screen.setup(width=800 , height=600)
screen.title("US State Game")
screen.bgpic(MAP_PATH)

score = Score()

counter = 0
game_is_on =True


while game_is_on:
    
    screen_text=screen.textinput("USA States", "Enter State Name:")
    country_name = screen_text.title()
    
    row_data = data[data.state == country_name]
    
    if (counter == 50):
        
        score.win_condition()
        game_is_on = False
        
        
    if (row_data.empty):
        
       game_is_on = False
       score.game_over()
    
    else:
        
        x_coordinate = row_data.x
        y_coordinate = row_data.y
        
        x_list= x_coordinate.to_list()
        y_list=y_coordinate.to_list()
        
        strings_x = [str(value_x) for value_x in x_list]
        x_string = "".join(strings_x)
        x_integer = int(x_string)
        
        strings_y = [str(value_y) for value_y in y_list]
        y_string = "".join(strings_y)
        y_integer = int(y_string)
        
        data_points = (x_integer,y_integer)
        
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(data_points)
        timmy.write(f"{country_name}",font=("Arial",8,"normal"))
        score.increase_score()
        counter = counter + 1

        


screen.exitonclick()
