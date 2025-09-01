from logic import *

rain = Symbol('rain') # It is raining.
hagrid = Symbol('hagrid') # Harry visited hagrid.
dumbledore = Symbol('dumbledore') # Harry visited dumbledore.

knowledge = And(Implication( Not(rain), hagrid),  # if it is not raining, then harry visited hagrid.
            Or(hagrid, dumbledore),  # harry visited hagrid or dumbledore.
            Not(And(hagrid, dumbledore)),  # harry not visited both hagrid and dumbledore.
            dumbledore  # harry visited dumbledore.
)

print(model_check(knowledge, hagrid))

# sentence = And(rain, hagrid)
# print(knowledge.formula())