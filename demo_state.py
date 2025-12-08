class SmartphoneState:

    UP = 1
    LEFT = 2
    RIGHT = 3
    DOWN = 4

class Smartphone:

    def __init__(self, callback=None):
        self.state = SmartphoneState.UP
        self.update_ui = callback

    def state_change(self, new_state):
        if (self.state == SmartphoneState.UP and new_state == SmartphoneState.LEFT) or \
           (self.state  == SmartphoneState.UP and new_state == SmartphoneState.RIGHT):
            self.state = new_state
            self.update_ui()
    
        if (self.state == SmartphoneState.LEFT and new_state == SmartphoneState.UP) or \
           (self.state  == SmartphoneState.LEFT and new_state == SmartphoneState.DOWN):
            self.state = new_state
            self.update_ui()

        if (self.state == SmartphoneState.RIGHT and new_state == SmartphoneState.UP) or \
           (self.state  == SmartphoneState.RIGHT and new_state == SmartphoneState.DOWN):
            self.state = SmartphoneState.UP
            self.update_ui()

        if (self.state == SmartphoneState.DOWN and new_state == SmartphoneState.LEFT) or \
           (self.state  == SmartphoneState.DOWN and new_state == SmartphoneState.RIGHT):
            self.state = new_state
            self.update_ui()   

        
        

def monCallback():
    print("Smartphone state changed !")  

phone = Smartphone(callback=monCallback)
phone.state_change(SmartphoneState.LEFT)
phone.state_change(SmartphoneState.RIGHT)
phone.state_change(SmartphoneState.UP)