# bases1/mimic.py
"""
Mimic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mimic
"""
from creature_base import GlobalCreatureBaseClass


class Mimic(GlobalCreatureBaseClass):
    """
    Medium monstrosity (Shapechanger) creature - Mimic
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 15, 'INT': 5, 'WIS': 13, 'CHAR': 8, 'armor_class': 12, 'alignment': 'neutral Armor Class  12 (natural armor) Hit Points  58 (9d8 + 18) Speed  15 ft. STR 17 (+3) DEX 12 (+1) CON 15 (+2) INT 5 (-3) WIS 13 (+1) CHA 8 (-1) Skills  Stealth +5 Damage Immunities  acid Condition Immunities  prone Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity (Shapechanger)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'pseudopod', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The mimic can use its action to polymorph into an object or back into its true, amorphous form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It """
        return "The mimic can use its action to polymorph into an object or back into its true, amorphous form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It "

    def pseudopod_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage. If the mimic is in object form, the target is subjected to its Adhesive trait."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage. If the mimic is in object form, the target is subjected to its Adhesive trait.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) acid damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) acid damage.'

