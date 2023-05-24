#have to import arcade in any of the files arcade is used
import arcade
#game class
class myGame(arcade.Window): #myGame's parent class is arcade.Window
    def __init__(self, width, height, title): #in python, self must be passed in class methods
        print("initializing myGame...")
        #how to call the parent class and initialize it in python
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.DIM_GRAY) #will be the dirt

        self.player_list = None
        self.walls_list = None
    
    def setup(self):
        #setting up the sprites here makes it easier to incorporate a reset button in the game
        
        #set up player sprite
        self.player_list = arcade.SpriteList()
        #use_spatial_hash makes it faster to find collisions but slower to move. for walls, that's not a problem
        self.walls_list = arcade.SpriteList(use_spatial_hash=True) 
        self.player_sprite = arcade.Sprite("images\player_first_draft.png", 0.5) #second parameter is the scale
        #origin of the screen is the bottom left corner
        self.player_sprite.center_x = 120
        self.player_sprite.center_y = 120
        self.player_list.append(self.player_sprite)

        #set up walls/obstacles
        wall_path = "images\ground.png"
        wall = arcade.Sprite(wall_path, 0.5)
        wall.position = [360,360]
        self.walls_list.append(wall)



    def on_draw(self):
        #print("drawing myGame...")
        self.clear()

        #draw the objects on the screen
        self.player_list.draw()
        self.walls_list.draw()