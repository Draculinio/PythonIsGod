import time
import curses 
from playsound import playsound

def pot(length, message, color):
    seconds = 0
    minutes = 0
    stdscr.addstr(1,30, f'{message}{length} minutes',curses.color_pair(color))
    while minutes<length:
        time.sleep(1)
        seconds+=1
        if seconds == 60:
            seconds = 0
            minutes+=1
        stdscr.addstr(10,35,f'{minutes:02}:{seconds:02}', curses.color_pair(color))
        stdscr.refresh()
    playsound('bell.mp3')
    stdscr.clear()

p = 1
stdscr = curses.initscr()
stdscr.clear()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
while(True):
    pot(25, 'Focus for ', 1)
    stdscr.addstr(15,1, f'Number of pomodoros done: {p}', curses.color_pair(4))
    p+=1
    pot(5, 'Take a little rest of ', 2) if p%4 != 0 else pot(15, 'Time of a long rest of ', 3)