# bases1/drow-inquisitor.py
"""
DrowInquisitor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-inquisitor
"""
from creature_base import GlobalCreatureBaseClass


class DrowInquisitor(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Cleric creature - DrowInquisitor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 149, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 15, 'CON': 14, 'INT': 16, 'WIS': 21, 'CHAR': 20, 'armor_class': 16, 'alignment': 'Elf)', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Cleric', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['discern_lie', 'multiattack', 'death_lance', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def discern_lie(self) -> str:
        """The drow discerns when a creature in earshot speaks a lie in a language the drow knows.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to slee"""
        return "The drow discerns when a creature in earshot speaks a lie in a language the drow knows.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to slee"

    def multiattack_attack(self) -> str:
        """The drow makes three Death Lance attacks."""
        return 'The drow makes three Death Lance attacks.'

    def death_lance_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) piercing damage plus 18 (4d8) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken. This reduction lasts until the target finishes a long rest. The target dies if its hit point maximum is reduced to 0."""
        return "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) piercing damage plus 18 (4d8) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken. This reduction lasts until the target finishes a long rest. The target dies if its hit point maximum is reduced to 0."

    def spellcasting_attack(self) -> str:
        """The drow's casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 18):"""
        return "The drow's casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 18):"

