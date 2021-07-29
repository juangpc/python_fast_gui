import fast_gui.app

def start():
    pass
    
def stop():
    pass

def void():
    pass

      
app = fast_gui.app.App()
app.set_menu(['START', 'STOP', 'RESTART', 'EXIT'])
app.set_callbacks([start, stop, void, app.exit])

app.start()
