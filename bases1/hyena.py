# bases1/hyena.py
"""
Hyena creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hyena
"""
from creature_base import GlobalCreatureBaseClass


class Hyena(GlobalCreatureBaseClass):
    """
    Medium beast creature - Hyena
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 5, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 13, 'CON': 12, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 11, 'alignment': "unaligned Armor Class  11 Hit Points  5 (1d8 + 1) Speed  50 ft. STR 11 (+0) DEX 13 (+1) CON 12 (+1) INT 2 (-4) WIS 12 (+1) CHA 5 (-3) Skills  Perception +3 Senses  passive Perception 13 Languages  — Challenge  0 (10 XP) Pack Tactics . The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 feet of the creature and the ally isn't incapacitated. Actions Bite .  Melee Weapon Attack : +2 to hit", 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 feet of the creature and the ally isn't incapacitated."""
        return "The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 feet of the creature and the ally isn't incapacitated."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage.'

