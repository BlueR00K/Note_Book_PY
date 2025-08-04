"""
Demo Project: Recursive Adventure Game

This project demonstrates Python functions, generators, coroutines, decorators, function attributes, recursive generators, and memoization—all in a fun, interactive text adventure game.
"""

import time
import sys
import os
import random
from functools import lru_cache

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


# --- 2D CLI Adventure Game ---
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
    """Create the game map with treasures and obstacles."""
    grid = [[' ' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    for _ in range(OBSTACLE_COUNT):
        x, y = random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)
        grid[y][x] = '#'
    placed = 0
    while placed < TREASURE_COUNT:
        x, y = random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)
        if grid[y][x] == ' ':
            grid[y][x] = 'T'
            placed += 1
    vx, vy = VENDOR_LOC
    cx, cy = CAVE_LOC
    if 0 <= vx < MAP_WIDTH and 0 <= vy < MAP_HEIGHT:
        grid[vy][vx] = 'V'
    if 0 <= cx < MAP_WIDTH and 0 <= cy < MAP_HEIGHT:
        grid[cy][cx] = 'C'
    return grid


def draw_map(grid, player):
    """Draw the game map with player and objects."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n  Adventure Map:")
    for y, row in enumerate(grid):
        line = ''
        for x, cell in enumerate(row):
            if player.x == x and player.y == y:
                line += '\033[92m@\033[0m'
            elif cell == '#':
                line += '\033[90m#\033[0m'
            elif cell == 'T':
                line += '\033[93m$\033[0m'
            elif cell == 'V':
                line += '\033[94mV\033[0m'
            elif cell == 'C':
                line += '\033[95mC\033[0m'
            else:
                line += ' '
        print(line)
    player.stats()
    print("Use arrow keys to move. [P]ick up, [H]it, [E]nter, [Q]uit.")


def echo():
    """Coroutine for game messages."""
    while True:
        msg = yield
        print(f"\033[96m{msg}\033[0m")


@log_calls
def move_player(player, grid, dx, dy):
    """Move player if possible."""
    nx, ny = player.x + dx, player.y + dy
    if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT and grid[ny][nx] != '#':
        player.x, player.y = nx, ny
        player.moves += 1
    else:
        print("\033[91mBlocked!\033[0m")


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
    """Enter cave or interact with vendor."""
    cell = grid[player.y][player.x]
    if cell == 'V':
        print("\033[94mVendor: Want to buy a potion for 1 treasure? [Y/N]\033[0m")
        ans = input().strip().lower()
        if ans == 'y' and player.treasures > 0:
            player.treasures -= 1
            player.inventory.append('Potion')
            player.vendor_deals += 1
            print("You bought a potion!")
        else:
            print("No deal.")
    elif cell == 'C':
        print("\033[95mYou enter the cave. It's dark and mysterious...\033[0m")
        challenge_type = random.choice(['fight', 'puzzle', 'skill'])
        if challenge_type == 'fight':
            print("A monster appears! Prepare to fight!")
            monster_hp = random.randint(3, 7)
            while monster_hp > 0 and player.hp > 0:
                action = input("[A]ttack or [R]un? ").strip().lower()
                if action == 'a':
                    dmg = random.randint(1, 4)
                    monster_hp -= dmg
                    print(
                        f"You hit the monster for {dmg} damage! Monster HP: {max(monster_hp, 0)}")
                    if monster_hp > 0:
                        mdmg = random.randint(1, 3)
                        player.hp -= mdmg
                        print(
                            f"Monster hits you for {mdmg} damage! Your HP: {max(player.hp, 0)}")
                elif action == 'r':
                    print("You run away from the cave!")
                    return
                else:
                    print("Invalid action. Choose [A]ttack or [R]un.")
            if player.hp > 0:
                print("You defeated the monster and found a hidden treasure!")
                player.inventory.append('Cave Treasure')
                player.treasures += 1
            else:
                print("You were defeated by the monster. Game over!")
                exit()
        elif challenge_type == 'puzzle':
            print("You encounter a mysterious puzzle!")
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            op = random.choice(['+', '-', '*'])
            if op == '+':
                answer = a + b
            elif op == '-':
                answer = a - b
            else:
                answer = a * b
            print(f"Solve: {a} {op} {b} = ?")
            guess = input("Your answer: ").strip()
            if guess.isdigit() and int(guess) == answer:
                print("Correct! You solved the puzzle and found a hidden treasure!")
                player.inventory.append('Cave Treasure')
                player.treasures += 1
            else:
                print(
                    f"Wrong! The answer was {answer}. You leave the cave empty-handed.")
        elif challenge_type == 'skill':
            print("A trap is triggered! Test your reflexes.")
            print("Press Enter as soon as you see GO!")
            time.sleep(random.uniform(1, 3))
            print("GO!")
            start = time.time()
            input()
            reaction = time.time() - start
            if reaction < 0.7:
                print(
                    f"Amazing reflexes! ({reaction:.2f}s) You dodge the trap and find a treasure!")
                player.inventory.append('Cave Treasure')
                player.treasures += 1
            else:
                print(
                    f"Too slow! ({reaction:.2f}s) The trap hits you. Lose 2 HP.")
                player.hp -= 2
                if player.hp <= 0:
                    print("You were defeated by the trap. Game over!")
                    exit()
        else:
            print("Nothing happens...")
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
    """Main entry point for the adventure game."""
    grid = create_game_map()
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
