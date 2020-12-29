class Weather:
    duration_ = 5

    def __init__(self):
        pass

    def set_duration(self, t):
        self.duration_ = t

    def dec_duration(self):
        self.duration_ -= 1

    def on_end_turn(self):
        pass
