# bases1/zariel.py
"""
Zariel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zariel
"""
from creature_base import GlobalCreatureBaseClass


class Zariel(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Zariel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 420, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 24, 'CON': 28, 'INT': 26, 'WIS': 27, 'CHAR': 30, 'armor_class': 21, 'alignment': 'Lawful Evil Armor Class  21 (natural armor) Hit Points  420 (29d10 + 261) Speed  50 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'flail', 'longsword', 'horrid_touch_(recharge_5–6)', 'spellcasting', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede Zariel's darkvision.Legendary Resistance (3/Day). If Zariel fails a saving throw, she can choose to succeed instead.Magic Resistance. Zariel has advantage on saving thr"""
        return "Magical darkness doesn't impede Zariel's darkvision.Legendary Resistance (3/Day). If Zariel fails a saving throw, she can choose to succeed instead.Magic Resistance. Zariel has advantage on saving thr"

    def multiattack_attack(self) -> str:
        """Zariel makes three Flail or Longsword attacks. She can replace one attack with a use of Horrid Touch, if available."""
        return 'Zariel makes three Flail or Longsword attacks. She can replace one attack with a use of Horrid Touch, if available.'

    def flail_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 17 (2d8 + 8) force damage plus 36 (8d8) fire damage."""
        return 'Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 17 (2d8 + 8) force damage plus 36 (8d8) fire damage.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 17 (2d8 + 8) radiant damage, or 19 (2d10 + 8) radiant damage when used with two hands, plus 36 (8d8) fire damage."""
        return 'Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 17 (2d8 + 8) radiant damage, or 19 (2d10 + 8) radiant damage when used with two hands, plus 36 (8d8) fire damage.'

    def horrid_touch_recharge_5_6_attack(self) -> str:
        """Zariel touches one creature within 10 feet of her. The target must succeed on a DC 26 Constitution saving throw or take 44 (8d10) necrotic damage and be poisoned for 1 minute. While poisoned in this way, the target is blinded and deafened. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Zariel touches one creature within 10 feet of her. The target must succeed on a DC 26 Constitution saving throw or take 44 (8d10) necrotic damage and be poisoned for 1 minute. While poisoned in this way, the target is blinded and deafened. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def spellcasting_attack(self) -> str:
        """Zariel casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 26):"""
        return 'Zariel casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 26):'

    def teleport_attack(self) -> str:
        """Zariel teleports, along with any equipment she is wearing or carrying, up to 120 feet to an unoccupied space she can see."""
        return 'Zariel teleports, along with any equipment she is wearing or carrying, up to 120 feet to an unoccupied space she can see.'
