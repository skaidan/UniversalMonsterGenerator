# bases1/drow-arachnomancer.py
"""
DrowArachnomancer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-arachnomancer
"""
from creature_base import GlobalCreatureBaseClass


class DrowArachnomancer(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Elf) creature - DrowArachnomancer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 162, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 17, 'CON': 14, 'INT': 19, 'WIS': 14, 'CHAR': 16, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (studded leather) Hit Points  162 (25d8 + 50) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'multiattack', 'bite_(spider_form_only)', 'poisonous_touch_(humanoid_form_only)', 'web_(spider_form_only;_recharge_5–6)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Spider Climb. The drow can climb difficult surfaces, including upside down on ceilings, without nee"""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Spider Climb. The drow can climb difficult surfaces, including upside down on ceilings, without nee"

    def multiattack_attack(self) -> str:
        """The drow makes three attacks, using Bite, Poisonous Touch, Web, or a combination of them. One attack can be replaced by a use of Spellcasting."""
        return 'The drow makes three attacks, using Bite, Poisonous Touch, Web, or a combination of them. One attack can be replaced by a use of Spellcasting.'

    def bite_(spider_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 31 (7d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 31 (7d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.'

    def poisonous_touch_(humanoid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 35 (10d6) poison damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 35 (10d6) poison damage.'

    def web_(spider_form_only;_recharge_5–6)_attack(self) -> str:
        """Ranged Weapon Attack: +8 to hit, range 30/60 ft., one target. Hit: The target is restrained by webbing. As an action, the restrained target can make a DC 15 Strength check, bursting the webbing on a success. The webbing can also be attacked and destroyed (AC 10; hp 5; vulnerability to fire damage; immunity to bludgeoning, poison, and psychic damage)."""
        return 'Ranged Weapon Attack: +8 to hit, range 30/60 ft., one target. Hit: The target is restrained by webbing. As an action, the restrained target can make a DC 15 Strength check, bursting the webbing on a success. The webbing can also be attacked and destroyed (AC 10; hp 5; vulnerability to fire damage; immunity to bludgeoning, poison, and psychic damage).'

    def spellcasting_attack(self) -> str:
        """The drow casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 17):"""
        return 'The drow casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 17):'

