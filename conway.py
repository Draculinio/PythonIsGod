import random
import time
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption('Conway Game of Life, Python is your GOD')
class World(pygame.sprite.Sprite):
    def __init__(self, size):
        self.size = size
        self.board = [[0] * self.size for _ in range(self.size)]
        self.live = 0
        self.dead = 0
        self.generation = 0
        self.record = 0
        self.less_record =size**2
        self.less_record_gen = 0
        self.record_generation = 0
        self.r = 10 if self.size<36 else 5
        self.init_board()
        self.main_loop()

    def count_population(self):
        self.live = self.dead = 0
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.board[i][j] == 0:
                    self.dead +=1
                else:
                    self.live +=1
        if self.live > self.record:
            self.record = self.live
            self.record_generation = self.generation
        if self.live < self.less_record:
            self.less_record = self.live
            self.less_record_gen = self.generation

    def init_board(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                self.board[i][j] = random.randint(0,1)
        self.count_population()

    def print_graphical_world(self):
        screen.fill((0, 0, 0))
        for i in range(0,self.size):
            for j in range(0,self.size):
                color = (255,0,0) if self.board[i][j] == 0 else (0,255,0)
                pygame.draw.circle(screen, color, ((i+1)*(self.r*2),(j+1)*(self.r*2)), self.r)
        font = pygame.font.Font(None,24)
        text = font.render('Generation: '+str(self.generation), True, (0,0,255))
        text_l = font.render('Live: '+str(self.live), True, (0,255,0))
        text_d = font.render('Dead: '+str(self.dead), True, (255,0,0))
        text_r = font.render('Live record: '+str(self.record), True, (120,85,32))
        text_r_g = font.render('Generation record: '+str(self.record_generation), True, (65,180,99))
        text_l_r = font.render('Less Live record: '+str(self.less_record), True, (255,20,20))
        text_l_r_g = font.render('Less Live Generation record: '+str(self.less_record_gen), True, (255,40,0))
        where = self.size*(self.r*2) + 170
        text_rect = text.get_rect(center=(where,100))
        text_rect_l = text_l.get_rect(center=(where,150))
        text_rect_d = text_d.get_rect(center=(where,200))
        text_rect_r = text_r.get_rect(center=(where,300))
        text_rect_r_g = text_r_g.get_rect(center=(where,350))
        text_rect_l_r = text_l_r.get_rect(center=(where,500))
        text_rect_l_r_g = text_l_r_g.get_rect(center=(where,550))
        screen.blit(text,text_rect)
        screen.blit(text_l,text_rect_l)
        screen.blit(text_d,text_rect_d)
        screen.blit(text_r,text_rect_r)
        screen.blit(text_r_g,text_rect_r_g)
        screen.blit(text_l_r,text_rect_l_r)
        screen.blit(text_l_r_g,text_rect_l_r_g)
        pygame.display.flip()

    def change_status(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                n = self.neighbours(i,j)
                if self.board[i][j] == 0:
                    if n==3:
                        self.board[i][j] = 1
                else:
                    if n>3 or n<2:
                        self.board[i][j] = 0
    
    def neighbours(self, i,j):
        n = 0
        if j-1>=0:
            if self.board[i][j-1] == 1:
                n+=1
        if j+1<self.size:
            if self.board[i][j+1] == 1:
                n+=1
        if i-1>=0:
            if self.board[i-1][j] == 1:
                n+=1
        if i+1<self.size:
            if self.board[i+1][j] == 1:
                n+=1
        if i+1<self.size and j+1<self.size:
            if self.board[i+1][j+1] == 1:
                n+=1
        if i+1<self.size and j-1>=0:
            if self.board[i+1][j-1] == 1:
                n+=1
        if i-1>=0 and j+1<self.size:
            if self.board[i-1][j+1] == 1:
                n+=1
        if i-1>=0 and j-1>=0:
            if self.board[i-1][j-1] == 1:
                n+=1
        return n
    
    def main_loop(self):
        clock.tick(30)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.print_graphical_world()
            self.change_status()
            self.count_population()
            self.generation+=1
            
            #time.sleep(0.1)

world = World(int(sys.argv[1]) if len(sys.argv)>1 else 30)