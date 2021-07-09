import curses
import threading

class Gui:
    def __init__(self):
        self.stdscr = curses.initscr()
        self.item_idx_selected = 0
        self._menu_items = []
        self._menu_callbacks = []
        self.continue_parsing_inputs = True
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.use_default_colors()
        self.input_parser_thread = threading.Thread(target=self.input_parser, daemon=True)
        self.counter = 0

    def __del__(self):
        self.stop_parsing_inputs()
        self.stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def set_menu_items(self, new_items):
        self._menu_items = new_items

    def set_callbacks(self, callbacks_list):
        for idx, callback in enumerate(callbacks_list):
            self._menu_callbacks.append(threading.Thread(target = callbacks_list[idx], daemon = True))

    def update(self, data = None):
        self.stdscr.clear()
        self.counter += 1
        self.stdscr.addstr(0, 10, "counter = " + str(self.counter))
        self._print_menu_items()
        self.stdscr.refresh()

    def input_parser(self):
        curses.wrapper(self.__input_parser)

    def __input_parser(self, stdscr):
        while self.continue_parsing_inputs: 
            key = self.stdscr.getch()
            # self.stdscr.addstr(0, 0, str(key))
            if key in {curses.KEY_UP, 450, ord('k')}:
                if self.item_idx_selected > 0:
                    self.item_idx_selected -= 1
            elif key in {curses.KEY_DOWN, 456, ord('j')}:
                if self.item_idx_selected < len(self._menu_items) - 1:
                    self.item_idx_selected += 1
            elif key in {curses.KEY_ENTER, 10, 13, 459}:
                self._menu_callbacks[self.item_idx_selected].start()

    def start_parsing_inputs(self):
        self.continue_parsing_inputs = True
        self.input_parser_thread.start()

    def stop_parsing_inputs(self):
        self.continue_parsing_inputs = False
        self.input_parser_thread.join()

    def exit_loop(self):
        self._exit_menu = True

    def _print_menu_items(self):
        curses.init_pair(1, curses.COLOR_WHITE, 242)
        screen_height, screen_width = self.stdscr.getmaxyx()
        for idx, item in enumerate(self._menu_items):
            x = screen_width//2 - len(item)//2
            y = screen_height//2 - len(self._menu_items)//2 + idx
            if idx == self.item_idx_selected:
                self.stdscr.addstr(y, x, item, curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, item)

