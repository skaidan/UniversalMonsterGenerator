# bases1/druid.py
"""
Druid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=druid
"""
from creature_base import GlobalCreatureBaseClass


class Druid(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Druid
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 12, 'CON': 13, 'INT': 12, 'WIS': 15, 'CHAR': 11, 'armor_class': 11, 'alignment': 'any alignment Armor Class  11 (16 with  barkskin ) Hit Points  27 (5d8 + 5) Speed  30 ft. STR 10 (+0) DEX 12 (+1) CON 13 (+1) INT 12 (+1) WIS 15 (+2) CHA 11 (+0) Skills  Medicine +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['spellcasting', 'quarterstaff']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def spellcasting(self) -> str:
        """The druid is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). It has the following druid spells prepared:Cantrips (at will): druidcraft, pr"""
        return 'The druid is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). It has the following druid spells prepared:Cantrips (at will): druidcraft, pr'

    def quarterstaff_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit (+4 to hit with shillelagh), reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage, 4 (1d8) bludgeoning damage if wielded with two hands, or 6 (1d8 + 2) bludgeoning damage with shillelagh."""
        return 'Melee Weapon Attack: +2 to hit (+4 to hit with shillelagh), reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage, 4 (1d8) bludgeoning damage if wielded with two hands, or 6 (1d8 + 2) bludgeoning damage with shillelagh.'

