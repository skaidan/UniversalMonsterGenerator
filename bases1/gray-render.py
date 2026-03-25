# bases1/gray-render.py
"""
GrayRender creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gray-render
"""
from creature_base import GlobalCreatureBaseClass


class GrayRender(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - GrayRender
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 13, 'CON': 20, 'INT': 3, 'WIS': 6, 'CHAR': 8, 'armor_class': 19, 'alignment': 'typically Chaotic Neutral Armor Class  19 (natural armor) Hit Points  189 (18d10 + 90) Speed  30 ft. STR 19 (+4) DEX 13 (+1) CON 20 (+5) INT 3 (-4) WIS 6 (-2) CHA 8 (-1) Saving Throws  Str +8', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The gray render makes one Bite attack and two Claw attacks."""
        return 'The gray render makes one Bite attack and two Claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 17 (2d12 + 4) piercing damage. If the target is Medium or smaller, the target must succeed on a DC 16 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 17 (2d12 + 4) piercing damage. If the target is Medium or smaller, the target must succeed on a DC 16 Strength saving throw or be knocked prone.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) slashing damage, plus 10 (3d6) bludgeoning damage if the target is prone."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) slashing damage, plus 10 (3d6) bludgeoning damage if the target is prone.'

