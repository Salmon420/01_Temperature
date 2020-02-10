from tkinter import *
from functools import partial


class Converter:
    def __init__(self):
        background_color = "light blue"

        self.converter_frame = Frame(width=400,height=400,bg=background_color)
        self.converter_frame.grid()

        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font="Arial 16 bold",
                                          bg=background_color,
                                          padx=10, pady=10)

        self.temp_converter_label.grid(row=0)

        self.help_button = Button(self.converter_frame, text="help",
                                  font=("Arial","14"),
                                  padx=10, pady=10, command=self.help)

        self.help_button.grid(row=1, pady=10)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="help text goes here")


class Help:
    def __init__(self,partner):

        background="orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie:help box)
        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW',partial(self.close_help,partner))

        self.help_frame = Frame(self.help_box,width=300, bg=background)
        self.help_frame.grid()

        self.how_heading = Label(self.help_frame,text="Help / Instructions",
                                 font="arial 10 bold",bg=background)
        self.how_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40,bg=background,wrap=250)
        self.help_text.grid(row=1)

        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help,partner))
        self.dismiss_btn.grid(row=2,pady=10)

    def close_help(self,partner):

        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title ("Temperature Converter")
    something = Converter()
    root.mainloop()
