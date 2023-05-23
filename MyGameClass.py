#have to import arcade in any of the files arcade is used
import arcade
#game class
class myGame(arcade.Window): #myGame's parent class is arcade.Window
    def __init__(self, width, height, title): #in python, self must be passed in class methods
        print("initializing myGame...")
        #how to call the parent class and initialize it in python
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.DIM_GRAY)
    
    def setup(self):
        print("underging setup...")

    def on_draw(self):
        #print("drawing myGame...")
        self.clear()
        #draw the screen