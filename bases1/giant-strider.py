# bases1/giant-strider.py
"""
GiantStrider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-strider
"""
from creature_base import GlobalCreatureBaseClass


class GiantStrider(GlobalCreatureBaseClass):
    """
    Large Elemental creature - GiantStrider
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 14, 'INT': 4, 'WIS': 12, 'CHAR': 6, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  22 (3d10 + 6) Speed  50 ft. STR 18 (+4) DEX 13 (+1) CON 14 (+2) INT 4 (-3) WIS 12 (+1) CHA 6 (-2) Damage Immunities  fire Senses  passive Perception 11 Languages  — Challenge  1 (200 XP) \xa0 \xa0  Proficiency Bonus  +2 Fire Absorption . Whenever the giant strider is subjected to fire damage', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fire_absorption', 'bite', 'fire_burst_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fire_absorption(self) -> str:
        """Whenever the giant strider is subjected to fire damage, it takes no damage and regains a number of hit points equal to half the fire damage dealt."""
        return 'Whenever the giant strider is subjected to fire damage, it takes no damage and regains a number of hit points equal to half the fire damage dealt.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.'

    def fire_burst_(recharge_5–6)_attack(self) -> str:
        """The giant strider hurls a gout of flame at a point it can see within 60 feet of it. Each creature in a 10-foot-radius sphere centered on that point must make a DC 12 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one. The fire spreads around corners, and it ignites flammable objects in that area that aren't being worn or carried"""
        return "The giant strider hurls a gout of flame at a point it can see within 60 feet of it. Each creature in a 10-foot-radius sphere centered on that point must make a DC 12 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one. The fire spreads around corners, and it ignites flammable objects in that area that aren't being worn or carried"

