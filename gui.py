from tkinter import *
THEME_COLOR = "#83CEDC"


class GUI(Tk):
    def __init__(self, logic):
        super().__init__()
        self.logic = logic

        self.setup()
    
    def setup(self):
        self.title("poster mvp")
        self.config(padx=200, pady=200, bg=THEME_COLOR)

        self.input = Text(bg='white', fg='black', insertbackground='black', highlightthickness=0, height=4, width=20, font=("Segoe UI", 16), wrap='word')
        self.input.grid(column=0, row=0)

        self.submit = Button(highlightbackground=THEME_COLOR, text='Post', command=self.handle_button)
        self.submit.grid(column=0, row=1)
        self.submit.bind('<Key-Return>',
                         self.handle_button)
        
        # got this solution from Honest Abe @ stack overflow https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
        self.attributes('-alpha', 0.0) # makes the window transparent so you don't see it flash across the screen
        self.center_window()
        self.attributes('-alpha', 1.0) # makes the window visible again
        
    def center_window(self):
        """
        centers a tkinter window
        :param self: the main window or Toplevel window to center
        """
        self.update_idletasks() # get accurate values
        width = self.winfo_width() # all these width functions get the width of the window
        frm_width = self.winfo_rootx() - self.winfo_x() 
        win_width = width + 2 * frm_width
        height = self.winfo_height() #all these height functions get the height of the window
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2 # get the center coordinate of the x plane
        y = self.winfo_screenheight() // 2 - win_height // 2 # get the center coordinate of the y plane
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y)) # finally, place the window in the center
        self.deiconify()
        
    def handle_button(self):
        text = self.input.get("1.0", END).strip()

        self.clipboard_functionality(text)

        if self.logic.should_post:
            res = self.logic.post(text)

            self.input.delete("1.0", "end") # delete the tweet that the user posted

            if res: self.input.insert("1.0", 'Posted! ;)') # let the user know it was successful
            else: self.input.insert("1.0", 'error tweeting; ask admin') # let the user know otherwise
        
        self.logic.should_post = True

    def clipboard_functionality(self, text):
        if text == 'ADD_TO_CLIPBOARD_AFTER_POSTING=True' or text == 'ADD_TO_CLIPBOARD_AFTER_POSTING=False': # a way for the user to change the settings on if the text gets added to the clipboard upon posting
            self.logic.change_setting(text)

            self.input.delete("1.0", "end") # delete the setting text
            self.input.insert("1.0", 'setting changed') # let the user know the setting change was successful
            self.logic.should_post = False

            return

        if self.logic.settings['ADD_TO_CLIPBOARD_AFTER_POSTING']:
            self.clipboard_clear() # add what was just posted to the clipboard
            self.clipboard_append(text)
