# bases1/medusa.py
"""
Medusa creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=medusa
"""
from creature_base import GlobalCreatureBaseClass


class Medusa(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - Medusa
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 15, 'CON': 16, 'INT': 12, 'WIS': 13, 'CHAR': 15, 'armor_class': 15, 'alignment': 'lawful evil Armor Class  15 (natural armor) Hit Points  127 (17d8 + 51) Speed  30 ft. STR 10 (+0) DEX 15 (+2) CON 16 (+3) INT 12 (+1) WIS 13 (+1) CHA 15 (+2) Skills  Deception +5', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['petrifying_gaze', 'multiattack', 'snake_hair', 'shortsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def petrifying_gaze(self) -> str:
        """When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the medusa can force it to make a DC 14 Constitution saving throw if the medusa isn't incapacitated and can"""
        return "When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the medusa can force it to make a DC 14 Constitution saving throw if the medusa isn't incapacitated and can"

    def multiattack_attack(self) -> str:
        """The medusa makes either three melee attacks -one with its snake hair and two with its shortsword- or two ranged attacks with its longbow."""
        return 'The medusa makes either three melee attacks -one with its snake hair and two with its shortsword- or two ranged attacks with its longbow.'

    def snake_hair_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage plus 14 (4d6) poison damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage plus 14 (4d6) poison damage.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 7 (2d6) poison damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 7 (2d6) poison damage.'

