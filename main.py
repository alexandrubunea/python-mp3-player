import tkinter
import config

def main():
    # Application Configuration
    root = tkinter.Tk()
    root.title(config.APPLICATION_TITLE)
    root.resizable(True, True)
    root.maxsize(config.APPLICATION_MAX_WIDTH, config.APPLICATION_MAX_HEIGHT)
    root.minsize(config.APLICATION_MIN_WIDTH, config.APLICATION_MIN_HEIGHT)

    root.mainloop()
main()