# A demo of networking inside of pygame
import pygame
import socket

HOST = '127.0.0.1' # Server hostname
PORT = 1234 # Server port

size = (500,500)
title = 'Networking demo'

BLACK = (0,0,0)
WHITE = (255,255,255)

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self,screen):
        rect = pygame.Rect(self.x, self.y, 20, 100)
        pygame.draw.rect(screen, BLACK, rect) 
   
def sendUpdate(socket,command):
    # Update the box position on the server side
    print("sending update")
    data = {'direction': command}
    socket.sendall(data)

def drawElements(data, player, screen): 
    # Fetch elements from the server and draw them
    print("making stuff")
    x,y = data['player'] 
    player.x = x
    player.y = y
    player.draw(screen)
    print("Done making stuff")




def main():
    # Connect to the server
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    
    clock = pygame.time.Clock()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Running')
    
        screen.fill(WHITE)
        pygame.display.flip()
        clock.tick(5)
        player = Player(100,100)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(5)
    
        while True:
            events = pygame.event.get()
            for event in events:
                print(event.type)
                if event.type == pygame.KEYDOWN:
                    print('pressed')
                    sendUpdate(socket, 'DOWN')
            data = s.recv(1024)
            if data:
                drawElements(data, player, screen)
            pygame.display.flip()
            clock.tick(5)
    
if __name__ == '__main__':
    main()
