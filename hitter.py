class Hitter:

    def __init__(self, hitter_name, fb, ch, cb, sl): #, eye, speed):
        self.__name = hitter_name
        self.__fastball = fb
        self.__changeup = ch
        self.__curveball = cb
        self.__slider = sl
        #self.__eye = eye
        #self.__speed = speed

    def set_name(self, hitter_name):
        self.__name = hitter_name

    def set_fastball(self, fb):
        self.__fastball = fb

    def set_changeup(self, ch):
        self.__changeup = ch

    def set_curveball(self, cb):
        self.__curveball = cb

    def set_slider(self, sl):
        self.__slider = sl

    def set_eye(self, eye):
        self.__eye = eye

    def set_speed(self, speed):
        self.__speed = speed

    def get_name(self):
        return self.__name

    def get_fastball(self):
        return self.__fastball

    def get_changeup(self):
        return self.__changeup

    def get_curveball(self):
        return self.__curveball

    def get_slider(self):
        return self.__slider

    def get_eye(self):
        return self.__eye

    def get_speed(self):
        return self.__speed


