# bases1/cult-fanatic.py
"""
CultFanatic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cult-fanatic
"""
from creature_base import GlobalCreatureBaseClass


class CultFanatic(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - CultFanatic
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 14, 'CON': 12, 'INT': 10, 'WIS': 13, 'CHAR': 14, 'armor_class': 13, 'alignment': 'any non-good alignment Armor Class  13 (leather armor) Hit Points  33 (6d8 + 6) Speed  30 ft. STR 11 (+0) DEX 14 (+2) CON 12 (+1) INT 10 (+0) WIS 13 (+1) CHA 14 (+2) Skills  Deception +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['dark_devotion', 'multiattack', 'dagger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dark_devotion(self) -> str:
        """The fanatic has advantage on saving throws against being charmed or frightened.Spellcasting. The fanatic is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 11, +3 to hit wit"""
        return 'The fanatic has advantage on saving throws against being charmed or frightened.Spellcasting. The fanatic is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 11, +3 to hit wit'

    def multiattack_attack(self) -> str:
        """The fanatic makes two melee attacks."""
        return 'The fanatic makes two melee attacks.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature. Hit: 4 (1d4 + 2) piercing damage.'

