import moves
import pokemon


class Terrain:
    duration_ = 5

    def __init__(self):
        pass

    def set_duration(self, t):
        self.duration_ = t
        pass

    def dec_duration(self):
        self.duration_ -= 1

    def pass_through(self, user, receiver, move):
        pass

    def on_end_turn(self):
        pass
