# bases1/undead-spirit.py
"""
UndeadSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=undead-spirit
"""
from creature_base import GlobalCreatureBaseClass


class UndeadSpirit(GlobalCreatureBaseClass):
    """
    Medium undead creature - UndeadSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 30, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 16, 'CON': 15, 'INT': 4, 'WIS': 10, 'CHAR': 9, 'armor_class': 11, 'alignment': '- Armor Class  11 + the level of the spell (natural armor) Hit Points  30 (Ghostly and Putrid only) or 20 (Skeletal only) + 10 for each spell level above 3rd Speed  30 ft.; fly 40 ft. (hover) (Ghostly only) STR 12 (+1) DEX 16 (+3) CON 15 (+2) INT 4 (-3) WIS 10 (+0) CHA 9 (-1) Damage Immunities  necrotic', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

