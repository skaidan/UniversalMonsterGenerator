# bases1/archmage.py
"""
Archmage creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=archmage
"""
from creature_base import GlobalCreatureBaseClass


class Archmage(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Archmage
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 99, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 12, 'INT': 20, 'WIS': 15, 'CHAR': 16, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  99 (18d8 + 18) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 12 (+1) INT 20 (+5) WIS 15 (+2) CHA 16 (+3) Saving Throws  Int +9', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'dagger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The archmage has advantage on saving throws against spells and other magical effects.Spellcasting. The archmage is an 18th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 17"""
        return 'The archmage has advantage on saving throws against spells and other magical effects.Spellcasting. The archmage is an 18th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 17'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

