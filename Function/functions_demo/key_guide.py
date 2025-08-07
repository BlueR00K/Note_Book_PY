# key_guide.py

KEY_GUIDE = [
    ("WASD/Arrows", "Move your character"),
    ("E", "Interact (context-sensitive: open, talk, trade, fight, etc.)"),
    ("P", "Pick up item (if available)"),
    ("H", "Hit/Attack (if possible)"),
    ("Q", "Quit the game"),
    ("T", "Talk/Trade with NPC or Vendor (if present)"),
    ("O", "Open door or secret (if present)")
]


def render_key_guide(left_pad=10):
    print(" " * left_pad + "Key Guide:")
    for key, desc in KEY_GUIDE:
        print(f"{' ' * (left_pad + 2)}{key:<12} - {desc}")
