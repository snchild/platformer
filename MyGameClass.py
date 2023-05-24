#have to import arcade in any of the files arcade is used
import arcade
#game class
class myGame(arcade.Window): #myGame's parent class is arcade.Window
    def __init__(self, width, height, title): #in python, self must be passed in class methods
        print("initializing myGame...")
        #how to call the parent class and initialize it in python
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.COFFEE) #will be the dirt

        self.player_list = None
        self.walls_list = None
    
    def setup(self, width, height):
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
        soil_path = "images\soil_1.png"

        #places soil along top and bottom of window
        for x in range(32, width, 64):
            #make walls, append them
            wallbottom = arcade.Sprite(soil_path, 0.5)
            wallbottom.position = [x,32]
            self.walls_list.append(wallbottom)

            walltop = arcade.Sprite(soil_path, 0.5)
            walltop.position = [x,height - 32]
            self.walls_list.append(walltop)

        



    def on_draw(self):
        #print("drawing myGame...")
        self.clear()

        #draw the objects on the screen
        self.player_list.draw()
        self.walls_list.draw()