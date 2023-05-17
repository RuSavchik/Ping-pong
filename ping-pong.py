from livewires import games, color
import random

games.init(screen_width = 437, screen_height = 780, fps = 50)


class Player(games.Sprite):

    image = games.load_image("rocket.bmp")
    
    def __init__(self):
        super(Player, self).__init__(image = Player.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
            

class Ball(games.Sprite):

    image = games.load_image("ball.bmp")
    
    speed = 2

    def __init__(self):
        super(Ball, self).__init__(image = Ball.image,
                                    x = games.screen.width / 2,
                                    top = 0,
                                    dx = Ball.speed,
                                    dy = Ball.speed)

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif self.top <= 0:
            self.dy = -self.dy
        if self.overlapping_sprites:
            self.dy = -self.dy
        self.check_catch()

    def check_catch(self):
        if self.bottom >= games.screen.height:
            self.end_game()
            self.destroy()

    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


def main():
    wall_image = games.load_image("table.jpg", transparent = False)
    games.screen.background = wall_image
    
    the_player = Player()
    games.screen.add(the_player)

    the_ball = Ball()
    games.screen.add(the_ball)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()


main()
