class ClassA():
    def __init__(self):
        self.speed = 50
    def AddSpeed(self, addSpeed):
        self.speed = addSpeed

class ClassB():
    def check_speed(self, ClassA):
        return ClassA.speed

object1 = ClassA()
object2 = ClassB()

object1.AddSpeed(100)
print(object2.check_speed(object1))
