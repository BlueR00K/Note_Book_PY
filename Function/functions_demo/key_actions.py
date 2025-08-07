# key_actions.py

def handle_key(key, player, grid):
    cell = grid[player.y][player.x]
    output = None
    if key in ['w', '\x1b[A']:
        return 'move', (0, -1)
    elif key in ['s', '\x1b[B']:
        return 'move', (0, 1)
    elif key in ['a', '\x1b[D']:
        return 'move', (-1, 0)
    elif key in ['d', '\x1b[C']:
        return 'move', (1, 0)
    elif key == 'p':
        if cell == 'T':
            return 'pick_up', None
        elif cell == 'P':
            return 'pick_up_potion', None
        else:
            return 'info', 'Nothing to pick up here.'
    elif key == 'h':
        if cell == 'M':
            return 'hit', None
        else:
            return 'info', 'Nothing to hit here.'
    elif key == 'e':
        if cell in ['V', 'C', 'N', 'M', 'P', 'T', '#']:
            return 'enter', None
        else:
            return 'info', 'Nothing to interact with here.'
    elif key == 't':
        if cell in ['N', 'V']:
            return 'talk', None
        else:
            return 'info', 'No one to talk/trade with here.'
    elif key == 'o':
        if cell == '#':
            return 'open', None
        else:
            return 'info', 'No door or secret here.'
    elif key == 'q':
        return 'quit', None
    else:
        return 'info', 'Unknown key.'
