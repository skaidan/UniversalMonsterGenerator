# bases1/kenku.py
"""
Kenku creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kenku
"""
from creature_base import GlobalCreatureBaseClass


class Kenku(GlobalCreatureBaseClass):
    """
    Medium humanoid (Kenku) creature - Kenku
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 16, 'CON': 10, 'INT': 11, 'WIS': 10, 'CHAR': 10, 'armor_class': 13, 'alignment': 'chaotic neutral Armor Class  13 Hit Points  13 (3d8) Speed  30 ft. STR 10 (+0) DEX 16 (+3) CON 10 (+0) INT 11 (+0) WIS 10 (+0) CHA 10 (+0) Skills  Deception +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Kenku)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['ambusher', 'shortsword', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def ambusher(self) -> str:
        """In the first round of a combat, the kenku has advantage on attack rolls against any creature it surprised.Mimicry. The kenku can mimic any sounds it has heard, including voices. A creature that hears """
        return 'In the first round of a combat, the kenku has advantage on attack rolls against any creature it surprised.Mimicry. The kenku can mimic any sounds it has heard, including voices. A creature that hears '

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

