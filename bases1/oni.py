# bases1/oni.py
"""
Oni creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=oni
"""
from creature_base import GlobalCreatureBaseClass


class Oni(GlobalCreatureBaseClass):
    """
    Large giant creature - Oni
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 110, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 11, 'CON': 16, 'INT': 14, 'WIS': 12, 'CHAR': 15, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (chain mail) Hit Points  110 (13d10 + 39) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'claw_(oni_form_only)', 'glaive', 'change_shape']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The oni's innate spellcasting ability is Charisma (spell save DC 13). The oni can innately cast the following spells, requiring no material components:At will: darkness, invisibility1/day each: charm """
        return "The oni's innate spellcasting ability is Charisma (spell save DC 13). The oni can innately cast the following spells, requiring no material components:At will: darkness, invisibility1/day each: charm "

    def multiattack_attack(self) -> str:
        """The oni makes two attacks, either with its claws or its glaive."""
        return 'The oni makes two attacks, either with its claws or its glaive.'

    def claw_(oni_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage.'

    def glaive_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) slashing damage, or 9 (1d10 + 4) slashing damage in Small or Medium form."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) slashing damage, or 9 (1d10 + 4) slashing damage in Small or Medium form.'

    def change_shape_attack(self) -> str:
        """The oni magically polymorphs into a Small or Medium humanoid, into a Large giant, or back into its true form. Other than its size, its statistics are the same in each form. The only equipment that is transformed is its glaive, which shrinks so that it can be wielded in humanoid form. If the oni dies, it reverts to its true form, and its glaive reverts to its normal size."""
        return 'The oni magically polymorphs into a Small or Medium humanoid, into a Large giant, or back into its true form. Other than its size, its statistics are the same in each form. The only equipment that is transformed is its glaive, which shrinks so that it can be wielded in humanoid form. If the oni dies, it reverts to its true form, and its glaive reverts to its normal size.'

