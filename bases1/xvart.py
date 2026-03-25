# bases1/xvart.py
"""
Xvart creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=xvart
"""
from creature_base import GlobalCreatureBaseClass


class Xvart(GlobalCreatureBaseClass):
    """
    Small Monstrosity creature - Xvart
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 14, 'CON': 10, 'INT': 8, 'WIS': 7, 'CHAR': 7, 'armor_class': 13, 'alignment': 'typically Chaotic Evil Armor Class  13 (leather armor) Hit Points  7 (2d6) Speed  30 ft. STR 8 (-1) DEX 14 (+2) CON 10 (+0) INT 8 (-1) WIS 7 (-2) CHA 7 (-2) Skills  Stealth +4 Senses  darkvision 30 ft.', 'legendary': False, 'size': 'Small', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['raxivorts_tongue', 'shortsword', 'sling']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def raxivorts_tongue(self) -> str:
        """The xvart can communicate with ordinary bats and rats, as well as giant bats and giant rats."""
        return 'The xvart can communicate with ordinary bats and rats, as well as giant bats and giant rats.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage. If at least one of the xvart's allies is within 5 feet of the target, the xvart can push the target 5 feet if the target is a Medium or smaller creature."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage. If at least one of the xvart's allies is within 5 feet of the target, the xvart can push the target 5 feet if the target is a Medium or smaller creature."

    def sling_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.'

