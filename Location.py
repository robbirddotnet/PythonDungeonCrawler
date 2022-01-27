from MyUtilities import *

class Location():
    def __init__(self):
        self.manager = ""
        self.forecolor = "white"
        self.backcolor = "black"
        self.week = 1

    def Enter(self, player):
        color = getattr(MyUtilities.term, self.forecolor+"_on_"+self.backcolor)
        print(color("Hello"))

    def Exit(self, player):
        color = getattr(MyUtilities.term, self.forecolor+"_on_"+self.backcolor)
        print(color("Goodbye"))

    def Upkeep(self):
        # called when time advances
        self.week += 1

# term = Terminal()
# with term.location(0, term.height - 1):
#     # print(getattr(term, "red_on_blue")+'ALL SYSTEMS GO')
#     # print(getattr(term, "snow_on_blue")+'ALL SYSTEMS GO')
#     # print(getattr(term, "snow_on_blue2")+'ALL SYSTEMS GO')
#     # print(getattr(term, "snow_on_blue3")+'ALL SYSTEMS GO')
#     # print(term.red('ALL SYSTEMS GO'))
#     # print(term.normal)

#     print(getattr(term, "snow_on_blue3"))
#     print(c1)
#     print(term.normal)
