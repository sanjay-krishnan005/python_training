class Animal:
    def dog(self):
        print("domestic")

class Sound(Animal):
    def dog(self):
        super().dog()
        print("bark")

a = Sound()
a.dog()