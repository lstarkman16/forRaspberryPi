deadCounter = 0

def main():

    import pygame
    import random

    pygame.init() 

    #how big is this going to be
    pageHeight = 485
    pageWidth = 700
    size = [pageWidth, pageHeight] 
    screen = pygame.display.set_mode(size) 

    pygame.display.set_caption("Raise Him From Perdition")

    #define colors
    black = [0, 0, 0]
    white = [255, 255, 255]
    bgred = [150, 0, 0]
    platformred = [200, 0, 0]

    #pygame.movie.Movie.play('preview.mpg')
    #pygame.movie.Movie.stop('preview.mpg')
    
    #how many times have you died
    #deadCounter = 0
    #deadCounter = deadCounter + 1
    #deadNumber = font.render(deadCounter, 1, (255, 255, 255))
    #screen.blit(deadNumber, (20, 450))
    
    #fire thingys
    flame = pygame.image.load("fire.png")
    class Fire(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([700, 80])
            transparent = flame.get_at((0, 0))
            flame.set_colorkey(transparent)
            transparent2 = self.image.get_at((0, 0))
            self.image.set_colorkey(transparent2)

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            
    #luicfer thingys
    luciferSprite = pygame.image.load("lucifersmall.png").convert()
    class Lucifer(pygame.sprite.Sprite):
        #ATTRIBUTES
        #speedish movementy things
        change_x = 0
        change_y = 0

        jump_ready = False  #not trying to jump

        frame_since_collision = 0   #frames since hit something after jumping
        frame_since_jump = 0    #can't jump from midair

        #METHODS
        #make a thing that exists 
        def __init__(self, x, y): 
            #make the sprite a thing 
            pygame.sprite.Sprite.__init__(self) 

            #set size and color 
            self.image = pygame.Surface([10, 39])
            color = luciferSprite.get_at((0, 0))
            luciferSprite.set_colorkey(color)
            color2 = luciferSprite.get_at((3, 0))

            luciferSprite.set_colorkey(color2)
            colorsquare = self.image.get_at((0, 0))
            self.image.set_colorkey(colorsquare)
            
            #upper left corner is traced 
            self.rect = self.image.get_rect() 
            self.rect.x = x
            self.rect.y = y

        #change player speed 
        def changespeed_x(self, x):
            self.change_x = x
            
        def changespeed_y(self, y):
            self.change_y = y
               
        #find new player location
        def update(self, blocks): 

            def move():         
                #save old x, update
                old_x = self.rect.x
                new_x = old_x + HoriMove
                self.rect.x = new_x

                #save old y, update
                old_y = self.rect.y 
                new_y = old_y + VertMove
                self.rect.y = new_y

            collide = pygame.sprite.spritecollide(self, blocks, False)
            block_hit_list = pygame.sprite.spritecollide(self, blocks, False) 

            #chasing
            #READER - if you want to make it harder, lower the number that these are divided by
            if pygame.sprite.collide_rect(lucifer, player) == False:
                if player.rect.x > lucifer.rect.x:
                    HoriWhichWay = [-10, 10, (player.rect.x-lucifer.rect.x)/8]#this one
                    HoriMove = random.choice(HoriWhichWay)
                    VertWhichWay = [-10, 10, (player.rect.y-lucifer.rect.y)/8]
                    VertMove = random.choice(VertWhichWay)
                else:
                    HoriWhichWay = [-10, 10, (lucifer.rect.x-player.rect.x)/8]
                    HoriMove = random.choice(HoriWhichWay)
                    VertWhichWay = [-10, 10, (lucifer.rect.y-player.rect.y)/8]
                    VertMove = random.choice(VertWhichWay)
                move()
                screen.blit(luciferSprite, lucifer.rect)
                
            elif pygame.sprite.collide_rect(lucifer, player) == True:
                HoriWhichWay = [0, 0]
                VertWhichWay = [0, 0]

    #dean thingys
    deanSprite = pygame.image.load("deansmall.png").convert()
    class Dean(pygame.sprite.Sprite):
        #ATTRIBUTES
        #speedish movementy things
        change_x = 0
        change_y = 0

        jump_ready = False  #not trying to jump

        frame_since_collision = 0   #frames since hit something after jumping
        frame_since_jump = 0    #can't jump from midair

        #METHODS
        #make a thing that exists 
        def __init__(self, x, y): 
            #make the sprite a thing 
            pygame.sprite.Sprite.__init__(self) 

            #set size and color 
            self.image = pygame.Surface([10, 39])
            
            color = deanSprite.get_at((0, 0))
            deanSprite.set_colorkey(color)

            color2 = deanSprite.get_at((5, 38))
            deanSprite.set_colorkey(color2)
            
            colorsquare = self.image.get_at((0, 0))
            self.image.set_colorkey(colorsquare)
            
            #upper left corner is traced 
            self.rect = self.image.get_rect() 
            self.rect.x = x
            self.rect.y = y

        #change player speed 
        def changespeed_x(self, x):
            self.change_x = x
            
        def changespeed_y(self, y):
            self.change_y = y
               
        #find new player location
        def update(self, blocks): 

            def move():         
                #save old x, update
                old_x = self.rect.x
                new_x = old_x + HoriMove
                self.rect.x = new_x

                #save old y, update
                old_y = self.rect.y 
                new_y = old_y + VertMove
                self.rect.y = new_y

            collide = pygame.sprite.spritecollide(self, blocks, False)
            block_hit_list = pygame.sprite.spritecollide(self, blocks, False) 

            #chasing
            #READER - if you want to make it harder, lower the number that these are divided by
            if pygame.sprite.collide_rect(dean, player) == False:
                if player.rect.x > dean.rect.x:
                    HoriWhichWay = [-10, 10, ((player.rect.x-dean.rect.x)/15)]#this one
                    HoriMove = random.choice(HoriWhichWay)
                    VertWhichWay = [-10, 10, ((player.rect.y-dean.rect.y)/15)]
                    VertMove = random.choice(VertWhichWay)
                else:
                    HoriWhichWay = [-10, 10, (dean.rect.x-player.rect.x)/15]
                    HoriMove = random.choice(HoriWhichWay)
                    VertWhichWay = [-10, 10, (dean.rect.y-player.rect.y)/15]
                    VertMove = random.choice(VertWhichWay)
                move()
                screen.blit(deanSprite, dean.rect)
                
            elif pygame.sprite.collide_rect(dean, player) == True:
                HoriWhichWay = [0, 0]
                VertWhichWay = [0, 0]
                lucifer.HoriWhichWay = [0, 0]
                lucifer.VertWhichWay = [0, 0]
                
    #main character / player
    castiel = pygame.image.load("cassmall.png").convert()
    class Player(pygame.sprite.Sprite):
        #ATTRIBUTES
        #speedish movementy things
        change_x = 0
        change_y = 0

        jump_ready = False  #not trying to jump

        frame_since_collision = 0   #frames since hit something after jumping
        frame_since_jump = 0    #can't jump from midair

        #METHODS
        #make a thing that exists 
        def __init__(self, x, y): 
            #make the sprite a thing 
            pygame.sprite.Sprite.__init__(self) 

            #set size and color 
            self.image = pygame.Surface([16, 40])
            color = castiel.get_at((0, 0))
            castiel.set_colorkey(color)
            colorsquare = self.image.get_at((0, 0))
            self.image.set_colorkey(colorsquare)
            
            #upper left corner is traced 
            self.rect = self.image.get_rect() 
            self.rect.x = x
            self.rect.y = y

        #change player speed 
        def changespeed_x(self, x):
            self.change_x = x

        def changespeed_y(self, y):
            self.change_y = y
               
        #find new player location
        def update(self, blocks): 
     
            #save old x, update, collision?
            old_x = self.rect.x
            new_x = old_x + self.change_x
            self.rect.x = new_x
     
            collide = pygame.sprite.spritecollide(self, blocks, False)
            if collide:
                #go back to the old location
                self.rect.x = old_x
     
            #save old y, update, collision?
            old_y = self.rect.y 
            new_y = old_y + self.change_y 
            self.rect.y = new_y
             
            block_hit_list = pygame.sprite.spritecollide(self, blocks, False) 
     
            for block in block_hit_list:
                #after collision, set the old location.
                self.rect.y = old_y
                self.rect.x = old_x

                #stop y movement
                self.change_y = 0

                #reset number of frames since collision
                self.frame_since_collision = 0
     
            #told to jump, was on solid ground, so jump
            if self.frame_since_collision < 6 and self.frame_since_jump < 6:
                self.frame_since_jump = 100
                self.change_y -= 9.2

            #count things
            self.frame_since_collision += 1
            self.frame_since_jump += 1

        #gravity is a thing that does stuff
        def calc_grav(self):
            self.change_y += .35
     
            #but only if you are on the ground
            if self.rect.y >= 485 and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = 485
                self.frame_since_collision = 0
     
        #you want to jump, so jumping is a thing you can do
        def jump(self, blocks):
            self.jump_ready = True
            self.frame_since_jump = 0

    #platform thingys
    class Platform(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            pygame.sprite.Sprite.__init__(self) #make it a thing that exists
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.rect = self.image.get_rect()

            
    def create_level1(block_list, all_sprites_list):
     
        for x in range(-240, 1000, 240):    #location of platforms
            block = Platform(platformred, 115, 20)  #size
            block.rect.x = x
            block.rect.y = 395  #y coordinate

            #they're on the list now
            block_list.add(block)
            all_sprites_list.add(block)

        for x in range(-360, 1000, 240):
            block = Platform(platformred, 115, 20)
            block.rect.x = x
            block.rect.y = 290

            block_list.add(block)
            all_sprites_list.add(block)

        for x in range(-240, 1000, 240):
            block = Platform(platformred, 115, 20)
            block.rect.x = x
            block.rect.y = 185

            block_list.add(block)
            all_sprites_list.add(block)

        for x in range(-360, 1000, 240):
            block = Platform(platformred, 115, 20)
            block.rect.x = x
            block.rect.y = 80

            block_list.add(block)
            all_sprites_list.add(block)

    #blocks are being made
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()

    create_level1(block_list, all_sprites_list)

    #player stuff
    player = Player(100, 100)
    player.rect.x = 290
    player.rect.y = 360
    all_sprites_list.add(player)

    #lucifer stuff
    lucifer = Lucifer(100, 100)
    lucifer.rect.x = 530
    lucifer.rect.y = 350
    all_sprites_list.add(lucifer)

    #dean stuff
    dean = Dean(100, 100)
    dean.rect.x = 530
    dean.rect.y = 350
    all_sprites_list.add(dean)
    
    #fire stuff
    fire = Fire(100, 100)
    fire.rect.x = 0
    fire.rect.y = 420
    all_sprites_list.add(fire)

    #musiqua
    pygame.mixer.music.load("comws.ogg")
    pygame.mixer.music.play(loops = 10, start=0.0)

    #instructions
    howTo = 'Arrows to move, avoid Lucifer, catch Dean, R to restart.'
    def texts():
        font = pygame.font.Font(None, 30)
        instructions = font.render(howTo, 1, (255, 255, 255))
        screen.blit(instructions, (65, 10))

    #did you die yet
    deadMessage = 'GAME OVER'
    def dead():
        font = pygame.font.Font(None, 60)
        deadWords = font.render(deadMessage, 1, (255, 255, 255))
        screen.blit(deadWords, (230, 230))

    #did cas save dean yet
    winMessage = 'YOU RAISED HIM FROM PERDITION!'
    def win():
        font = pygame.font.Font(None, 50)
        winWords = font.render(winMessage, 1, (255, 255, 255))
        screen.blit(winWords, (45, 230))

    def cassaveddean():
        if pygame.sprite.collide_rect(player, dean) == True:
            win()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  #you want to go left
                  player.changespeed_x(0)    #so go left
                if event.key == pygame.K_RIGHT: #and repeat
                   player.changespeed_x(0)
                if event.key == pygame.K_UP:
                    player.changespeed_y(0)
                if event.key == pygame.K_DOWN:
                    player.changespeed_y(0)
        
    def luciferkilledyou():
        if pygame.sprite.collide_rect(player, lucifer) == True:
            dead()
            pygame.mixer.music.play(loops = 0, start=0.0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  #you want to go left
                  player.changespeed_x(0)    #so go left
                if event.key == pygame.K_RIGHT: #and repeat
                   player.changespeed_x(0)
                if event.key == pygame.K_UP:
                    player.changespeed_y(0)
                if event.key == pygame.K_DOWN:
                    player.changespeed_y(0)
            
    def firekilledyou():
        if pygame.sprite.collide_rect(player, fire) == True:
            font = pygame.font.Font(None, 60)
            deadWords = font.render(deadMessage, 1, (255, 255, 255))
            screen.blit(deadWords, (230, 230))
            pygame.mixer.music.play(loops = 0, start=0.0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  #you will never move again
                    player.changespeed_x(0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed_x(0)
                if event.key == pygame.K_UP:
                    player.changespeed_y(0)
                if event.key == pygame.K_DOWN:
                    player.changespeed_y(0)
                
    #you shall never end
    done=False

    #this is the main thing make sure this works that would be good
    while done == False:
        for event in pygame.event.get(): #you did something good for you. 
            if event.type == pygame.QUIT: #why must you leave me 
                done = True #apparently you shall end
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  #you want to go left
                    player.changespeed_x(-5)    #so go left
                if event.key == pygame.K_RIGHT: #and repeat
                    player.changespeed_x(5)
                if event.key == pygame.K_UP:
                    player.jump(block_list)
                if event.key == pygame.K_DOWN:
                    player.changespeed_y(5)
                if event.key == pygame.K_r:
                    main()

            if event.type == pygame.KEYUP:  #never let go
                if event.key == pygame.K_LEFT:
                    player.changespeed_x(-0)    #but if you do then you stop
                if event.key == pygame.K_RIGHT:
                    player.changespeed_x(0)

            firekilledyou()
            luciferkilledyou()
            
        #hyperspace is good for you
        if player.rect.x >= 700:
            player.rect.x = 1
        if player.rect.x <= 0:
            player.rect.x = 698
        if lucifer.rect.x >= 700:
            lucifer.rect.x = 1
        if lucifer.rect.x <= 0:
            lucifer.rect.x = 698
        if lucifer.rect.y >= 500:
            lucifer.rect.y = 1
        if lucifer.rect.y <= 0:
            lucifer.rect.y = 498

        if dean.rect.x >= 700:
            dean.rect.x = 1
        if dean.rect.x <= 0:
            dean.rect.x = 698
        if dean.rect.y >= 500:
            dean.rect.y = 1
        if dean.rect.y <= 0:
            dean.rect.y = 498
            
        player.calc_grav()
        player.update(block_list)
        lucifer.update(block_list)
        dean.update(block_list)
        block_list.update()

        #bg 
        screen.fill(bgred)

        #fire
        screen.blit(flame, fire.rect)

        #lucifer
        screen.blit(luciferSprite, lucifer.rect)

        #dean
        screen.blit(deanSprite, dean.rect)
        
        #cas
        screen.blit(castiel, player.rect)

        #show instructions
        texts()
        
        #murder
        luciferkilledyou()
        firekilledyou()
        cassaveddean()

        #timer
        pygame.time.Clock().tick()

        #everyone can see what you did there 
        all_sprites_list.draw(screen)

        #don't explode please 
        pygame.time.Clock().tick(50)


        #show the world that you've moved 6 pixels you should be proud 
        pygame.display.flip() 

    #don't make IDLE idle
    pygame.quit()


main()
