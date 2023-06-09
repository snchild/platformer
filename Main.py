#imports
import arcade
import MyGameClass

#declare constants
MAP_HEIGHT = 2016 #should both be divisible by 64
MAP_WIDTH = 3056 
SCREEN_HEIGHT = 600 #units: pixels
SCREEN_WIDTH = 1000
SCREEN_TITLE = "Sierra's Platformer"
PLAYER_SPEED = 5 #number of pixels it moves each frame
JUMP_SPEED = 20

def main ():
    myWindow = MyGameClass.myGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PLAYER_SPEED, JUMP_SPEED)
    myWindow.setup(MAP_WIDTH, MAP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run() #begins gameplay loop

if __name__ == "__main__":
    main()
