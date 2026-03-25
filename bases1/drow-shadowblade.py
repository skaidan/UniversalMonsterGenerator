# bases1/drow-shadowblade.py
"""
DrowShadowblade creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-shadowblade
"""
from creature_base import GlobalCreatureBaseClass


class DrowShadowblade(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Elf) creature - DrowShadowblade
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 150, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 21, 'CON': 16, 'INT': 12, 'WIS': 14, 'CHAR': 13, 'armor_class': 17, 'alignment': 'any alignment Armor Class  17 (studded leather) Hit Points  150 (20d8 + 60) Speed  30 ft. STR 14 (+2) DEX 21 (+5) CON 16 (+3) INT 12 (+1) WIS 14 (+2) CHA 13 (+1) Saving Throws  Dex +9', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'shadow_sword', 'hand_crossbow', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the drow's darkvision.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in """
        return "Magical darkness doesn't impede the drow's darkvision.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in "

    def multiattack_attack(self) -> str:
        """The drow makes three Shadow Sword attacks. One of the attacks can be replaced by a Hand Crossbow attack. The drow can also use Spellcasting to cast darkness."""
        return 'The drow makes three Shadow Sword attacks. One of the attacks can be replaced by a Hand Crossbow attack. The drow can also use Spellcasting to cast darkness.'

    def shadow_sword_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +9 to hit, reach 5 ft. or range 30/60 ft., one target. Hit: 27 (7d6 + 5) necrotic damage."""
        return 'Melee or Ranged Weapon Attack: +9 to hit, reach 5 ft. or range 30/60 ft., one target. Hit: 27 (7d6 + 5) necrotic damage.'

    def hand_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +9 to hit, range 30/120 ft., one target. Hit: 8 (1d6 + 5) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target regains consciousness if it takes damage or if another creature takes an action to shake it."""
        return 'Ranged Weapon Attack: +9 to hit, range 30/120 ft., one target. Hit: 8 (1d6 + 5) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target regains consciousness if it takes damage or if another creature takes an action to shake it.'

    def spellcasting_attack(self) -> str:
        """The drow casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 13):"""
        return 'The drow casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 13):'

