# bases1/firenewt-warrior.py
"""
FirenewtWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=firenewt-warrior
"""
from creature_base import GlobalCreatureBaseClass


class FirenewtWarrior(GlobalCreatureBaseClass):
    """
    Medium Elemental creature - FirenewtWarrior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 13, 'CON': 12, 'INT': 7, 'WIS': 11, 'CHAR': 8, 'armor_class': 13, 'alignment': 'typically Neutral Armor Class  13 (shield) Hit Points  27 (5d8 + 5) Speed  30 ft. STR 10 (+0) DEX 13 (+1) CON 12 (+1) INT 7 (-2) WIS 11 (+0) CHA 8 (-1) Damage Immunities  fire Senses  passive Perception 10 Languages  Draconic', 'legendary': False, 'size': 'Medium', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'scimitar', 'spit_fire_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The firenewt can breathe air and water."""
        return 'The firenewt can breathe air and water.'

    def multiattack_attack(self) -> str:
        """The firenewt makes two Scimitar attacks."""
        return 'The firenewt makes two Scimitar attacks.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.'

    def spit_fire_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """The firenewt spits fire at a creature within 10 feet of it. The creature must make a DC 11 Dexterity saving throw, taking 9 (2d8) fire damage on a failed save, or half as much damage on a successful one."""
        return 'The firenewt spits fire at a creature within 10 feet of it. The creature must make a DC 11 Dexterity saving throw, taking 9 (2d8) fire damage on a failed save, or half as much damage on a successful one.'

