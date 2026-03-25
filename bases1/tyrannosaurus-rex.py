# bases1/tyrannosaurus-rex.py
"""
TyrannosaurusRex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tyrannosaurus-rex
"""
from creature_base import GlobalCreatureBaseClass


class TyrannosaurusRex(GlobalCreatureBaseClass):
    """
    Huge beast creature - TyrannosaurusRex
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 10, 'CON': 19, 'INT': 2, 'WIS': 12, 'CHAR': 9, 'armor_class': 13, 'alignment': "unaligned Armor Class  13 (natural armor) Hit Points  136 (13d12 + 52) Speed  50 ft. STR 25 (+7) DEX 10 (+0) CON 19 (+4) INT 2 (-4) WIS 12 (+1) CHA 9 (-1) Skills  Perception +4 Senses  passive Perception 14 Languages  — Challenge  8 (3900 XP) Actions Multiattack . The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both attacks against the same target. Bite .  Melee Weapon Attack : +10 to hit", 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'tail']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both attacks against the same target."""
        return "The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both attacks against the same target."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 33 (4d12 + 7) piercing damage. If the target is a Medium or smaller creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the tyrannosaurus can't bite another target."""
        return "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 33 (4d12 + 7) piercing damage. If the target is a Medium or smaller creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the tyrannosaurus can't bite another target."

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage.'

