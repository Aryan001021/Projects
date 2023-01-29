from tkinter import *
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import markers


class photo:
    def __init__(self,dirtory,wedthw,heighth,canvas,sizex,sizey):
        self.l=wedthw
        self.w=heighth
        self.a=Image.open(f"image/{dirtory}")
        self.size=self.a.resize((sizex,sizey))
        self.try1=ImageTk.PhotoImage(self.size)
        self.draw=canvas.create_image(self.l,self.w,image=self.try1)


class btn:
    def __init__(self,axis,colorn,voltage,ampere,frequency):
        self.on=False
        self.clrns=colorn
        self.btn=Button(win,text=f"{colorn} light",bg=f"{colorn}",font="bold ",fg="Black",bd=7,command=self.clrs)
        self.btn.place(x=axis,y=height-47,height=50,width=130)
        self.volt=voltage
        self.amp=ampere
        self.freq=frequency
        
    def clrs(self):
        global is_on,vmtrtxt,gmtrtxt,freq1,amapa
        if is_on==False:
            self.on=True
            vmtrtxt=self.volt
            labelpmtr.config(text=f"{vmtrtxt}")
            amapa=self.amp
            gmtrtxt=amapa
            labelgmtr.config(text=f"{gmtrtxt}")
            #implement frequency and ampere
            freq1=self.freq
            
            self.pic=photo(f'{self.clrns} light.png',width/2-70,550,canvas,200,200)
            

#functions
def vmeterleft():
    global is_on,vmtrtxt,gmtrtxt
    if is_on==False:
        vmtrtxt-=0.01
        labelpmtr.config(text=f"{round(vmtrtxt,3)}")
        gmtrtxt-=0.02
        labelgmtr.config(text=f"{round(gmtrtxt,3)}")       


def vmeterright():
    global is_on,vmtrtxt,gmtrtxt
    if is_on==False:
        vmtrtxt+=0.01
        gmtrtxt+=0.02
        labelgmtr.config(text=f"{round(gmtrtxt,3)}")
        labelpmtr.config(text=f"{round(vmtrtxt,3)}")
def calu():
    cal=Tk()

    cal.config(background="light green")
    Label1=Label(cal,text="h(Plank's constant)=e x Delta(v)/delta(frequency)",font="14",background="light green").pack()
    sumv=0
    sumf=0
    for i in range(len(lstf)):
        sumv+=lstv[i]
        sumf+=lstf[i]
    sumv=sumv
    matha=(sumv/sumf)*10
    trail=1.6*(sumv/sumf)
    labe=Label(cal,text="e=1.6x10^-19",font="14",background="light green").pack()
    labv=Label(cal,text=f"Delta(v)={sumv}",font="14",background="light green").pack()
    labf=Label(cal,text=f"delta(frequency)={sumf}x10^-14",font="14",background="light green").pack()
    label2=Label(cal,text=f"h=(1.6x10^-19)x{sumv}/({sumf}x10^-14)",font="14",background="light green").pack()

    label3=Label(cal,text=f"h={round(trail*10,2)}x10^-34 joule second",font="14",background="light green").pack()

    cal.mainloop()


def graph():
    try:
        win.destroy()
        
        x = np.array(lstf)
        y = np.array(lstv)
        plt.plot(x, y)
        lst1=[4.3,6.8,5.1,7.4,5.4]
        use=[]
        clr=["r","b","y","m","g"]
        for i in range(len(lstf)):
            for j in range(len(lst1)):
                if lst1[j]==lstf[i]:
                    use.append(clr[j])
                    break
        for i in range(len(lstv)):
            plt.plot(x[i],y[i],marker='o',color=use[i])
        plt.xlabel("frequency in 10**-14")
        plt.ylabel("voltage")
        plt.title("Graph")
        plt.show() 
        calu()  
    except Exception as e:
        print(e)
        x = np.array(lstf)
        y = np.array(lstv)
        plt.plot(x, y)
        plt.xlabel("frequency in 10**-14")
        plt.ylabel("voltage")
        plt.title("Graph")
        plt.show()    

   

def set_value():
    global is_on
    if is_on==False:
        lstv.append(-vmtrtxt)
        lstf.append(freq1)


def switch():
    global is_on,vmtrtxt,gmtrtxt  
    if is_on:
        vmtrtxt=0
        gmtrtxt=0
        labelgmtr.config(text=f"{gmtrtxt}")
        labelpmtr.config(text=f"{vmtrtxt}")
        button1.config(image=image1a)
        is_on=False
    
    elif is_on==False:
            vmtrtxt=" "
            gmtrtxt=" "
            labelgmtr.config(text=f"{gmtrtxt}")
            labelpmtr.config(text=f"{vmtrtxt}")
            button1.config(image=image2a)
            is_on=True
            
            if red.on==True:
                canvas.delete(red.pic.draw)
                red.on=False
            
            if blue.on==True:
                canvas.delete(blue.pic.draw)
                blue.on=False
            
            if green.on==True:
                canvas.delete(green.pic.draw)
                green.on=False
            
            if violet.on==True:
                canvas.delete(violet.pic.draw)
                violet.on=False
            
            if yellow.on==True:
                canvas.delete(yellow.pic.draw)
                yellow.on=False


#visual
win=Tk()

#width,height = win.winfo_screenwidth(), win.winfo_screenheight()
width,height =1366,768
win.geometry(f"{width}x{height}+0+0")
win.resizable(False, False)
win.config(bg="black")
canvas=Canvas(win,height=height-54,width=width,bg='light green')


#wires
canvas.create_line(1240,50,640,50, fill="black", width=5)
canvas.create_line(1240,50,1240,450, fill="black", width=5)
canvas.create_line(93,50,640,50, fill="red", width=5)
canvas.create_line(95,50,95,493, fill="red", width=5)
canvas.create_line(190,490,95,490, fill="red", width=5)
canvas.create_line(190,368,190,660, fill="red", width=5)
canvas.create_line(190,370,400,370, fill="red", width=5)
canvas.create_line(188,660,410,660, fill="red", width=5)
canvas.create_line(410,651,410,663, fill="red", width=9)
canvas.create_line(950,660,456,660, fill="black", width=5)
canvas.create_line(950,370,458,370, fill="black", width=5)
canvas.create_line(950,368,950,663, fill="black", width=5)
canvas.create_line(1100,450,1243,450, fill="black", width=5)
canvas.create_line(1100,450,953,450, fill="red", width=5)


#Switch
image1=Image.open("image/switchon.png")
image1b=image1.resize((80,150))
image1a=ImageTk.PhotoImage(image=image1b)
image2=Image.open("image/switchoff.png")
image2b=image2.resize((80,150))
image2a=ImageTk.PhotoImage(image=image2b)
is_on=True
button1=Button(canvas,image=image2a,command=switch,bg='brown',bd=0)
button1.place(x=width*3/4+200,y=30)


#labels for vmeter and gmeter
gmtrx,gmtry=width*2/3+200,400
vmtrx,vmtry=width*1/4+100,310
vmtrtxt=" "
gmtrtxt=" "
labelgmtr=Label(canvas,text=f'{vmtrtxt}')
labelpmtr=Label(canvas,text=f'{gmtrtxt}')
labelgmtr.place(x=gmtrx-48,y=gmtry+78,height=35,width=100)
labelpmtr.place(x=vmtrx-53,y=vmtry+88,height=35,width=100)
vmtrlow=Button(text="◄",font="bold",bd=7,command=vmeterleft).place(x=vmtrx-73,y=vmtry+88,height=35)
vmtrhigh=Button(text="►",font="bold",bd=7,command=vmeterright).place(x=vmtrx+47,y=vmtry+88,height=35)

#here graph and value system
lstv=[]
lstf=[]

#place non changing pic here
battery=photo('battery.png',width/2,70,canvas,330,150)
galmetr=photo('galvanmeter.png',gmtrx,gmtry,canvas,200,200)
pecell=photo('pecell.png',width/2-200,580,canvas,200,200)
pot_metr=photo('pot_meter.png',vmtrx,vmtry,canvas,200,200)
torch=photo('torch.png',width/2+109,550-9,canvas,200,200)
canvas.place(x=0,y=0)
button_graph=Button(win,font="bold",text="Graph",bg="#AC7A56",fg="white",command=graph,bd=7)
button_graph.place(x=width-135,y=height-47,height=50,width=130)
button_value=Button(win,text="Record Value",font="bold",bg='#AC7A56',fg="white",command=set_value,bd=7)
button_value.place(x=width-269,y=height-47,height=50,width=130)

#create color button520-390-260-130-0
violet=btn(520,"Violet",0,2*(0.76),7.4)
blue=btn(390,"Blue",0,2*(0.61),6.8)
green=btn(260,"Green",0,2*(0.45),5.4)
yellow=btn(130,"Yellow",0,2*(0.25),5.1)
red=btn(0,"Red",0,2*(0.19),4.3)
win.mainloop()
