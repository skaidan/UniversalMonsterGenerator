# bases1/astral-dreadnought.py
"""
AstralDreadnought creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=astral-dreadnought
"""
from creature_base import GlobalCreatureBaseClass


class AstralDreadnought(GlobalCreatureBaseClass):
    """
    Gargantuan Monstrosity (Titan) creature - AstralDreadnought
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 297, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 7, 'CON': 25, 'INT': 5, 'WIS': 14, 'CHAR': 18, 'armor_class': 20, 'alignment': 'unaligned Armor Class  20 (natural armor) Hit Points  297 (17d20 + 119) Speed  15 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Monstrosity (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['antimagic_cone', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def antimagic_cone(self) -> str:
        """The dreadnought's eye creates an area of antimagic, as in the antimagic field spell, in a 150-foot cone. At the start of each of its turns, it decides which way the cone faces. The cone doesn't functi"""
        return "The dreadnought's eye creates an area of antimagic, as in the antimagic field spell, in a 150-foot cone. At the start of each of its turns, it decides which way the cone faces. The cone doesn't functi"

    def multiattack_attack(self) -> str:
        """The dreadnought makes one Bite attack and two Claw attacks."""
        return 'The dreadnought makes one Bite attack and two Claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 36 (5d10 + 9) force damage. If the target is a Huge or smaller creature and this damage reduces it to 0 hit points or it is incapacitated, the dreadnought swallows it. The swallowed target, along with everything it is wearing and carrying, appears in an unoccupied space on the floor of the Demiplanar Donjon."""
        return 'Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 36 (5d10 + 9) force damage. If the target is a Huge or smaller creature and this damage reduces it to 0 hit points or it is incapacitated, the dreadnought swallows it. The swallowed target, along with everything it is wearing and carrying, appears in an unoccupied space on the floor of the Demiplanar Donjon.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 19 (3d6 + 9) force damage."""
        return 'Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 19 (3d6 + 9) force damage.'

