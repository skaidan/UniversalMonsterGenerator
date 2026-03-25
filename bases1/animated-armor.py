# bases1/animated-armor.py
"""
AnimatedArmor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=animated-armor
"""
from creature_base import GlobalCreatureBaseClass


class AnimatedArmor(GlobalCreatureBaseClass):
    """
    Medium construct creature - AnimatedArmor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 11, 'CON': 13, 'INT': 1, 'WIS': 3, 'CHAR': 1, 'armor_class': 18, 'alignment': 'unaligned Armor Class  18 (natural armor) Hit Points  33 (6d8 + 6) Speed  25 ft. STR 14 (+2) DEX 11 (+0) CON 13 (+1) INT 1 (-5) WIS 3 (-4) CHA 1 (-5) Damage Immunities  poison', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['antimagic_susceptibility', 'multiattack', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def antimagic_susceptibility(self) -> str:
        """The armor is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the armor must succeed on a Constitution saving throw against the caster's spell save DC or fall uncons"""
        return "The armor is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the armor must succeed on a Constitution saving throw against the caster's spell save DC or fall uncons"

    def multiattack_attack(self) -> str:
        """The armor makes two melee attacks."""
        return 'The armor makes two melee attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage.'

