#have to import arcade in any of the files arcade is used
import arcade
#game class
class myGame(arcade.Window): #myGame's parent class is arcade.Window
    def __init__(self, width, height, title, speed, jump_speed): #in python, self must be passed in class methods
        
        #how to call the parent class and initialize it in python
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.COFFEE) #will be the dirt

        self.player_speed = speed
        self.player_jump_speed = jump_speed
        self.gravity = 1

        self.scene = None #scene object (all the walls)
        self.physics_engine = None #physics engine
        self.player_sprite = None

        self.camera = None

    def setup(self, width, height, camera_width, camera_height):
        #setting up the sprites here makes it easier to incorporate a reset button in the game
        #we can use scene instead of player lists and wall lists
        self.scene = arcade.Scene() 
        #use_spatial_hash makes it faster to find collisions but slower to move. for walls, that's not a problem
        

        self.player_sprite = arcade.Sprite("images\player_sprite.png", 0.5) #second parameter is the scale
        #origin of the screen is the bottom left corner
        self.player_sprite.center_x = 120
        self.player_sprite.center_y = 120
        self.scene.add_sprite("Player", self.player_sprite)
        
        #set up walls/obstacles
        soil_path = "images\soil_1.png"

        #places soil along top and bottom of window
        for x in range(32, width, 64):
            #make walls, append them
            wallbottom = arcade.Sprite(soil_path, 0.5)
            wallbottom.position = [x,32]
            self.scene.add_sprite("Walls",wallbottom)

            walltop = arcade.Sprite(soil_path, 0.5)
            walltop.position = [x,height - 32]
            self.scene.add_sprite("Walls",walltop)

        for y in range(32, height, 64):
            #make walls, append them
            wallleft = arcade.Sprite(soil_path, 0.5)
            wallleft.position = [32,y]
            self.scene.add_sprite("Walls",wallleft)

            wallright = arcade.Sprite(soil_path, 0.5)
            wallright.position = [width - 32,y]
            self.scene.add_sprite("Walls",wallright)

        #place soil in other specific places
        ledge_one = [[i, 250] for i in range(86, 832, 64)]
        fence_one = [[1000,j] for j in range(86, 151,64)]
        fence_two = [[2000,j] for j in range(86, 151,64)]
        ledge_two = [[i, 300] for i in range(1128, 1896, 64)]
        ledge_three = [[2064,214], [2064,278]] + [[i,342] for i in range(2128, 2704, 64)] + [[2896,182], [2832,18250]]

        soil_coordinates = ledge_one + fence_one + fence_two + ledge_two + ledge_three
        for coor in soil_coordinates:
            wall = arcade.Sprite(soil_path, 0.5)
            wall.position = coor
            self.scene.add_sprite("Walls",wall)

        #set up game physics
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, gravity_constant = self.gravity, walls = self.scene["Walls"])
        #platforms will be walls that can move

        self.camera = arcade.Camera(camera_width, camera_height)

    def on_key_press(self, key, modifiers):
        #have to used multiple if and elif statements because python has to switch case functions built in
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = self.player_jump_speed
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -self.player_speed
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = self.player_speed

    def on_key_release(self, key, modifiers):
        #have to used multiple if and elif statements because python has to switch case functions built in
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_on_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        #prevents camera from moving past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0

        player_centered = screen_center_x, screen_center_y
        self.camera.move_to(player_centered)
    
    def on_update(self, delta_time):
        self.physics_engine.update()

        self.center_camera_on_player()


    def on_draw(self):
        #print("drawing myGame...")
        self.clear()

        #draw the objects on the screen
        self.scene.draw()
        self.camera.use()