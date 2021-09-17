import pygame
import sys
import random
from numpy import sqrt
from typing import List, Tuple


# NODE CLASS
class Node(object):

    def __init__(self, surface: pygame.Surface, width: int, height: int) -> None:
        """Node attributes"""
        self.color: Tuple = (0, 0, 255)

        self.width: int = width

        self.height: int = height

        self.surface: pygame.Surface = surface

        self.radius: int = random.randint(4, 8)

        self.pos: List = [random.randint(self.radius, self.width - self.radius),
                          random.randint(self.radius, self.height - self.radius)]

        self.vel: List = [random.randint(1, 7),
                          random.randint(1, 7)]

    def create(self) -> pygame.Rect:
        """Draw pygame circle on screen"""
        return pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

    def move(self) -> None:
        """Start movement randomly"""
        if self.pos[0] > (self.width - self.radius) or self.pos[0] < self.radius:

            self.vel[0] = -self.vel[0]

        if self.pos[1] > (self.height - self.radius) or self.pos[1] < self.radius:

            self.vel[1] = -self.vel[1]

        self.pos[0] += self.vel[0]

        self.pos[1] += self.vel[1]

    def link(self, allnodes: List, threshold: int) -> None:
        """Link nodes using euclidean distance"""
        for node in allnodes:

            distance: float = sqrt((self.pos[0] - node.pos[0]) ** 2 + (self.pos[1] - node.pos[1]) ** 2)

            if distance < threshold:

                pygame.draw.line(self.surface, self.color, (self.pos[0], self.pos[1]), (node.pos[0], node.pos[1]), 1)


def generate(surface: pygame.Surface, nsamples: int, winsize: Tuple) -> List:
    """Generate a node list"""
    nodeset: List = []

    for _ in range(nsamples):

        nodeset.append(Node(surface, winsize[0], winsize[1]))

    return nodeset


# PARAMS
BACKGROUND: Tuple = (0, 0, 0)

WINSIZE: Tuple = (800, 600)

FRAMES: int = 60

NNODES: int = 50  # NUMBER OF NODES TO GENERATE

THRESH: int = 150  # LINK RADIUS

# PYGAME PARAMS
pygame.init()

pygame.display.set_caption('Linked nodes animation')

screen: pygame.Surface = pygame.display.set_mode((WINSIZE[0], WINSIZE[1]))

clock: pygame.time.Clock = pygame.time.Clock()

# CREATE A NODES LIST
nodes: List = generate(screen, NNODES, WINSIZE)


def run():

    while True:

        screen.fill(BACKGROUND)

        # READ KEYBOARD INPUT
        keys = pygame.key.get_pressed()

        # DRAW NODES AND LINK
        for node in nodes:

            node.create()

            node.link(nodes, THRESH)

            # PRESS SPACE KEY TO START MOVEMENT
            if keys[pygame.K_SPACE]:
                node.move()

        # GET PYGAME EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # CLOSE WINDOW
                sys.exit()

        # UPDATE SCREEN

        pygame.display.update()

        # UPDATE SPEED
        clock.tick(FRAMES)


# RUN PROGRAM
if __name__ == "__main__":

    run()
