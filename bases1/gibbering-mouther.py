# bases1/gibbering-mouther.py
"""
GibberingMouther creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gibbering-mouther
"""
from creature_base import GlobalCreatureBaseClass


class GibberingMouther(GlobalCreatureBaseClass):
    """
    Medium aberration creature - GibberingMouther
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 8, 'CON': 16, 'INT': 3, 'WIS': 10, 'CHAR': 6, 'armor_class': 9, 'alignment': 'neutral Armor Class  9 Hit Points  67 (9d8 + 27) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aberrant_ground', 'multiattack', 'bites', 'blinding_spittle_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aberrant_ground(self) -> str:
        """The ground in a 10-foot radius around the mouther is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have itsSpeed reduced"""
        return 'The ground in a 10-foot radius around the mouther is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have itsSpeed reduced'

    def multiattack_attack(self) -> str:
        """The gibbering mouther makes one bite attack and, if it can, uses its Blinding Spittle."""
        return 'The gibbering mouther makes one bite attack and, if it can, uses its Blinding Spittle.'

    def bites_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 17 (5d6) piercing damage. If the target is Medium or smaller, it must succeed on a DC 10 Strength saving throw or be knocked prone. If the target is killed by this damage, it is absorbed into the mouther."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 17 (5d6) piercing damage. If the target is Medium or smaller, it must succeed on a DC 10 Strength saving throw or be knocked prone. If the target is killed by this damage, it is absorbed into the mouther.'

    def blinding_spittle_(recharge_5-6)_attack(self) -> str:
        """The mouther spits a chemical glob at a point it can see within 15 feet of it. The glob explodes in a blinding flash of light on impact. Each creature within 5 feet of the flash must succeed on a DC 13 Dexterity saving throw or be blinded until the end of the mouther's next turn."""
        return "The mouther spits a chemical glob at a point it can see within 15 feet of it. The glob explodes in a blinding flash of light on impact. Each creature within 5 feet of the flash must succeed on a DC 13 Dexterity saving throw or be blinded until the end of the mouther's next turn."

