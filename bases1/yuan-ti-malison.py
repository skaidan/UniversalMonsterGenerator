# bases1/yuan-ti-malison.py
"""
YuanTiMalison creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-malison
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiMalison(GlobalCreatureBaseClass):
    """
    Medium monstrosity (Shapechanger creature - YuanTiMalison
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 13, 'INT': 14, 'WIS': 12, 'CHAR': 16, 'armor_class': 12, 'alignment': 'Yuan-ti)', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity (Shapechanger', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack_(yuan-ti_form_only)', 'bite', 'scimitar_(yuan-ti_form_only)', 'longbow_(yuan-ti_form_only)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The yuan-ti can use its action to polymorph into a Medium snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doe"""
        return "The yuan-ti can use its action to polymorph into a Medium snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doe"

    def multiattack_(yuan-ti_form_only)_attack(self) -> str:
        """The yuan-ti makes two ranged attacks or two melee attacks, but can use its bite only once."""
        return 'The yuan-ti makes two ranged attacks or two melee attacks, but can use its bite only once.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) poison damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) poison damage.'

    def scimitar_(yuan-ti_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

    def longbow_(yuan-ti_form_only)_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 7 (2d6) poison damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 7 (2d6) poison damage.'

