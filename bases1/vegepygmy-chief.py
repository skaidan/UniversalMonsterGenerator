# bases1/vegepygmy-chief.py
"""
VegepygmyChief creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vegepygmy-chief
"""
from creature_base import GlobalCreatureBaseClass


class VegepygmyChief(GlobalCreatureBaseClass):
    """
    Small Plant creature - VegepygmyChief
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 14, 'INT': 7, 'WIS': 12, 'CHAR': 9, 'armor_class': 14, 'alignment': 'typically Neutral Armor Class  14 (natural armor) Hit Points  33 (6d6 + 12) Speed  30 ft. STR 14 (+2) DEX 14 (+2) CON 14 (+2) INT 7 (-2) WIS 12 (+1) CHA 9 (-1) Skills  Perception +3', 'legendary': False, 'size': 'Small', 'type': 'Plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['plant_camouflage', 'multiattack', 'claws', 'spear', 'spores_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def plant_camouflage(self) -> str:
        """The vegepygmy has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The vegepygmy regains 5 hit points at the start of its turn. If it takes"""
        return 'The vegepygmy has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The vegepygmy regains 5 hit points at the start of its turn. If it takes'

    def multiattack_attack(self) -> str:
        """The vegepygmy makes two Claw attacks or two melee Spear attacks."""
        return 'The vegepygmy makes two Claw attacks or two melee Spear attacks.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack.'

    def spores_(1/day)_attack(self) -> str:
        """A 15-foot-radius cloud of toxic spores extends out from the vegepygmy. The spores spread around corners. Each creature in that area that isn't a Plant must succeed on a DC 12 Constitution saving throw or be poisoned. While poisoned in this way, a target takes 9 (2d8) poison damage at the start of each of its turns. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return "A 15-foot-radius cloud of toxic spores extends out from the vegepygmy. The spores spread around corners. Each creature in that area that isn't a Plant must succeed on a DC 12 Constitution saving throw or be poisoned. While poisoned in this way, a target takes 9 (2d8) poison damage at the start of each of its turns. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

