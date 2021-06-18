class Riven:

    def __init__(self,
                 hero_name='瑞文',
                 hero_money='6300B',
                 hero_hp='414',
                 hero_mp='0',
                 hero_attack='54'
                 ):
        self.hero_name = hero_name
        self.hero_money = hero_money
        self.hero_hp = hero_hp
        self.hero_mp = hero_mp
        self.hero_attack = hero_attack

    def attack(self, attack):
        hero_hp_new = self.hero_hp - attack
