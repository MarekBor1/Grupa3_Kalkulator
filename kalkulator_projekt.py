from tkinter import *
import math
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring


#Klasa Liczby oraz dzialania dodawania odejmowania mnozenia dzielenia potegowania i pierwiastkowania
class Liczby:
    def __init__(self, x_axis, y_axis):
        self.czesc_rzeczywista = x_axis
        self.czesc_urojona = y_axis

    def dostac_czesc_rzeczywista(self):
        return self.czesc_rzeczywista

    def dostac_czesc_urojona(self):
        return self.czesc_urojona

    def ustaw_czesc_rzeczywista(self, parametr):
        self.czesc_rzeczywista = parametr

    def ustaw_czesc_urojona(self, parametr):
        self.czesc_urojona = parametr

    def modul(self):
        return math.sqrt(self.czesc_rzeczywista * 2 + self.czesc_urojona * 2)

    def set_both_parts(self, parametr_x, parametr_y):
        self.ustaw_czesc_rzeczywista(parametr_x)
        self.ustaw_czesc_urojona(parametr_y)

    def get_angle(self):
        if self.modul() != 0:
            return math.acos(self.czesc_rzeczywista / self.modul())
        else:
            return 0

    def ustaw_modul_katowy(self, kat, modul):
        self.czesc_rzeczywista = math.cos(kat) * modul
        self.czesc_urojona = math.sin(kat) * modul


class Operacje: 
    def __init__(self, numer1, numer2, znak):
        self.numer_1 = numer1
        self.numer_2 = numer2
        self.znak = znak  
        
        if znak == '+':
            self.result = Liczby(self.numer_1.dostac_czesc_rzeczywista() + self.numer_2.dostac_czesc_rzeczywista(),
                                 self.numer_1.dostac_czesc_urojona() + self.numer_2.dostac_czesc_urojona())
        elif znak == '-':
            self.result = Liczby(self.numer_1.dostac_czesc_rzeczywista() - self.numer_2.dostac_czesc_rzeczywista(),
                                 self.numer_1.dostac_czesc_urojona() - self.numer_2.dostac_czesc_urojona())
        elif znak == '*':
            self.result = Liczby((self.numer_1.dostac_czesc_rzeczywista() * self.numer_2.dostac_czesc_rzeczywista()) - (
                    self.numer_1.dostac_czesc_urojona() * self.numer_2.dostac_czesc_urojona()),
                                 (self.numer_1.dostac_czesc_urojona() * self.numer_2.dostac_czesc_rzeczywista()) + (
                                         self.numer_1.dostac_czesc_rzeczywista() * self.numer_2.dostac_czesc_urojona()))
        elif znak == '/':
            if self.numer_2.modul() != 0:
                self.result = Liczby(((self.numer_1.dostac_czesc_rzeczywista() * self.numer_2.dostac_czesc_rzeczywista()) + (
                        self.numer_1.dostac_czesc_urojona() * self.numer_2.dostac_czesc_urojona())) / (
                                             self.numer_2.dostac_czesc_rzeczywista() ** 2 + self.numer_2.dostac_czesc_urojona() ** 2),
                                     ((self.numer_1.dostac_czesc_urojona() * self.numer_2.dostac_czesc_rzeczywista()) + (
                                             self.numer_1.dostac_czesc_rzeczywista() * self.numer_2.dostac_czesc_urojona())) / (
                                             self.numer_2.dostac_czesc_rzeczywista() ** 2 + self.numer_2.dostac_czesc_urojona() ** 2))
            else:
                self.result = "Nie można dzielić przez '0' "
        elif znak == '^':
            self.result = Liczby(0, 0)
            self.result.ustaw_modul_katowy((self.numer_1.dostac_kat()) * (self.numer_2.dostac_czesc_rzeczywista()),
                                         self.numer_1.modul() ** int(self.numer_2.dostac_czesc_rzeczywista()))
        elif znak == 'r':
            self.korzen = []
            self.pierwszy_kąt = self.numer_1.dostac_kat() / int(self.numer_2.dostac_czesc_rzeczywista())
            self.modul_numer = self.numer_1.module() ** (1 / int(self.numer_2.dostac_czesc_rzeczywista()))
            for i in range(0, int(self.numer_2.dostac_czesc_rzeczywista())):
                self.korzen.append(Liczby(0, 0))
                self.korzen[i].ustaw_modul_katowy(
                    self.pierwszy_kąt + ((2 * math.pi) / int(self.numer_2.dostac_czesc_rzeczywista())) * i, self.modul_numer)
            self.result = self.korzen
        else:
            self.result = "BLAD"

    def dostac_numer_1(self):
        return self.numer_1

    def dostac_numer_2(self):
        return self.numer_2

    def dostac_operacje(self):
        return self.znak_

    def dostac_result(self):
        return self.result


def dodaj_do_pamieci(operation_obj):
    global memory
    memory.append(operation_obj)
    if len(memory) > 10:
            memory.pop(0)


def czysc_pamiec():
    global memory
    memory = []

def test_message_boxx(info):
    messagebox.showinfo("wynik pierwiastek", info)


def wiadomosc_tekstowa(info):
    number = askstring("jaki wynik?", info)
    return int(number)

input_text = StringVar()

def pokaz_pamiec(result_index: int):
    global memory
    global first_number
    global witch_number
    global expression
   
    if len(memory) > result_index:
        temp = memory[result_index]
        if temp.dostac_result() == "BLAD":
            return "BLAD"
        if temp.dostac_operacje() == "r":
            info = ""
            for i in range(0, len(temp.dostac_result())):
                info = info + str(i) + ":  " + str(temp.dostac_result()[i].dostac_czesc_rzeczywista()) + "+i" + str(
                    temp.dostac_result()[i].dostac_czesc_urojona()) + "\n"

            numba = int(wiadomosc_tekstowa(info))
            if numba >= len(temp.dostac_result()):
                expression = "ERROR"
                input_text.set(expression)
            else:
                input_text.set(expression)
                x_part = temp.dostac_result()[numba].dostac_czesc_rzeczywista()
                y_part = temp.dostac_result()[numba].dostac_czesc_urojona()
                expression = str(x_part) + "+i" + str(y_part)
                input_text.set(expression)
        else:
            if temp.dostac_result().dostac_czesc_urojona() == 0:
                expression = str(temp.dostac_result().dostac_czesc_rzeczywista())
            else:
                expression = str(temp.dostac_result().dostac_czesc_rzeczywista()) + '+i' + str(temp.dostac_result().dostac_czesc_urojona())
            input_text.set(expression)
    else:
        expression = "BLAD"
        input_text.set(expression)

def number_str_to_number(str_number):  ##dziala
    numba = Liczby(0, 0)
    x_param = 0
    y_param = 0
    if str_number.find("+i", 0) > 0:
        x_param = float(str_number[0:str_number.find("+i", 0)])
        y_param = float(str_number[str_number.find("+i", 0) + 2:])
        numba.set_both_parts(x_param, y_param)
    elif str_number.find("e^i(", 0) > 0:
        x_param = float(str_number[0:str_number.find("e^i(", 0)])
        y_param = float(str_number[str_number.find("e^i(", 0) + 4:])
        numba.set_angle_module(y_param, x_param)
    else:
        numba.set_both_parts(float(str_number), 0.0)
    return numba

def interpretation(first, second, mark):  ####dostaje string daje wynik
    number__1 = number_str_to_number(first)
    number__2 = number_str_to_number(second)
    print(number__1.get_real_part())
    oper = Operacje(number__1, number__2, mark)
    dodaj_do_pamieci(oper)  # juz naprawione

    if oper.result == "BLAD":
        return "BLAD"
    if mark != 'r':
        if oper.result.dostac_czesc_urojona() == 0:
            return str(oper.result.dostac_czesc_rzeczywista())
        return str(oper.result.dostac_czesc_rzeczywista()) + "+i" + str(oper.result.dostac_czesc_urojona())
    if mark == 'r':
        string_stream_like_in_cpluspus = ""
        for i in range(0, len(oper.get_result())):
            if oper.result[i].dostac_czesc_urojona() == 0:
                string_stream_like_in_cpluspus = string_stream_like_in_cpluspus + str(i) + ":  " + str(
                    oper.get_result()[i].dostac_czesc_rzeczywista()) + "\n"
            else:
                string_stream_like_in_cpluspus = string_stream_like_in_cpluspus + str(i) + ":  " + str(
                    oper.get_result()[i].dostac_czesc_rzeczywista()) + "+i" + str(oper.get_result()[i].dostac_czesc_urojona()) + "\n"

        test_message_boxx(string_stream_like_in_cpluspus)
        if oper.get_result()[0].dostac_czesc_urojona() == 0:
            return str(oper.get_result()[0].dostac_czesc_rzeczywista())
        return str(oper.get_result()[0].dostac_czesc_rzeczywista()) + "+i" + str(oper.get_result()[0].dostac_czesc_urojona())
    return "BLAD"  # do poprawy

def result_normal(nummber):
    return str(nummber.get_real_part()) + "+i" + str(nummber.get_imaginary_part())


global memory
memory = []
global if_first_after_equal
if_first_after_equal = 0
# GUI

main_window = Tk()
# wyglad okna
main_window.geometry("700x400")
main_window.title("Calcualtor")


##Poczatek cześci graficznej 
input_frame = Frame(main_window, width=20, height=50, bd=0, highlightbackground="blue", highlightcolor="blue",
                    highlightthickness=1)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('times', 20, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# klawisze

btns_frame = Frame(main_window, width=350, height=272.5, bg="grey")
btns_frame.pack(side=LEFT)
######
czysc = Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="red", cursor="hand2", font="times",
               activebackground="silver",
               command=lambda: btn_clear()).grid(row=0, column=1, padx=1, pady=1)
I = Button(btns_frame, text="zamien na: \n a+ib", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
           font="times",
           command=lambda: etoi()).grid(row=3, column=5, padx=1, pady=1)
E = Button(btns_frame, text="zamien na: \n exp(i)", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
           font="times",
           command=lambda: iore()).grid(row=2, column=5, padx=1, pady=1)
dziel = Button(btns_frame, text="÷", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", font="times",
                activebackground="silver",
                command=lambda: number_input("/")).grid(row=0, column=5, padx=1, pady=1)
######
siedem = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", font="times",
               command=lambda: btn_click(7)).grid(row=1, column=1, padx=1, pady=1)
osiem = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", font="times",
               command=lambda: btn_click(8)).grid(row=1, column=2, padx=1, pady=1)
dziewieć = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="cyan", cursor="hand2", font="times",
              command=lambda: btn_click(9)).grid(row=1, column=3, padx=1, pady=1)
mnożenie = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2", font="times",
                  activebackground="silver",
                  command=lambda: number_input("*")).grid(row=1, column=5, padx=1, pady=1)
