class dog:
    breed = "shepherd"
    def __init__(self, name, age):
       self.name = name
       self.age = age

Dein = dog("dein", 9)
max = dog("max", 69)

print("dein is a {}".format(Dein.breed))
print("max is a {}".format(max.breed))

