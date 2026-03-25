# bases1/dragonbone-golem.py
"""
DragonboneGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonbone-golem
"""
from creature_base import GlobalCreatureBaseClass


class DragonboneGolem(GlobalCreatureBaseClass):
    """
    Large Construct creature - DragonboneGolem
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 161, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 10, 'CON': 17, 'INT': 3, 'WIS': 11, 'CHAR': 10, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  161 (19d10 + 57) Speed  40 ft. STR 20 (+5) DEX 10 (+0) CON 17 (+3) INT 3 (-4) WIS 11 (+0) CHA 10 (+0) Damage Immunities  poison Condition Immunities  charmed', 'legendary': False, 'size': 'Large', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

