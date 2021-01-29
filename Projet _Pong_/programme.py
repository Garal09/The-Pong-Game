#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:51:21 2020

@author: ant
"""

import arcade
import random
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

SW = 1000
SH = 650
ST = "The Ultimate Pong Game"
SpeedBarre = 20


class InstructionView(arcade.View):
    
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("The Ultimate Pong Game", SW/2, SH/2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("press any key to continue", SW / 2, SH / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

class GameView(arcade.View):
    
    def __init__(self):
        
        super().__init__()
        
        self.barre1_list = None
        self.barre2_list = None
        self.ball_list = None
        self.barre1_Sprite = None
        self.barre2_Sprite = None
        self.balle_Sprite = None
        self.wall_list = None
        self.wall_Sprite = None
        self.physics_engine1 = None
        self.physics_engine2 = None
        self.limite_list = None
        self.limite_Sprite = None
        self.game_over = None
        self.game_change = None
        self.total_time = 0.0
        self.counter_time = 0.0
        self.message = ""
        self.Lscore = 0
        self.Rscore = 0
        self.limite_list_L = None
        self.limite_list_R = None


        

        arcade.set_background_color(arcade.csscolor.WHITE)
        
        self.limite_list_L = arcade.SpriteList()
        self.limite_list_R = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.ball_Sprite = arcade.Sprite("balle.png", 0.1)
        self.ball_Sprite.center_x = 500
        self.ball_Sprite.center_y = 300
        self.ball_list.append(self.ball_Sprite)
        self.ball_Sprite.change_x = random.randrange(1,3)
        self.ball_Sprite.change_y = random.randrange(1,3)

    
    def setup(self):
        
        self.barre1_list = arcade.SpriteList()
        self.barre2_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.limite_list = arcade.SpriteList()
        
        for i in range(0, 768, 128):
            wall = arcade.Sprite("wall.png",1)
            wall.center_x = -64
            wall.center_y = i
            self.limite_list.append(wall)
            self.limite_list_L.append(wall)
            
        for i in range(0, 768, 128):
            wall = arcade.Sprite("wall.png",1)
            wall.center_x = 1064
            wall.center_y = i
            self.limite_list.append(wall)
            self.limite_list_R.append(wall)

        

        for i in range(0, 1000, 128):
            wall = arcade.Sprite("wall.png",1)
            wall.center_x = i
            wall.center_y = 714
            self.wall_list.append(wall)
            
        for i in range(0, 1000, 128):
            wall = arcade.Sprite("wall.png",1)
            wall.center_x = i
            wall.center_y = -64
            self.wall_list.append(wall)
            
        
        
        image_source = "barre.png"
        self.barre1_Sprite = arcade.Sprite(image_source, 1)
        self.barre2_Sprite = arcade.Sprite(image_source, 1)
        self.barre1_Sprite.center_x = 64
        self.barre1_Sprite.center_y = 300
        self.barre2_Sprite.center_x = 936
        self.barre2_Sprite.center_y = 300
        self.barre1_list.append(self.barre1_Sprite)
        self.barre2_list.append(self.barre2_Sprite)
        
        self.ball_list = arcade.SpriteList()
        self.ball_Sprite = arcade.Sprite("balle.png", 0.1)
        self.ball_Sprite.center_x = 500
        self.ball_Sprite.center_y = 300
        self.ball_list.append(self.ball_Sprite)
        self.ball_Sprite.change_x = random.randrange(1,3)
        self.ball_Sprite.change_y = random.randrange(1,3)
        
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.barre1_Sprite, self.wall_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.barre2_Sprite, self.wall_list)
        
    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.Z:
            self.barre1_Sprite.change_y = SpeedBarre
            
        elif key == arcade.key.S:
            self.barre1_Sprite.change_y = - SpeedBarre
            
        elif key == arcade.key.UP:
            self.barre2_Sprite.change_y = SpeedBarre
        
        elif key == arcade.key.DOWN:
            self.barre2_Sprite.change_y = -SpeedBarre
        
    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.Z:
            self.barre1_Sprite.change_y = 0
        elif key == arcade.key.S:
            self.barre1_Sprite.change_y = 0
            
        elif key == arcade.key.UP:
            self.barre2_Sprite.change_y = 0
        
        elif key == arcade.key.DOWN:
            self.barre2_Sprite.change_y = 0
        
    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_text(self.message, 500, 300, arcade.color.BLACK, 30)
        arcade.draw_text(str(self.Lscore), 0, 600, arcade.color.BLACK, 30)
        arcade.draw_text(str(self.Rscore), 970, 600, arcade.color.BLACK, 30)
        self.barre1_list.draw()
        self.barre2_list.draw()
        self.wall_list.draw()
        self.ball_list.draw()

    def on_update(self, delta_time):
        
        self.physics_engine1.update()
        self.physics_engine2.update()
        self.ball_Sprite.update()
        self.total_time += delta_time

            
        if arcade.check_for_collision_with_list(self.ball_Sprite, self.limite_list_L):
            self.Rscore += 1
#            self.counter_time = self.total_time
#            self.message = str(int(self.counter_time))
            self.ball_Sprite.center_y = 300
            self.ball_Sprite.center_x = 500
            self.ball_Sprite.change_x = random.randrange(1,3)
            self.ball_Sprite.change_y = random.randrange(1,3)
            
        if arcade.check_for_collision_with_list(self.ball_Sprite, self.limite_list_R):
            self.Lscore += 1
            self.ball_Sprite.center_y = 300
            self.ball_Sprite.center_x = 500
            self.ball_Sprite.change_x = random.randrange(1,3)
            self.ball_Sprite.change_y = random.randrange(1,3)
            

        elif arcade.check_for_collision(self.ball_Sprite, self.barre1_Sprite):
                self.ball_Sprite.change_x *= -1.2
        elif arcade.check_for_collision(self.ball_Sprite, self.barre2_Sprite):
                self.ball_Sprite.change_x *= -1.2
        elif arcade.check_for_collision_with_list(self.ball_Sprite, self.wall_list):
                self.ball_Sprite.change_y *= -1
                

def main():
    window = arcade.Window(SW,SH,ST)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()