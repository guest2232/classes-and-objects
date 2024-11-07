class parrot:
    species = "bird"
    def __init__(self, name, age):
       self.name = name
       self.age = age

blu = parrot("blu", 9)
wu = parrot("wu", 69)

print("blu is a{}".format(blu.species))
print("wu is a{}".format(wu.species))


