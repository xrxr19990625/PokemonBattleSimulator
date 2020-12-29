import random
import utility
import pokemon


class Move:
    type_ = None
    name_ = None
    accuracy_ = 0
    kind_ = None  # special, physical, status
    crit_lvl_ = 0
    priority_ = 0
    user_ = None
    receivers_ = None
    flags_: dict = dict()
    weather_: str = None
    terrain_: str = None
    field_user_ = None
    field_receiver_ = None

    # TODO: add user and receiver into the constructor
    def __init__(self, type_, name, kind):
        self.power_ = 0
        self.dynamax_power_ = 0
        self.type_ = type_
        self.name_ = name
        self.kind_ = kind

    def set_accuracy(self, accuracy):
        self.accuracy_ = accuracy

    def set_power(self, power):
        self.power_ = power
        pass

    def get_power(self):
        return self.power_

    def effect(self, **kwargs):
        raise NotImplementedError('Stub')
        pass

    def set_crit_lvl(self, crit):
        self.crit_lvl_ = crit

    def get_crit_lvl(self):
        return self.crit_lvl_

    def set_user(self, user: pokemon.Pokemon):
        self.user_ = user

    def set_receiver(self, receivers: list):
        self.receivers_ = receivers

    def damage_calc(self):
        assert self.user_ is not None
        assert self.receivers_ is not None
        assert self.kind_ != 'sta'
        if len(self.receivers_) == 2:
            attack = 0
            defense = 0

            pass
        else:
            pass


class StatusMove(Move):
    def __init__(self, type_, name, kind):
        super().__init__(type_, name, kind)
        self.power_ = 0

    def effect(self, **kwargs):
        pass


class SenmanVoltThunderbolt(Move):
    def __init__(self):
        super().__init__('electric', '10,000,000 Volt Thunderbolt', 'spa')
        self.power_ = 195
        self.crit_lvl_ = 2

    def effect(self, **kwargs):
        pass


class Absorb(Move):
    def __init__(self):
        super().__init__('grass', 'Absorb', 'spa')
        self.power_ = 20

    def effect(self, **kwargs):
        dmg = kwargs['damage']
        self.user_.actual_value_[0] += dmg // 2


class Accelerock(Move):
    def __init__(self):
        super().__init__('rock', 'Accelerock', 'atk')
        self.power_ = 40
        self.priority_ = 1


class Acid(Move):
    def __init__(self):
        super().__init__('poison', 'Acid', 'spa')
        self.power_ = 40

    def effect(self, **kwargs):
        roll = utility.get_roll()
        if roll > 0.9:
            self.receivers_[0].change_spd_lvl(-1)


class AcidArmor(StatusMove):
    def __init__(self):
        super().__init__('poison', 'AcidArmor', 'sta')

    def effect(self, **kwargs):
        self.user_.change_def_lvl(2)


class AcidSpray(Move):
    def __init__(self):
        super().__init__('poison', 'AcidSpray', 'spa')

    def effect(self, **kwargs):
        self.receivers_[0].change_spd_lvl(-2)


class Acrobatics(Move):
    def __init__(self):
        super().__init__('Flying', 'Acrobatics', 'atk')
        if self.user_.item_ is None:
            self.power_ = 110
        else:
            self.power_ = 55

    def effect(self, **kwargs):
        pass


if __name__ == '__main__':
    print(random.uniform(0, 1))
    pass
