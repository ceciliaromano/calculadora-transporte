from tkinter import *

root = Tk()
root.title("Transport price calculator")
root.geometry("400x200")

lst = [[0, 0]]
train_price = 0
bus_price = 0
subte_price = 30
subte_times = 0
pressed_round_trip = False
pressed_30_days = False

def addTrain(*args):
    try:
        global train_price
        train_price = int(train_entry.get())
    except:
        train_entry.delete(0, 'end')
        train_entry.insert(0, "Debe ser un número")


def addBus(*args):
    try:
        global bus_price
        bus_price = int(bus_entry.get())
    except:
        bus_entry.delete(0, 'end')
        bus_entry.insert(0, "Debe ser un número")


train_entry = Entry(root)
train_entry.insert(0, "Precio del tren")
train_entry.grid(row=0, column=0)

bus_entry = Entry(root)
bus_entry.insert(0, "Precio del colectivo")
bus_entry.grid(row=0, column=1)


def addTransToList(name, price):
    print(pressed_round_trip, pressed_30_days)
    if pressed_round_trip == True or pressed_30_days == True:
        pass
    else:
        print("agregado")
        if len(lst) == 0 or lst[-1][1] == 0:
            lst.append([name, price])
        elif lst[-1][1] != 0 and lst[-2][1] == 0:
            lst.append([name, price*0.5])
        elif lst[-1][1] != 0 and lst[-2][1] != 0:
            lst.append([name, price*0.25]) 


def subteTimes(*args):
    global subte_times
    global subte_price

    if subte_times == 21:
        subte_price = 24
    elif subte_times == 31:
        subte_price = 21
    elif subte_times == 41:
        subte_price = 18


def roundTrip(*args):
    global pressed_round_trip
    print(pressed_round_trip)

    if pressed_round_trip == True:
        pass
    else:
        lst.append(["overtwo", 0])
        i = 0
        
        for value in reversed(lst):
            i += 1
            if value[0] == "subte" and i == 1:
                lst.append(["subte", subte_price])
            elif value[0] == "subte" and i == 2:
                lst.append(["subte", subte_price*0.5])
            elif value[0] == "subte" and i >= 3:
                lst.append(["subte", subte_price*0.25])

            if value[0] == "bus" and i == 1:
                lst.append(["bus", bus_price])
            elif value[0] == "bus" and i == 2:
                lst.append(["bus", bus_price*0.5])
            elif value[0] == "bus" and i >= 3:
                lst.append(["bus", bus_price*0.25])

            if value[0] == "tren" and i == 1:
                lst.append(["tren", train_price])
            elif value[0] == "tren" and i == 2:
                lst.append(["tren", train_price*0.5])
            elif value[0] == "tren" and i >= 3:
                lst.append(["tren", train_price*0.25])

            if value[0] == "overtwo":
                i = 0
        
        lst.append(["overtwo", 0])

        total_day = 0
        for value in lst:
            total_day += value[1]
            print(total_day)
        
        total_day_txt = StringVar()
        total_day_txt.set("El gasto de ida y vuelta es: $" + str(total_day))
        total_day_label = Label(root, textvariable=total_day_txt)
        total_day_label.grid(row=4, column=3)
        pressed_round_trip = True


lst2 = []


def calculateTrip(*args):
    global pressed_30_days
    print(pressed_30_days)

    if pressed_30_days == True:
        pass
    else:
        global subte_times
        for i in range(30):
            for idx, item in enumerate(lst):
                if item[0] == "subte":
                    subte_times+=1
                    subteTimes()
                    if lst[idx-1][1] == 0:
                        lst2.append(["subte", subte_price])
                    elif lst[idx-1][1] != 0 and lst[idx-2][1] == 0:
                        lst2.append(["subte", subte_price*0.5])
                    else:
                        lst2.append(["subte", subte_price*0.25])
                else:
                    lst2.append(item)
        
        total = 0
        for item in lst2:
            total += item[1]

        total_var = StringVar()
        total_var.set("El gasto para 30 días es: $" + str(total))
        total_label = Label(root, textvariable=total_var)
        total_label.grid(row=5, column=3)
        pressed_30_days = True


def destroy():
    addBus()
    addTrain()

    if train_price != 0 and bus_price !=0:
        train_entry.destroy()
        bus_entry.destroy()
        submit_btn.destroy()

        instruction = Label(root, text="Carga tu viaje diario")
        instruction.grid(row=0, column=0, columnspan=3)
        train_btn = Button(root, text="Tren", command= lambda:addTransToList("tren", train_price))
        train_btn.grid(row=1, column=0)
        bus_btn = Button(root, text="Bus", command= lambda:addTransToList("bus", bus_price))
        bus_btn.grid(row=1, column=1)
        subte_btn = Button(root, text="Subte", command= lambda:addTransToList("subte", subte_price))
        subte_btn.grid(row=1, column=2)
        over_two = Button(root, text="Pasaron más de 2 horas", command= lambda:addTransToList("overtwo", 0))
        over_two.grid(row=1, column=3)
        round_trip = Button(root, text="Viaje ida y vuelta", command=roundTrip)
        round_trip.grid(row=2, column=3)
        calculate = Button(root, text="Calcular gasto para 30 días", command=calculateTrip)
        calculate.grid(row=3, column=3)
    else:
        label = Label(root, text="Debes ingresar el precio del transporte")
        label.grid(row=1, column=1, columnspan=3)

        def labelDestroy(*args):
            label.destroy()

        try:
            train_entry.bind("<1>", labelDestroy)
            bus_entry.bind("<1>", labelDestroy)
        except:
            pass


submit_btn = Button(root, text="Continuar", command= destroy)
submit_btn.grid(row=1, column=0)

root.mainloop()
