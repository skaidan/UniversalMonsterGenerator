# bases1/drow-favored-consort.py
"""
DrowFavoredConsort creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-favored-consort
"""
from creature_base import GlobalCreatureBaseClass


class DrowFavoredConsort(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Elf creature - DrowFavoredConsort
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 240, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 20, 'CON': 16, 'INT': 18, 'WIS': 15, 'CHAR': 18, 'armor_class': 15, 'alignment': 'Wizard)', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Elf', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'multiattack', 'scimitar', 'arcane_eruption', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in sunlight, the drow has disadvantage on attack rolls, as well as on W"""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in sunlight, the drow has disadvantage on attack rolls, as well as on W"

    def multiattack_attack(self) -> str:
        """The drow makes three Scimitar or Arcane Eruption attacks. The drow can replace one of the attacks with a use of Spellcasting."""
        return 'The drow makes three Scimitar or Arcane Eruption attacks. The drow can replace one of the attacks with a use of Spellcasting.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) slashing damage plus 27 (6d8) poison damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 8 (1d6 + 5) slashing damage plus 27 (6d8) poison damage.'

    def arcane_eruption_attack(self) -> str:
        """Ranged Spell Attack: +10 to hit, range 120 ft., one target. Hit: 36 (8d8) force damage, and the drow can push the target up to 10 feet away if it is a Large or smaller creature."""
        return 'Ranged Spell Attack: +10 to hit, range 120 ft., one target. Hit: 36 (8d8) force damage, and the drow can push the target up to 10 feet away if it is a Large or smaller creature.'

    def spellcasting_attack(self) -> str:
        """The drow casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 18):"""
        return 'The drow casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 18):'

