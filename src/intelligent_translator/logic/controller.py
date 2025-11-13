# projektname/logic/controller.py

class Controller:
    def __init__(self, model=None):
        self.model = model

    def do_something(self):
        print("Wiwiwiwi")

    def compute_value(self, x, y):
        try:
            return x + y
        except Exception:
            return None
