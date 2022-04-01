from tkinter import *
import csv
import os
import platform
from tkinter import messagebox
from functools import partial
from glob import glob

def setFont(plt):

    fontDict = {}

    if plt == "Windows":
        fontDict['small_font'] = 10
        fontDict['medium_font'] = 10
        fontDict['large_font'] = 16
        return fontDict
    elif plt == "Linux":
        fontDict['small_font'] = 8
        fontDict['medium_font'] = 12
        fontDict['large_font'] = 20
        return fontDict
    elif plt == "Darwin":
        print("Your system is MacOS")
        fontDict['small_font'] = 15
        fontDict['medium_font'] = 15
        fontDict['large_font'] = 20
        return fontDict
    else:
        print("Unidentified system")

def onLbxSel(lbx):

    import Calc as ex
    itm= lbx.get(lbx.curselection())
    try:
         with open('config.csv', 'r', newline='') as config:
            x = csv.reader(config)
            data = list(x)
            con=data[1][0]
    except:
        con= 0.0

    #creates new separate windows
    calcApp = Toplevel()
    ex.analize(itm, con, calcApp)
    calcApp.title(os.path.basename(itm))

def onLbxSel2(lbx):

    import K_Calc as kx
    itm= lbx.get(lbx.curselection())
    #creates new separate windows
    calcApp2 = Toplevel()
    kx.analize2(itm, calcApp2)
    calcApp2.title(os.path.basename(itm))



def buildStep1(app, fontDict):

    small_font = fontDict['small_font']
    medium_font = fontDict['medium_font']
    large_font = fontDict['large_font']

    # Constructing the first frame, frame1
    frame1 = LabelFrame(app, bg="Blue",
                        fg="white", font=(None, 20), padx=12, pady=20)
    Label(frame1, text="Welcome to Finding Analyzer" + '\n', background="Blue", fg="White", anchor='w',
          font=(None, large_font)).pack(fill='both')
    Label(frame1, text="This App shows the risks voted by the raters, ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="the Probability, the Impact and Cost Profile" + '\n', background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="Please configure your Working Directory and Risk Consensus" + '\n', background="Blue",
          fg="White", anchor='w', font=(None, small_font)).pack(fill='both')
    Label(frame1, text="    Working Directory is where ISO9001 finding csv files are stored ", background="Blue",
          fg="White", anchor='w', font=(None, small_font)).pack(fill='both')
    Label(frame1, text="    Risk Consensus is a number between 0% and 100%", background="Blue", fg="White", anchor='w',
          font=(None, small_font)).pack(fill='both')
    Label(frame1, text="    e.g.: 0% means that you want all voted risks", background="Blue", fg="White", anchor='w',
          font=(None, small_font)).pack(fill='both')
    Label(frame1, text="    e.g.: 50% means that you want only risks voted by 50% of the raters.", background="Blue",
          fg="White", anchor='w', font=(None, small_font)).pack(fill='both')
    Label(frame1, text="", background="Blue", fg="White", anchor='w', font=(None, small_font)).pack(fill='both')

    frame1.grid(row=0, column=0)

    ################ Second Frame
    try:
        with open('config.csv', 'r', newline='') as config:
            x = csv.reader(config)
            data = list(x)
            currentDir = data[1][1]
    except:
        currentDir = os.getcwd()

    try:
        with open('config.csv', 'r', newline='') as config:
           x = csv.reader(config)
           data = list(x)
           con = data[1][0]
    except:
        con = 0.0

    # Constructing the second frame, frame2
    frame2 = LabelFrame(app, bg="white", font=(None, large_font), padx=12, pady=67)
    frame2.grid(row=0, column=1)
    variable = StringVar()
    consensus = ('0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%')
    variable.set(f'{round(float(con) * 100)}%')

    # Displaying the frame2 in row 0 and column 1
    Label(frame2, text="Working Directory", font=('Arial', small_font), bg='white').grid(row=2, column=0, sticky=W,pady=10)
    bro_btn = Button(frame2, width=10, text=' Browse ... ', font=('Arial', small_font), bg='blue', fg="White",
                     command=partial(onSetDirButton, frame2, medium_font)).grid(row=2, column=2, sticky=W, pady=10)
    Label(frame2, text="Select Consensus", font=('Arial', small_font), bg='white').grid(row=4, column=0, sticky=W,pady=10)

    dir1 = StringVar(frame2, value=currentDir)
    reg_mo = Entry(frame2, textvariable=dir1, font=('Arial', medium_font), width=30)  # working directory
    reg_ge = OptionMenu(frame2, variable, *consensus)  # Consensus Percentage option menù
    reg_ge.config(width=10, font=('Arial', small_font), bg='blue', fg="White")
    reg_btn = Button(frame2, width=10, text='Next >', font=('Arial', small_font), bg='blue', fg="White",
                     command=partial(onNext, variable, currentDir, frame1, frame2, fontDict))

    # widgets placement
    reg_btn.grid(row=2, column=1, pady=10, padx=20)  # Browse Button
    reg_mo.grid(row=2, column=1, pady=10, padx=20)  # Entry 1
    reg_ge.grid(row=4, column=1, pady=10, padx=20)  # Consensus Percentage option menù
    reg_btn.grid(row=7, column=1, pady=20, padx=20)  # Next Button
    # frame2.place(x=500, y=50)
    framesAndStepDict = {'frame1': frame1,
                         'frame2': frame2,
                         'nextstep': 1}
    return framesAndStepDict

def buildStep2(frame1, frame2, fontDict):
    small_font = fontDict['small_font']
    medium_font = fontDict['medium_font']
    large_font = fontDict['large_font']

    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="Select your file and click on Run Analyzer                ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    Label(frame1, text="   ", background="Blue", fg="White", anchor='w',
          font=(None, medium_font)).pack(fill='both')
    # Displaying the frame1 in row 0 and column 0
    frame1.grid(row=0, column=0)

    ###########Second Frame
    folders = get_file_folder()
    lbx = Listbox(frame2, width=76, height=10, selectmode=EXTENDED)
    lbx.pack(fill="both", expand=1)
    list_of_files(folders, lbx)
    RunCalcButton = Button(frame2, text= 'Run Analyzer', font=('Arial', medium_font), command=partial(onLbxSel, lbx )).pack()
    RunCalcK = Button(frame2, text= 'Run K inter-rater agreemet', font=('Arial', medium_font), command=partial(onLbxSel2, lbx )).pack()

def clearFrame(frame):
   for widget in frame.winfo_children():
      widget.destroy()

def validinput(val,val_min,val_max,IsFloat=False):
    try:
        if IsFloat:
            x= float(val)
        else:
            x = int(val)
    except ValueError:
        return -1
    if x < val_min or x > val_max:
        return -1
    return True

def onNext(variable,currentDir,frame1,frame2, fontDict):

    consensus1 = int(variable.get().replace('%', ''))/100
    if validinput(consensus1, 0, 1, True) == -1:
        messagebox.showerror('Error consensus', 'Error: range 0-1. Set default = 0.5')
        consensus1 = 0.5
    else:
        consensus1 = round(float(consensus1), 1)
    try:
        with open('SetDir.csv', 'r') as setdir:
            x = csv.reader(setdir)
            newDir = list(x)
        with open('config.csv', 'w+', newline='') as file_config:
            writer = csv.writer(file_config)
            writer.writerow(['Consensus, Current Working Directory'])
            writer.writerow([consensus1, newDir[0][0]])
        os.remove('SetDir.csv')
    except:
        with open('config.csv', 'w+', newline='') as file_config:
            writer = csv.writer(file_config)
            writer.writerow(
                ['Consensus, Current Working Directory'])
            writer.writerow([consensus1, currentDir])

    clearFrame(frame1)
    clearFrame(frame2)
    buildStep2(frame1, frame2, fontDict)

def onSetDirButton(frame2,medium_font):
    import csv
    from tkinter import filedialog as fd
    currentDir = fd.askdirectory()
    with open('SetDir.csv', 'w', newline='') as setdir:
        x = csv.writer(setdir)
        x.writerow([currentDir])

    dir1 = StringVar(frame2, value=currentDir)
    reg_mo = Entry(frame2,textvariable=dir1, font=('Arial', medium_font), width=30).grid(row=2, column=1, pady=10, padx=20)

def get_file_folder() -> list:
    """ returns all files in a given folder """
    with open('config.csv', 'r', newline='') as config:
        x = csv.reader(config)
        data = list(x)
        getCsvDir = data[1][1]
    folders = glob(getCsvDir + "/*.csv")
    print(folders)
    return folders

def openfolders(f):
    os.startfile(f)

def list_of_files(folders, lbx):
    for f in folders:
        norm_f = os.path.normpath(f)
        lbx.insert(0, norm_f)

def main():
    plt = platform.system()
    fontDict= setFont(plt)
    # deletes setdir in case onNext function was not called
    if os.path.exists('SetDir.csv'):
        os.remove('SetDir.csv')

    # Create a GUI app
    app = Tk()
    app.title("Finding Analyzer")
    framesAndStepDict = buildStep1(app, fontDict)
    app.mainloop()

if __name__ == "__main__":
    main()