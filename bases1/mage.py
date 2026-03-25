# bases1/mage.py
"""
Mage creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mage
"""
from creature_base import GlobalCreatureBaseClass


class Mage(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Mage
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 40, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 11, 'INT': 17, 'WIS': 12, 'CHAR': 11, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  40 (9d8) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 11 (+0) INT 17 (+3) WIS 12 (+1) CHA 11 (+0) Saving Throws  Int +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['spellcasting', 'dagger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def spellcasting(self) -> str:
        """The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:Cantrips (at will): fi"""
        return 'The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:Cantrips (at will): fi'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

