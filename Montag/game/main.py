import pygame
import sys
import random




class PingPong:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.BACKGROUND_COLOR = (0, 0, 0)
        self.BUTTON_COLOR = (255, 255, 255)
        self.TEXT_COLOR = (0,0,0)
        self.TEXT_COLOR_TITLE = (255,255,255)
        self.FONT_NAME = 'freesansbold.ttf'
        self.paddlewidth = 30
        self.paddleheight = 100
        self.ballwidth = 20
        self.ballheight = self.ballwidth
        self.hit_sound = pygame.mixer.Sound("Montag\game\hitsound.mp3")

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("PingPong")
        self.button_heigth = 100
        self.button_width = 300
        self.training_button = pygame.Rect(self.SCREEN_WIDTH // 2 - (self.button_width // 2), (self.SCREEN_HEIGHT // 2) + (-110), self.button_width, self.button_heigth)
        self.p2_button = pygame.Rect((self.SCREEN_WIDTH // 2 - (self.button_width // 2)), (self.SCREEN_HEIGHT // 2) + (0), self.button_width, self.button_heigth)
        self.fun_button = pygame.Rect((self.SCREEN_WIDTH // 2 - (self.button_width // 2)), (self.SCREEN_HEIGHT // 2) + (+110), self.button_width, self.button_heigth)


    def training_game(self):
        #Paddle
        paddle_speed = 5
        paddle_react=pygame.Rect(0,self.SCREEN_HEIGHT//2 - (self.paddleheight//2),self.paddlewidth,self.paddleheight)
        #Ball
        counter = 0
        ball_speed = 2
        ball_dx = -ball_speed
        ball_dy = random.choice([-ball_speed,ball_speed])
        ball_accel = 1
        ball_react = pygame.Rect(self.SCREEN_WIDTH // 2 - (self.ballwidth//2),self.SCREEN_HEIGHT // 2 - (self.ballheight//2),self.ballwidth,self.ballheight)
        #Fenster
        window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        running = True
        #Spiel
        while running:
            window.fill(self.BACKGROUND_COLOR)
            #Event Checking
            
            for event in pygame.event.get():
                #verlassen
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            #paddle bewegung
            presse_keys = pygame.key.get_pressed()
            if presse_keys[pygame.K_w] and paddle_react.top > 0:
                paddle_react.y -= paddle_speed
            if presse_keys[pygame.K_s] and paddle_react.bottom < self.SCREEN_HEIGHT:
                paddle_react.y += paddle_speed

            #ball bewegung
            ball_react.x += ball_dx
            ball_react.y += ball_dy
            #ball colider
            if ball_react.colliderect(paddle_react) or ball_react.right >= self.SCREEN_WIDTH:
                if ball_react.colliderect(paddle_react):
                    self.hit_sound.play()
                ball_dx = -ball_dx
                #schneller werden
                counter += 1
                #alle 3 pannel berürungung wird es schneller
                if counter % 6 == 0:
                    ball_dx -= ball_accel
                    if ball_dx > 0:
                        ball_dx += ball_accel
                    else:
                        ball_dy-=ball_accel
            if ball_react.top <= 0 or ball_react.bottom >= self.SCREEN_HEIGHT:
                ball_dy = -ball_dy
            #wenn ball auserhalb
            if ball_react.x  <= 0:
                print("Verloren")
                return None

            pygame.draw.rect(window, self.BUTTON_COLOR, paddle_react)
            pygame.draw.rect(window, self.BUTTON_COLOR, ball_react)
            pygame.display.flip()
            pygame.time.Clock().tick(100)

    def start_train(self):
        print("Starting Train...")
        self.training_game()

    def p2_game(self):
        #Paddle
        paddle_speed = 5
        paddle_react_p1=pygame.Rect(0,self.SCREEN_HEIGHT//2 - (self.paddleheight//2),self.paddlewidth,self.paddleheight)
        paddle_react_p2=pygame.Rect(self.SCREEN_WIDTH - self.paddlewidth,self.SCREEN_HEIGHT//2 - (self.paddleheight//2),self.paddlewidth,self.paddleheight)
        #Ball
        counter = 0
        ball_speed = 2
        ball_dx = -ball_speed
        ball_dy = random.choice([-ball_speed,ball_speed])
        ball_accel = 1
        ball_react = pygame.Rect(self.SCREEN_WIDTH // 2 - (self.ballwidth//2),self.SCREEN_HEIGHT // 2 - (self.ballheight//2),self.ballwidth,self.ballheight)
        #Fenster
        window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        running = True
        #Spiel
        while running:
            window.fill(self.BACKGROUND_COLOR)
            #Event Checking
            
            for event in pygame.event.get():
                #verlassen
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            #paddle bewegung P1
            presse_keys = pygame.key.get_pressed()
            #nach oben
            if presse_keys[pygame.K_w] and paddle_react_p1.top > 0:
                paddle_react_p1.y -= paddle_speed
            #nach unten
            if presse_keys[pygame.K_s] and paddle_react_p1.bottom < self.SCREEN_HEIGHT:
                paddle_react_p1.y += paddle_speed
            #paddle bewegung P2
            if presse_keys[pygame.K_UP] and paddle_react_p2.top > 0:
                paddle_react_p2.y -= paddle_speed
            if presse_keys[pygame.K_DOWN] and paddle_react_p2.bottom < self.SCREEN_HEIGHT:
                paddle_react_p2.y += paddle_speed

            #ball bewegung
            ball_react.x += ball_dx
            ball_react.y += ball_dy
            #ball colider
            if ball_react.colliderect(paddle_react_p1) or ball_react.colliderect(paddle_react_p2):
                self.hit_sound.play()
                ball_dx = -ball_dx
                #schneller werden
                counter += 1
                #alle 3 pannel berürungung wird es schneller
                if counter % 6 == 0:
                    ball_dx -= ball_accel
                    if ball_dx > 0:
                        ball_dx += ball_accel
                    else:
                        ball_dy-=ball_accel
            if ball_react.top <= 0 or ball_react.bottom >= self.SCREEN_HEIGHT:
                ball_dy = -ball_dy
            #wenn ball auserhalb
            if ball_react.x  <= 0 or ball_react.x >= self.SCREEN_WIDTH:
                print("Verloren")
                return None

            pygame.draw.rect(window, self.BUTTON_COLOR, paddle_react_p1)
            pygame.draw.rect(window, self.BUTTON_COLOR, paddle_react_p2)
            pygame.draw.rect(window, self.BUTTON_COLOR, ball_react)
            pygame.display.flip()
            pygame.time.Clock().tick(100)
    def start_p2(self):
        print("Starting 1v1...")
        self.p2_game()
    
    def generateRandomColorFUN(self):
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


    def randomVariationFUN(self):
        # random value between 0.9 and 1.1
        return random.randint(3, 6)
    
    def fun_game(self):
        width = self.SCREEN_WIDTH
        height = self.SCREEN_HEIGHT

        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        running = True

        RGBMODE = True
        print(f"RGBMODE is set to {RGBMODE}!")
        p1w = self.paddlewidth
        p1h = self.paddleheight
        p1x = 0
        p1y = (height/2)-(p1h/2)

        bw = self.ballwidth

        balls = [
            {
                "x": (width/2)-(bw/2),
                "y": (height/2)-(bw/2),
                "vx": -5,
                "vy": 0,
                "color": self.generateRandomColorFUN()
            }
        ]

        hits = 0
        mSpeed = 5
        mSpeedHits = 0

        color = (255, 255, 255)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("black")

            if hits >= 2:
                balls.append({
                    "x": (width/2)-(20/2),
                    "y": (height/2)-(20/2),
                    "vx": -5,
                    "vy": 0,
                    "color": self.generateRandomColorFUN()
                })
                hits = 0
                print("1 ball added")
                if (p1h < height):
                    mSpeed += 0.1
                    print(f"Movement speed increased to {mSpeed}")
                    p1h += 5
                    print(f"Player height increased to {p1h}")

            for ball in balls:
                ball["x"] += ball["vx"]
                ball["y"] += ball["vy"]

                print(f"Position {ball['x']}, {ball['y']}")

                if ball["y"] <= 0 or ball["y"] >= height-bw:
                    ball["vy"] = -ball["vy"]

                if ball["x"] > width-bw:
                    ball["vx"] = -ball["vx"]

                if ball["x"] <= p1x+p1w and ball["y"] in list(range(int(p1y), int(p1y+p1h))):
                    self.hit_sound.play()
                    ball["vx"] = -ball["vx"]
                    if ball["y"] < p1y + (p1h/2):
                        ball["vy"] = -self.randomVariationFUN()
                        hits += 1
                    elif ball["y"] > p1y + (p1h/2):
                        ball["vy"] = self.randomVariationFUN()
                        hits += 1
                    else:
                        ball["vy"] = 0

                    if RGBMODE:
                        ball["color"] = self.generateRandomColorFUN()
                        color = self.generateRandomColorFUN()

                if ball["x"] <= (0):  # (p1w-5)
                    # remove ball and another one as punishment
                    balls.remove(ball)
                    if len(balls) > 0:
                        balls.pop(0)
                        print("2 balls removed")
                    if len(balls) == 0:
                        running = False
                        print("You lost")

                pygame.draw.rect(screen, ball["color"], pygame.Rect(
                    ball["x"], ball["y"], bw, bw))

            pygame.draw.rect(screen, color, pygame.Rect(p1x, p1y, p1w, p1h))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                if p1y > 0:
                    p1y -= mSpeed
            if keys[pygame.K_s]:
                if (p1y+p1h) < height:
                    p1y += mSpeed

            pygame.display.flip()

            clock.tick(100)

        # (p1y >= ball["y"] >= (p1y + p1h) |||  ball["y"] in list(range(p1y,p1y+p1h))
    def start_fun(self):
        print("Starting Fun...")
        self.fun_game()

    def draw_button(self, button_rect, text):
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, button_rect)
        font = pygame.font.Font(self.FONT_NAME, 32)
        text_surface = font.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
    
    def draw_title(self, text, size, y_pos):
        font = pygame.font.Font(self.FONT_NAME, size)
        text_surface = font.render(text, True, self.TEXT_COLOR_TITLE)
        text_rect = text_surface.get_rect(center=(self.SCREEN_WIDTH // 2, y_pos))
        self.screen.blit(text_surface, text_rect)

    def main(self):
        running = True
        #sap logo
        sap_logos = [SAP_Logo(self.SCREEN_WIDTH,self.SCREEN_HEIGHT, self.screen)]
        while running:
            self.screen.fill(self.BACKGROUND_COLOR)
            #sap logo
            for logo in sap_logos:
                logo.update_and_draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Linksklick
                        if self.training_button.collidepoint(event.pos):
                            self.start_train()
                            sap_logos.append(SAP_Logo(self.SCREEN_WIDTH,self.SCREEN_HEIGHT, self.screen))
                        if self.p2_button.collidepoint(event.pos):
                            self.start_p2()
                            sap_logos.append(SAP_Logo(self.SCREEN_WIDTH,self.SCREEN_HEIGHT, self.screen))
                        if self.fun_button.collidepoint(event.pos):
                            self.start_fun()
                            sap_logos.append(SAP_Logo(self.SCREEN_WIDTH,self.SCREEN_HEIGHT, self.screen))
            self.draw_title("Ping Pong @SAP",50,100)
            self.draw_button(self.training_button, "Trainings Modus")
            self.draw_button(self.p2_button, "1v1 Modus")
            self.draw_button(self.fun_button, "Spaß Modus")
            pygame.display.flip()
            pygame.time.Clock().tick(60)

class SAP_Logo:
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,screen) -> None:
        self.sap_logo = pygame.image.load("Montag\game\sap-logo.png")
        self.sap_logo = pygame.transform.scale(self.sap_logo,(120,40))
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.screen = screen
        self.image_x = SCREEN_WIDTH // 2
        self.image_y = SCREEN_HEIGHT // 2
        self.image_dx = 3
        self.image_dy = 3
        self.image_react = self.sap_logo.get_rect()

    def update_and_draw(self):
        self.image_x += self.image_dx
        self.image_y += self.image_dy
        if self.image_react.left + self.image_x <= 0 or self.image_react.right + self.image_x >= self.SCREEN_WIDTH:
            self.image_dx = -self.image_dx
        if self.image_react.top + self.image_y <= 0 or self.image_react.bottom + self.image_y >= self.SCREEN_HEIGHT:
            self.image_dy = -self.image_dy
        self.screen.blit(self.sap_logo,(self.image_x,self.image_y))


if __name__ == "__main__":
    gamemenu = PingPong()
    gamemenu.main()