# importing requirements
import time
from tkinter import *
from tkinter import messagebox
global running
global is_close
global we_pause_it
global given_time
import pyttsx3
is_close = True

# code start from here
if __name__ == '__main__':
    # initializing object
    root = Tk()

    # function overriding of [x] button
    def close_ex():
        global is_close, given_time
        is_close = False
        given_time = -4
        root.destroy()

    # overriding [x] close button
    root.protocol('WM_DELETE_WINDOW', close_ex)

    # app dimensions
    app_width = 86
    app_height = 310

    # fetching screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # window position
    x_coordinates = screen_width - app_width
    y_coordinates = 0

    # app must pop on right side of screen out of browser
    root.geometry(f'{app_width}x{app_height}+{x_coordinates}+{y_coordinates}')

    # other basics stuff
    root.configure(background="black")
    root.title('Problem Solving StopWatch')
    root.maxsize(300, 320)
    root.minsize(app_width, app_height)

    # variables for time
    hours = StringVar()
    mints = StringVar()
    secs = StringVar()

    # default value of these variables
    hours.set('00')
    mints.set('05')
    secs.set('00')

    try:
        # creating object of widgets
        hours_entry = Entry(root, width=2, font='verdana 17 bold', bd=18, textvariable=hours)
        hours_entry.place(x=8, y=15)

        mints_entry = Entry(root, width=2, font='verdana 17 bold', bd=18, textvariable=mints)
        mints_entry.place(x=8, y=75)

        secs_entry = Entry(root, width=2, font='verdana 17 bold', bd=18, textvariable=secs)
        secs_entry.place(x=8, y=135)
    except: exit(0)

    # defining a local function
    def submit_timer():
        # input given by user
        try:
            # i am providing only access for 12 hrs
            hrs = int(hours.get())
            mnt = int(mints.get())
            sec = int(secs.get())

            if hrs >= 12: hrs = 11
            if mnt >= 60: mnt = 59
            if sec > 60: sec = 59
        except:
            hrs = 0
            mnt = 5
            sec = 0

        global running
        running = True

        global we_pause_it
        we_pause_it = True

        # now calculate given time in seconds
        global given_time
        given_time = hrs * 3600 + mnt * 60 + sec

        try:
            # now writing logic for this project
            while given_time > -1:
                # mnt = given_time // 60, sec = given_time % 60
                mnt, sec = divmod(given_time, 60)

                hrs = 0
                if mnt > 60:
                    hrs, mnt = divmod(mnt, 60)

                # now set value of output variables
                hours.set("{0:2d}".format(hrs))
                mints.set("{0:2d}".format(mnt))
                secs.set("{0:2d}".format(sec))

                # now update the window after decrementing given output variables
                try:
                    root.update()
                    time.sleep(1)
                except: pass

                # alert message of times up
                try:
                    if given_time == 0 and is_close:
                        # make our app to speak
                        engine = pyttsx3.init()
                        engine.say('timees upp')
                        engine.say('leave itt')
                        engine.runAndWait()

                        # show a dialogue box
                        messagebox.showinfo('Time Over', 'Time Over')

                except: pass

                # now decrease the values every seconds
                if we_pause_it:
                    given_time -= 1


                # if close button pressed then this statement will close everything after running
                if not running:
                    hours.set('00')
                    mints.set('05')
                    secs.set('00')
                    try:
                        root.update()
                    except: pass
                    break
        except: pass

    # this method close the window
    def pause_timer():
        global we_pause_it
        we_pause_it = False

    # this method reset the timer
    def reset_timer():
        global running
        running = False

    # here we are out of the local function
    submit_btn = Button(root, text="Start Timer", bd=5, command=submit_timer)
    submit_btn.place(x=5, y=220)

    # close all activity
    close_btn = Button(root, text="Pause", bd=5, command=pause_timer, padx=16.5)
    close_btn.place(x=5, y=250)

    # reset timer
    reset_btn = Button(root, text="Reset", bd=5, command=reset_timer, padx=17.5)
    reset_btn.place(x=5, y=280)

    try:
        # for running window
        root.mainloop()
    except: root.destroy()
