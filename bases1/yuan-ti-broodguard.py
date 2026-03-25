# bases1/yuan-ti-broodguard.py
"""
YuanTiBroodguard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-broodguard
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiBroodguard(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - YuanTiBroodguard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 14, 'INT': 6, 'WIS': 11, 'CHAR': 4, 'armor_class': 14, 'alignment': 'typically Neutral Evil Armor Class  14 (natural armor) Hit Points  45 (7d8 + 14) Speed  30 ft. STR 15 (+2) DEX 14 (+2) CON 14 (+2) INT 6 (-2) WIS 11 (+0) CHA 4 (-3) Saving Throws  Str +4', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['reckless', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def reckless(self) -> str:
        """At the start of its turn, the broodguard can gain advantage on all melee weapon attack rolls it makes during that turn, but attack rolls against it have advantage until the start of its next turn."""
        return 'At the start of its turn, the broodguard can gain advantage on all melee weapon attack rolls it makes during that turn, but attack rolls against it have advantage until the start of its next turn.'

    def multiattack_attack(self) -> str:
        """The broodguard makes one Bite attack and two Claw attacks."""
        return 'The broodguard makes one Bite attack and two Claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.'

