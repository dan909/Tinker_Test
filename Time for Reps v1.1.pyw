from Tkinter import *
import tkMessageBox as box

col_bg = "#EEEEDB" # Background Col
col_fg = "#003b6f" # Foreground Col
col_im = "#da635d" # Important col
col_bt = "#088DA5" # Button Col
col_et = "#000b16" # Entry text
col_eb = "#DEDEB8" # Entry Background

def Real_Time(reps, time_taken, units):
    if units == "seconds":
        seconds = reps * time_taken
    elif units == "minutes":
        seconds = reps * time_taken * 60
    elif units == "hours":
        seconds = reps * time_taken * 60 * 60
    else:
        print "ERROR"

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 8)
    w, d = divmod(d, 5)
    real_time = "\n%02d Weeks\n%d Days\n%d:%02d:%02d" % (w, d, h, m, s)
    return real_time


def valueGET(tme, rep, opt):
    output = {'time_taken':0, 'reps':0, 'units':0}
    output['time_taken'] = tme
    output['reps'] = rep
    output['units'] = opt
    if output['time_taken'] == "" or output['reps'] == "":
        box.showerror("Basic Error", "You Need to Write in the Boxes")
    elif output['time_taken'].isdigit() == False or output['reps'].isdigit() == False:
        box.showerror("Very Basic Error", "YOU NEED TO ENTER NUMBERS!!")
    elif 0 > float(output['time_taken']) < 1000:
        box.showerror("Time Error", "Inappropriate Number for Time")
    elif type(int(output['reps'])) != int:
        box.showerror("Other Rep Error", "Reps Must be a Hole Number")
    elif 0 > float(output['reps']) < 50000:
        box.showerror("Rep Error", "Inappropriate Number of Reps")
    else:
        if float(output['reps']) * float(output['time_taken']) > 100000:
            box.showwarning("Warning", "This may be too big")
        final = Real_Time(float(output['reps']), float(output['time_taken']), str(output['units']))
        box.showinfo("Time to Take Readings", "Working Time Based\n" + final + "  H:MM:SS")


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background=col_bg)

        self.parent = parent
        self.parent.title("Rep Time Calculator")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):

        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        #self.configure(background="gold2")

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        quitButton = Button(self, text="Quit", fg=col_im, bg=col_fg,
            command=self.onQuest)
        quitButton.place(x=250, y=120)

        inform = Button(self, text="Calculate", fg=col_fg, bg=col_bt,
                        command=lambda: valueGET(inputs_tme.get(),inputs_rep.get(), opt.get()))
        inform.place(x=5, y=120)
        lable_tme = Label(self, text="Time per Rep", fg=col_fg, bg=col_bg)
        lable_tme.grid(row=1, column=1)
        inputs_tme = Entry(self, bd =1, fg=col_et, bg=col_eb)
        inputs_tme.grid(row=1, column=2)

        lable_rep = Label(self, text="Reps", fg=col_fg, bg=col_bg)
        lable_rep.grid(row=2, column=1)
        inputs_rep = Entry(self, bd =1, fg=col_et, bg=col_eb)
        inputs_rep.grid(row=2, column=2)

        opt = StringVar(self)
        opt.set("minuets") # initial value
        lable_opt = Label(self, text="Units", fg=col_fg, bg=col_bg)
        lable_opt.grid(row=3, column=1)
        option = OptionMenu(self, opt, "seconds", "minutes", "hours")
        option.grid(row=3, column=2)
        option.config(bd=1,fg=col_fg, bg=col_bt)

    def onQuest(self):
        result = box.askquestion("Quit", "Did you intend to Quit?\n(is this app not nifty?)")
        if result == 'yes':
            self.quit()
        else:
            return True

def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()

main()