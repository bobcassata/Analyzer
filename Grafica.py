from ttkwidgets import Table
import tkinter as tk
from tkinter import ttk
import operator
import platform
try:
    from idlelib.tooltip import Hovertip
except ImportError:
    print("idlelib.tooltip not supported on MacOS")

def calc_Lk_Agr(k):
    if k < 0 :
        LKSTRING = "Poor"
    elif (k > 0.01 and k <= 0.2):
        LKSTRING = "Slight"
    elif (k >= 0.21 and k <= 0.4):
        LKSTRING = "Fair"
    elif (k >= 0.41 and k <= 0.6):
        LKSTRING = "Moderate"
    elif (k >= 0.61 and k <= 0.8):
        LKSTRING = "Substantial"
    elif (k >= 0.81 and k <= 1) :
        LKSTRING = "Substantial"
    else:
        LKSTRING = "Error"

    return LKSTRING

# Run K inter-rater agreement
def buildtable2(FileSelected, app2, k_raList, k_srList, k_ndList):

    app2.geometry('600x180')
    app2.resizable(False, False)
    #app.configure(bg= 'gray100')
    app2.columnconfigure(0, weight=1)
    app2.rowconfigure(0, weight=1)

    style = ttk.Style(app2)
    style.theme_use('alt')
    sortable = tk.BooleanVar(app2, False)
    drag_row = tk.BooleanVar(app2, False)
    drag_col = tk.BooleanVar(app2, False)

    columns = ["Risk Class", "Kra", "Ksr", "K*"]
    table = Table(app2, columns=columns, sortable=sortable.get(), drag_cols=drag_col.get(),
                  drag_rows=drag_row.get(), height=6)

    table.grid(row=0, column= 0, columnspan=5)

    for col in columns:
        table.heading(col, anchor= 'c' ,text=col)
        table.column(col, width=140, anchor= 'c' ,stretch=True)

    kra_0 = calc_Lk_Agr(k_raList[0])
    ksr_0 = calc_Lk_Agr(k_srList[0])
    knd_0 = calc_Lk_Agr(k_ndList[0])
    kra_1 = calc_Lk_Agr(k_raList[1])
    ksr_1 = calc_Lk_Agr(k_srList[1])
    knd_1 = calc_Lk_Agr(k_ndList[1])
    kra_2 = calc_Lk_Agr(k_raList[2])
    ksr_2 = calc_Lk_Agr(k_srList[2])
    knd_2 = calc_Lk_Agr(k_ndList[2])
    kra_3 = calc_Lk_Agr(k_raList[3])
    ksr_3 = calc_Lk_Agr(k_srList[3])
    knd_3 = calc_Lk_Agr(k_ndList[3])
    kra_4 = calc_Lk_Agr(k_raList[4])
    ksr_4 = calc_Lk_Agr(k_srList[4])
    knd_4 = calc_Lk_Agr(k_ndList[4])

    tuple1 = ('Strategic Risk',str(round(k_raList[0],2)) +"  "+ kra_0, str(round(k_srList[0],2))+"  "+ ksr_0,str(round(k_ndList[0],2))+"  "+ knd_0)
    table.insert('', 'end', iid=1, values=tuple1)

    tuple2 = ('Legal Risk',str(round(k_raList[1],2)) +"  "+ kra_1, str(round(k_srList[1],2))+"  "+ ksr_1,str(round(k_ndList[1],2))+"  "+ knd_1)
    table.insert('', 'end', iid=2, values=tuple2)

    tuple3 = ('Operational',str(round(k_raList[2],2)) +"  "+ kra_2, str(round(k_srList[2],2))+"  "+ ksr_2,str(round(k_ndList[2],2))+"  "+ knd_2)
    table.insert('', 'end', iid=3, values=tuple3)

    tuple4 = ('Compliance',str(round(k_raList[3],2)) +"  "+ kra_3, str(round(k_srList[3],2))+"  "+ ksr_3,str(round(k_ndList[3],2))+"  "+ knd_3)
    table.insert('', 'end', iid=4, values=tuple4)

    tuple5 = ('Technical',str(round(k_raList[4],2)) +"  "+ kra_4, str(round(k_srList[4],2))+"  "+ ksr_4,str(round(k_ndList[4],2))+"  "+ knd_4)
    table.insert('', 'end', iid=5, values=tuple5)



# Run Analyzer table
def buildtable(Quality_goal_not_met_Count,
    Credit_Count,
    Infrastructure_Count,
    Resource_Count,
    IP_Count,
    Brand_Count,
    Lawsuit_Count,
    Inefficient_process_Count,
    Ineffective_process_Count,
    Ineffective_KPI_Count,
    Country_Count,
    Health_and_Safety_Count,
    ESD_Count,
    Limitations_Count,
    International_standard_Count,
    Testability_Count,
    Performance_Count,
    Reliability_Count,
    Availability_Count,
    Scalability_Count,
    Security_Count,
    Maintainability_Count,
    con,
    numberOfRaters,
    numberOfRisks,
    array1,
    prob_rel,
    imp_rel,
    prof_rel,
    app):

    plt1 = platform.system()

    app.geometry('1050x600')
    app.resizable(False, False)
    #app.configure(bg= 'gray100')
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    style = ttk.Style(app)
    style.theme_use('alt')
    sortable = tk.BooleanVar(app, False)
    drag_row = tk.BooleanVar(app, False)
    drag_col = tk.BooleanVar(app, False)

    columns = ["Risk Type", "Risk Name", "# Votes", "Consensus Lvl"]
    table = Table(app, columns=columns, sortable=sortable.get(), drag_cols=drag_col.get(),
                  drag_rows=drag_row.get(), height=6)

    table.grid(row=0, column= 0, columnspan=5)

    for col in columns:
        table.heading(col, anchor= 'c' ,text=col)
        table.column(col, width=100, anchor= 'c' ,stretch=True)

    #fills the table with data:  (1 tuple --> 1 line)

    if (Quality_goal_not_met_Count/numberOfRaters) >= con:
        tuple1= ('Strategic Risk', 'Quality Goal not Met', Quality_goal_not_met_Count,
                 f'{round((Quality_goal_not_met_Count/numberOfRaters)*100)}%')
        table.insert('', 'end', iid = 1 , values=tuple1)
    if Credit_Count / numberOfRaters >= con:
        tuple2 = ('Strategic Risk', 'Impact on Credit', Credit_Count,
                  f'{round((Credit_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=2, values=tuple2)
    if Infrastructure_Count / numberOfRaters >= con:
        tuple3 = ('Strategic Risk', 'Impact on Infrastructures Availability', Infrastructure_Count,
                  f'{round((Infrastructure_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=3, values=tuple3)
    if Resource_Count / numberOfRaters >= con:
        tuple4 = ('Strategic Risk', 'Impact on Resources and Headcount', Resource_Count,
                  f'{round((Resource_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=4, values=tuple4)
    if IP_Count / numberOfRaters >= con:
        tuple5 = ('Operational Risk (LEGAL)', 'Intellectual Property', IP_Count,
                  f'{round((IP_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=5, values=tuple5)
    if Brand_Count / numberOfRaters >= con:
        tuple6 = ('Operational Risk (LEGAL)', 'Brand Protection and Reputation', Brand_Count,
                  f'{round((Brand_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=6, values=tuple6)
    if Lawsuit_Count / numberOfRaters >= con:
        tuple7 = ('Operational Risk (LEGAL)', 'Potential Lawsuit', Lawsuit_Count,
                  f'{round((Lawsuit_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=7, values=tuple7)
    if Inefficient_process_Count / numberOfRaters >= con:
        tuple8 = ('Operational Risk', 'Inefficient Process', Inefficient_process_Count,
                  f'{round((Inefficient_process_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=8, values=tuple8)
    if Ineffective_process_Count / numberOfRaters >= con:
        tuple9 = ('Operational Risk', 'Ineffective Process', Ineffective_process_Count,
                  f'{round((Ineffective_process_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=9, values=tuple9)
    if Ineffective_KPI_Count / numberOfRaters >= con:
        tuple10 = ('Operational Risk', 'Ineffective KPI', Ineffective_KPI_Count,
                  f'{round((Ineffective_KPI_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=10, values=tuple10)
    if Country_Count / numberOfRaters >= con:
        tuple11 = ('Compliance Risk', 'Ability to Sell in Specific Countries', Country_Count,
                   f'{round((Country_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=11, values=tuple11)
    if Health_and_Safety_Count / numberOfRaters >= con:
        tuple12 = ('Compliance Risk', 'Health and Safety', Health_and_Safety_Count,
                   f'{round((Health_and_Safety_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=12, values=tuple12)
    if ESD_Count / numberOfRaters >= con:
        tuple13 = ('Compliance Risk', 'Electrostatic Discharge (ESD)', ESD_Count,
                   f'{round((ESD_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=13, values=tuple13)
    if Limitations_Count / numberOfRaters >= con:
        tuple14 = ('Compliance Risk', 'Product/Service Limitations', Limitations_Count,
                   f'{round((Limitations_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=14, values=tuple14)
    if International_standard_Count / numberOfRaters >= con:
        tuple15 = ('Compliance Risk', 'International Standard', International_standard_Count,
                   f'{round((International_standard_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=15, values=tuple15)
    if Testability_Count / numberOfRaters >= con:
        tuple16 = ('Technical Risk', 'Testability', Testability_Count,
                   f'{round((Testability_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=16, values=tuple16)
    if Performance_Count / numberOfRaters >= con:
        tuple17 = ('Technical Risk', 'Performance', Performance_Count,
                   f'{round((Performance_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=17, values=tuple17)
    if Reliability_Count / numberOfRaters >= con:
        tuple18 = ('Technical Risk', 'Reliability', Reliability_Count,
                   f'{round((Reliability_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=18, values=tuple18)
    if Availability_Count / numberOfRaters >= con:
        tuple19 = ('Technical Risk', 'Availability', Availability_Count,
                   f'{round((Availability_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=19, values=tuple19)
    if Scalability_Count / numberOfRaters >= con:
        tuple20 = ('Technical Risk', 'Scalability', Scalability_Count,
                   f'{round((Scalability_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=20, values=tuple20)
    if Security_Count / numberOfRaters >= con:
        tuple21 = ('Technical Risk', 'Security', Security_Count,
                   f'{round((Security_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=21, values=tuple21)
    if Maintainability_Count / numberOfRaters >= con:
        tuple22 = ('Technical Risk', 'Maintainability', Maintainability_Count,
                   f'{round((Maintainability_Count / numberOfRaters) * 100)}%')
        table.insert('', 'end', iid=22, values=tuple22)



    #vuota = tk.Label(app, text='', anchor="w").grid(row=2, column=0)
    canvas_width = 340
    canvas_height = 240

    #first gauge.
    cnvs = tk.Canvas(app, width=canvas_width, height=canvas_height)
    cnvs.grid(row=1, column=1)

    background = cnvs.create_rectangle(10, 0, 400, 400, fill="gray100", outline="gray100")
    coord = 10, 50, 350, 350  # define the size of the gauge

    low_r = '0%'  # chart low range
    hi_r = '100%'  # chart hi range

    # add hi/low bands
    # red starts at 0%, ends at 40%
    # yellow starts at 40%, ends at 60%
    # green starts at 60%, ends 100%
    start_prob_bar = 135 - (90 * prob_rel / 100)

    cnvs.create_arc(coord, start=45, extent=90, outline="gray75", style="arc", width=20)
    cnvs.create_arc(coord, start=45, extent=55, outline="gray60", style="arc", width=20)
    cnvs.create_arc(coord, start=45, extent=37, outline="gray45", style="arc", width=20)

    # Formula to calculate pointer position:
    # 135 - (90 * percentage) . Example to represent 10% of votes:   135-(90*0.6)=81
    start_prob_needle = 135 - (90*prob_rel/100)
    id_needle = cnvs.create_arc(coord, start=start_prob_needle, extent=1, width=2)

    # added
    hide_needle = cnvs.create_rectangle(100,100,250,200, fill= "gray100", outline= "gray100")

    id_text = cnvs.create_text(180, 110, font="Times 12 bold", )

    cnvs.itemconfig(id_text, text="Support to mean  " + str(prob_rel) + "%")

    cnvs.create_text(90, 190, font='Times 8',  text= "Rare    Possible   Probable")
    cnvs.create_text(80, 210, font='Times 8', text="1--------2--------3")

    cnvs.create_text(270, 195, font="Times 9", text=f"Mean: {array1[0,0]}", fill="black")
    cnvs.create_text(270, 210, font="Times 9", text=f"Mode: {array1[0,1]}", fill="black")
    cnvs.create_text(270, 225, font="Times 9", text=f"St.Dev.: {array1[0,2]}", fill="black")
    # Add some labels


    if round(array1[0,0]) <= 1:
        cnvs.create_text(180, 150, font="Times 14 bold", text="Probability: Rare", fill="black")
        circleBG = cnvs.create_oval(47, 140, 67, 160, fill="green", outline="black")
    elif round(array1[0,0]) == 2:
        cnvs.create_text(180, 150, font="Times 14 bold", text="Probability: Possible", fill="black")
        circleBG = cnvs.create_oval(47, 140, 67, 160, fill="yellow", outline="black")
    else:
        cnvs.create_text(180, 150, font="Times 14 bold", text="Probability: Probable", fill="black")
        circleBG = cnvs.create_oval(47, 140, 67, 160, fill="red", outline="black")

    if plt1 == "Windows":
        myTip = Hovertip(cnvs, 'Support to mean: percentage of votes given to the value corresponding to the rounded mean')
    cnvs.create_text(60, 110, font="Times 10 bold", text=low_r)
    cnvs.create_text(310, 110, font="Times 10 bold", text=hi_r)

    # second gauge
    cnvs1 = tk.Canvas(app, width=canvas_width, height=canvas_height)
    cnvs1.grid(row=1, column=2)
    background1 = cnvs1.create_rectangle(10, 0, 400, 400, fill="gray100", outline="gray100")

    cnvs1.create_arc(coord, start=45, extent=90, outline="gray75", style="arc", width=20)
    cnvs1.create_arc(coord, start=45, extent=55, outline="gray60", style="arc", width=20)
    cnvs1.create_arc(coord, start=45, extent=37, outline="gray45", style="arc", width=20)

    # add needle/value pointer FRECCIA
    # 150 = 0%  180-30
    # 90 = 50 %
    # 30 = 100%
    # Formula to calculate pointer position:
    # 135 - (90 * percentage) . Example to represent 10% of votes:   135-(90*0.6)=81
    start_imp_needle = 135 - (90 * imp_rel / 100)
    id_needle1 = cnvs1.create_arc(coord, start=start_imp_needle, extent=1, width=2)
    # added

    hide_needle1 = cnvs1.create_rectangle(100, 100, 250, 200, fill="gray100", outline="gray100")

    id_text1 = cnvs1.create_text(180, 110, font="Times 12 bold" )

    cnvs1.itemconfig(id_text1, text="Support to mean  " + str(imp_rel) + "%")

    cnvs1.create_text(90, 190, font='Times 8', text="Low    Medium   High")
    cnvs1.create_text(90, 210, font='Times 8', text="1--------2--------3")

    cnvs1.create_text(270, 195, font="Times 9", text=f"Mean: {array1[1,0]}", fill="black")
    cnvs1.create_text(270, 210, font="Times 9", text=f"Mode: {array1[1, 1]}", fill="black")
    cnvs1.create_text(270, 225, font="Times 9", text=f"St.Dev.: {array1[1, 2]}", fill="black")

    if round(array1[1,0]) <= 1:
        cnvs1.create_text(180, 150, font="Times 14 bold", text="Impact: Low", fill="black")
        circleBG1 = cnvs1.create_oval(47, 140, 67, 160, fill="green", outline="black")
    elif round(array1[1,0]) == 2:
        cnvs1.create_text(180, 150, font="Times 14 bold", text="Impact: Medium", fill="black")
        circleBG1 = cnvs1.create_oval(47, 140, 67, 160, fill="yellow", outline="black")
    else:
        cnvs1.create_text(180, 150, font="Times 14 bold", text="Impact: High", fill="black" )
        circleBG1 = cnvs1.create_oval(47, 140, 67, 160, fill="red", outline="black")

    if plt1 == "Windows":
        myTip1 = Hovertip(cnvs1, 'Support to mean: percentage of votes given to the value corresponding to the rounded mean')
    cnvs1.create_text(60, 110, font="Times 10 bold", text=low_r)
    cnvs1.create_text(310, 110, font="Times 10 bold", text=hi_r)
###third gauge
    cnvs2 = tk.Canvas(app, width=canvas_width, height=canvas_height)
    cnvs2.grid(row=1, column=3)
    background2 = cnvs2.create_rectangle(10, 0, 400, 400, fill="gray100", outline="gray100")

    cnvs2.create_arc(coord, start=45, extent=90, outline="gray75", style="arc", width=20)
    cnvs2.create_arc(coord, start=45, extent=55, outline="gray60", style="arc", width=20)
    cnvs2.create_arc(coord, start=45, extent=37, outline="gray45", style="arc", width=20)


    # add needle/value pointer FRECCIA
    # 150 = 0%  180-30
    # 90 = 50 %
    # 30 = 100%
    # Formula to calculate pointer position:
    # 135 - (90 * percentage) . Example to represent 10% of votes:   135-(90*0.6)=81
    start_prof_needle = 135 - (90 * prof_rel / 100)
    id_needle2 = cnvs2.create_arc(coord, start=start_prof_needle, extent=1, width=2)

    # added

    hide_needle2 = cnvs2.create_rectangle(100, 100, 250, 200, fill="gray100", outline="gray100")
    id_text2 = cnvs2.create_text(180, 110, font="Times 12 bold" )

    cnvs2.itemconfig(id_text2, text="Support to mean  " + str(prof_rel) + "%")

    cnvs2.create_text(120, 190, font='Times 8', text="Constant  Logarithmic  Linear  Exponential")
    cnvs2.create_text(120, 210, font='Times 8', text="1------------2------------3------------4")

    cnvs2.create_text(270, 195, font="Times 9", text=f"Mean: {array1[2, 0]}", fill="black")
    cnvs2.create_text(270, 210, font="Times 9", text=f"Mode: {array1[2, 1]}", fill="black")
    cnvs2.create_text(270, 225, font="Times 9", text=f"St.Dev.: {array1[2, 2]}", fill="black")

    # Add some labels

    # buttonTXT = cnvs.create_text(50, 15, text="Probable")
    if round(array1[2,0]) <= 1:
        cnvs2.create_text(180, 150, font="Times 14 bold", text="Cost Profile: Constant", fill="black")
        circleBG2 = cnvs2.create_oval(47, 140, 67, 160, fill="green", outline="black")
    elif round(array1[2,0]) == 2:
        cnvs2.create_text(180, 150, font="Times 14 bold", text="Cost Profile: Logarithmic", fill="black")
        circleBG2 = cnvs2.create_oval(47, 140, 67, 160, fill="yellow", outline="black")
    elif round(array1[2,0]) == 3:
        cnvs2.create_text(180, 150, font="Times 14 bold", text="Cost Profile: Linear", fill="black")
        circleBG2 = cnvs2.create_oval(47, 140, 67, 160, fill="orange", outline="black")
    else:
        cnvs2.create_text(180, 150, font="Times 14 bold", text="Cost Profile: Exponential", fill="black")
        circleBG2 = cnvs2.create_oval(47, 140, 67, 160, fill="red", outline="black")

    if plt1 == "Windows":
        myTip2 = Hovertip(cnvs2, 'Support to mean: percentage of votes given to the value corresponding to the rounded mean')
    cnvs2.create_text(60, 110, font="Times 10 bold", text=low_r)
    cnvs2.create_text(310, 110, font="Times 10 bold", text=hi_r)

    # add scrollbars
    sx = tk.Scrollbar(app, orient='horizontal', command=table.xview)
    sy = tk.Scrollbar(app, orient='vertical', command=table.yview)
    table.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

    table.grid(sticky='ewns')
    #sx.grid(row=1, column=0, sticky='ew')
    #sy.grid(row=0, column=1, sticky='ns')
    app.update_idletasks()