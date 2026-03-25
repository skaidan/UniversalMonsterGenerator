# bases1/clockwork-iron-cobra.py
"""
ClockworkIronCobra creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=clockwork-iron-cobra
"""
from creature_base import GlobalCreatureBaseClass


class ClockworkIronCobra(GlobalCreatureBaseClass):
    """
    Medium Construct creature - ClockworkIronCobra
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 91, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 16, 'CON': 14, 'INT': 3, 'WIS': 10, 'CHAR': 1, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  91 (14d8 + 28) Speed  30 ft. STR 12 (+1) DEX 16 (+3) CON 14 (+2) INT 3 (-4) WIS 10 (+0) CHA 1 (-5) Skills  Stealth +7 Damage Immunities  poison Condition Immunities  charmed', 'legendary': False, 'size': 'Medium', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

