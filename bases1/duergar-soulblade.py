# bases1/duergar-soulblade.py
"""
DuergarSoulblade creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-soulblade
"""
from creature_base import GlobalCreatureBaseClass


class DuergarSoulblade(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Dwarf) creature - DuergarSoulblade
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 10, 'INT': 11, 'WIS': 10, 'CHAR': 12, 'armor_class': 14, 'alignment': 'any alignment Armor Class  14 (leather armor) Hit Points  27 (6d8) Speed  25 ft. STR 11 (+0) DEX 16 (+3) CON 10 (+0) INT 11 (+0) WIS 10 (+0) CHA 12 (+1) Damage Resistances  poison Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

