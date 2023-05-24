#imports
import arcade
import MyGameClass

#declare constants
SCREEN_HEIGHT = 650 #units: pixels
SCREEN_WIDTH = 1000
SCREEN_TITLE = "Sierra's Platformer"

def main ():
    myWindow = MyGameClass.myGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    myWindow.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run() #begins gameplay loop

if __name__ == "__main__":
    main()
