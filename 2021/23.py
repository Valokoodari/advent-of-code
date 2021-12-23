import pygame


# TODO: Add a check to see if an amphipod in the hallway can go straight to home
# TODO: Read the input from a file
# TODO: Clean up the code
# TODO: Autosolve the problem


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

HELP_TEXT = "Arrow keys or WASD to move, Tab to select, Escape to quit,"
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
    pods_1 = (
        ((2,1), 'B'), ((4,1), 'C'), ((6,1), 'B'), ((8,1), 'D'),
        ((2,2), 'A'), ((4,2), 'D'), ((6,2), 'C'), ((8,2), 'A'),
    )
    pods_2 = (
        ((2,2), 'D'), ((4,2), 'C'), ((6,2), 'B'), ((8,2), 'A'),
        ((2,3), 'D'), ((4,3), 'B'), ((6,3), 'A'), ((8,3), 'C'),
    )

    spaces_1 = (
        ((0,0), 'F'), ((1,0), 'F'), ((2,0), 'E'), ((3,0), 'F'),
        ((4,0), 'E'), ((5,0), 'F'), ((6,0), 'E'), ((7,0), 'F'),
        ((8,0), 'E'), ((9,0), 'F'), ((10,0), 'F'),
        ((2,1), 'A'), ((4,1), 'B'), ((6,1), 'C'), ((8,1), 'D'),
        ((2,2), 'A'), ((4,2), 'B'), ((6,2), 'C'), ((8,2), 'D'),
    )
    spaces_2 = (
        ((2,3), 'A'), ((4,3), 'B'), ((6,3), 'C'), ((8,3), 'D'),
        ((2,4), 'A'), ((4,4), 'B'), ((6,4), 'C'), ((8,4), 'D'),
    )

    def __init__(self, part):
        self.__moves = []

        self.__spaces = { pos: Space(pos, None, typ) for pos, typ in self.spaces_1 }
        if part == 2:
            self.__spaces = {
                **self.__spaces,
                **{ pos: Space(pos, None, typ) for pos, typ in self.spaces_2 }
            }

        for pos, typ in self.pods_1:
            self.__spaces[(pos[0], 4) if part == 2 and pos[1] == 2 else pos].setOccupant(Amphipod(typ))
        if part == 2:
            for pos, typ in self.pods_2:
                self.__spaces[pos].setOccupant(Amphipod(typ))

        self.__spaces[(2,1)].getOccupant().isSelected = True
        self.selected = (2,1)

    @property 
    def spaces(self):
        return self.__spaces

    def get_size(self):
        return (max(self.__spaces.keys(), key=lambda x: x[0])[0] + 1, max(self.__spaces.keys(), key=lambda x: x[1])[1] + 1)

    def check_homes(self):
        for space in self.__spaces.values():
            if space.isOccupied:
                if space.type == space.getOccupant().type:
                    space.getOccupant().isHome = True
                else:
                    space.getOccupant().isHome = False

    def select_next(self, backward=False):
        if self.__spaces[self.selected].type == "E":
            return

        pods = [pos for pos, space in self.__spaces.items() if space.isOccupied]
        current = pods.index(self.selected)
        next_position = pods[(current+(-1 if backward else 1))%len(pods)]

        self.selected = next_position

    def move(self, direction):
        new_position = (self.selected[0] + direction[0], self.selected[1] + direction[1])
        if new_position in self.__spaces and not self.__spaces[new_position].isOccupied:
            occupant = self.__spaces[self.selected].popOccupant()
            cost = occupant.move()
            if len(self.__moves) > 0 and self.__moves[-1] == (new_position, self.selected):
                self.__moves.pop()
                cost = -cost
            else:
                self.__moves.append((self.selected, new_position))
            self.__spaces[new_position].setOccupant(occupant)
            self.selected = new_position

            return cost
        return 0
    
    def undo_move(self):
        if len(self.__moves) < 1:
            return 0
        prev_pos, curr_pos = self.__moves.pop()
        occupant = self.__spaces[curr_pos].popOccupant()
        self.__spaces[prev_pos].setOccupant(occupant)
        self.selected = prev_pos
        return -occupant.move()

    @property
    def solved(self):
        for space in self.__spaces.values():
            if space.isOccupied and not space.getOccupant().isHome:
                return False
        return True


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
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
            match event.key:
                case pygame.K_UP | pygame.K_w:
                    score += burrow.move(Direction.UP)
                case pygame.K_DOWN | pygame.K_s:
                    score += burrow.move(Direction.DOWN)
                case pygame.K_LEFT | pygame.K_a:
                    score += burrow.move(Direction.LEFT)
                case pygame.K_RIGHT | pygame.K_d:
                    score += burrow.move(Direction.RIGHT)
                case pygame.K_TAB:
                    if pygame.KMOD_LSHIFT & pygame.key.get_mods():
                        burrow.select_next(True)
                    else:
                        burrow.select_next()
                case pygame.K_z:
                    if pygame.KMOD_LCTRL & pygame.key.get_mods():
                        score += burrow.undo_move()
                case pygame.K_ESCAPE:
                    running = False
                case pygame.K_1:
                    score = 0
                    burrow = Burrow(1)
                case pygame.K_2:
                    score = 0
                    burrow = Burrow(2)

    screen.fill(Color.BACKGROUND)

    burrow.check_homes()

    score_text = score_font.render(f"Score: {score}", True, Color.TEXT_WHITE)
    screen.blit(score_text, score_text.get_rect().move(15, 5))

    for position, space in burrow.spaces.items():
        pygame.draw.rect(screen, Color.SPACE_OUTLINE, (space.getPosition()[0] * TILE_SIZE + 9, space.getPosition()[1] * TILE_SIZE + 59, TILE_SIZE-8, TILE_SIZE-8))
        pygame.draw.rect(screen, Color.SPACE_FILL, (space.getPosition()[0] * TILE_SIZE + 10, space.getPosition()[1] * TILE_SIZE + 60, TILE_SIZE-10, TILE_SIZE-10))

        if not space.isOccupied and space.type in ['A', 'B', 'C', 'D']:
            text = font.render(space.type, True, Color.TEXT_DIM)
            screen.blit(text, (space.getPosition()[0] * TILE_SIZE + 20, space.getPosition()[1] * TILE_SIZE+52))

        if space.isOccupied:
            occupant = space.getOccupant()
            color = Color.TEXT_SILVER
            if occupant.isHome:
                color = Color.TEXT_GOLD
            if position == burrow.selected:
                color = Color.TEXT_GREEN
            occupant_img = font.render(occupant.type, True, color)
            screen.blit(occupant_img, (space.getPosition()[0] * TILE_SIZE + 20, space.getPosition()[1] * TILE_SIZE+52))

    help_text = help_font.render(HELP_TEXT, True, Color.TEXT_WHITE)
    screen.blit(help_text, help_text.get_rect(center=(SCREEN_WIDTH/2, 0)).move(0, TILE_SIZE*7-20))
    help_text_2 = help_font.render(HELP_TEXT_2, True, Color.TEXT_WHITE)
    screen.blit(help_text_2, help_text_2.get_rect(center=(SCREEN_WIDTH/2, 0)).move(0, TILE_SIZE*7+10))

    pygame.display.flip()
    clock.tick(30)