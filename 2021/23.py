import pygame
import sys

# TODO: Add a check to see if an amphipod in the hallway can go straight to home
# TODO: Read the input from a file
# TODO: Clean up the code
# TODO: Autosolve the problem


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

HELP_TEXT = "Arrow keys to move, Tab to select, Escape to quit,"
HELP_TEXT_2 = "and 1 or 2 to select the part / reset."


class Color:
    BACKGROUND = (15, 15, 35)

    SPACE_FILL = (16, 16, 26)
    SPACE_OUTLINE = (51, 51, 64)

    TEXT_GREEN = (0, 153, 0)
    TEXT_WHITE = (204, 204, 204)
    TEXT_SILVER = (153, 153, 204)
    TEXT_GOLD = (255, 255, 102)
    TEXT_DIM = (102, 102, 102)


class Direction:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Amphipod:
    COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000 }

    def __init__(self, type):
        self.__type = type
        self.isHome = False
        self.isSelected = False

    def move(self) -> int:
        return self.COSTS[self.__type]

    @property
    def type(self):
        return self.__type


class Space:
    def __init__(self, position, occupant, type):
        self.__position = position
        self.__occupant = occupant
        self.__type = type

    @property
    def isOccupied(self):
        return self.__occupant != None

    def getOccupant(self):
        return self.__occupant

    def popOccupant(self):
        occupant = self.__occupant
        self.__occupant = None
        return occupant

    def setOccupant(self, occupant):
        self.__occupant = occupant

    def getPosition(self):
        return self.__position[:]

    @property
    def type(self):
        return self.__type


class Burrow:
    pods = {
        (2,1): Amphipod("B"),
        (4,1): Amphipod("C"),
        (6,1): Amphipod("B"),
        (8,1): Amphipod("D"),
        (2,2): Amphipod("A"),
        (4,2): Amphipod("D"),
        (6,2): Amphipod("C"),
        (8,2): Amphipod("A"),
    }
    pods2 = {
        (2,2): Amphipod("D"),
        (4,2): Amphipod("C"),
        (6,2): Amphipod("B"),
        (8,2): Amphipod("A"),
        (2,3): Amphipod("D"),
        (4,3): Amphipod("B"),
        (6,3): Amphipod("A"),
        (8,3): Amphipod("C"),
    }

    def __init__(self, part):
        self.__spaces = {
            (0,0): Space((0,0), None, "Free"),
            (1,0): Space((1,0), None, "Free"),
            (2,0): Space((2,0), None, "Door"),
            (3,0): Space((3,0), None, "Free"),
            (4,0): Space((4,0), None, "Door"),
            (5,0): Space((5,0), None, "Free"),
            (6,0): Space((6,0), None, "Door"),
            (7,0): Space((7,0), None, "Free"),
            (8,0): Space((8,0), None, "Door"),
            (9,0): Space((9,0), None, "Free"),
            (10,0): Space((10,0), None, "Free"),
            (2,1): Space((2,1), None, "A"),
            (4,1): Space((4,1), None, "B"),
            (6,1): Space((6,1), None, "C"),
            (8,1): Space((8,1), None, "D"),
            (2,2): Space((2,2), None, "A"),
            (4,2): Space((4,2), None, "B"),
            (6,2): Space((6,2), None, "C"),
            (8,2): Space((8,2), None, "D"),
        }
        if part == 2:
            self.__spaces = {
                **self.__spaces,
                (2,3): Space((2,3), None, "A"),
                (4,3): Space((4,3), None, "B"),
                (6,3): Space((6,3), None, "C"),
                (8,3): Space((8,3), None, "D"),
                (2,4): Space((2,4), None, "A"),
                (4,4): Space((4,4), None, "B"),
                (6,4): Space((6,4), None, "C"),
                (8,4): Space((8,4), None, "D"),
            }

        for pos in self.pods:
            self.__spaces[(pos[0], 4) if part == 2 and pos[1] == 2 else pos].setOccupant(self.pods[pos])
        if part == 2:
            for pos in self.pods2:
                self.__spaces[pos].setOccupant(self.pods2[pos])

        self.__spaces[(2,1)].getOccupant().isSelected = True
        self.__selected = (2,1)

    def get_spaces(self):
        return self.__spaces.values()

    def get_size(self):
        return (max(self.__spaces.keys(), key=lambda x: x[0])[0] + 1, max(self.__spaces.keys(), key=lambda x: x[1])[1] + 1)

    def check_homes(self):
        for space in self.__spaces.values():
            if space.isOccupied:
                if space.type == space.getOccupant().type:
                    space.getOccupant().isHome = True
                else:
                    space.getOccupant().isHome = False

    def select(self, pos):
        self.__spaces[self.__selected].getOccupant().isSelected = False
        self.__selected = pos
        self.__spaces[self.__selected].getOccupant().isSelected = True

    def select_next(self):
        if self.__spaces[self.__selected].type == "Door":
            return
        it = iter(self.__spaces.keys())
        while next(it) != self.__selected:
            pass
        while True:
            try:
                pos = next(it)
                if self.__spaces[pos].isOccupied:
                    self.select(pos)
                    return
            except (StopIteration):
                break
        it = iter(self.__spaces.keys())
        while True:
            pos = next(it)
            if self.__spaces[pos].isOccupied:
                self.select(pos)
                return

    def move(self, direction):
        new_position = (self.__selected[0] + direction[0], self.__selected[1] + direction[1])
        if new_position in self.__spaces and not self.__spaces[new_position].isOccupied:
            occupant = self.__spaces[self.__selected].popOccupant()
            self.__spaces[new_position].setOccupant(occupant)
            self.__selected = new_position
            return occupant.move()
        return 0

    @property
    def solved(self):
        for space in self.__spaces.values():
            if space.isOccupied and not space.getOccupant().isHome:
                return False
        return True


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Day 23: Amphipod")

burrow = Burrow(1)
score = 0

TILE_SIZE = min(SCREEN_WIDTH // burrow.get_size()[0], SCREEN_HEIGHT // 7)
help_font = pygame.font.SysFont("monospace", 20)
score_font = pygame.font.SysFont("monospace", 40)
font = pygame.font.SysFont("monospace", TILE_SIZE-2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                score += burrow.move(Direction.UP)
            elif event.key == pygame.K_DOWN:
                score += burrow.move(Direction.DOWN)
            elif event.key == pygame.K_LEFT:
                score += burrow.move(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                score += burrow.move(Direction.RIGHT)
            elif event.key == pygame.K_TAB:
                burrow.select_next()
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_1:
                score = 0
                burrow = Burrow(1)
            elif event.key == pygame.K_2:
                score = 0
                burrow = Burrow(2)

    screen.fill(Color.BACKGROUND)

    burrow.check_homes()

    score_text = score_font.render(f"Score: {score}", True, Color.TEXT_WHITE)
    screen.blit(score_text, score_text.get_rect().move(15, 5))

    for space in burrow.get_spaces():
        pygame.draw.rect(screen, Color.SPACE_OUTLINE, (space.getPosition()[0] * TILE_SIZE + 9, space.getPosition()[1] * TILE_SIZE + 59, TILE_SIZE-8, TILE_SIZE-8))
        pygame.draw.rect(screen, Color.SPACE_FILL, (space.getPosition()[0] * TILE_SIZE + 10, space.getPosition()[1] * TILE_SIZE + 60, TILE_SIZE-10, TILE_SIZE-10))

        if not space.isOccupied and len(space.type) == 1:
            text = font.render(space.type, True, Color.TEXT_DIM)
            screen.blit(text, (space.getPosition()[0] * TILE_SIZE + 20, space.getPosition()[1] * TILE_SIZE+52))

        if space.isOccupied:
            occupant = space.getOccupant()
            color = Color.TEXT_SILVER
            if occupant.isHome:
                color = Color.TEXT_GOLD
            if occupant.isSelected:
                color = Color.TEXT_GREEN
            occupant_img = font.render(occupant.type, True, color)
            screen.blit(occupant_img, (space.getPosition()[0] * TILE_SIZE + 20, space.getPosition()[1] * TILE_SIZE+52))

    help_text = help_font.render(HELP_TEXT, True, Color.TEXT_WHITE)
    screen.blit(help_text, help_text.get_rect(center=(SCREEN_WIDTH/2, 0)).move(0, TILE_SIZE*7-20))
    help_text_2 = help_font.render(HELP_TEXT_2, True, Color.TEXT_WHITE)
    screen.blit(help_text_2, help_text_2.get_rect(center=(SCREEN_WIDTH/2, 0)).move(0, TILE_SIZE*7+10))

    pygame.display.flip()