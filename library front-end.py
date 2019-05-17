from tkinter import *
import sys,time
import tkinter.messagebox
from tkinter import ttk
window = Tk()
window.title('图书馆占座系统')
sw = window.winfo_screenwidth() #屏幕宽度
sh = window.winfo_screenheight()   #屏幕高度
width = 800    #窗口宽
height = 600    #窗口高
stair = 1   #1层楼
#occTime = {2:45} #占座时间
'''
flag1 = False #占座状态  true为被占
flag2 = False #占座状态
flag3 = True #占座状态
flag4 = False #占座状态
'''
window.geometry('%dx%d+%d+%d' % (width, height, (sw-width)/2, (sh-height)/2))
times = Label(window, text='请输入时间', width=10, height=1, font=("Arial", 14))
times.place(x=0,y=5)

# sysDate = time.strftime("%Y-%m-%d")
sysYear = time.strftime("%Y")
sysMonth = time.strftime("%m")
sysDay = time.strftime("%d")
#年月日
sysYearText = Entry(window,width = 4)
sysYearText.insert ('end',sysYear )
sysYearText.place(x=100,y=0)
#sysYearText.config(state=DISABLED)
h1 = Label(window, text='-', width=1, height=1, font=("Arial", 12))
h1.place(x=150,y=5)
h2 = Label(window, text='-', width=1, height=1, font=("Arial", 12))
h2.place(x=190,y=5)
sysMonthText = Entry(window,width = 2)
sysMonthText.insert ('end',sysMonth )
sysMonthText.place(x=160,y=0)
sysDayText = Entry(window,width = 2)
sysDayText.insert ('end',sysDay )
sysDayText.place(x=200,y=0)

#课节
h3 = Label(window, text='第', width=1, height=1, font=("Arial", 12))
h3.place(x=290,y=5)
lesson = ttk.Combobox(window , width = 2)
lesson['value'] = (1,2,3,4,5)
lesson.current(0)
lesson.place(x='310',y = 0)
h4 = Label(window, text='节课', width=3, height=1, font=("Arial", 12))
h4.place(x=360,y=5)
#提交按钮
def get_value(year,mon,day,lesson,room_n):
    time=([int(year.get()),int(mon.get()),int(day.get())])
    lesson=lesson.get()
     
    num=(int(room_n.get()[0:1])-1) * 80 + (int(room_num.get()[1:3]) - 1) * 4
    num_list = [num+1,num+2,num+3,num+4]
    
    print(time,lesson,num_list)
    return time,lesson,num_list


submit = Button(window , text = "查询" , fg = 'green', activeforeground = 'blue',height = 1,width = 4,command=lambda:get_value(sysYearText,sysMonthText,sysDayText,lesson,room_num))
submit.place(x=400,y = 5)

#框架布局
frame_table = Frame(window,height = '500' , width = '600' , bg = 'Tan').place(x = 0,y=30)   #房间内
frame_room = Frame(window,height = '500' , width = '200',bg = 'coral').place(x = 600,y=30)    #房间号选择



def isOcc():
    return 0

table1 = Canvas ( frame_table, height = 150 , width = 200 , bg = 'Tan')
table1.place(x = 50 , y = 100)

table2 = Canvas ( frame_table, height = 150 , width = 200 , bg = 'tan')
table2.place(x = 350 , y = 100)

table3 = Canvas ( frame_table, height = 150 , width = 200 , bg = 'tan')
table3.place(x = 50 , y = 300)

table4 = Canvas ( frame_table, height = 150 , width = 200 , bg = 'tan')
table4.place(x = 350 , y = 300)

def OccTable():
   # global flag1,flag2,flag3,flag4,occTime
    occTime={table1:False,table2:False,table3:False,table4:True,2:45,3:30}
    flag1=occTime[table1]
    flag2=occTime[table2]
    flag3=occTime[table3]
    flag4=occTime[table4]
    
    if flag1 == False and 1 in occTime.keys():
        tableOccTime1 = Button(table1 , text='剩余'+str(occTime.get(1))+'分钟' , bg = 'orange', width = 10 , height = 3 , font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    elif flag1 == False and 1 not in occTime.keys():

        tableUnwanted1 = Button(table1 , text = '空闲可占' , width = 10 , height = 3 ,bg = 'green', font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    else:
        tableOcc1 = Label(table1 , text='已被占' , width = 10 , height = 3 , font=("Arial", 14) , bg = 'gray').place(x = 60 , y=20)

    if flag2 == False and 2 in occTime.keys():
        tableOccTime2 = Button(table2 , text='剩余'+str(occTime.get(2))+'分钟' , bg = 'orange', width = 10 , height = 3 , font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    elif flag2 == False and 2 not in occTime.keys():
        tableUnwanted2 = Button(table2 , text = '空闲可占' , width = 10 , height = 3 ,bg = 'green', font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    else:
        tableOcc2 = Label(table2 , text='已被占' , width = 10 , height = 3 , font=("Arial", 14) , bg = 'gray').place(x = 60 , y=20)

    if flag3 == False and 3 in occTime.keys():
        tableOccTime3 = Button(table3 , text='剩余'+str(occTime.get(3))+'分钟' , bg = 'orange', width = 10 , height = 3 , font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    elif flag3 == False and 3 not in occTime.keys():
        tableUnwanted3 = Button(table3 , text = '空闲可占' , width = 10 , height = 3 ,bg = 'green', font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    else:
        tableOcc3 = Label(table3 , text='已被占' , width = 10 , height = 3 , font=("Arial", 14) , bg = 'gray').place(x = 60 , y=20)

    if flag4 == False and 4 in occTime.keys():
        tableOccTime4 = Button(table4 , text='剩余'+str(occTime.get(4))+'分钟' , bg = 'orange', width = 10 , height = 3 , font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    elif flag4 == False and 4 not in occTime.keys():
        tableUnwanted4 = Button(table4 , text = '空闲可占' , width = 10 , height = 3 ,bg = 'green', font=("Arial", 14),command = isOcc).place(x = 60 , y=20)
    else:
        tableOcc4 = Label(table4 , text='已被占' , width = 10 , height = 3 , font=("Arial", 14) , bg = 'gray').place(x = 60 , y=20)



OccTable()
tableLabel1 = Label(table1, text='1号桌', width=10, height=1, font=("Arial", 14)).place(x = 60 , y = 100)
#tableOcc1 = Label(table1 , text='已被占' , width = 10 , height = 3 , font=("Arial", 14) , bg = 'gray').place(x = 60 , y=20)


tableLabel2 = Label(table2, text='2号桌', width=10, height=1, font=("Arial", 14)).place(x = 60 , y = 100)
#tableOcc2 = Label(table1 , text='已被占' , width = 10 , height = 3 , font=("Arial", 14) , bg = 'gray')

#tableOccTime = Button(table2 , text='剩余'+str(occTime)+'分钟' , bg = 'orange', width = 10 , height = 3 , font=("Arial", 14)).place(x = 60 , y=20)





#tableUnwanted = Button(table3 , text = '空闲可占' , width = 10 , height = 3 ,bg = 'green', font=("Arial", 14),command = isOcc).place(x = 60 , y=20)

#tableOcc3 = Label(table1 , text='已被占' , width = 10 , height = 3 , font=("Arial", 14) , bg = 'gray')
#tableOcc3.place(x = 60 , y=20)
tableLabel3 = Label(table3, text='3号桌', width=10, height=1, font=("Arial", 14))
tableLabel3.place(x = 60 , y = 100)



tableLabel4 = Label(table4, text='4号桌', width=10, height=1, font=("Arial", 14)).place(x = 60 , y = 100)



radioVar = StringVar()
def select_room():
    print(radioVar.get())

'''
def sel_room(*args):
    
    #num = int(room_num.get()[0:1]) * 100 + (int(room_num.get()[1:3]) - 1) * 4
    num=(int(room_num.get()[0:1])-1) * 80 + (int(room_num.get()[1:3]) - 1) * 4
    num_list = [num+1,num+2,num+3,num+4]
    #print(num_list)
'''
    
   

# radio1 = Radiobutton(frame_room ,value = '101', text = '101房间', variable = radioVar , command = select_room)
# radio1.place(x = 650 , y = 80)
# radio2 = Radiobutton(frame_room ,value = '102', text = '102房间', variable = radioVar , command = select_room)
# radio2.place(x = 650 , y = 180)
# radio3 = Radiobutton(frame_room ,value = '103', text = '103房间', variable = radioVar , command = select_room)
# radio3.place(x = 650 , y = 280)
# radio4 = Radiobutton(frame_room ,value = '104', text = '104房间', variable = radioVar , command = select_room)
# radio4.place(x = 650, y = 380)
# radio5 = Radiobutton(frame_room ,value = '105', text = '105房间', variable = radioVar , command = select_room)
# radio5.place(x = 650 , y = 480)
h5 = Label(window, text='请选择房间：', width=10, height=2, font=("Arial", 12))
h5.place(x = 650 , y = 100)

room_num = ttk.Combobox(frame_room , width = 6)
room_num.place(x = 650 , y = 150)
room_num['value'] = ('101房间','102房间','103房间','104房间','105房间','106房间','107房间','108房间','109房间','110房间'
                   , '111房间','112房间','113房间','114房间','115房间','116房间','117房间','118房间','119房间','120房间')

room_num.current(0)
#room_num.bind("<<ComboboxSelected>>",sel_room)



def go_upstairs(up):
    global stair

    if up == 1:
        if stair == 5:
            tkinter.messagebox.showwarning('错误','已经是最高层了')
        else:
            global radio1
            stair +=1
            print('stair',stair)
            room_num['value'] = (str(stair)+'01房间', str(stair)+'02房间', str(stair)+'03房间', str(stair)+'04房间', str(stair)+'05房间', str(stair)+'06房间', str(stair)+'07房间'
                               , str(stair)+'08房间', str(stair)+'09房间', str(stair)+'10房间', str(stair)+'11房间', str(stair)+'12房间', str(stair)+'13房间', str(stair)+'14房间'
                               , str(stair)+'15房间', str(stair)+'16房间', str(stair)+'17房间', str(stair)+'18房间', str(stair)+'19房间',str(stair)+'20房间')
            room_num.current(0)
            # radio1.config(text=str(stair)+'01房间')
            # radio1.config(value=str(stair)+'01')
            # radio2.config(text=str(stair)+'02房间')
            # radio2.config(value=str(stair)+'02')
            # radio3.config(text=str(stair)+'03房间')
            # radio3.config(value=str(stair)+'03')
            # radio4.config(text=str(stair)+'04房间')
            # radio4.config(value=str(stair)+'04')
            # radio5.config(text=str(stair)+'05房间')
            # radio5.config(value=str(stair)+'05')
    else:
        if stair == 1:
            tkinter.messagebox.showwarning('错误','已经是第一层了')
        else:
            stair -=1
            print('stair',stair)
            room_num['value'] = (str(stair) + '01房间', str(stair) + '02房间', str(stair) + '03房间', str(stair) + '04房间', str(stair) + '05房间',str(stair) + '06房间', str(stair) + '07房间'
                                , str(stair) + '08房间', str(stair) + '09房间', str(stair) + '10房间', str(stair) + '11房间', str(stair) + '12房间',str(stair) + '13房间', str(stair) + '14房间'
                                , str(stair) + '15房间', str(stair) + '16房间', str(stair) + '17房间', str(stair) + '18房间', str(stair) + '19房间',str(stair) + '20房间')
            room_num.current(0)
            # radio1.config(text=str(stair)+'01房间')
            # radio1.config(value=str(stair)+'01')
            # radio2.config(text=str(stair)+'02房间')
            # radio2.config(value=str(stair)+'02')
            # radio3.config(text=str(stair)+'03房间')
            # radio3.config(value=str(stair)+'03')
            # radio4.config(text=str(stair)+'04房间')
            # radio4.config(value=str(stair)+'04')
            # radio5.config(text=str(stair)+'05房间')
            # radio5.config(value=str(stair)+'05')


upButton = Button(window , text = '上楼' , command = lambda:go_upstairs(up = 1 )).place(x = 710 , y = 550)
downButton = Button(window , text = '下楼' , command = lambda:go_upstairs(up = 0 )).place(x = 750 , y = 550)



        






window.mainloop()