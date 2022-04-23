import pygame,sys,pymunk,time
from buttons import Button

class simulation():
    def __init__(self):
        pygame.init()
        self.space=pymunk.Space()
        self.xgravitylmao=0
        self.ygravitylmao=0
        
        self.clock = pygame.time.Clock()
        self.playing =True
        self.display_width,self.display_height = 1100,1000
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("simulation")
        pygame.mouse.set_visible(True)
        self.background = pygame.image.load("assets/background.png")
        pygame.mouse.set_visible(True)


        self.bodies=[]        
        self.obstacles=[]
        self.obstacles.append(self.static_obstacles(self.space,(500,500)))
        self.obstacles.append(self.static_obstacles(self.space,(91,393)))
        self.obstacles.append(self.static_obstacles(self.space,(672,778)))
        self.obstacles.append(self.static_obstacles(self.space,(737,342)))
        self.obstacles.append(self.static_obstacles(self.space,(961,557)))
        self.obstacles.append(self.static_obstacles(self.space,(730,560)))
        self.obstacles.append(self.static_obstacles(self.space,(374,768)))
        self.obstacles.append(self.static_obstacles(self.space,(174,600)))
        self.obstacles.append(self.static_obstacles(self.space,(95,808)))
        self.obstacles.append(self.static_obstacles(self.space,(298,961)))
        self.obstacles.append(self.static_obstacles(self.space,(941,896)))

        

    def screen_loop(self):
        while self.playing:
            self.space.gravity = (self.xgravitylmao,self.ygravitylmao)
            self.screen.blit(self.background,(0,0))
            self.check_events()
            #self.screen.fill((217,217,217))
            self.xincremnetbutton = Button(image = pygame.image.load("assets/xincrement.png"),pos=(1010,20))
            self.xincremnetbutton.update(self.screen)
            self.xdecrementbutton = Button(image = pygame.image.load("assets/xdecrement.png"),pos=(1010,75))
            self.xdecrementbutton.update(self.screen)
            self.yincrementbutton = Button(image = pygame.image.load("assets/yincrement.png"),pos=(1010,130))
            self.yincrementbutton.update(self.screen)
            self.ydecrementbutton = Button(image = pygame.image.load("assets/ydecrement.png"),pos=(1010,185))
            self.ydecrementbutton.update(self.screen)
            self.draw_body(self.bodies)
            self.draw_obstacles(self.obstacles)
            pygame.display.update()
            

            self.space.step(1/50)
            
            
            
    def check_events(self):
        self.clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running,self.playing = False,False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.xincremnetbutton.check_for_input(pygame.mouse.get_pos()):
                    self.xgravitylmao+=10
                    print("x gravity = ",self.space.gravity[0])
                if self.xdecrementbutton.check_for_input(pygame.mouse.get_pos()):
                    self.xgravitylmao-=10
                    print("x gravity = ",self.space.gravity[0])
                if self.yincrementbutton.check_for_input(pygame.mouse.get_pos()):
                    self.ygravitylmao+=10
                    print("y gravity = ",self.space.gravity[1])
                if self.ydecrementbutton.check_for_input(pygame.mouse.get_pos()):
                    self.ygravitylmao-=10
                    print("y gravity = ",self.space.gravity[1])
                #print(pygame.mouse.get_pos())
                self.bodies.append(self.create_body(self.space,event.pos))#pygame.mouse.get_pos()))

                
    def create_body(self,space,spawnposition):
        self.body = pymunk.Body(1,50,body_type=pymunk.Body.DYNAMIC)
        self.body.position = spawnposition
        self.shape = pymunk.Circle(self.body,20)
        space.add(self.body,self.shape)
        return  self.shape
    def static_obstacles(self,space,obstacleposition):
        self.static_platform=pymunk.Body(body_type=pymunk.Body.STATIC)
        self.static_platform.position=obstacleposition
        self.shape = pymunk.Circle(self.static_platform,50)
        space.add(self.static_platform,self.shape)
        return self.shape
    def draw_obstacles(self,obstacles):
        for self.obstacle in obstacles:
            self.pos_x=int(self.obstacle.body.position.x)
            self.pos_y=int(self.obstacle.body.position.y)
            pygame.draw.circle(self.screen,(255,87,51),(self.pos_x,self.pos_y),50)

    def draw_body(self,bodies):
        for self.boday in bodies:
            self.pos_x=int(self.boday.body.position.x)
            self.pos_y=int(self.boday.body.position.y)
            pygame.draw.circle(self.screen,(81,195,210),(self.pos_x,self.pos_y),20)




            
if __name__=="__main__":
    social_settings=simulation()
    social_settings.screen_loop()


