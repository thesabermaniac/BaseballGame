import random


class Pitcher:

    def __init__(self, fb, ch, cb, sl, pick, control):
        self.__fastball = fb
        self.__changeup = ch
        self.__curveball = cb
        self.__slider = sl
        self.__pickoff = pick
        self.__control = control

    def set_fastball(self, fb):
        self.__fastball = fb

    def set_changeup(self, ch):
        self.__changeup = ch

    def set_curveball(self, cb):
        self.__curveball = cb

    def set_slider(self, sl):
        self.__slider = sl

    def set_pick(self, pick):
        self.__pickoff = pick

    def set_control(self, control):
        self.__control = control

    def get_fastball(self):
        return self.__fastball

    def get_changeup(self):
        return self.__changeup

    def get_curveball(self):
        return self.__curveball

    def get_slider(self):
        return self.__slider

    def get_pickoff(self):
        return self.__pickoff

    def get_control(self):
        return self.__control




