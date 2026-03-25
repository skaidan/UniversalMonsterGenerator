# bases1/darkling.py
"""
Darkling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=darkling
"""
from creature_base import GlobalCreatureBaseClass


class Darkling(GlobalCreatureBaseClass):
    """
    Small Fey creature - Darkling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 16, 'CON': 12, 'INT': 10, 'WIS': 12, 'CHAR': 10, 'armor_class': 14, 'alignment': 'typically Chaotic Neutral Armor Class  14 (leather armor) Hit Points  13 (3d6 + 3) Speed  30 ft. STR 9 (-1) DEX 16 (+3) CON 12 (+1) INT 10 (+0) WIS 12 (+1) CHA 10 (+0) Skills  Acrobatics +5', 'legendary': False, 'size': 'Small', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_flash', 'dagger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_flash(self) -> str:
        """When the darkling dies, nonmagical light flashes out from it in a 10-foot radius as its body and possessions, other than metal or magic objects, burn to ash. Any creature in that area must succeed on """
        return 'When the darkling dies, nonmagical light flashes out from it in a 10-foot radius as its body and possessions, other than metal or magic objects, burn to ash. Any creature in that area must succeed on '

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) necrotic damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) necrotic damage.'

