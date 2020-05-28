# curses key catch
import argparse
import curses

FILENAME = "CursesKeyCatchLog.txt"


def log_to_file(ch: str) -> None:
    with open(FILENAME, "a") as f:
        f.write(f"{chr(ch)}  {str(ch)}\n")


def curses_main(screen, args):
    screen.addstr(0, 0, "enter 'Q' to quit")
    while True:
        screen.move(1, 0)
        ch  = screen.getch()

        if args.log:
            log_to_file(ch)

        screen.clear()
        screen.addstr(0, 0, "enter 'Q' to quit")
        screen.addstr(1, 0, f"{chr(ch)}   {str(ch)}")
        screen.refresh()
        if ch in [81, 113]:
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", dest="log", action="store_true",
                        help="save key codes to file")
    args = parser.parse_args()
    curses.wrapper(curses_main, args)


if __name__ == "__main__":
    exit(main())
