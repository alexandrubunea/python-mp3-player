import tkinter
import os
import config

def load_settings():
    # Create settings.cfg if it's missing ...
    if not os.path.isfile('./settings.cfg'):
        with open('settings.cfg', 'w') as cfg_file:
            cfg_file.write("SCREEN_WIDTH=1280\n")
            cfg_file.write("SCREEN_HEIGHT=720\n")
    
    # Load the settings and export them in a dictonary
    settings = {}
    
    cfg_file = open('settings.cfg', 'r')
    cfg_lines = cfg_file.readlines()

    for line in cfg_lines:
        split_line = line.split("=")
        variable = split_line[0]
        value = split_line[1]
        settings[variable] = str(value[:-1]) # Remove the newline character '\n'

    return settings

def save_settings(settings):
    open('settings.cfg', 'w').close() # Erase all the settings from the .cfg file

    with open('settings.cfg', 'w') as cfg_file:
        for variable in settings:
            value = settings[variable]
            cfg_file.write(variable + "=" + value + "\n")

def window_change_size(event, settings):
    settings['SCREEN_WIDTH'] = str(event.width)
    settings['SCREEN_HEIGHT'] = str(event.height)

def exit_application(root, settings):
    save_settings(settings)
    
    root.destroy()

def main():
    # Load Application Settings
    settings = load_settings()

    # Application Configuration
    root = tkinter.Tk()
    root.title(config.APPLICATION_TITLE)
    root.resizable(True, True)
    root.maxsize(config.APPLICATION_MAX_WIDTH, config.APPLICATION_MAX_HEIGHT)
    root.minsize(config.APLICATION_MIN_WIDTH, config.APLICATION_MIN_HEIGHT)
    root.geometry(settings['SCREEN_WIDTH'] + "x" + settings['SCREEN_HEIGHT'])

    root['bg'] = config.APPLICATION_BACKGROUND_COLOR

    # Events
    root.bind('<Configure>', lambda event : window_change_size(event, settings))
    root.protocol('WM_DELETE_WINDOW', lambda : exit_application(root, settings))

    root.mainloop()
main()