# bases1/elemental-spirit.py
"""
ElementalSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elemental-spirit
"""
from creature_base import GlobalCreatureBaseClass


class ElementalSpirit(GlobalCreatureBaseClass):
    """
    Medium elemental creature - ElementalSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 17, 'INT': 4, 'WIS': 10, 'CHAR': 16, 'armor_class': 11, 'alignment': '- Armor Class  11 + the level of the spell (natural armor) Hit Points  50 + 10 for each spell level above 4th Speed  40 ft.; burrow 40 ft. (Earth only); fly 40 ft. (hover) (Air only); swim 40 ft. (Water only) STR 18 (+4) DEX 15 (+2) CON 17 (+3) INT 4 (-3) WIS 10 (+0) CHA 16 (+3) Damage Resistances  acid (Water only); lightning and thunder (Air only); piercing and slashing (Earth only) Damage Immunities  poison; fire (Fire only) Condition Immunities  exhaustion', 'legendary': False, 'size': 'Medium', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

