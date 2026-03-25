# bases1/storm-giant.py
"""
StormGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=storm-giant
"""
from creature_base import GlobalCreatureBaseClass


class StormGiant(GlobalCreatureBaseClass):
    """
    Huge giant creature - StormGiant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 230, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 14, 'CON': 20, 'INT': 16, 'WIS': 18, 'CHAR': 18, 'armor_class': 16, 'alignment': 'chaotic good Armor Class  16 (scale mail) Hit Points  230 (20d12 + 100) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'greatsword', 'rock', 'lightning_strike_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The giant can breathe air and water.Innate Spellcasting. The giant's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material compon"""
        return "The giant can breathe air and water.Innate Spellcasting. The giant's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material compon"

    def multiattack_attack(self) -> str:
        """The giant makes two greatsword attacks."""
        return 'The giant makes two greatsword attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 30 (6d6 + 9) slashing damage."""
        return 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 30 (6d6 + 9) slashing damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +14 to hit, range 60/240 ft., one target. Hit: 35 (4d12 + 9) bludgeoning damage."""
        return 'Ranged Weapon Attack: +14 to hit, range 60/240 ft., one target. Hit: 35 (4d12 + 9) bludgeoning damage.'

    def lightning_strike_(recharge_5-6)_attack(self) -> str:
        """The giant hurls a magical lightning bolt at a point it can see within 500 feet of it. Each creature within 10 feet of that point must make a DC 17 Dexterity saving throw, taking 54 (12d8) lightning damage on a failed save, or half as much damage on a successful one."""
        return 'The giant hurls a magical lightning bolt at a point it can see within 500 feet of it. Each creature within 10 feet of that point must make a DC 17 Dexterity saving throw, taking 54 (12d8) lightning damage on a failed save, or half as much damage on a successful one.'

