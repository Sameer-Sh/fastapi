import random


class BattleField:
    # field size should always be even because should be shared equally between two players
    #upper half rows for player1 and lower half rows for player 2

    def __init__(self, field_size):
        self.field_id = random.randint(0, 100)
        self.field_size = field_size
        self.battle_field = [[' ' for _ in range(field_size)] for _ in range(field_size)]
        self.player_a_ships = []
        self.player_b_ships = []