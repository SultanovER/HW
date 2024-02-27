import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "STARWARS"
LAZER_SPEED = 5
METEOR_SPPED = 3

class Lazer(arcade.Sprite):
    def __init__(self):
        super().__init__('laser.png', 0.8)
        self.center_x = window.falcon.center_x
        self.bottom = window.falcon.top
        self.change_y = 5


class Falcon(arcade.Sprite):
    def __init__(self):
        super().__init__('falcon.png', 0.3)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = LAZER_SPEED
        self.laser_sound = arcade.load_sound('laser.wav')

    def update(self):
        self.center_y += self.change_y
        if self.center_y > SCREEN_HEIGHT:
            self.kill()

    def update(self):
        self.center_x += self.change_x

class Meteor(arcade.Sprite):
    def __init__(self):
        super().__init__('meteorit.png', 0.3)
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT + 50
        self.change_y = -METEOR_SPPED
    def update(self):
        super().update()
        if self.top < 0:
            self.kill()

class Game(arcade.Window):
    def __init__(self, width, height, tile):
        super().__init__(width, height, tile)
        self.bg = arcade.load_texture('background.jpg')
        self.falcon = Falcon()
        self.set_mouse_visible(False)
        self.lasers = arcade.SpriteList()
        self.meteors = arcade.SpriteList()
        self.setup()

    # Размещение объектов на сцене
    def setup(self):
        for i in range(5):
            meteor = Meteor()
            self.meteors.append(meteor)

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.falcon.draw()
        self.lasers.draw()
        self.meteors.draw()


    def update(self, delta_time: float):
        self.falcon.update()
        self.lasers.update()
        self.meteors.update()

        for meteor in arcade.check_for_collision_with_list(self.falcon, self.meteors):
            meteor.kill()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.falcon.center_x = x
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        laser = Lazer()


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
