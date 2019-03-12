import pitcher
import hitter


class Orioles:

    def __init__(self):
        self.__pitchers = []
        self.__hitters = []

    def set_pitchers(self):
        AlexCobb = pitcher.Pitcher(50, 60, 30, 20, 10, 80)
        DylanBundy = pitcher.Pitcher(70, 40, 60, 30, 5, 80)
        AndrewCashner = pitcher.Pitcher(40, 60, 50, 30, 10, 70)
        DavidHess = pitcher.Pitcher(30, 40, 50, 30, 5, 60)
        YefryRamirez = pitcher.Pitcher(40, 30, 40, 20, 10, 60)
        self.__pitchers = [AlexCobb, DylanBundy, AndrewCashner, DavidHess, YefryRamirez]

    def get_pitchers(self):
        return self.__pitchers

    def set_hitters(self):
        ChanceCisco = hitter.Hitter('Chance Cisco', 50, 30, 20, 40)
        ChrisDavis = hitter.Hitter('Chris Davis', 70, 30, 10, 20)
        JonathanVillar = hitter.Hitter('Jonathan Villar', 50, 60, 40, 50)
        RenatoNunez = hitter.Hitter('Renato Nunez', 50, 40, 50, 60)
        RichieMartin = hitter.Hitter('Richie Martin', 50, 60, 30, 50)
        DJStewart = hitter.Hitter('DJ Stewart', 50, 40, 50, 60)
        CedricMullins = hitter.Hitter('Cedric Mullins', 60, 50, 50, 60)
        TreyMancini = hitter.Hitter('Trey Mancini', 50, 60, 30, 50)
        MarkTrumbo = hitter.Hitter('Mark Trumbo', 70, 30, 10, 20)
        self.__hitters = [ChanceCisco, ChrisDavis, JonathanVillar, RenatoNunez, RichieMartin, DJStewart, CedricMullins, TreyMancini, MarkTrumbo]

    def get_hitters(self):
        return self.__hitters

