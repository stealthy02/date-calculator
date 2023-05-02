import tkinter as tk
from data import Date
from tkinter import messagebox
date= Date()
root=tk.Tk()#创建对象
root.geometry('240x270')#设计尺寸
root.title('日期计算')
menubar=tk.Menu(root)
#-------------------分割线-------------------
def clear():
    try:
        global window1
        window1.destroy()
    except:
        pass
    try:
        global window2
        window2.destroy()
    except:
        pass
    try:
        global window3
        window3.destroy()
    except:
        pass
    try:
        global window4
        window4.destroy()
    except:
        pass
def do_job1():
    clear()
    #global window1
    window1=tk.Frame(root, height=280, width=240, bg='pink')
    window1.place(x=0,y=30)
    today=tk.StringVar(value=f'今天是{date.today.year}年{date.today.month}月{date.today.day}日,{date.today_weekday}')#当前日期
    today_t=tk.Label(window1,textvariable=today,width=34,height=1)
    today_t.pack(side='top')
    #-------------------分割线-------------------
    list_n_hday=date.list_date_dif
    n_hday=tk.StringVar(value=f'距离下一个节日"{list_n_hday[0][0]}"还有{str(list_n_hday[0][1])}天')#下一个节日
    n_hday_fra=tk.Label(window1,textvariable=n_hday,width=34,height=2) #textvariable=var变动文本
    n_hday_fra.pack(side='top')
    hday_t=''
    for hday in list_n_hday[1:]:
        hday_t+='距离下个  "'+str(hday[0])+'"\t还有 '+str(hday[1])+'\t天\n'
    total_hday=tk.StringVar(value=hday_t)   
    hday_fra=tk.Label(window1,textvariable=total_hday,width=34,height=15,anchor="n",bg="white")
    hday_fra.pack()
def do_job2():
    clear()
    window2=tk.Frame(root, height=280, width=240)
    window2.place(x=0,y=30)
    def flunar_def():
        if flunar_b.cget('text')=='阳历':
            flunar_b.config(text="阴历")
        else:
            flunar_b.config(text="阳历")
    tk.Label(window2,text="两日期间隔时间",font=("楷体", 16)).place(x=40,y=10)
    t_dif=tk.StringVar()#构建变量储存两日期间隔天数
    tk.Label(window2,text="起始日期:").place(x=30,y=50)
    from_fra=tk.Entry(window2,width=10)#输入起始日期
    from_fra.place(x=100,y=50)
    flunar_b=tk.Button(window2,text='阳历',width=4,height=1,command=flunar_def)
    flunar_b.place(x=180,y=45)
    def tlunar_def():
        if tlunar_b.cget('text')=='阳历':
            tlunar_b.config(text="阴历")
        else:
            tlunar_b.config(text="阳历")
    tk.Label(window2,text="截止日期:").place(x=30,y=80)
    to_fra=tk.Entry(window2,width=10)#输入结束日期
    to_fra.place(x=100,y=80)
    def cal_dif():#计算量日期的差值
        flunar_bool=False
        tlunar_bool=False
        if flunar_b.cget('text')=='阴历':
            flunar_bool=True
        if tlunar_b.cget('text')=='阴历':
            tlunar_bool=True
        t_dif_data=date.cal_dif(from_fra.get(), to_fra.get(),flunar_bool,tlunar_bool)
        if t_dif_data!=None:
            t_dif.set(str(t_dif_data)+'天')#两日期的间隔
        else:
            t_dif.set("请输入正确格式")
    tlunar_b=tk.Button(window2,text='阳历',width=4,height=1,command=tlunar_def)
    tlunar_b.place(x=180,y=75)

    tk.Label(window2,text="时间间隔:").place(x=30,y=110)
    t_dif_fra=tk.Label(window2,textvariable=t_dif,width=12)#结果框
    t_dif_fra.place(x=90,y=110)

    t_dif_b=tk.Button(window2,text='确定',width=6,height=1,command=cal_dif)
    t_dif_b.place(x=100,y=140)
def do_job3():
    clear()
    window3=tk.Frame(root, height=280, width=240, )
    window3.place(x=0,y=30)
    def lunar_def():
        if lunar_b.cget('text')=='阳历':
            lunar_b.config(text="阴历")
        else:
            lunar_b.config(text="阳历")
    
    tk.Label(window3,text="距今时间",font=("楷体", 16)).place(x=70,y=10)
    to_inter=tk.StringVar()#构建变量储据今日有多少天
    weekday=tk.StringVar()#变量周几
    tk.Label(window3,text="起始日期:").place(x=30,y=60)
    date_fra=tk.Entry(window3,width=10)#输入日期
    date_fra.place(x=100,y=60)
    def to_inter_def():#计算量日期的差值
        if lunar_b.cget('text')=='阴历':
            new_date_obj=date.str_to_date(date_fra.get(),True)
            to_inter_data=date.today_interval(new_date_obj)
            weekday_data=date.myweekday(new_date_obj)
        else:
            new_date_obj=date.str_to_date(date_fra.get())
            to_inter_data=date.today_interval(new_date_obj)
            weekday_data=date.myweekday(new_date_obj)
        if to_inter_data!=None:
            weekday.set(weekday_data)
            to_inter.set(to_inter_data)#间隔
        else:
            to_inter.set("请输入正确格式")
    lunar_b=tk.Button(window3,text='阳历',width=4,height=1,command=lunar_def)
    lunar_b.place(x=180,y=55)
    tk.Label(window3,text="星期:").place(x=50,y=90)
    tk.Label(window3,text="时间间隔:").place(x=30,y=120)
    to_inter_fra=tk.Label(window3,textvariable=weekday,width=12)#周几
    to_inter_fra.place(x=90,y=90)
    to_inter_fra=tk.Label(window3,textvariable=to_inter,width=12)#结果框
    to_inter_fra.place(x=90,y=120)
    to_inter_b=tk.Button(window3,text='确定',width=4,height=1,command=to_inter_def)
    to_inter_b.place(x=100,y=160)
def do_job4():
    clear()
    window4=tk.Frame(root, height=280, width=240)
    window4.place(x=0,y=30)
    def lunar_def():#阴历阳历按钮转换
        if lunar_b.cget('text')=='阳历':
            lunar_b.config(text="阴历")
        else:
            lunar_b.config(text="阳历")
    tk.Label(window4,text="自定义节日",font=("楷体", 16)).place(x=50,y=5)
    def clear_def():
        try:
            with open("data.txt","w",encoding='UTF-8') as f:
                f.write('')
            tk.messagebox.showinfo(title='提示',message='清除成功')
        except:
            tk.messagebox.showwarning(title='警告',message='清除失败')
        global date
        date=Date()
        do_job4()
    tk.Button(window4,text='清空',width=4,height=1,command=clear_def).place(x=180,y=3)
    tk.Label(window4,text="日期:").place(x=50,y=45)
    date_fra=tk.Entry(window4,width=10)#输入日期
    date_fra.place(x=100,y=45)
    def resave_def():#写入文件
        global date
        if lunar_b.cget('text')=='阴历':
           Y_N=date.data_save(name=name_fra.get(),date=date_fra.get(),lunar=True)
           if not Y_N:
               tk.messagebox.showwarning(title='警告',message='录入失败')
           else:
               tk.messagebox.showinfo(title='提示',message='录入成功')
               date=Date()
        else:
            Y_N=date.data_save(name=name_fra.get(),date=date_fra.get())
            if not Y_N:
               tk.messagebox.showwarning(title='警告',message='录入失败')
            else:
               tk.messagebox.showinfo(title='提示',message='录入成功')
               date=Date()
               do_job4()
    lunar_b=tk.Button(window4,text='阳历',width=4,height=1,command=lunar_def)#阴历阳历按钮
    lunar_b.place(x=180,y=40)
    tk.Label(window4,text="节日名称:").place(x=26,y=70)
    name_fra=tk.Entry(window4,width=6)#输入名称
    name_fra.place(x=100,y=70)
    resave_b=tk.Button(window4,text='确定',width=4,height=1,command=resave_def)
    resave_b.place(x=180,y=70)
    try:
        with open("data.txt","r",encoding='UTF-8') as f:
            diy_hday_t=f.read()
        diy_hday_t=diy_hday_t.replace('&',"\t")         
    except: 
        diy_hday_t="无自定义节日"
    total_hday=tk.StringVar(value=diy_hday_t)     
    hday_fra=tk.Label(window4,textvariable=total_hday,width=34,height=15,anchor="n",bg="white")
    hday_fra.place(x=0,y=100)
    
# 创建顶部框架
top_frame = tk.Frame(root,height=50)
top_frame.pack(side="top", fill="x")
# 添加多个按钮
button1 = tk.Button(top_frame, text="主页",width=7,height=1, command=do_job1)
button1.pack(side="left")
button2 = tk.Button(top_frame, text="计算",width=7,height=1, command=do_job2)
button2.pack(side="left")
button3 = tk.Button(top_frame, text="距今",width=7,height=1, command=do_job3)
button3.pack(side="right")
button3 = tk.Button(top_frame, text="节日",width=7,height=1, command=do_job4)
button3.pack(side="right")
do_job1()
#-------------------分割线-------------------
root.mainloop()
