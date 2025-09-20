import sys, tty, termios

text = """Of government the properties to unfold,
Would seem in me to affect speech and discourse;"""

def raw_mode(fd):
    old = termios.tcgetattr(fd)
    tty.setraw(fd)
    return old

fd = sys.stdin.fileno()
old = raw_mode(fd)


def render():
    display = ""
    for idx, ch in enumerate(text):
        current_char = ch
        if idx == i:
            current_char = f"[{current_char}]"
        if mistakes[idx]:
            current_char = f"\033[31m{current_char}\033[0m"
        display += current_char
    # Clear screen + home; force newlines to start at column 0
    sys.stdout.write("\x1b[2J\x1b[H" + display.replace("\n", "\r\n"))
    sys.stdout.flush()

try:
    i = 0
    mistakes = [False] * len(text)
    render()
    count = 0
    total = len(text)

    while i < len(text):
        char = text[i]
        input_char = sys.stdin.read(1)

        # quit on esc
        if input_char == "\x1b":
            sys.stdout.write("\r\nQuit.\r\n")
            break
        # skip newline
        if char == "\n":
            i += 1
            if i < len(text):
                render()
            continue

        # Advance on correct key
        if input_char == char:
            i += 1
            if i < len(text):
                render()
            else:
                sys.stdout.write("\r\nDone.\r\n")
                sys.stdout.flush()
                break
        elif input_char != "\x1b":
            mistakes[i] = True
            count += 1
            render()

    accuracy = (total - count) / total * 100
    print(f"{total-count}/{total}")
    print(f"Accuracy: {round(accuracy, 2)}%")
finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old)