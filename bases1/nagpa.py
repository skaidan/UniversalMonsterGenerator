# bases1/nagpa.py
"""
Nagpa creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nagpa
"""
from creature_base import GlobalCreatureBaseClass


class Nagpa(GlobalCreatureBaseClass):
    """
    Medium Monstrosity (Wizard) creature - Nagpa
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 203, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 15, 'CON': 12, 'INT': 23, 'WIS': 18, 'CHAR': 21, 'armor_class': 19, 'alignment': 'typically Neutral Evil Armor Class  19 (natural armor) Hit Points  203 (37d8 + 37) Speed  30 ft. STR 9 (-1) DEX 15 (+2) CON 12 (+1) INT 23 (+6) WIS 18 (+4) CHA 21 (+5) Saving Throws  Int +12', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity (Wizard)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'staff', 'deathly_ray', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The nagpa makes three Staff or Deathly Ray attacks. It can replace one attack with a use of Spellcasting."""
        return 'The nagpa makes three Staff or Deathly Ray attacks. It can replace one attack with a use of Spellcasting.'

    def staff_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage plus 24 (7d6) necrotic damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage plus 24 (7d6) necrotic damage.'

    def deathly_ray_attack(self) -> str:
        """Ranged Spell Attack: +12 to hit, range 120 ft., one target. Hit: 30 (7d6 + 6) necrotic damage."""
        return 'Ranged Spell Attack: +12 to hit, range 120 ft., one target. Hit: 30 (7d6 + 6) necrotic damage.'

    def spellcasting_attack(self) -> str:
        """The nagpa casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 20):"""
        return 'The nagpa casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 20):'

