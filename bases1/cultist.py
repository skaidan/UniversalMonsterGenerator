# bases1/cultist.py
"""
Cultist creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cultist
"""
from creature_base import GlobalCreatureBaseClass


class Cultist(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Cultist
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 12, 'CON': 10, 'INT': 10, 'WIS': 11, 'CHAR': 10, 'armor_class': 12, 'alignment': 'any non-good alignment Armor Class  12 (leather armor) Hit Points  9 (2d8) Speed  30 ft. STR 11 (+0) DEX 12 (+1) CON 10 (+0) INT 10 (+0) WIS 11 (+0) CHA 10 (+0) Skills  Deception +2', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['dark_devotion', 'scimitar']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dark_devotion(self) -> str:
        """The cultist has advantage on saving throws against being charmed or frightened."""
        return 'The cultist has advantage on saving throws against being charmed or frightened.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) slashing damage.'

