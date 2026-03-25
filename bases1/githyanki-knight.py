# bases1/githyanki-knight.py
"""
GithyankiKnight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githyanki-knight
"""
from creature_base import GlobalCreatureBaseClass


class GithyankiKnight(GlobalCreatureBaseClass):
    """
    Medium humanoid (Gith) creature - GithyankiKnight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 91, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 15, 'INT': 14, 'WIS': 14, 'CHAR': 15, 'armor_class': 18, 'alignment': 'lawful evil Armor Class  18 (plate) Hit Points  91 (14d8 + 28) Speed  30 ft. STR 16 (+3) DEX 14 (+2) CON 15 (+2) INT 14 (+2) WIS 14 (+2) CHA 15 (+2) Saving Throws  Con +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting_(psionics)', 'multiattack', 'silver_greatsword']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting_(psionics)(self) -> str:
        """The githyanki's innate spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no components:At will: mage hand (the"""
        return "The githyanki's innate spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no components:At will: mage hand (the"

    def multiattack_attack(self) -> str:
        """The githyanki makes two silver greatsword attacks."""
        return 'The githyanki makes two silver greatsword attacks.'

    def silver_greatsword_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage plus 10 (3d6) psychic damage. This is a magic weapon attack. On a critical hit against a target in an astral body (as with the astral projection spell), the githyanki can cut the silvery cord that tethers the target to its material body, instead of dealing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage plus 10 (3d6) psychic damage. This is a magic weapon attack. On a critical hit against a target in an astral body (as with the astral projection spell), the githyanki can cut the silvery cord that tethers the target to its material body, instead of dealing damage.'

