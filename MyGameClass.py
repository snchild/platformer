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
        f_1 = [[i, 250] for i in range(86, 832, 64)]
        f_2 = [[1000,j] for j in range(86, 151,64)]
        f_3 = [[i, 300] for i in range(1128, 1896, 64)] + [[2000,j] for j in range(86, 151,64)]
        f_4 = [[2064,214], [2064,278]] + [[i,342] for i in range(2128, 2704, 64)] + [[2896,182], [2832,182]]
        f_5 = [[i, 650] for i in range(278, 663, 64)] + [[i, 842] for i in range(470, 662, 64)] + [[598,1034], [662,1034], [726,1162], [918, 1162]]
        f_6 = [[668,420], [732,420]] + [[i, 548] for i in range(892, 1724, 64)] + [[1724,484]] + [[1276, j] for j in range(612, 741, 64)]
        f_7 = [[i, 804] for i in range(1340, 1661, 64)] + [[1468, j] for j in range(868, 1125, 64)] + [[i, 1188] for i in range(1148, 1597, 64)]
        f_8 = [[i, 676] for i in range(1852, 2129, 64)]
        f_9 = [[i, 534] for i in range(2448, 2769, 64)]
        f_10 = [[i, 804] for i in range(2256, 2768, 64)] + [[2320,868], [2960,804]]
        f_11 = [[1596, j] for j in range(1252, 1700, 64)] + [[1468,1380],[1532,1380], [1532, 1508]]
        f_12 = [[1852,932],[1870,1500],[1900,1168],[2164,1000],[2320,1400],[2400,1100],[2500,1250],[2600,950],[2700,1100],[2900,1100],[2950,1300]]
        f_13 = [[i, 1604] for i in range(96, 253, 64)] + [[i, 1732] for i in range(444, 1020, 64)] + [[i, 1732] for i in range(1148, 1405, 64)]
        f_14 = [[i, 1699] for i in range(1660, 2045, 64)]
        f_15 = [[i, 1603] for i in range(2173, 2896, 64)]
        f_16 = [[2704,1731],[2768,1795],[2832,1827],[2896, 1827],[2960,1827]]

        soil_coordinates = f_1 + f_2 + f_3 + f_4 + f_5 + f_6 + f_7 + f_8 + f_9 + f_10 + f_11 + f_12 + f_13 + f_14 + f_15 + f_16
        for coor in soil_coordinates:
            wall = arcade.Sprite(soil_path, 0.5)
            wall.position = coor
            self.scene.add_sprite("Walls",wall)

        #add door
        door = arcade.Sprite("images\door_sprite.png",0.5)
        door.position = [96,1668]
        self.scene.add_sprite("Door", door)

        #set up game physics
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, gravity_constant = self.gravity, walls = [self.scene["Walls"],self.scene["Door"]])
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

        #check if the player has reached the "door"
        if (self.player_sprite.position == (160,1668) or self.player_sprite.position == (96,1732)):
            self.if_won()
            
    def on_draw(self):
        #print("drawing myGame...")
        self.clear()

        #draw the objects on the screen
        self.scene.draw()
        self.camera.use()

    def if_won(self):
        print("Congradulations you won!")
        arcade.close_window()