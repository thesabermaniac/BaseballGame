import random
import pitcher
import hitter
import orioles


class Game:

    def __init__(self, hitters, pitchers):
        self.__cpu_pitch = random.randint(1, 4)
        self.__cpu_hit = random.randint(1, 4)
        self.__hitters = hitters
        self.__pitchers = pitchers

    def set_cpu_pitch(self, pitch):
        self.__cpu_pitch = pitch

    def set_cpu_hit(self, hit):
        self.__cpu_hit = hit

    def set_hitters(self, hitters):
        self.__hitters = hitters

    def set_pitchers(self, pitchers):
        self.__pitchers = pitchers

    def get_cpu_pitch(self):
        return self.__cpu_pitch

    def get_cpu_hit(self):
        return self.__cpu_hit

    def get_hitters(self):
        return self.__hitters

    def get_pitchers(self):
        return self.__pitchers

    def hit_or_pitch(self):
        user = input("Would you like to hit or pitch? ")
        return user

    def choose_lineup(self):
        lineup = []
        print("Ok, begin choosing your lineup by simply entering the name of the player you want to lead off. ")
        print("Here are your options:")
        lineup_tracker = 1
        while len(lineup) < 9:
            for i in range(len(self.__hitters)):
                print(i+1, ") ", self.__hitters[i].get_name(), sep='')
            print()
            user_response = input(str(lineup_tracker) + ") ")
            print()
            if user_response.isdigit():
                lineup.append(self.__hitters[int(user_response) - 1])
                del self.__hitters[int(user_response) - 1]
            else:
                for j in range(len(self.__hitters)-1):
                    if user_response.lower() == self.__hitters[j].get_name().lower():
                        lineup.append(self.__hitters[j])
                        del self.__hitters[j]
            lineup_tracker += 1
        print("OK, here is your lineup: ")
        for i in range(len(lineup)):
            print(i+1, ") ", lineup[i].get_name(), sep='')
        return lineup

    def current_batter(self, i):
        return self.__hitters[i]

    def is_swing(self):
        user = input("Would you like to swing (y/n)? ")
        if user.lower() == 'y':
            return True
        else:
            return False

    def throw_strike(self):
        user = input("Do you want to throw a strike (y/n)? ")
        if user.lower() == 'y':
            return True

    def strike(self, my_pitcher):
        result = random.randint(1, 100)
        if self.throw_strike() and (my_pitcher.get_control() > result):
            return True

    def hitter_pitch_ability(self, my_hitter):
        if self.cpu_pitch() == 1:
            return my_hitter.get_fastball()
        elif self.cpu_pitch() == 2:
            return my_hitter.get_changeup()
        elif self.cpu_pitch() == 3:
            return my_hitter.get_curveball()
        else:
            return my_hitter.get_slider()

    def is_fair(self):
        num = random.randint(1, 10)
        if num > 2:
            return True

    def contact(self, my_pitcher, my_hitter):
        if self.is_swing() and self.strike(my_pitcher) and self.hitter_pitch_ability(my_hitter) > random.randint(1, 100):
            return True

    def user_pitch(self):
        print("Please select a pitch from the following options (1-5):")
        print("1) Fastball")
        print("2) Changeup")
        print("3) Curveball")
        print("4) Slider")
        pitch = int()
        return pitch

    def cpu_pitch(self):
        pitch = random.randint(1, 4)
        return pitch


my_team = orioles.Orioles()
my_team.set_hitters()
my_team.set_pitchers()
my_game = Game(my_team.get_hitters(), my_team.get_pitchers())
if my_game.hit_or_pitch().lower() == 'hit':
    my_game.choose_lineup()


