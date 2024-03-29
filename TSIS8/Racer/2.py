import pygame as pg
   
pg.init()        
 
class Laser:
    def __init__(self, loc, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.Surface((5,40)).convert()
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect(center=loc)
        self.speed = 5
   
    def update(self):
        self.rect.y -= self.speed
   
    def render(self, surf):
        surf.blit(self.image, self.rect)
   
class Player:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.image.load('TSIS8\Racer\Без имени.png').convert()
        self.image.set_colorkey((255,0,255))
        self.transformed_image = pg.transform.rotate(self.image, 180)
        start_buffer = 300
        self.rect = self.image.get_rect(
            center=(screen_rect.centerx, screen_rect.centery + start_buffer)
        )
        self.dx = 300
        self.dy = 300
        self.lasers = []
        self.timer = 0.0
        self.laser_delay = 500
        self.add_laser = False
   
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if self.add_laser:
                    self.lasers.append(Laser(self.rect.center, self.screen_rect))
                    self.add_laser = False
   
    def update(self, keys, dt):
        self.rect.clamp_ip(self.screen_rect)
        if keys[pg.K_LEFT]:
            self.rect.x -= self.dx * dt
        if keys[pg.K_RIGHT]:
            self.rect.x += self.dx * dt
        if keys[pg.K_UP]:
            self.rect.y -= self.dy * dt
        if keys[pg.K_DOWN]:
            self.rect.y += self.dy * dt
        for laser in self.lasers:
            laser.update()
        if pg.time.get_ticks()-self.timer > self.laser_delay:
            self.timer = pg.time.get_ticks()
            self.add_laser = True
   
    def draw(self, surf):
        for laser in self.lasers:
            laser.render(surf)
        surf.blit(self.transformed_image, self.rect)
   
screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
player = Player(screen_rect)

clock = pg.time.Clock()
done = False
while not done:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        player.get_event(event)
    screen.fill((0,0,0))
    delta_time = clock.tick(60)/1000.0
    player.update(keys, delta_time)
 
    player.draw(screen)
   
    pg.display.update()