class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False
def main():
    l0 = LightSwitch()
    l1 = LightSwitch()
    l2 = LightSwitch()
    #l1.switchIsOn = True
    l1.turnOn()
    l2.turnOn()
    l1.turnOff()
    print(l0.switchIsOn)
    print(l1.switchIsOn)
    print(l2.switchIsOn)
main()