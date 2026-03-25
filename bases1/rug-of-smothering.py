# bases1/rug-of-smothering.py
"""
RugOfSmothering creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rug-of-smothering
"""
from creature_base import GlobalCreatureBaseClass


class RugOfSmothering(GlobalCreatureBaseClass):
    """
    Large construct creature - RugOfSmothering
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 14, 'CON': 10, 'INT': 1, 'WIS': 3, 'CHAR': 1, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  33 (6d10) Speed  10 ft. STR 17 (+3) DEX 14 (+2) CON 10 (+0) INT 1 (-5) WIS 3 (-4) CHA 1 (-5) Damage Immunities  poison', 'legendary': False, 'size': 'Large', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['antimagic_susceptibility', 'smother']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def antimagic_susceptibility(self) -> str:
        """The rug is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the rug must succeed on a Constitution saving throw against the caster's spell save DC or fall unconsciou"""
        return "The rug is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the rug must succeed on a Constitution saving throw against the caster's spell save DC or fall unconsciou"

    def smother_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one Medium or smaller creature. Hit: The creature is grappled (escape DC 13). Until this grapple ends, the target is restrained, blinded, and at risk of suffocating, and the rug can't smother another target. In addition, at the start of each of the target's turns, the target takes 10 (2d6 + 3) bludgeoning damage."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one Medium or smaller creature. Hit: The creature is grappled (escape DC 13). Until this grapple ends, the target is restrained, blinded, and at risk of suffocating, and the rug can't smother another target. In addition, at the start of each of the target's turns, the target takes 10 (2d6 + 3) bludgeoning damage."

