# bases1/drake-companion.py
"""
DrakeCompanion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drake-companion
"""
from creature_base import GlobalCreatureBaseClass


class DrakeCompanion(GlobalCreatureBaseClass):
    """
    Small dragon creature - DrakeCompanion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 15, 'INT': 8, 'WIS': 14, 'CHAR': 8, 'armor_class': 14, 'alignment': '- Armor Class  14 + PB (natural armor) Hit Points  5 + five times your ranger level (the drake has a number of Hit Dice [d10s] equal to your ranger level) Speed  40 ft. STR 16 (+3) DEX 12 (+1) CON 15 (+2) INT 8 (-1) WIS 14 (+2) CHA 8 (-1) Saving Throws  Dex +1 plus PB', 'legendary': False, 'size': 'Small', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['draconic_essence', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def draconic_essence(self) -> str:
        """When you summon the drake, choose a damage type: acid, cold, fire, lightning, or poison. The chosen type determines the drake's damage immunity and the damage of its Infused Strikes trait."""
        return "When you summon the drake, choose a damage type: acid, cold, fire, lightning, or poison. The chosen type determines the drake's damage immunity and the damage of its Infused Strikes trait."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 plus PB to hit, reach 5 ft., one target. Hit: 1d6 plus PB piercing damage."""
        return 'Melee Weapon Attack: +3 plus PB to hit, reach 5 ft., one target. Hit: 1d6 plus PB piercing damage.'

