from tkinter import*
from tkinter import messagebox
from math import*
from PIL import Image, ImageTk
"""Ventana"""
def cal_K ():
    a= float(valor1.get())
    resultado1=(a)
    Vresultado1.config(text=resultado1)
    resultado2=(a*10)
    Vresultado2.config(text=resultado2)
    resultado3 = (a *100)
    Vresultado3.config(text=resultado3)
    resultado4 = (a *1000)
    Vresultado4.config(text=resultado4)
    resultado5 = (a *10000)
    Vresultado5.config(text=resultado5)
    resultado6 = (a *100000)
    Vresultado6.config(text=resultado6)
 
def cal_H():
    b= float(valor2.get())
    resultadoh1=(b/10)
    Vresultadoh1.config(text=resultadoh1)
    resultadoh2=(b)
    Vresultadoh2.config(text=resultadoh2)
    resultadoh3 = (b *10)
    Vresultadoh3.config(text=resultadoh3)
    resultadoh4 = (b *100)
    Vresultadoh4.config(text=resultadoh4)
    resultadoh5 = (b *1000)
    Vresultadoh5.config(text=resultadoh5)
    resultadoh6 = (b *10000)
    Vresultadoh6.config(text=resultadoh6)
def cal_D():
    c= float(valor3.get())
    resultadod1=(c/100)
    Vresultadod1.config(text=resultadod1)
    resultadod2=(c/10)
    Vresultadod2.config(text=resultadod2)
    resultadod3 = (c)
    Vresultadod3.config(text=resultadod3)
    resultadod4 = (c *10)
    Vresultadod4.config(text=resultadod4)
    resultadod5 = (c *100)
    Vresultadod5.config(text=resultadod5)
    resultadod6 = (c *1000)
    Vresultadod6.config(text=resultadod6)
 
def cal_M():
    d = float(valor4.get())
    resultadom1 = (d / 1000)
    Vresultadom1.config(text=resultadom1)
    resultadom2 = (d / 100)
    Vresultadom2.config(text=resultadom2)
    resultadom3 = (d/10)
    Vresultadom3.config(text=resultadom3)
    resultadom4 = (d)
    Vresultadom4.config(text=resultadom4)
    resultadom5 = (d * 10)
    Vresultadom5.config(text=resultadom5)
    resultadom6 = (d * 100)
    Vresultadom6.config(text=resultadom6)
 
def cal_De():
    e = float(valor5.get())
    resultadodc1 = (e / 100000)
    Vresultadodc1.config(text=resultadodc1)
    resultadodc2 = (e / 10000)
    Vresultadodc2.config(text=resultadodc2)
    resultadodc3 = (e/100)
    Vresultadodc3.config(text=resultadodc3)
    resultadodc4 = (e/10)
    Vresultadodc4.config(text=resultadodc4)
    resultadodc5 = (e)
    Vresultadodc5.config(text=resultadodc5)
    resultadodc6 = (e * 10)
    Vresultadodc6.config(text=resultadodc6)
 
def cal_Cm():
    f = float(valor6.get())
    resultadodcm1 = (f / 1000000)
    Vresultadodcm1.config(text=resultadodcm1)
    resultadodcm2 = (f / 100000)
    Vresultadodcm2.config(text=resultadodcm2)
    resultadodcm3 = (f / 1000)
    Vresultadodcm3.config(text=resultadodcm3)
    resultadodcm4 = (f / 100)
    Vresultadodcm4.config(text=resultadodcm4)
    resultadodcm5 = (f/10)
    Vresultadodcm5.config(text=resultadodcm5)
    resultadodcm6 = (f)
    Vresultadodcm6.config(text=resultadodcm6)
 
def limpiar():
    valor1.set(float())
    Vresultado1.place_forget()
    Vresultado2.place_forget()
    Vresultado3.place_forget()
    Vresultado4.place_forget()
    Vresultado5.place_forget()
    Vresultado6.place_forget()
    valor2.set(float())
    valor3.set(float())
    valor4.set(float())
    valor5.set(float())
    valor6.set(float())
 
 
def limpiargr():
    vgrados.set(float())
 
def calgrados():
    numero= float(vgrados.get())
    if valorRButton.get()==1:
        resultado=(numero)+273.15
    elif valorRButton.get()==2:
        resultado=((numero)*9/5)+32
    else:
        print("No ha seleccionado nada")
    resX.config(text=resultado)
    print("Resultado:", resultado)
 
ventanagril=Tk()
 
ventanagril.title("Conversor de unidades ") #title le da el nombre al programa
ventanagril.geometry("1000x600")
#ventanagril.configure(bg="#76D7C4")
 
#----------------------------------------------------Titulos-------------------------------------------------------------------
#-------------------------------------------------Titulo Principal-------------------------------------------------
titulo=Label(ventanagril, text="CONVERSOR DE UNIDADES", font=("Arial Bold", 18), fg="white", bg="#8F3A84")
titulo.place(x=350, y=10)
#-------------------------------------------------UNIDADES DE DISTANCIA-------------------------------------------------
titulo=Label(ventanagril, text="Unidades de distancia", font=("Arial Bold", 16), fg="black")
titulo.place(x=10, y=50)
#-------------------------------------------------UNIDADES DE GRADOS-------------------------------------------------
titulo=Label(ventanagril, text="Unidades de Temperatura", font=("Arial Bold", 16), fg="black")
titulo.place(x=350, y=50)
 
#-------------------------------------------ETIQUETAS----------------------------------------------
#-------------------------------------------UNIDADES DE DISTANCIA----------------------------------------------
 
kilometro=Label(ventanagril, text="Kilometro (Km)", font=("Arial Bold", 10), fg="blue")
kilometro.place(x=10, y=130)
hectometro=Label(ventanagril, text="Hectometro (Hm)", font=("Arial Bold", 10), fg="blue")
hectometro.place(x=10, y=160)
decametro=Label(ventanagril, text="Decametro (Dam)", font=("Arial Bold", 10), fg="blue")
decametro.place(x=10, y=190)
metro=Label(ventanagril, text="Metro (m)", font=("Arial Bold", 10), fg="blue")
metro.place(x=10, y=220)
decimetro=Label(ventanagril, text="Decimetro (dm)", font=("Arial Bold", 10), fg="blue")
decimetro.place(x=10, y=250)
centimetro=Label(ventanagril, text="Centimetro (cm)", font=("Arial Bold", 10), fg="blue")
centimetro.place(x=10, y=280)
#-------------------------------------------UNIDADES DE TEMPERATURA----------------------------------------------
celcius=Label(ventanagril, text="Celcius (°C)", font=("Arial Bold", 10), fg="black")
celcius.place(x=375, y=130)
 
#-----------------------------------------------KILOMETRO----------------------------------------------
Vresultado1=Label(ventanagril)
Vresultado1.place(x=240,  y=135)
Vresultado2=Label(ventanagril)
Vresultado2.place(x=240,  y=165)
Vresultado3=Label(ventanagril)
Vresultado3.place(x=240,  y=195)
Vresultado4=Label(ventanagril)
Vresultado4.place(x=240,  y=225)
Vresultado5=Label(ventanagril)
Vresultado5.place(x=240,  y=255)
Vresultado6=Label(ventanagril)
Vresultado6.place(x=240,  y=285)
 
#-----------------------------------------------HECTOMETRO----------------------------------------------
Vresultadoh1=Label(ventanagril)
Vresultadoh1.place(x=240,  y=135)
Vresultadoh2=Label(ventanagril)
Vresultadoh2.place(x=240,  y=165)
Vresultadoh3=Label(ventanagril)
Vresultadoh3.place(x=240,  y=195)
Vresultadoh4=Label(ventanagril)
Vresultadoh4.place(x=240,  y=225)
Vresultadoh5=Label(ventanagril)
Vresultadoh5.place(x=240,  y=255)
Vresultadoh6=Label(ventanagril)
Vresultadoh6.place(x=240,  y=285)
 
#-----------------------------------------------DECAMETRO----------------------------------------------
Vresultadod1=Label(ventanagril)
Vresultadod1.place(x=240,  y=135)
Vresultadod2=Label(ventanagril)
Vresultadod2.place(x=240,  y=165)
Vresultadod3=Label(ventanagril)
Vresultadod3.place(x=240,  y=195)
Vresultadod4=Label(ventanagril)
Vresultadod4.place(x=240,  y=225)
Vresultadod5=Label(ventanagril)
Vresultadod5.place(x=240,  y=255)
Vresultadod6=Label(ventanagril)
Vresultadod6.place(x=240,  y=285)
 
#-----------------------------------------------METRO----------------------------------------------
Vresultadom1=Label(ventanagril)
Vresultadom1.place(x=240,  y=135)
Vresultadom2=Label(ventanagril)
Vresultadom2.place(x=240,  y=165)
Vresultadom3=Label(ventanagril)
Vresultadom3.place(x=240,  y=195)
Vresultadom4=Label(ventanagril)
Vresultadom4.place(x=240,  y=225)
Vresultadom5=Label(ventanagril)
Vresultadom5.place(x=240,  y=255)
Vresultadom6=Label(ventanagril)
Vresultadom6.place(x=240,  y=285)
 
#-----------------------------------------------DECIMETRO----------------------------------------------
Vresultadodc1=Label(ventanagril)
Vresultadodc1.place(x=240,  y=135)
Vresultadodc2=Label(ventanagril)
Vresultadodc2.place(x=240,  y=165)
Vresultadodc3=Label(ventanagril)
Vresultadodc3.place(x=240,  y=195)
Vresultadodc4=Label(ventanagril)
Vresultadodc4.place(x=240,  y=225)
Vresultadodc5=Label(ventanagril)
Vresultadodc5.place(x=240,  y=255)
Vresultadodc6=Label(ventanagril)
Vresultadodc6.place(x=240,  y=285)
 
#-----------------------------------------------CENTIMETRO----------------------------------------------
Vresultadodcm1=Label(ventanagril)
Vresultadodcm1.place(x=240,  y=135)
Vresultadodcm2=Label(ventanagril)
Vresultadodcm2.place(x=240,  y=165)
Vresultadodcm3=Label(ventanagril)
Vresultadodcm3.place(x=240,  y=195)
Vresultadodcm4=Label(ventanagril)
Vresultadodcm4.place(x=240,  y=225)
Vresultadodcm5=Label(ventanagril)
Vresultadodcm5.place(x=240,  y=255)
Vresultadodcm6=Label(ventanagril)
Vresultadodcm6.place(x=240,  y=285)
#-----------------------------------------------CASILLAS--------------------------------------------------
valor1=DoubleVar() #DoubleVar permite ingresar cualquier valor decimal
casilla_kilometro=Entry(ventanagril, width=10, fg="#3A738F", bd=3, textvariable=valor1)
casilla_kilometro.place(x=140, y=130)
valor2=DoubleVar()
casilla_hectometro=Entry(ventanagril, width=10, fg="#3A738F", bd=3, textvariable=valor2) #el comando bd sirve para darle cierto sombreado a la casilla en los bordes
casilla_hectometro.place(x=140, y=160)
valor3=DoubleVar()
casilla_decametro=Entry(ventanagril, width=10, fg="#3A738F", bd=3, textvariable=valor3) #el comando bd sirve para darle cierto sombreado a la casilla en los bordes
casilla_decametro.place(x=140, y=190)
valor4=DoubleVar()
casilla_metro=Entry(ventanagril, width=10, fg="#3A738F", bd=3, textvariable=valor4) #el comando bd sirve para darle cierto sombreado a la casilla en los bordes
casilla_metro.place(x=140, y=220)
valor5=DoubleVar()
casilla_decimetro=Entry(ventanagril, width=10, fg="#3A738F", bd=3, textvariable=valor5) #el comando bd sirve para darle cierto sombreado a la casilla en los bordes
casilla_decimetro.place(x=140, y=250)
valor6=DoubleVar()
casilla_centimetro=Entry(ventanagril, width=10, fg="#3A738F", bd=3, textvariable=valor6) #el comando bd sirve para darle cierto sombreado a la casilla en los bordes
casilla_centimetro.place(x=140, y=280)
#-----------------------------------------------CASILLAS DE TEMPERATURA--------------------------------------------------
vgrados=DoubleVar()
casilla_grados=Entry(ventanagril, width=10, fg="#3A738F", bd=4, textvariable=vgrados)
casilla_grados.place(x=475, y=130)
#----------------------------------------------------RadioButton----------------------------------------------------
valorRButton=IntVar()
R1=Radiobutton(ventanagril, text="Kelvin (°K)",value=1, variable=valorRButton).place(x=375, y=170)
R2=Radiobutton(ventanagril, text="Fahrenheit (°F)",value=2, variable=valorRButton).place(x=375, y=200)
img = Image.open('convertir.png')
img = img.resize((23, 20), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
img2=Image.open('cleaner.png')
img2= img2.resize((23, 20), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img2= ImageTk.PhotoImage(img2)
 
#----------------------------------------------------BOTONES----------------------------------------------------
botonCal_K = Button (ventanagril,  image=img,compound="top", command = cal_K).place(x=200, y=130)
botonCal_H = Button (ventanagril,  image=img,compound="top", command = cal_H).place(x=200, y=160)
botonCal_D = Button (ventanagril,  image=img,compound="top", command = cal_D).place(x=200, y=190)
botonCal_M = Button (ventanagril,  image=img,compound="top", command = cal_M).place(x=200, y=220)
botonCal_Dc = Button (ventanagril,  image=img,compound="top", command = cal_De).place(x=200, y=250)
botonCal_Cm = Button (ventanagril,  image=img,compound="top", command = cal_Cm).place(x=200, y=280)
botonLimp = Button (ventanagril, image=img2,bd=3,compound="top", command = limpiar).place(x=100, y=310)
botonSalir= Button(ventanagril, text="SALIR", width=20,bd=3,font=("Arial Bold", 18), bg="red", fg="black", command=quit).place(x=500, y=520)
botonConv = Button (ventanagril, image=img,compound="top", font=("Arial Bold", 18),  command = calgrados).place(x=475, y=275)
botoncleaner = Button (ventanagril,image=img2,bd=3,compound="top", font=("Arial Bold", 18), command = limpiargr).place(x=525, y=275)
 
 
resX=Label(ventanagril, text="El resultado en grados aparecera aqui",font=("Arial Bold", 8))
resX.place(x=375, y=250)
ventanagril.mainloop()