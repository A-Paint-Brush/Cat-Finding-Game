from Path import get_path
import pygame
import pygame.mixer
import random
import Cat
import Timer


class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.r = random.Random()
        self.first_run = True
        self.first_play = True
        self.load_screen = Timer.Timer()
        self.bubble_timer = Timer.Timer()
        self.bubble_timer.reset()
        self.found = False
        self.wrong = False
        self.active = True
        self.data = []
        self.bubble = False
        self.mode = ""
        self.full_screen = False
        self.cat_pen = []
        self.page = 0
        self.mistakes = 0
        self.cats_found = 0
        self.current_game = "Instructions"
        self.font1 = pygame.font.SysFont("Times New Roman", 18)
        self.enter_full_screen_icon = pygame.image.load(get_path("Images/Enter Fullscreen Icon.png"))
        self.exit_full_screen_icon = pygame.image.load(get_path("Images/Exit Fullscreen Icon.png"))
        self.meow = pygame.mixer.Sound(get_path("Sounds/Meow.wav"))
        self.connect = pygame.mixer.Sound(get_path("Sounds/Connect.wav"))
        self.disconnect = pygame.mixer.Sound(get_path("Sounds/Disconnect.wav"))
        self.clock = pygame.time.Clock()
        self.gameRun = True
        self.monitor_width = pygame.display.Info().current_w
        self.monitor_height = pygame.display.Info().current_h
        self.fraction_x_pos = [0.0125,
                               0.10625,
                               0.2,
                               0.29375,
                               0.3875,
                               0.48125,
                               0.575,
                               0.66875,
                               0.7625,
                               0.85625,
                               0.0125,
                               0.10625,
                               0.2,
                               0.29375,
                               0.3875,
                               0.48125,
                               0.575,
                               0.66875,
                               0.7625,
                               0.85625,
                               0.0125,
                               0.10625,
                               0.2,
                               0.29375,
                               0.3875,
                               0.48125,
                               0.575,
                               0.66875,
                               0.7625,
                               0.85625,
                               0.0125,
                               0.10625,
                               0.2,
                               0.29375,
                               0.3875,
                               0.48125,
                               0.575,
                               0.66875,
                               0.7625,
                               0.85625,
                               0.0125,
                               0.10625,
                               0.2,
                               0.29375,
                               0.3875,
                               0.48125,
                               0.575,
                               0.66875,
                               0.7625,
                               0.85625,
                               0.0125,
                               0.10625,
                               0.2,
                               0.29375,
                               0.3875,
                               0.48125,
                               0.575,
                               0.66875,
                               0.7625,
                               0.85625,
                               0.0125,
                               0.10625,
                               0.2,
                               0.29375,
                               0.3875,
                               0.48125,
                               0.575,
                               0.66875,
                               0.7625,
                               0.85625]
        self.fraction_y_pos = [0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.00694444444,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.1375,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.26805555555,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.39861111111,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.52916666666,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.65972222222,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777,
                               0.79027777777]
        self.images = [pygame.transform.scale(pygame.image.load(get_path("Images/%d.png" % (i,))), (44, 47))
                       for i in range(1, 14 + 1)]
        pygame.display.set_caption("Cat Finding Game")
        self.screen = pygame.display.set_mode((480, 360), pygame.RESIZABLE)
        while self.gameRun:
            self.clock.tick(60)
            if self.current_game == "Instructions":
                pages = [["Instructions:", "Find the different cat and click it. Click the button on the",
                          "bottom right corner of the screen to enter or exit fullscreen",
                          "mode. You can also press the escape key to exit fullscreen",
                          "mode.",
                          "Press space to start the game."]]
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.gameRun = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if self.page == len(pages) - 1:
                                self.current_game = "Main"
                        elif event.key == pygame.K_LEFT:
                            if self.page > 0:
                                self.page = self.page - 1
                        elif event.key == pygame.K_RIGHT:
                            if self.page < len(pages) - 1:
                                self.page = self.page + 1
                        elif event.key == pygame.K_ESCAPE:
                            if self.full_screen:
                                self.full_screen = False
                                self.screen = pygame.display.set_mode((480, 360), pygame.RESIZABLE)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.display.Info().current_w - 28 <= \
                                pygame.mouse.get_pos()[0] <= pygame.display.Info().current_w - 2 and pygame.display.Info().current_h - 28 <= \
                                pygame.mouse.get_pos()[1] <= pygame.display.Info().current_h - 2:
                            if not self.full_screen:
                                self.full_screen = True
                                self.screen = pygame.display.set_mode((self.monitor_width, self.monitor_height), pygame.FULLSCREEN)
                            else:
                                self.full_screen = False
                                self.screen = pygame.display.set_mode((480, 360), pygame.RESIZABLE)
                    elif event.type == pygame.VIDEORESIZE:
                        if not self.full_screen:
                            width = event.w
                            height = event.h
                            if width < 480:
                                width = 480
                            elif height < 360:
                                height = 360
                            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    self.screen.fill((109, 255, 102))
                    for line in range(0, len(pages[self.page])):
                        self.screen.blit(self.font1.render(pages[self.page][line],
                                                           True,
                                                           (0, 0, 0),
                                                           (109, 255, 102)), (10, 25 * line))
                    if not self.full_screen:
                        self.screen.blit(self.enter_full_screen_icon, (pygame.display.Info().current_w - 28, pygame.display.Info().current_h - 28))
                    else:
                        self.screen.blit(self.exit_full_screen_icon, (pygame.display.Info().current_w - 28, pygame.display.Info().current_h - 28))
                    pygame.display.update()
            elif self.current_game == "Main":
                if self.first_run:
                    self.first_play = True
                    self.correct_cat = self.r.randint(0, 69)
                    self.different_cat = self.images[self.r.randint(1, len(self.images) - 1)]
                    self.first_run = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.gameRun = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.active:
                            mouse_pos = pygame.mouse.get_pos()
                            for cat in self.cat_pen:
                                if cat.collision_check(mouse_pos):
                                    if cat.cat_identity_check(self.correct_cat):
                                        self.bubble_timer.reset()
                                        self.found = True
                                        self.active = False
                                        self.speaking_cat = cat.clone_number
                                        self.cats_found = self.cats_found + 1
                                        self.connect.play()
                                        break
                                    else:
                                        self.bubble_timer.reset()
                                        self.wrong = True
                                        self.active = False
                                        self.speaking_cat = cat.clone_number
                                        self.mistakes = self.mistakes + 1
                                        self.meow.play()
                                        break
                        if pygame.display.Info().current_w - 28 <= \
                                pygame.mouse.get_pos()[
                                    0] <= pygame.display.Info().current_w - 2 and pygame.display.Info().current_h - 28 <= \
                                pygame.mouse.get_pos()[1] <= pygame.display.Info().current_h - 2:
                            if not self.full_screen:
                                self.full_screen = True
                                self.screen = pygame.display.set_mode((self.monitor_width, self.monitor_height),
                                                                      pygame.FULLSCREEN)
                            else:
                                self.full_screen = False
                                self.screen = pygame.display.set_mode((480, 360), pygame.RESIZABLE)
                    elif event.type == pygame.VIDEORESIZE:
                        if not self.full_screen:
                            width = event.w
                            height = event.h
                            if width < 480:
                                width = 480
                            elif height < 360:
                                height = 360
                            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if self.full_screen:
                                self.full_screen = False
                                self.screen = pygame.display.set_mode((480, 360), pygame.RESIZABLE)
                if not self.active:
                    message_pos_x = self.cat_pen[self.speaking_cat].pos_x
                    message_pos_y = self.cat_pen[self.speaking_cat].pos_y
                width = pygame.display.Info().current_w
                height = pygame.display.Info().current_h
                self.cat_pen.clear()
                for number in range(0, len(self.fraction_x_pos)):
                    self.cat_pen.append(Cat.Cat(width * self.fraction_x_pos[number], height * self.fraction_y_pos[number], number))
                self.screen.fill((109, 255, 102))
                for cat in range(0, len(self.cat_pen)):
                    if self.cat_pen[cat].clone_number == self.correct_cat:
                        self.screen.blit(self.different_cat, (int(self.cat_pen[cat].pos_x), int(self.cat_pen[cat].pos_y)))
                    else:
                        self.screen.blit(self.images[0], (int(self.cat_pen[cat].pos_x), int(self.cat_pen[cat].pos_y)))
                if self.found:
                    if message_pos_y < 237.499999992:
                        if message_pos_x > 276:
                            self.create_text_bubble(["You found me!"],
                                                    (round(message_pos_x - 80), round(message_pos_y + 65)), 5,
                                                    "top_right")
                        else:
                            self.create_text_bubble(["You found me!"],
                                                    (round(message_pos_x), round(message_pos_y + 65)), 5,
                                                    "top_left")
                    else:
                        if message_pos_x > 276:
                            self.create_text_bubble(["You found me!"],
                                                    (round(message_pos_x - 70), round(message_pos_y - 40)), 5,
                                                    "bottom_right")
                        else:
                            self.create_text_bubble(["You found me!"],
                                                    (round(message_pos_x), round(message_pos_y - 40)), 5,
                                                    "bottom_left")
                if self.wrong:
                    if message_pos_y < 237.499999992:
                        if message_pos_x > 276:
                            self.create_text_bubble(["Meow!", "It's not me!", "Look more carefully!"],
                                                    (round(message_pos_x - 120), round(message_pos_y + 65)), 5,
                                                    "top_right")
                        else:
                            self.create_text_bubble(["Meow!", "It's not me!", "Look more carefully!"],
                                                    (round(message_pos_x), round(message_pos_y + 65)), 5,
                                                    "top_left")
                    else:
                        if message_pos_x > 276:
                            self.create_text_bubble(["Meow!", "It's not me!", "Look more carefully!"],
                                                    (round(message_pos_x - 120), round(message_pos_y - 75)), 5,
                                                    "bottom_right")
                        else:
                            self.create_text_bubble(["Meow!", "It's not me!", "Look more carefully!"],
                                                    (round(message_pos_x), round(message_pos_y - 75)), 5,
                                                    "bottom_left")
                if not self.full_screen:
                    self.screen.blit(self.enter_full_screen_icon,
                                     (pygame.display.Info().current_w - 28, pygame.display.Info().current_h - 28))
                else:
                    self.screen.blit(self.exit_full_screen_icon, (pygame.display.Info().current_w - 28, pygame.display.Info().current_h - 28))
                self.screen.blit(self.font1.render("Cats Found: " + str(self.cats_found) + "   Mistakes: " + str(self.mistakes), True, (0, 0, 0), (109, 255, 102)), (10, pygame.display.Info().current_h - 21))
                pygame.display.update()
            elif self.current_game == "Loading":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.gameRun = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.display.Info().current_w - 28 <= \
                                pygame.mouse.get_pos()[0] <= pygame.display.Info().current_w - 2 and pygame.display.Info().current_h - 28 <= \
                                pygame.mouse.get_pos()[1] <= pygame.display.Info().current_h - 2:
                            if not self.full_screen:
                                self.full_screen = True
                                self.screen = pygame.display.set_mode((self.monitor_width, self.monitor_height), pygame.FULLSCREEN)
                            else:
                                self.full_screen = False
                                self.screen = pygame.display.set_mode((480, 360), pygame.RESIZABLE)
                    elif event.type == pygame.VIDEORESIZE:
                        if not self.full_screen:
                            width = event.w
                            height = event.h
                            if width < 480:
                                width = 480
                            elif height < 360:
                                height = 360
                            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if self.full_screen:
                                self.full_screen = False
                                self.screen = pygame.display.set_mode((480, 360), pygame.RESIZABLE)
                if self.load_screen.get_time() > 5:
                    self.current_game = "Main"
                    self.first_run = True
                elif self.load_screen.get_time() >= 4:
                    if self.first_play:
                        self.disconnect.play()
                        self.first_play = False
                self.screen.fill((109, 255, 102))
                self.screen.blit(self.font1.render("Herding Cats...", True, (0, 0, 0), (109, 255, 102)), (int(pygame.display.Info().current_w / 2 - 54.5), int(pygame.display.Info().current_h / 2 - 10.5)))
                if not self.full_screen:
                    self.screen.blit(self.enter_full_screen_icon,
                                     (pygame.display.Info().current_w - 28, pygame.display.Info().current_h - 28))
                else:
                    self.screen.blit(self.exit_full_screen_icon,
                                     (pygame.display.Info().current_w - 28, pygame.display.Info().current_h - 28))
                pygame.display.update()
        pygame.quit()

    def create_text_bubble(self, lines, location, seconds, direction):
        self.data.clear()
        self.data.append(lines)
        self.data.append(location)
        self.data.append(seconds)
        self.mode = direction
        if self.bubble_timer.get_time() <= seconds:
            self.text_bubble()
        else:
            self.bubble = False
            self.wrong = False
            self.active = True
            if self.found:
                self.current_game = "Loading"
                self.load_screen.reset()
            self.found = False

    def text_bubble(self):
        self.bubble = True
        self.lines = self.data[0]
        self.location = self.data[1]
        self.text = []
        self.text_locations = []
        for item in self.lines:
            self.text.append(self.font1.render(item, False, (0, 0, 0), (255, 255, 255)))
        self.max_width = 0
        for item in self.lines:
            if self.font1.size(item)[0] > self.max_width:
                self.max_width = self.font1.size(item)[0]
        for line in range(0, len(self.text)):
            self.text_locations.append((self.location[0] + 10, self.location[1] + line * 18))
        if self.gameRun:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             [self.location[0], self.location[1], self.max_width + 20, len(self.text) * 18], 0)
            pygame.draw.rect(self.screen, (255, 255, 255),
                             [self.location[0] + 10, self.location[1] - 10, self.max_width, len(self.text) * 18 + 20],
                             0)
            pygame.draw.circle(self.screen, (255, 255, 255), [self.location[0] + 10, self.location[1]], 10, 0)
            pygame.draw.circle(self.screen, (255, 255, 255), [self.location[0] + self.max_width + 10, self.location[1]],
                               10, 0)
            pygame.draw.circle(self.screen, (255, 255, 255),
                               [self.location[0] + 10, self.location[1] + len(self.text) * 18], 10, 0)
            pygame.draw.circle(self.screen, (255, 255, 255),
                               [self.location[0] + self.max_width + 10, self.location[1] + len(self.text) * 18], 10, 0)
            if self.mode == "top_left":
                pygame.draw.polygon(self.screen, (255, 255, 255), [(self.location[0] + 10, self.location[1]),
                                                                   (self.location[0] + 30, self.location[1]),
                                                                   (self.location[0] + 15, self.location[1] - 20)], 0)
            elif self.mode == "top_right":
                pygame.draw.polygon(self.screen, (255, 255, 255),
                                    [(self.location[0] + self.max_width - 10, self.location[1]),
                                     (self.location[0] + self.max_width - 30, self.location[1]),
                                     (self.location[0] + self.max_width - 15, self.location[1] - 20)], 0)
            elif self.mode == "bottom_left":
                pygame.draw.polygon(self.screen, (255, 255, 255),
                                    [(self.location[0] + 10, self.location[1] + len(self.text) * 18),
                                     (self.location[0] + 40, self.location[1] + len(self.text) * 18),
                                     (self.location[0] + 30, self.location[1] + len(self.text) * 18 + 20)], 0)
            elif self.mode == "bottom_right":
                pygame.draw.polygon(self.screen, (255, 255, 255),
                                    [(self.location[0] + self.max_width - 10, self.location[1] + len(self.text) * 18),
                                     (self.location[0] + self.max_width - 30, self.location[1] + len(self.text) * 18),
                                     (self.location[0] + self.max_width - 20,
                                      self.location[1] + len(self.text) * 18 + 20)], 0)
            for line in range(0, len(self.text)):
                self.screen.blit(self.text[line], self.text_locations[line])


if __name__ == "__main__":
    Main()
