import time
import fast_gui.gui

class App:
    def __init__(self):
        self.gui = fast_gui.gui.Gui()
        self.exit_application = False
        self.gui.start_parsing_inputs()
    def __del__(self):
        pass

    def start(self):
        self.__loop()

    def set_menu(self, items_list):
        self.gui.set_menu_items(items_list)

    def exit(self):
        self.gui.exit_loop()
        self.exit_application = True

    def set_callbacks(self, func_list):
        self.gui.set_callbacks(func_list)

    def __loop(self):
        while not self.exit_application:
            self.gui.update()
            time.sleep(.001)
