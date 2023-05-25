#have to import arcade in any of the files arcade is used
import arcade
#game class
class myGame(arcade.Window): #myGame's parent class is arcade.Window
    def __init__(self, width, height, title): #in python, self must be passed in class methods
        
        #how to call the parent class and initialize it in python
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.COFFEE) #will be the dirt

        self.player_list = None
        self.scene = None #scene object (all the walls)
        #self.walls_list = None
    
    def setup(self, width, height):
        #setting up the sprites here makes it easier to incorporate a reset button in the game
        #we can use scene instead of player lists and wall lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls",use_spatial_hash=True)
        #use_spatial_hash makes it faster to find collisions but slower to move. for walls, that's not a problem
        


        self.player_sprite = arcade.Sprite("images\player_sprite.png", 0.5) #second parameter is the scale
        #origin of the screen is the bottom left corner
        self.player_sprite.center_x = 120
        self.player_sprite.center_y = 120
        self.scene.add_aprite("Player", self.player_sprite)
        
        #set up walls/obstacles
        soil_path = "images\soil_1.png"

        #places soil along top and bottom of window
        for x in range(32, width, 64):
            #make walls, append them
            wallbottom = arcade.Sprite(soil_path, 0.5)
            wallbottom.position = [x,32]
            self.scene.add_sprite("Wall",wallbottom)

            walltop = arcade.Sprite(soil_path, 0.5)
            walltop.position = [x,height - 32]
            self.scene.add_sprite("Wall",walltop)

        #place soil in other specific places
        wall = arcade.Sprite(soil_path, 0.5)
        wall.position = [360,360]
        self.scene.add_sprite("Wall",wall)

        #set up game physics
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls"))



    def on_draw(self):
        #print("drawing myGame...")
        self.clear()

        #draw the objects on the screen
        self.scene.draw()