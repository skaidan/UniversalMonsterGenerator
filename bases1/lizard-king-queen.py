# bases1/lizard-king-queen.py
"""
LizardKingQueen creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lizard-king-queen
"""
from creature_base import GlobalCreatureBaseClass


class LizardKingQueen(GlobalCreatureBaseClass):
    """
    Medium humanoid (Lizardfolk) creature - LizardKingQueen
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 78, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 15, 'INT': 11, 'WIS': 11, 'CHAR': 15, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  78 (12d8 + 24) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Lizardfolk)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'multiattack', 'bite', 'claws', 'trident']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The lizardfolk can hold its breath for 15 minutes.Skewer. Once per turn, when the lizardfolk makes a melee attack with its trident and hits, the target takes an extra 10 (3d6) damage, and the lizardfo"""
        return 'The lizardfolk can hold its breath for 15 minutes.Skewer. Once per turn, when the lizardfolk makes a melee attack with its trident and hits, the target takes an extra 10 (3d6) damage, and the lizardfo'

    def multiattack_attack(self) -> str:
        """The lizardfolk makes two attacks: one with its bite and one with its claws or trident or two melee attacks with its trident."""
        return 'The lizardfolk makes two attacks: one with its bite and one with its claws or trident or two melee attacks with its trident.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) slashing damage.'

    def trident_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack.'

