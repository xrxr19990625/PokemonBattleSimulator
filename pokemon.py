from item import Item
import moves


class Pokemon:
    name_: str = None
    id_: int = None
    stats_ = {
        'hp': 0,
        'atk': 0,
        'def': 0,
        'spa': 0,
        'spd': 0,
        'spe': 0
    }
    ab_lvl_changes_: dict = None
    accuracy_: int = 100
    actual_value_ = {
        'hp': 0,
        'atk': 0,
        'def': 0,
        'spa': 0,
        'spd': 0,
        'spe': 0
    }
    iv_ = {
        'hp': 0,
        'atk': 0,
        'def': 0,
        'spa': 0,
        'spd': 0,
        'spe': 0
    }
    ev_ = {
        'hp': 0,
        'atk': 0,
        'def': 0,
        'spa': 0,
        'spd': 0,
        'spe': 0
    }
    move1_: moves.Move = None
    move2_: moves.Move = None
    move3_: moves.Move = None
    move4_: moves.Move = None
    item_: Item = None
    status_: list = None  # burnt, paralyzed, poisoned, poisoned, frozen, sleep
    status_condition_: str = None
    nature_: str = None
    ability_: str = None
    additional_type_: list = []
    flags_: list = []  # recoil, flinch, charge, onfield, confusion, cantswitch...

    def __init__(self, name, id_):
        self.name_ = name
        self.id_ = id_
        self.ab_lvl_changes_ = {
            'atk': 0,
            'def': 0,
            'spa': 0,
            'spd': 0,
            'spe': 0,
            'acc': 0
        }

    def set_stats(self, stats):
        self.stats_['hp'] = stats[0]
        self.stats_['atk'] = stats[1]
        self.stats_['def'] = stats[2]
        self.stats_['spa'] = stats[3]
        self.stats_['spd'] = stats[4]
        self.stats_['spe'] = stats[5]

    def set_iv(self, ivs):
        self.stats_['hp'] = ivs[0]
        self.stats_['atk'] = ivs[1]
        self.stats_['def'] = ivs[2]
        self.stats_['spa'] = ivs[3]
        self.stats_['spd'] = ivs[4]
        self.stats_['spe'] = ivs[5]

    def set_ev(self, evs):
        self.stats_['hp'] = evs[0]
        self.stats_['atk'] = evs[1]
        self.stats_['def'] = evs[2]
        self.stats_['spa'] = evs[3]
        self.stats_['spd'] = evs[4]
        self.stats_['spe'] = evs[5]

    def calc_actual_val(self):
        pass

    def change_atk_lvl(self, n):
        self.ab_lvl_changes_['atk'] += n

    def change_def_lvl(self, n):
        self.ab_lvl_changes_['def'] += n

    def change_spa_lvl(self, n):
        self.ab_lvl_changes_['spa'] += n

    def change_spd_lvl(self, n):
        self.ab_lvl_changes_['spd'] += n

    def change_spe_lvl(self, n):
        self.ab_lvl_changes_['spe'] += n

    def change_acc_lvl(self, n):
        self.ab_lvl_changes_['acc'] += n

    def get_atk_lvl(self):
        return self.ab_lvl_changes_['atk']

    def get_def_lvl(self):
        return self.ab_lvl_changes_['def']

    def get_spa_lvl(self):
        return self.ab_lvl_changes_['spa']

    def get_spd_lvl(self):
        return self.ab_lvl_changes_['spd']

    def get_spe_lvl(self):
        return self.ab_lvl_changes_['spe']

    def get_acc_lvl(self):
        return self.ab_lvl_changes_['acc']

    def get_atk_av(self):
        return self.actual_value_['atk']

    def get_def_av(self):
        return self.actual_value_['def']

    def get_spa_av(self):
        return self.actual_value_['spa']

    def get_spd_av(self):
        return self.actual_value_['spd']

    def get_spe_av(self):
        return self.actual_value_['spe']

    def get_hp_av(self):
        return self.actual_value_['hp']

    def on_status_change(self):
        pass

    def on_item_change(self):
        pass

    def on_weather_change(self):
        pass

    def on_terrain_change(self):
        pass

    def on_ability_value_change(self):
        pass

    def on_faint(self):
        pass

    def on_switch_in(self):
        pass

    def on_switch_out(self):
        pass

    def on_turn_begins(self):
        pass

    def on_turn_ends(self):
        pass


class SingleTypePokemon(Pokemon):
    t1_ = None

    def __init__(self, name, id_, type1):
        super().__init__(name, id_)
        self.t1_ = type1


class DualTypePokemon(Pokemon):
    t1_ = None
    t2_ = None

    def __init__(self, name, id_, type1, type2):
        super().__init__(name, id_)
        self.t1_ = type1
        self.t2_ = type2
