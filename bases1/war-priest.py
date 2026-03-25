# bases1/war-priest.py
"""
WarPriest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=war-priest
"""
from creature_base import GlobalCreatureBaseClass


class WarPriest(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Cleric) creature - WarPriest
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 117, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 10, 'CON': 14, 'INT': 11, 'WIS': 17, 'CHAR': 13, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  117 (18d8 + 36) Speed  30 ft. STR 16 (+3) DEX 10 (+0) CON 14 (+2) INT 11 (+0) WIS 17 (+3) CHA 13 (+1) Saving Throws  Con +6', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Cleric)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'maul', 'holy_fire', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The war priest makes two Maul attacks, and it uses Holy Fire."""
        return 'The war priest makes two Maul attacks, and it uses Holy Fire.'

    def maul_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) radiant damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) radiant damage.'

    def holy_fire_attack(self) -> str:
        """The war priest targets one creature it can see within 60 feet of it. The target must make a DC 15 Wisdom saving throw. On a failed save, the target takes 12 (2d8 + 3) radiant damage, and it is blinded until the start of the war priest's next turn. On a successful save, the target takes half as much damage and isn't blinded."""
        return "The war priest targets one creature it can see within 60 feet of it. The target must make a DC 15 Wisdom saving throw. On a failed save, the target takes 12 (2d8 + 3) radiant damage, and it is blinded until the start of the war priest's next turn. On a successful save, the target takes half as much damage and isn't blinded."

    def spellcasting_attack(self) -> str:
        """The war priest casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 15):"""
        return 'The war priest casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 15):'

