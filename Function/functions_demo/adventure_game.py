"""
Demo Project: Recursive Adventure Game

This project demonstrates Python functions, generators, coroutines, decorators, function attributes, recursive generators, and memoization—all in a fun, interactive text adventure game.
"""

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
        print(f"Calling {func.__name__}({args})")
        return func(*args, **kwargs)
    return wrapper

# --- Memoization Example ---
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# --- Recursive Generator Example ---
def walk_map(location):
    yield location['name']
    for place in location.get('places', []):
        yield from walk_map(place)

# --- Coroutine Example ---
def echo():
    while True:
        value = yield
        print(f"Echo: {value}")

# --- Recursive Decorator Example ---
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
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
def main():
    print(greet("Adventurer"))
    print("\n--- Exploring the Map ---")
    for place in walk_map(game_map):
        print(f"You see: {place}")

    print("\n--- Finding Treasure Paths (Memoized) ---")
    for path in treasure_paths(game_map):
        print("Path to treasure:", " -> ".join(path))

    print("\n--- Fibonacci Puzzle (Memoized) ---")
    n = random.randint(5, 10)
    print(f"Fibonacci({n}) = {fib(n)}")

    print("\n--- Echo Coroutine Demo ---")
    e = echo()
    next(e)
    e.send("Welcome to the adventure!")
    e.send("Find all the treasures!")

    print("\n--- Decorator Demo: Logging Calls ---")
    @log_calls
    def open_chest():
        print("You opened a chest!")
    open_chest()

if __name__ == "__main__":
    main()
