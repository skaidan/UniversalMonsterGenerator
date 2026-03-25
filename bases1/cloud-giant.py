# bases1/cloud-giant.py
"""
CloudGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cloud-giant
"""
from creature_base import GlobalCreatureBaseClass


class CloudGiant(GlobalCreatureBaseClass):
    """
    Huge giant creature - CloudGiant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 200, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 10, 'CON': 22, 'INT': 12, 'WIS': 16, 'CHAR': 16, 'armor_class': 14, 'alignment': 'neutral good (50 %) or neutral evil (50 %) Armor Class  14 (natural armor) Hit Points  200 (16d12 + 96) Speed  40 ft. STR 27 (+8) DEX 10 (+0) CON 22 (+6) INT 12 (+1) WIS 16 (+3) CHA 16 (+3) Saving Throws  Con +10', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'multiattack', 'morningstar', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The giant has advantage on Wisdom (Perception) checks that rely on smell.InnateSpellcasting. The giant's innate spellcasting ability is Charisma. It can innately cast the following spells, requiring n"""
        return "The giant has advantage on Wisdom (Perception) checks that rely on smell.InnateSpellcasting. The giant's innate spellcasting ability is Charisma. It can innately cast the following spells, requiring n"

    def multiattack_attack(self) -> str:
        """The giant makes two morningstar attacks."""
        return 'The giant makes two morningstar attacks.'

    def morningstar_attack(self) -> str:
        """Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) piercing damage."""
        return 'Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) piercing damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +12 to hit, range 60/240 ft., one target. Hit: 30 (4d10 + 8) bludgeoning damage."""
        return 'Ranged Weapon Attack: +12 to hit, range 60/240 ft., one target. Hit: 30 (4d10 + 8) bludgeoning damage.'

