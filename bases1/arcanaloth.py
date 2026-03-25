# bases1/arcanaloth.py
"""
Arcanaloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=arcanaloth
"""
from creature_base import GlobalCreatureBaseClass


class Arcanaloth(GlobalCreatureBaseClass):
    """
    Medium fiend (Yugoloth) creature - Arcanaloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 104, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 14, 'INT': 20, 'WIS': 16, 'CHAR': 17, 'armor_class': 17, 'alignment': 'neutral evil Armor Class  17 (natural armor) Hit Points  104 (16d8 + 32) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'claws', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The arcanaloth's innate spellcasting ability is Charisma (spell save DC 15). The arcanaloth can innately cast the following spells, requiring no material components:At will: alter self, darkness, heat"""
        return "The arcanaloth's innate spellcasting ability is Charisma (spell save DC 15). The arcanaloth can innately cast the following spells, requiring no material components:At will: alter self, darkness, heat"

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) slashing damage. The target must make a DC 14 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) slashing damage. The target must make a DC 14 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one.'

    def teleport_attack(self) -> str:
        """The arcanaloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."""
        return 'The arcanaloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see.'

