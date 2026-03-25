# bases1/warlord.py
"""
Warlord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warlord
"""
from creature_base import GlobalCreatureBaseClass


class Warlord(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - Warlord
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 229, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 16, 'CON': 18, 'INT': 12, 'WIS': 12, 'CHAR': 18, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  229 (27d8 + 108) Speed  30 ft. STR 20 (+5) DEX 16 (+3) CON 18 (+4) INT 12 (+1) WIS 12 (+1) CHA 18 (+4) Saving Throws  Str +9', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['indomitable_(3/day)', 'multiattack', 'greatsword', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def indomitable_(3/day)(self) -> str:
        """The warlord can reroll a saving throw it fails. It must use the new roll.Survivor. The warlord regains 10 hit points at the start of its turn if it has fewer than half its hit points but at least 1 hi"""
        return 'The warlord can reroll a saving throw it fails. It must use the new roll.Survivor. The warlord regains 10 hit points at the start of its turn if it has fewer than half its hit points but at least 1 hi'

    def multiattack_attack(self) -> str:
        """The warlord makes two Greatsword or Short bow attacks."""
        return 'The warlord makes two Greatsword or Short bow attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +7 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +7 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

