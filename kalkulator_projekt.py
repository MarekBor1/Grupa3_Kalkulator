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
                self.result = "BLAD"
        elif znak == '^':
            self.result = Liczby(0, 0)
            self.result.ustaw_modul_katowy((self.numer_1.dostac_kat()) * (self.numer_2.dostac_czesc_rzeczywista()),
                                         self.numer_1.modul() ** int(self.numer_2.dostac_czesc_rzeczywista()))
