# bases1/lemure.py
"""
Lemure creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lemure
"""
from creature_base import GlobalCreatureBaseClass


class Lemure(GlobalCreatureBaseClass):
    """
    Medium fiend (Devil) creature - Lemure
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 5, 'CON': 11, 'INT': 1, 'WIS': 11, 'CHAR': 3, 'armor_class': 7, 'alignment': 'lawful evil Armor Class  7 Hit Points  13 (3d8) Speed  15 ft. STR 10 (+0) DEX 5 (-3) CON 11 (+0) INT 1 (-5) WIS 11 (+0) CHA 3 (-4) Damage Resistances  cold Damage Immunities  fire', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'fist']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the lemure's darkvision.Hellish Rejuvenation. A lemure that dies in the Nine Hells comes back to life with all its hit points in 1d10 days unless it is killed by a good"""
        return "Magical darkness doesn't impede the lemure's darkvision.Hellish Rejuvenation. A lemure that dies in the Nine Hells comes back to life with all its hit points in 1d10 days unless it is killed by a good"

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.'

