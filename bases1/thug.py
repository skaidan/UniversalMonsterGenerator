# bases1/thug.py
"""
Thug creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=thug
"""
from creature_base import GlobalCreatureBaseClass


class Thug(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Thug
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 11, 'CON': 14, 'INT': 10, 'WIS': 10, 'CHAR': 11, 'armor_class': 11, 'alignment': "any non-good alignment Armor Class  11 (leather armor) Hit Points  32 (5d8 + 10) Speed  30 ft. STR 15 (+2) DEX 11 (+0) CON 14 (+2) INT 10 (+0) WIS 10 (+0) CHA 11 (+0) Skills  Intimidation +2 Senses  passive Perception 10 Languages  any one language (usually Common) Challenge  1/2 (100 XP) Pack Tactics . The thug has advantage on an attack roll against a creature if at least one of the thug's allies is within 5 feet of the creature and the ally isn't incapacitated. Actions Multiattack . The thug makes two melee attacks. Mace .  Melee Weapon Attack : +4 to hit", 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'multiattack', 'mace', 'heavy_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The thug has advantage on an attack roll against a creature if at least one of the thug's allies is within 5 feet of the creature and the ally isn't incapacitated."""
        return "The thug has advantage on an attack roll against a creature if at least one of the thug's allies is within 5 feet of the creature and the ally isn't incapacitated."

    def multiattack_attack(self) -> str:
        """The thug makes two melee attacks."""
        return 'The thug makes two melee attacks.'

    def mace_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) bludgeoning damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) bludgeoning damage.'

    def heavy_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +2 to hit, range 100/400 ft., one target. Hit: 5 (1d10) piercing damage."""
        return 'Ranged Weapon Attack: +2 to hit, range 100/400 ft., one target. Hit: 5 (1d10) piercing damage.'

