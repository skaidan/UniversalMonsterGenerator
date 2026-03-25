# bases1/merregon.py
"""
Merregon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merregon
"""
from creature_base import GlobalCreatureBaseClass


class Merregon(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Merregon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 17, 'INT': 6, 'WIS': 12, 'CHAR': 8, 'armor_class': 16, 'alignment': 'typically Lawful Evil Armor Class  16 (natural armor) Hit Points  45 (6d8 + 18) Speed  30 ft. STR 18 (+4) DEX 14 (+2) CON 17 (+3) INT 6 (-2) WIS 12 (+1) CHA 8 (-1) Damage Resistances  cold; bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'halberd', 'heavy_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the merregon's darkvision.Magic Resistance. The merregon has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the merregon's darkvision.Magic Resistance. The merregon has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The merregon makes three Halberd attacks."""
        return 'The merregon makes three Halberd attacks.'

    def halberd_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) slashing damage.'

    def heavy_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 100/400 ft., one target. Hit: 7 (1d10 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 100/400 ft., one target. Hit: 7 (1d10 + 2) piercing damage.'

