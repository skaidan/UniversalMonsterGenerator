# bases1/giant-crocodile.py
"""
GiantCrocodile creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-crocodile
"""
from creature_base import GlobalCreatureBaseClass


class GiantCrocodile(GlobalCreatureBaseClass):
    """
    Huge beast creature - GiantCrocodile
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 9, 'CON': 17, 'INT': 2, 'WIS': 10, 'CHAR': 7, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  85 (9d12 + 27) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'multiattack', 'bite', 'tail']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The crocodile can hold its breath for 30 minutes."""
        return 'The crocodile can hold its breath for 30 minutes.'

    def multiattack_attack(self) -> str:
        """The crocodile makes two attacks: one with its bite and one with its tail."""
        return 'The crocodile makes two attacks: one with its bite and one with its tail.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 21 (3d10 + 5) piercing damage, and the target is grappled (escape DC 16). Until this grapple ends, the target is restrained, and the crocodile can't bite another target."""
        return "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 21 (3d10 + 5) piercing damage, and the target is grappled (escape DC 16). Until this grapple ends, the target is restrained, and the crocodile can't bite another target."

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target not grappled by the crocodile. Hit: 14 (2d8 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target not grappled by the crocodile. Hit: 14 (2d8 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked prone.'

