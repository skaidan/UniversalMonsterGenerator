# bases1/flying-sword.py
"""
FlyingSword creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flying-sword
"""
from creature_base import GlobalCreatureBaseClass


class FlyingSword(GlobalCreatureBaseClass):
    """
    Small construct creature - FlyingSword
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 17, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 15, 'CON': 11, 'INT': 1, 'WIS': 5, 'CHAR': 1, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  17 (5d6) Speed  0 ft.', 'legendary': False, 'size': 'Small', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['antimagic_susceptibility', 'longsword']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def antimagic_susceptibility(self) -> str:
        """The sword is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the sword must succeed on a Constitution saving throw against the caster's spell save DC or fall uncons"""
        return "The sword is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the sword must succeed on a Constitution saving throw against the caster's spell save DC or fall uncons"

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) slashing damage.'

