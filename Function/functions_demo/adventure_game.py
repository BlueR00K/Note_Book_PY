"""
Demo Project: Recursive Adventure Game

This project demonstrates Python functions, generators, coroutines, decorators, function attributes, recursive generators, and memoization—all in a fun, interactive text adventure game.
"""

from item_guides import ASCII_GUIDES, DEFAULT_SWORD_ART
from functools import lru_cache
import time
import sys
import os
import random
from colorama import Fore, Style, init
init(autoreset=True)

# --- Function Attributes Example ---


def greet(name):
    greet.language = "English"
    greet.greeting_type = "friendly"
    return f"Hello, {name}!"

# --- Decorator Example ---


def log_calls(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# --- Memoization Example ---


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def random_map_size():
    width = 20
    height = 20
    return width, height


def random_item():
    # Weighted: more empty spaces, items are rare, NPCs are very rare
    return random.choices(
        population=[' ', '#', 'T', 'V', 'C', 'M', 'P', 'N'],
        weights=[200, 10, 5, 2, 2, 5, 7, 1],
        k=1
    )[0]


def generate_procedural_map():
    width, height = random_map_size()
    grid = [[random_item() for _ in range(width)] for _ in range(height)]
    # Ensure at least one vendor, cave, and treasure
    vendor_x, vendor_y = random.randint(
        0, width-1), random.randint(0, height-1)
    cave_x, cave_y = random.randint(0, width-1), random.randint(0, height-1)
    treasure_x, treasure_y = random.randint(
        0, width-1), random.randint(0, height-1)
    grid[vendor_y][vendor_x] = 'V'
    grid[cave_y][cave_x] = 'C'
    grid[treasure_y][treasure_x] = 'T'
    return grid, width, height


try:
    import msvcrt

    def get_key():
        """Get a single keypress (Windows), handling arrow keys and decoding safely."""
        ch = msvcrt.getch()
        # Arrow keys and function keys start with b'\x00' or b'\xe0'
        if ch in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
            # Arrow keys: up, down, left, right
            arrow_map = {b'H': '\x1b[A', b'P': '\x1b[B',
                         b'K': '\x1b[D', b'M': '\x1b[C'}
            return arrow_map.get(key, '')
        try:
            return ch.decode('cp1252').lower()
        except UnicodeDecodeError:
            return ''
except ImportError:
    import tty
    import termios

    def get_key():
        """Get a single keypress (Unix)."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

MAP_WIDTH = 10
MAP_HEIGHT = 7
TREASURE_COUNT = 3
OBSTACLE_COUNT = 8
VENDOR_LOC = (2, 7)
CAVE_LOC = (5, 2)


def create_game_map():
    return generate_procedural_map()[0]


def draw_map(grid, player):
    os.system('cls' if os.name == 'nt' else 'clear')
    left_pad = 10
    print(" " * left_pad + f"{Fore.YELLOW}Adventure Map:{Style.RESET_ALL}")
    guide_item = None
    for y, row in enumerate(grid):
        line = ''
        for x, cell in enumerate(row):
            if player.x == x and player.y == y:
                line += Fore.GREEN + '@' + Style.RESET_ALL
                if cell in ASCII_GUIDES:
                    guide_item = cell
            elif cell == '#':
                line += Fore.WHITE + '#' + Style.RESET_ALL
            elif cell == 'T':
                line += Fore.YELLOW + '$' + Style.RESET_ALL
            elif cell == 'V':
                line += Fore.BLUE + 'V' + Style.RESET_ALL
            elif cell == 'C':
                line += Fore.MAGENTA + 'C' + Style.RESET_ALL
            elif cell == 'M':
                line += Fore.RED + 'M' + Style.RESET_ALL
            elif cell == 'P':
                line += Fore.CYAN + 'P' + Style.RESET_ALL
            elif cell == 'N':
                line += Fore.LIGHTWHITE_EX + 'N' + Style.RESET_ALL
            else:
                line += ' '
        # Print map row centered
        print(" " * left_pad + line, end='')
        print()
    # Always show the image panel on the right
    if guide_item:
        ascii_art, info = ASCII_GUIDES[guide_item]
    else:
        ascii_art, info = DEFAULT_SWORD_ART
    # Show the guide at the top (20-width area, any height)
    print(" " * left_pad + f"{Fore.YELLOW}Item Guide:{Style.RESET_ALL}")
    # Format info to 20-width lines

    def wrap_text(text, width=20):
        import textwrap
        return textwrap.wrap(text, width=width)
    if ascii_art:
        art_lines = ascii_art.splitlines()
        for art_line in art_lines[:20]:
            print(" " * left_pad + art_line[:20])
    if info:
        for line in wrap_text(info, 20):
            print(" " * left_pad + line)
    print()
    print(" " * left_pad + f"{Fore.YELLOW}Adventure Map:{Style.RESET_ALL}")
    for y, row in enumerate(grid):
        line = ''
        for x, cell in enumerate(row):
            if player.x == x and player.y == y:
                line += Fore.GREEN + '@' + Style.RESET_ALL
            elif cell == '#':
                line += Fore.WHITE + '#' + Style.RESET_ALL
            elif cell == 'T':
                line += Fore.YELLOW + '$' + Style.RESET_ALL
            elif cell == 'V':
                line += Fore.BLUE + 'V' + Style.RESET_ALL
            elif cell == 'C':
                line += Fore.MAGENTA + 'C' + Style.RESET_ALL
            elif cell == 'M':
                line += Fore.RED + 'M' + Style.RESET_ALL
            elif cell == 'P':
                line += Fore.CYAN + 'P' + Style.RESET_ALL
            elif cell == 'N':
                line += Fore.LIGHTWHITE_EX + 'N' + Style.RESET_ALL
            else:
                line += ' '
        print(" " * left_pad + line)
    # Status bar and key guide at the bottom
    print("\n" + " " * left_pad +
          f"Player: {player.name} | HP: {player.hp} | Treasures: {player.treasures} | Inventory: {player.inventory}")
    print(" " * left_pad +
          "Keys: [WASD/Arrows] Move | [E] Interact | [P] Pick Up | [H] Hit | [Q] Quit | [T] Talk/Trade | [O] Open Door")


def echo():
    """Coroutine for game messages."""
    while True:
        msg = yield
        print(f"\033[96m{msg}\033[0m")


@log_calls
def move_player(player, grid, dx, dy):
    """Move player if possible."""
    nx, ny = player.x + dx, player.y + dy
    map_height = len(grid)
    map_width = len(grid[0])
    if 0 <= nx < map_width and 0 <= ny < map_height and grid[ny][nx] != '#':
        player.x, player.y = nx, ny
        player.moves += 1
    else:
        print(Fore.RED + "Blocked!" + Style.RESET_ALL)


@log_calls
def pick_up(player, grid):
    """Pick up treasure if present."""
    if grid[player.y][player.x] == 'T':
        player.inventory.append('Treasure')
        player.treasures += 1
        grid[player.y][player.x] = ' '
        print("\033[93mYou picked up a treasure!\033[0m")
    else:
        print("Nothing to pick up here.")


@log_calls
def hit(player, grid):
    """Hit obstacle or interact."""
    print("You swing your sword!")


@log_calls
def enter(player, grid):
    cell = grid[player.y][player.x]
    # Regenerate map at each gate/checkpoint (vendor/cave)
    if cell in ['V', 'C']:
        print(Fore.CYAN + "Checkpoint reached! The world shifts..." + Style.RESET_ALL)
        new_grid, new_width, new_height = generate_procedural_map()
        player.x, player.y = 0, 0
        grid[:] = new_grid
    elif cell == 'N':
        print(Fore.LIGHTWHITE_EX +
              "You meet an NPC! Press [T] to talk or [E] to interact." + Style.RESET_ALL)
    elif cell == '#':
        print(
            Fore.WHITE + "It's a wall. Maybe you can open a secret door with [O]." + Style.RESET_ALL)
    elif cell == 'P':
        print(Fore.CYAN +
              "You found a potion! Press [P] to pick up." + Style.RESET_ALL)
    elif cell == 'M':
        print(
            Fore.RED + "A monster blocks your way! Press [H] to hit or [E] to interact." + Style.RESET_ALL)
    elif cell == 'T':
        print(Fore.YELLOW +
              "Treasure! Press [P] to pick up." + Style.RESET_ALL)
    else:
        print("Nothing to enter here.")


def find_all_treasures(grid):
    """Recursively yield all treasure locations."""
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'T':
                yield (x, y)


class Player:
    """Player state and actions."""

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.inventory = []
        self.hp = 10
        self.treasures = 0
        self.moves = 0
        self.vendor_deals = 0
        self.__dict__['special'] = 'Adventurer'

    def stats(self):
        """Show player stats."""
        print(
            f"Player: {self.name} | HP: {self.hp} | Treasures: {self.treasures} | Inventory: {self.inventory}")


def main():
    grid, map_width, map_height = generate_procedural_map()
    name = input("Enter your adventurer's name: ")
    player = Player(name)
    msg = echo()
    next(msg)
    while True:
        draw_map(grid, player)
        msg.send(f"Moves: {player.moves} | Treasures: {player.treasures}")
        key = get_key()
        if key in ['q']:
            print("Thanks for playing!")
            break
        elif key in ['w', '\x1b[A']:
            move_player(player, grid, 0, -1)
        elif key in ['s', '\x1b[B']:
            move_player(player, grid, 0, 1)
        elif key in ['a', '\x1b[D']:
            move_player(player, grid, -1, 0)
        elif key in ['d', '\x1b[C']:
            move_player(player, grid, 1, 0)
        elif key == 'p':
            pick_up(player, grid)
        elif key == 'h':
            hit(player, grid)
        elif key == 'e':
            enter(player, grid)
        else:
            msg.send("Unknown key.")
        time.sleep(0.1)
    print("\n--- Game Summary ---")
    player.stats()
    print("Treasures found:", player.treasures)
    print("Vendor deals:", player.vendor_deals)
    print("Inventory:", player.inventory)
    print("All treasure locations:")
    for loc in find_all_treasures(grid):
        print(loc)
    print("\nThanks for playing the 2D Adventure Game!")


def print_location(location):
    print(f"\nYou are at: {location['name']}")
    if location.get('treasure'):
        print("\033[93mYou sense treasure nearby!\033[0m")
    if location.get('places'):
        print("Places to explore:")
        for idx, place in enumerate(location['places']):
            print(f"  [{idx+1}] {place['name']}")


def print_map(location, depth=0):
    print("  " * depth + f"- {location['name']}")
    for place in location.get('places', []):
        print_map(place, depth+1)

# --- Memorization Decorator ---


def memorize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@memorize
def treasure_paths(map_data, path=None):
    if path is None:
        path = []
    if map_data.get('treasure', False):
        yield path + [map_data['name']]
    for place in map_data.get('places', []):
        yield from treasure_paths(place, path + [map_data['name']])


# --- Game Map ---
game_map = {
    'name': 'Village',
    'places': [
        {'name': 'Forest', 'places': [
            {'name': 'Cave', 'treasure': True},
            {'name': 'Lake'}
        ]},
        {'name': 'Castle', 'places': [
            {'name': 'Dungeon', 'treasure': True},
            {'name': 'Tower'}
        ]}
    ]
}

# --- Main Game Logic ---


if __name__ == "__main__":
    main()
