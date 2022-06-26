import tkinter as tk
import random

def colour_randomizer():
    '''Generates a random six digit HEX for colours in 
    the format: #ffffff'''
    generated_string = (hex(random.randint(0,16777215)))[2:]
    padded_string = f'#{generated_string.zfill(6)}'
    return padded_string

def main():

    # Create main window and set to fullscreen
    window = tk.Tk()
    window.attributes('-fullscreen', True)

    # create a frame with green to start with
    frame = tk.Frame(master=window, bg="grey")
    frame.pack(fill=tk.BOTH, expand=True)

    def bg_colour(event):
        frame['bg'] = colour_randomizer()

    # Exit program with CTRL+x
    window.bind_all("<Control-Key-x>", lambda close: window.destroy())

    # Press any key for pretty colour
    window.bind("<Key>", bg_colour)
    window.mainloop()

if __name__ == "__main__":
    main()
