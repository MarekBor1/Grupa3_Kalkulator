from tkinter import *
import math

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


class Operation:
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

    def get_numer_1(self):
        return self.numer_1

    def get_numer_2(self):
        return self.numer_2

    def get_operation(self):
        return self.znak_

    def get_result(self):
        return self.result


    def add_to_memory(operation_obj):
        global memory
        memory.append(operation_obj)
        if len(memory) > 10:
            memory.pop(0)


    def clear_memory():
        global memory
        memory = []

def show_memory(result_index: int):
    global memory
   
    if len(memory) > result_index:
        temp = memory[result_index]
        if temp.get_result() == "BLAD":
            return "BLAD"
        if temp.get_operation() == "r":
            info = ""
            for i in range(0, len(temp.get_result())):
                info = info + str(i) + ":  " + str(temp.get_result()[i].dostac_czesc_rzeczywista()) + "+i" + str(
                    temp.get_result()[i].dostac_czesc_urojona()) + "\n"

# merson dodaj commita jakiegos bitte
