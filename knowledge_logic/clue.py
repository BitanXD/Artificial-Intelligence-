import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

# print(knowledge.formula())
# check_knowledge(knowledge)

# # Initial cards
knowledge.add(And(
    Not(scarlet), Not(kitchen), Not(knife)
))

# # Unknown card
knowledge.add(Or(
    Not(mustard), Not(ballroom), Not(wrench)
))

# # Known cards
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))
knowledge.add(Not(wrench))

check_knowledge(knowledge)