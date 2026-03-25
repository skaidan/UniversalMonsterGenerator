# bases1/skulk.py
"""
Skulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=skulk
"""
from creature_base import GlobalCreatureBaseClass


class Skulk(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - Skulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 19, 'CON': 10, 'INT': 10, 'WIS': 7, 'CHAR': 1, 'armor_class': 14, 'alignment': 'typically Chaotic Neutral Armor Class  14 Hit Points  18 (4d8) Speed  30 ft. STR 6 (-2) DEX 19 (+4) CON 10 (+0) INT 10 (+0) WIS 7 (-2) CHA 1 (-5) Saving Throws  Con +2 Skills  Stealth +8 Condition Immunities  blinded Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fallible_invisibility', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fallible_invisibility(self) -> str:
        """The skulk is invisible. This invisibility can be circumvented by three things:Charnel Candles. The skulk appears as a dim, translucent form in the light of a candle made of fat rendered from a corpse """
        return 'The skulk is invisible. This invisibility can be circumvented by three things:Charnel Candles. The skulk appears as a dim, translucent form in the light of a candle made of fat rendered from a corpse '

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) slashing damage plus 3 (1d6) necrotic damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) slashing damage plus 3 (1d6) necrotic damage.'

