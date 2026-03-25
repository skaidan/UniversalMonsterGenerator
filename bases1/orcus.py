# bases1/orcus.py
"""
Orcus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orcus
"""
from creature_base import GlobalCreatureBaseClass


class Orcus(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - Orcus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 405, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 14, 'CON': 25, 'INT': 20, 'WIS': 20, 'CHAR': 25, 'armor_class': 17, 'alignment': 'Chaotic Evil Armor Class  17 (natural armor)', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['special_equipment', 'multiattack', 'wand_of_orcus', 'tail', 'necrotic_bolt', 'conjure_undead_(1/day)', 'spellcasting', 'wand_spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def special_equipment(self) -> str:
        """Orcus wields the Wand of Orcus.Legendary Resistance (3/Day). If Orcus fails a saving throw, he can choose to succeed instead.Magic Resistance. Orcus has advantage on saving throws against spells and o"""
        return 'Orcus wields the Wand of Orcus.Legendary Resistance (3/Day). If Orcus fails a saving throw, he can choose to succeed instead.Magic Resistance. Orcus has advantage on saving throws against spells and o'

    def multiattack_attack(self) -> str:
        """Orcus makes three Wand of Orcus, Tail, or Necrotic Bolt attacks."""
        return 'Orcus makes three Wand of Orcus, Tail, or Necrotic Bolt attacks.'

    def wand_of_orcus_attack(self) -> str:
        """Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 24 (3d8 + 11) bludgeoning damage plus 13 (2d12) necrotic damage."""
        return 'Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 24 (3d8 + 11) bludgeoning damage plus 13 (2d12) necrotic damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) force damage plus 9 (2d8) poison damage."""
        return 'Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) force damage plus 9 (2d8) poison damage.'

    def necrotic_bolt_attack(self) -> str:
        """Ranged Spell Attack: +15 to hit, range 120 ft., one target. Hit: 29 (5d8 + 7) necrotic damage."""
        return 'Ranged Spell Attack: +15 to hit, range 120 ft., one target. Hit: 29 (5d8 + 7) necrotic damage.'

    def conjure_undead_(1/day)_attack(self) -> str:
        """While holding the Wand of Orcus, Orcus conjures Undead creatures whose combined average hit points don't exceed 500. These creatures magically rise up from the ground or otherwise form in unoccupied spaces within 300 feet of Orcus and obey his commands until they are destroyed or until he dismisses them as an action."""
        return "While holding the Wand of Orcus, Orcus conjures Undead creatures whose combined average hit points don't exceed 500. These creatures magically rise up from the ground or otherwise form in unoccupied spaces within 300 feet of Orcus and obey his commands until they are destroyed or until he dismisses them as an action."

    def spellcasting_attack(self) -> str:
        """Orcus casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 23):"""
        return 'Orcus casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 23):'

    def wand_spellcasting_attack(self) -> str:
        """While holding the Wand of Orcus, Orcus casts one of the following spells (spell save DC 18), some of which require charges; the wand has 7 charges to fuel these spells, and it regains 1d4 + 3 charges daily at dawn:"""
        return 'While holding the Wand of Orcus, Orcus casts one of the following spells (spell save DC 18), some of which require charges; the wand has 7 charges to fuel these spells, and it regains 1d4 + 3 charges daily at dawn:'

