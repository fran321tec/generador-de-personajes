import random
import pandas as pd
import tkinter as tk


caracteristicas = ["fuerza", 
                   "destreza", 
                   "constitución",
                   "inteligencia",
                   "sabiduria",
                   "carisma",
                   " "]

costospuntos={
    8:0,
    9:1,
    10:2,
    11:3,
    12:4,
    13:5,
    14:7,
    15:9,
}

chara = list(caracteristicas)

def conseguirpuntos():
    global puntosdecompra
    puntosdecompra = puntos.get()
    puntosl.config(text=puntosdecompra)
puntosdecompra = 0



caracteristicas_jugador = {}
Clases = r'datarol\clasesysubclasesDyD.csv'
CLASS = pd.read_csv(Clases)
razas = r'datarol\razasysubrazasdyd.csv'
RACE = pd.read_csv(razas)

cont = 0

def moddecar(a):
    if a == 10:
        return 0
    else:
        b = a -10
        c = b / 2
        return c

def compradepuntos(cantidaddepuntosgastados,puntajedecaracteristica,caracteristicaensi,nombredeboton):
        global puntosdecompra
        global caracteristicas_jugador
        global puntajedechara
        
        if caracteristicaensi in caracteristicas_jugador:

            cara = caracteristicas_jugador[caracteristicaensi]
    
        if caracteristicaensi in caracteristicas_jugador and cara > puntajedecaracteristica:
            caracteristicasenficha = caracteristicas_jugador[caracteristicaensi]

            nombredeboton2 = caracteristicaensi + str(caracteristicasenficha)

            nombredeboton3 = botonesvar[nombredeboton2]

            puntajedechara = caracteristicas_jugador[caracteristicaensi]
        
            restar = costospuntos[puntajedechara]
        
            res = restar - cantidaddepuntosgastados
        
            puntosdecompra = int(puntosdecompra) + res
            
            insertor(caracteristicaensi, puntajedecaracteristica)
            nombredeboton3.config(state="normal")
        elif caracteristicaensi in caracteristicas_jugador and cara == puntajedecaracteristica:
            insertor(caracteristicaensi, puntajedecaracteristica)
        elif caracteristicaensi in caracteristicas_jugador and cara < puntajedecaracteristica:
            
            puntajedechara = caracteristicas_jugador[caracteristicaensi]
        
            caracteristicasenficha = caracteristicas_jugador[caracteristicaensi]

            nombredeboton2 = caracteristicaensi + str(caracteristicasenficha)

            nombredeboton3 = botonesvar[nombredeboton2]

            puntajedechara = caracteristicas_jugador[caracteristicaensi]
        
            sumar=costospuntos[puntajedechara]
        
            res = cantidaddepuntosgastados - sumar
        
            puntosdecompra = int(puntosdecompra) - res
            
            insertor(caracteristicaensi,puntajedecaracteristica)
            nombredeboton3.config(state="normal")
        else:
            puntosdecompra = int(puntosdecompra) - cantidaddepuntosgastados
            insertor(caracteristicaensi, puntajedecaracteristica)
        puntosl.config(text=puntosdecompra)
        nombredeboton.config(state="disabled")


def ventanadepointbuy():
    global puntosl
    global puntos
    root_rol2 = tk.Tk()
    puntos = tk.Entry(root_rol2)
    puntos.insert(0,"27")
    sacarpuntos = tk.Button(root_rol2,text="acceptar", command=conseguirpuntos)
    puntosl = tk.Label(root_rol2,text=str(puntosdecompra))
    fuelabel = tk.Label(root_rol2,text="fuerza: ")
    deslabel = tk.Label(root_rol2,text="destreza: ")
    conlabel = tk.Label(root_rol2,text="constitucion: ")
    intlabel = tk.Label(root_rol2,text="inteligencia: ")
    sablabel = tk.Label(root_rol2,text="sabiduria: ")
    carlabel = tk.Label(root_rol2,text="carisma: ")

    fuerza8 = tk.Button(root_rol2,text="8",command=lambda: (compradepuntos(0,8,"fuerza",fuerza8)))
    fuerza9 = tk.Button(root_rol2,text="9",command=lambda: (compradepuntos(1,9,"fuerza",fuerza9)))
    fuerza10 = tk.Button(root_rol2,text="10",command=lambda: (compradepuntos(2,10,"fuerza",fuerza10)))
    fuerza11 = tk.Button(root_rol2,text="11",command=lambda: (compradepuntos(3,11,"fuerza",fuerza11)))
    fuerza12 = tk.Button(root_rol2,text="12",command=lambda: (compradepuntos(4,12,"fuerza",fuerza12)))
    fuerza13 = tk.Button(root_rol2,text="13",command=lambda: (compradepuntos(5,13,"fuerza",fuerza13)))
    fuerza14 = tk.Button(root_rol2,text="14",command=lambda: (compradepuntos(7,14,"fuerza",fuerza14)))
    fuerza15 = tk.Button(root_rol2,text="15",command=lambda: (compradepuntos(9,15,"fuerza",fuerza15)))

    destreza8 = tk.Button(root_rol2,text="8",command=lambda: (compradepuntos(0,8,"destreza",destreza8)))
    destreza9 = tk.Button(root_rol2,text="9",command=lambda: (compradepuntos(1,9,"destreza",destreza9)))
    destreza10 = tk.Button(root_rol2,text="10",command=lambda: (compradepuntos(2,10,"destreza",destreza10)))
    destreza11 = tk.Button(root_rol2,text="11",command=lambda: (compradepuntos(3,11,"destreza",destreza11)))
    destreza12 = tk.Button(root_rol2,text="12",command=lambda: (compradepuntos(4,12,"destreza",destreza12)))
    destreza13 = tk.Button(root_rol2,text="13",command=lambda: (compradepuntos(5,13,"destreza",destreza13)))
    destreza14 = tk.Button(root_rol2,text="14",command=lambda: (compradepuntos(7,14,"destreza",destreza14)))
    destreza15 = tk.Button(root_rol2,text="15",command=lambda: (compradepuntos(9,15,"destreza",destreza15)))

    constitucion8 = tk.Button(root_rol2,text="8",command=lambda: (compradepuntos(0,8,"constitucion",constitucion8)))
    constitucion9 = tk.Button(root_rol2,text="9",command=lambda: (compradepuntos(1,9,"constitucion",constitucion9)))
    constitucion10 = tk.Button(root_rol2,text="10",command=lambda: (compradepuntos(2,10,"constitucion",constitucion10)))
    constitucion11 = tk.Button(root_rol2,text="11",command=lambda: (compradepuntos(3,11,"constitucion",constitucion11)))
    constitucion12 = tk.Button(root_rol2,text="12",command=lambda: (compradepuntos(4,12,"constitucion",constitucion12)))
    constitucion13 = tk.Button(root_rol2,text="13",command=lambda: (compradepuntos(5,13,"constitucion",constitucion13)))
    constitucion14 = tk.Button(root_rol2,text="14",command=lambda: (compradepuntos(7,14,"constitucion",constitucion14)))
    constitucion15 = tk.Button(root_rol2,text="15",command=lambda: (compradepuntos(9,15,"constitucion",constitucion15)))

    inteligencia8 = tk.Button(root_rol2,text="8",command=lambda: (compradepuntos(0,8,"inteligencia",inteligencia8)))
    inteligencia9 = tk.Button(root_rol2,text="9",command=lambda: (compradepuntos(1,9,"inteligencia",inteligencia9)))
    inteligencia10 = tk.Button(root_rol2,text="10",command=lambda: (compradepuntos(2,10,"inteligencia",inteligencia10)))
    inteligencia11 = tk.Button(root_rol2,text="11",command=lambda: (compradepuntos(3,11,"inteligencia",inteligencia11)))
    inteligencia12 = tk.Button(root_rol2,text="12",command=lambda: (compradepuntos(4,12,"inteligencia",inteligencia12)))
    inteligencia13 = tk.Button(root_rol2,text="13",command=lambda: (compradepuntos(5,13,"inteligencia",inteligencia13)))
    inteligencia14 = tk.Button(root_rol2,text="14",command=lambda: (compradepuntos(7,14,"inteligencia",inteligencia14)))
    inteligencia15 = tk.Button(root_rol2,text="15",command=lambda: (compradepuntos(9,15,"inteligencia",inteligencia15)))

    sabiduria8 = tk.Button(root_rol2,text="8",command=lambda: (compradepuntos(0,8,"sabiduria",sabiduria8)))
    sabiduria9 = tk.Button(root_rol2,text="9",command=lambda: (compradepuntos(1,9,"sabiduria",sabiduria9)))
    sabiduria10 = tk.Button(root_rol2,text="10",command=lambda: (compradepuntos(2,10,"sabiduria",sabiduria10)))
    sabiduria11 = tk.Button(root_rol2,text="11",command=lambda: (compradepuntos(3,11,"sabiduria",sabiduria11)))
    sabiduria12 = tk.Button(root_rol2,text="12",command=lambda: (compradepuntos(4,12,"sabiduria",sabiduria12)))
    sabiduria13 = tk.Button(root_rol2,text="13",command=lambda: (compradepuntos(5,13,"sabiduria",sabiduria13)))
    sabiduria14 = tk.Button(root_rol2,text="14",command=lambda: (compradepuntos(7,14,"sabiduria",sabiduria14)))
    sabiduria15 = tk.Button(root_rol2,text="15",command=lambda: (compradepuntos(9,15,"sabiduria",sabiduria15)))

    carisma8 = tk.Button(root_rol2,text="8",command=lambda: (compradepuntos(0,8,"carisma",carisma8)))
    carisma9 = tk.Button(root_rol2,text="9",command=lambda: (compradepuntos(1,9,"carisma",carisma9)))
    carisma10 = tk.Button(root_rol2,text="10",command=lambda: (compradepuntos(2,10,"carisma",carisma10)))
    carisma11 = tk.Button(root_rol2,text="11",command=lambda: (compradepuntos(3,11,"carisma",carisma11)))
    carisma12 = tk.Button(root_rol2,text="12",command=lambda: (compradepuntos(4,12,"carisma",carisma12)))
    carisma13 = tk.Button(root_rol2,text="13",command=lambda: (compradepuntos(5,13,"carisma",carisma13)))
    carisma14 = tk.Button(root_rol2,text="14",command=lambda: (compradepuntos(7,14,"carisma",carisma14)))
    carisma15 = tk.Button(root_rol2,text="15",command=lambda: (compradepuntos(9,15,"carisma",carisma15)))


    global botonesvar 
    botonesvar= {

    "fuerza8" : fuerza8,
    "fuerza9" : fuerza9,
    "fuerza10" : fuerza10,
    "fuerza11" : fuerza11,
    "fuerza12" : fuerza12,
    "fuerza13" : fuerza13,
    "fuerza14" : fuerza14,
    "fuerza15" : fuerza15,

    "destreza8" : destreza8,
    "destreza9" : destreza9,
    "destreza10" : destreza10,
    "destreza11" : destreza11,
    "destreza12" : destreza12,
    "destreza13" : destreza13,
    "destreza14" : destreza14,
    "destreza15" : destreza15,

    "constitucion8" : constitucion8,
    "constitucion9" : constitucion9,
    "constitucion10" : constitucion10,
    "constitucion11" : constitucion11,
    "constitucion12" : constitucion12,
    "constitucion13" : constitucion13,
    "constitucion14" : constitucion14,
    "constitucion15" : constitucion15,

    "inteligencia8" : inteligencia8,
    "inteligencia9" : inteligencia9,
    "inteligencia10" : inteligencia10,
    "inteligencia11" : inteligencia11,
    "inteligencia12" : inteligencia12,
    "inteligencia13" : inteligencia13,
    "inteligencia14" : inteligencia14,
    "inteligencia15" : inteligencia15,

    "sabiduria8" : sabiduria8,
    "sabiduria9" : sabiduria9,
    "sabiduria10" : sabiduria10,
    "sabiduria11" : sabiduria11,
    "sabiduria12" : sabiduria12,
    "sabiduria13" : sabiduria13,
    "sabiduria14" : sabiduria14,
    "sabiduria15" : sabiduria15,

    "carisma8" : carisma8,
    "carisma9" : carisma9,
    "carisma10" : carisma10,
    "carisma11" : carisma11,
    "carisma12" : carisma12,
    "carisma13" : carisma13,
    "carisma14" : carisma14,
    "carisma15" : carisma15
    }
    puntos.grid(column=0,row=0)
    sacarpuntos.grid(column=0,row=1)
    puntosl.grid(column=0,row=2)

    fuelabel.grid(column=0, row=4)

    fuerza8.grid(row=4,column=1)
    fuerza9.grid(row=4,column=2)
    fuerza10.grid(row=4,column=3)
    fuerza11.grid(row=4,column=4)
    fuerza12.grid(row=4,column=5)
    fuerza13.grid(row=4,column=6)
    fuerza14.grid(row=4,column=7)
    fuerza15.grid(row=4,column=8)

    deslabel.grid(row=5,column=0)

    destreza8.grid(row=5,column=1)
    destreza9.grid(row=5,column=2)
    destreza10.grid(row=5,column=3)
    destreza11.grid(row=5,column=4)
    destreza12.grid(row=5,column=5)
    destreza13.grid(row=5,column=6)
    destreza14.grid(row=5,column=7)
    destreza15.grid(row=5,column=8)

    conlabel.grid(row=7,column=0)

    constitucion8.grid(row=7,column=1)
    constitucion9.grid(row=7,column=2)
    constitucion10.grid(row=7,column=3)
    constitucion11.grid(row=7,column=4)
    constitucion12.grid(row=7,column=5)
    constitucion13.grid(row=7,column=6)
    constitucion14.grid(row=7,column=7)
    constitucion15.grid(row=7,column=8)

    intlabel.grid(row=8, column=0)

    inteligencia8.grid(row=8,column=1)
    inteligencia9.grid(row=8,column=2)
    inteligencia10.grid(row=8,column=3)
    inteligencia11.grid(row=8,column=4)
    inteligencia12.grid(row=8,column=5)
    inteligencia13.grid(row=8,column=6)
    inteligencia14.grid(row=8,column=7)
    inteligencia15.grid(row=8,column=8)

    sablabel.grid(row=9, column=0)

    sabiduria8.grid(row=9, column=1)
    sabiduria9.grid(row=9, column=2)
    sabiduria10.grid(row=9, column=3)
    sabiduria11.grid(row=9, column=4)
    sabiduria12.grid(row=9, column=5)
    sabiduria13.grid(row=9, column=6)
    sabiduria14.grid(row=9, column=7)
    sabiduria15.grid(row=9, column=8)

    carlabel.grid(row=10,column=0)

    carisma8.grid(row=10,column=1)
    carisma9.grid(row=10,column=2)
    carisma10.grid(row=10,column=3)
    carisma11.grid(row=10,column=4)
    carisma12.grid(row=10,column=5)
    carisma13.grid(row=10,column=6)
    carisma14.grid(row=10,column=7)
    carisma15.grid(row=10,column=8)
    tk.mainloop()
   

def ventanaderollstats():
    res_3d6 = []
    for i in range(1,8):
        res_3d6.append(generadordecar(4))
    root_rol3 = tk.Tk()
    global caracteristicasj
    caracteristicasj = tk.Label(root_rol3,text= "que numero quieres para tu " + chara[0])
    tresd6ui1 = tk.Button(root_rol3, text=str(res_3d6[0]), command=lambda d = res_3d6[0]: (botonesparausar1(d,tresd6ui1), comandor()))
    tresd6ui2 = tk.Button(root_rol3, text=str(res_3d6[1]), command=lambda d = res_3d6[1]: (botonesparausar1(d,tresd6ui2), comandor()))
    tresd6ui3 = tk.Button(root_rol3, text=str(res_3d6[2]), command=lambda d = res_3d6[2]: (botonesparausar1(d,tresd6ui3), comandor()))
    tresd6ui4 = tk.Button(root_rol3, text=str(res_3d6[3]), command=lambda d = res_3d6[3]: (botonesparausar1(d,tresd6ui4), comandor()))
    tresd6ui5 = tk.Button(root_rol3, text=str(res_3d6[4]), command=lambda d = res_3d6[4]: (botonesparausar1(d,tresd6ui5), comandor()))
    tresd6ui6 = tk.Button(root_rol3, text=str(res_3d6[5]), command=lambda d = res_3d6[5]: (botonesparausar1(d,tresd6ui6), comandor()))
    tresd6ui7 = tk.Button(root_rol3, text=str(res_3d6[6]), command=lambda d = res_3d6[6]: (botonesparausar1(d,tresd6ui7), comandor()))
    acceptarstats = tk.Button(root_rol3,text="aceptar", command=root_rol3.destroy)

    tresd6ui1.grid(column=1, row= 6)
    tresd6ui2.grid(column=2, row= 6)
    tresd6ui3.grid(column=3, row= 6)
    tresd6ui4.grid(column=4, row= 6)
    tresd6ui5.grid(column=5, row= 6)
    tresd6ui6.grid(column=6, row= 6)
    tresd6ui7.grid(column=7, row= 6)
    acceptarstats.grid(column=4,row=7)
    caracteristicasj.grid(row=5,column=4, columnspan= 7)
    
    tk.mainloop()

#escritura en archivo .txt

def escrituraenarchivo():
    with open("ficha de "+Nombrejugador +".txt", "w", encoding='utf-8') as archivo:
        archivo.write(str(caracteristicas_jugador))
        archivo.write("\n"+Nombrepersonajejugable)
        archivo.write("\n" + pnjsr)
        archivo.write(pnjr)
        archivo.write("\n"+pnjsc+" ")
        archivo.write(pnjc)


def conseguirnombrej():
    n=nombrej.get()
    global Nombrejugador
    Nombrejugador = str(n)
    nombrej.delete(0, tk.END)
    printeadornj = tk.Label(text=Nombrejugador)
    printeadornj.grid(row=1, column=2)

def conseguirnombrepj():
    n=nombrepj.get()
    global Nombrepersonajejugable
    Nombrepersonajejugable = str(n)
    nombrepj.delete(0, tk.END)
    printeadornpj = tk.Label(text=Nombrepersonajejugable)
    printeadornpj.grid(row=1, column=3)


def dados(dcuanto):
          if dcuanto == "1d2":
              return random.randint(1,2)
          elif dcuanto == "1d3":
              return random.randint(1,3)
          elif dcuanto == "1d4":
              return random.randint(1,4)
          elif dcuanto == "1d6":
              return random.randint(1,6)
          elif dcuanto == "1d8":
              return random.randint(1,8)
          elif dcuanto == "1d10":
              return random.randint(1,10)
          elif dcuanto == "1d20":
              return random.randint(1,20)
          elif dcuanto == "1d100":
              return random.randint(1,100)
          else:
              print("has puesto mal los datos y la funcion dados() no reconoce tu tipo de dado")

def generadordecar(a):
    sumad = 0
    resd = []
    for i in range(1,a+1):
        resd.append(dados("1d6"))
    menor = min(resd)
    resd.remove(menor)
    sumad = sum(resd)
    return sumad

def comandor():
    global cont
    cont = cont +1

def botonesparausar1(a,b):
    ad = a
    
    ba1 = tk.getint(ad)
    caracteristicasj.config(text= "que numero quieres para tu " + chara[cont+1])
    b.config(state = "disabled")
    insertor(chara[cont], ba1)
    




def characteristics():
    caracteristicas_jugador = {}
    res_3d6 = []
    chara = list(caracteristicas)
    for i in range(1,8):
        res_3d6.append(generadordecar(4))
    for c in chara:
        print(res_3d6)
        caracteristicas_jugador[c]= int(input("elije el valor que quieres para tu " + c))
        res_3d6.remove(caracteristicas_jugador[c])
    return caracteristicas_jugador

def contadorstring(b,a,c):
    d = 1
    f = []
    for i in range(1,a+1):
        f.append(b+str(d)+c)
        d=d+1
    return f

def insertor(baka, idiot):
    global caracteristicas_jugador
    caracteristicas_jugador[baka] = (idiot)
    print(caracteristicas_jugador)
    caracteristicasui.grid(column=4, row=7, columnspan=4)


def selectorderace():
    numr=random.randint(0,48)
    Raza=RACE.loc[numr,"Raza:"]
    return Raza


def selectordeclass():
    numc=random.randint(0,12)
    Clase=CLASS.loc[numc,"Clase:"]
    return Clase

def selectordesubclase(clasep):
    if clasep == "Artificer":
        pociones = contadorstring("Subclase",4,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[0,ColumA]
        return subclass
    elif clasep == "Barbarian":
        pociones = contadorstring("Subclase",10,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[1,ColumA]
        return subclass
    elif clasep == "Bard":
        pociones = contadorstring("Subclase",9,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[2,ColumA]
        return subclass
    elif clasep == "Cleric":
        pociones = contadorstring("Subclase",16,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[3,ColumA]
        return subclass
    elif clasep == "Druid":
        pociones = contadorstring("Subclase",8,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[4,ColumA]
        return subclass
    elif clasep == "Fighter":
        pociones = contadorstring("Subclase",9,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[5,ColumA]
        return subclass
    elif clasep == "Monk":
        pociones = contadorstring("Subclase",11,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[6,ColumA]
        return subclass
    elif clasep == "Paladin":
        pociones = contadorstring("Subclase",10,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[7,ColumA]
        return subclass
    elif clasep == "Ranger":
        pociones = contadorstring("Subclase",8,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[8,ColumA]
        return subclass
    elif clasep == "Rogue":
        pociones = contadorstring("Subclase",9,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[9,ColumA]
        return subclass
    elif clasep == "Sorcerer":
        pociones = contadorstring("Subclase",9,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[10,ColumA]
        return subclass
    elif clasep == "Warlock":
        pociones = contadorstring("Subclase",9,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[11,ColumA]
        return subclass
    elif clasep == "Wizard":
        pociones = contadorstring("Subclase",14,":")
        ColumA = random.choice(pociones)
        subclass = CLASS.loc[12,ColumA]
        return subclass

    else:
        print("Hi I am ERROR")


def selectordesubrace(Racep):
    if Racep == "Aasimar":
        nc = contadorstring("Subraza",3 , ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[1,ncolum]
        return subrace 
    elif Racep == "Dragonborn":
        nc = contadorstring("Subraza",15 , ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[7,ncolum]
        return subrace 
    elif Racep == "Dragonborn (Ravenite)":
        nc = contadorstring("Subraza",10 , ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[9,ncolum]
        return subrace 
    elif Racep == "Dragonborn (Draconblood)":
        nc = contadorstring("Subraza",10 , ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[8,ncolum]
        return subrace 
    elif Racep == "Dwarf":
        nc = contadorstring("Subraza", 3, ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[10,ncolum]
        return subrace 
    elif Racep == "Elf":
        nc = contadorstring("Subraza", 11, ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[11,ncolum]
        return subrace 
    elif Racep == "Genasi":
        nc = contadorstring("Subraza", 4, ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[14,ncolum]
        return subrace 
    elif Racep == "Gith":
        nc = contadorstring("Subraza", 2, ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[16,ncolum]
        return subrace 
    elif Racep == "Gnomes":
        nc = contadorstring("Subraza", 3, ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[17,ncolum]
        return subrace 
    elif Racep == "Halfling":
        nc = contadorstring("Subraza", 4, ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[23,ncolum]
        return subrace 
    elif Racep == "Shifter":
        nc = contadorstring("Subraza", 4, ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[41,ncolum]
        return subrace 
    elif Racep == "Tiefling":
        nc = contadorstring("Subraza",11 , ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[44,ncolum]
        return subrace 
    elif Racep == "Dhanpir":
        nc = contadorstring("Subraza",42 , ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[6,ncolum]
        return subrace 
    elif Racep == "Reborn":
        nc = contadorstring("Subraza",42 , ":")
        ncolum = random.choice(nc)
        subrace = RACE.loc[39,ncolum]
        return subrace     
    else:
        return ""

#llamada de funciones e interfaz de usuario
if __name__== "__main__":
    root_rol1 = tk.Tk()
    
    pnjc = selectordeclass()
    pnjsc = selectordesubclase(pnjc)
    pnjr = selectorderace()
    pnjsr = selectordesubrace(pnjr)
    razaysubclase = pnjsr+" "+ pnjr+" "+ pnjsc+" " +pnjc



    


    rollstats = tk.Button(root_rol1, text="roll stats",command=ventanaderollstats)

    imprimir = tk.Button(root_rol1, text="imprimir", command= lambda :(escrituraenarchivo(), root_rol1.destroy()))

    caracteristicasui = tk.Label(root_rol1, textvariable=caracteristicas_jugador)

    ventanabuy = tk.Button(root_rol1, text="point buy", command=ventanadepointbuy)
    

    RYC = tk.Label(root_rol1,text=razaysubclase)
    
    nombrepj = tk.Entry(root_rol1)
    
    nombrej = tk.Entry(root_rol1)
    
    enter_namej = tk.Button(root_rol1, text="Acceptar", command=conseguirnombrej)
    
    enter_namepj = tk.Button(root_rol1, text="Acceptar", command=conseguirnombrepj)

    
    #insercion de las entradas
    
    nombrepj.insert(0,"cual va ser su nombre?")
    nombrej.insert(0, "cual es TU nombre?")
    
    #poner las cosas en su sitio

    ventanabuy.grid(row=6,column=1)
    imprimir.grid(column=8, row=7)
    RYC.grid(column=0, row=0)
    nombrepj.grid(row=1,column=0)
    enter_namepj.grid(row=2, column=0)
    nombrej.grid(row=3,column=0)
    enter_namej.grid(row=4, column=0)
    rollstats.grid(column=1,row=5)
    tk.mainloop()
