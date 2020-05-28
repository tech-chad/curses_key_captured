# curses key catch
import curses


def curses_main(screen):
    screen.addstr(0, 0, "enter 'Q' to quit")
    while True:
        screen.move(1, 0)
        ch  = screen.getch()
        screen.clear()
        screen.addstr(0, 0, "enter 'Q' to quit")
        screen.addstr(1, 0, f"{chr(ch)}   {str(ch)}")
        screen.refresh()
        if ch in [81, 113]:
            break


def main():
    curses.wrapper(curses_main)


if __name__ == "__main__":
    exit(main())

