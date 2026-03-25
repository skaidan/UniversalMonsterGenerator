# bases1/babau.py
"""
Babau creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=babau
"""
from creature_base import GlobalCreatureBaseClass


class Babau(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Babau
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 82, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 16, 'CON': 16, 'INT': 11, 'WIS': 12, 'CHAR': 13, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  82 (11d8 + 33) Speed  40 ft. STR 19 (+4) DEX 16 (+3) CON 16 (+3) INT 11 (+0) WIS 12 (+1) CHA 13 (+1) Skills  Perception +5', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'claw', 'spellcasting', 'weakening_gaze']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The babau makes two Claw attacks. It can replace one attack with a use of Spellcasting or Weakening Gaze."""
        return 'The babau makes two Claw attacks. It can replace one attack with a use of Spellcasting or Weakening Gaze.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) slashing damage plus 2 (1d4) acid damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) slashing damage plus 2 (1d4) acid damage.'

    def spellcasting_attack(self) -> str:
        """The babau casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 11):"""
        return 'The babau casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 11):'

    def weakening_gaze_attack(self) -> str:
        """The babau targets one creature that it can see within 20 feet of it. The target must make a DC 13 Constitution saving throw. On a failed save, the target deals only half damage with weapon attacks that use Strength for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The babau targets one creature that it can see within 20 feet of it. The target must make a DC 13 Constitution saving throw. On a failed save, the target deals only half damage with weapon attacks that use Strength for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

