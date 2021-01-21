#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:51:21 2020

@author: ant
"""

import arcade
import random

SW = 1000
SH = 650
ST = "Blue Square"
SpeedBarre = 20



class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(SW, SH, ST)
        
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

        

        
        arcade.set_background_color(arcade.csscolor.WHITE)
        
        
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
            
        for i in range(0, 768, 128):
            wall = arcade.Sprite("wall.png",1)
            wall.center_x = 1064
            wall.center_y = i
            self.limite_list.append(wall)
        

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
        
        self.barre1_list.draw()
        self.barre2_list.draw()
        self.wall_list.draw()
        self.ball_list.draw()
        
    def on_update(self, delta_time):
        
        self.physics_engine1.update()
        self.physics_engine2.update()
        self.ball_Sprite.update()
            
        if arcade.check_for_collision_with_list(self.ball_Sprite, self.limite_list):
            self.game_change = True
        if self.game_change != True :
            if arcade.check_for_collision(self.ball_Sprite, self.barre1_Sprite):
                self.ball_Sprite.change_x *= -1.2
            elif arcade.check_for_collision(self.ball_Sprite, self.barre2_Sprite):
                self.ball_Sprite.change_x *= -1.2
            elif arcade.check_for_collision_with_list(self.ball_Sprite, self.wall_list):
                self.ball_Sprite.change_y *= -1
        else:
            
            self.ball_list = arcade.SpriteList()
            self.ball_Sprite = arcade.Sprite("balle.png", 0.1)
            self.ball_Sprite.center_x = 500
            self.ball_Sprite.center_y = 300
            self.ball_list.append(self.ball_Sprite)
            self.ball_Sprite.change_x = random.randrange(1,3)
            self.ball_Sprite.change_y = random.randrange(1,3)
            
        
        

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()