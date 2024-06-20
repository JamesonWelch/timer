import time
import os
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    size = shutil.get_terminal_size((80, 20))
    return size.columns, size.lines

def print_large_time(minutes):
    # ASCII art representation for digits 0-9
    digits = [
        [" 000 ", "0   0", "0   0", "0   0", " 000 "],  # 0
        ["  1  ", " 11  ", "  1  ", "  1  ", "11111"],  # 1
        [" 222 ", "2   2", "   2 ", "  2  ", "22222"],  # 2
        [" 333 ", "    3", " 333 ", "    3", " 333 "],  # 3
        ["4   4", "4   4", " 4444", "    4", "    4"],  # 4
        ["55555", "5    ", "5555 ", "    5", "5555 "],  # 5
        [" 666 ", "6    ", "6666 ", "6   6", " 666 "],  # 6
        ["77777", "    7", "   7 ", "  7  ", " 7   "],  # 7
        [" 888 ", "8   8", " 888 ", "8   8", " 888 "],  # 8
        [" 9999", "9   9", " 9999", "    9", " 999 "],  # 9
    ]

    # Convert minutes to string
    time_str = f"{minutes:04}"
    
    # Build the large display for the current time
    lines = [""] * 5
    for char in time_str:
        digit = int(char)
        for i in range(5):
            lines[i] += digits[digit][i] + " "

    # Get terminal size
    term_width, term_height = get_terminal_size()
    
    # Calculate horizontal and vertical padding
    horizontal_padding = (term_width - len(lines[0])) // 2
    vertical_padding = (term_height - len(lines)) // 2

    # Print the padded lines to center the output
    for _ in range(vertical_padding):
        print()
    
    for line in lines:
        print(" " * horizontal_padding + line)

def countdown_timer(minutes=1000):
    while minutes >= 0:
        clear_screen()
        print_large_time(minutes)
        time.sleep(60)
        minutes -= 1

if __name__ == "__main__":
    countdown_timer()
