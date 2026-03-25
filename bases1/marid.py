# bases1/marid.py
"""
Marid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=marid
"""
from creature_base import GlobalCreatureBaseClass


class Marid(GlobalCreatureBaseClass):
    """
    Large elemental creature - Marid
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 229, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 12, 'CON': 26, 'INT': 18, 'WIS': 17, 'CHAR': 18, 'armor_class': 17, 'alignment': 'chaotic neutral Armor Class  17 (natural armor) Hit Points  229 (17d10 + 136) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'trident', 'water_jet']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The marid can breathe air and water.Elemental Demise. If the marid dies, its body disintegrates into a burst of water and foam, leaving behind only equipment the marid was wearing or carrying.Innate S"""
        return 'The marid can breathe air and water.Elemental Demise. If the marid dies, its body disintegrates into a burst of water and foam, leaving behind only equipment the marid was wearing or carrying.Innate S'

    def multiattack_attack(self) -> str:
        """The marid makes two trident attacks."""
        return 'The marid makes two trident attacks.'

    def trident_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +10 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 13 (2d6 + 6) piercing damage, or 15 (2d8 + 6) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +10 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 13 (2d6 + 6) piercing damage, or 15 (2d8 + 6) piercing damage if used with two hands to make a melee attack.'

    def water_jet_attack(self) -> str:
        """The marid magically shoots water in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw. On a failure, a target takes 21 (6d6) bludgeoning damage and, if it is Huge or smaller, is pushed up to 20 feet away from the marid and knocked prone. On a success, a target takes half the bludgeoning damage, but is neither pushed nor knocked prone."""
        return 'The marid magically shoots water in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw. On a failure, a target takes 21 (6d6) bludgeoning damage and, if it is Huge or smaller, is pushed up to 20 feet away from the marid and knocked prone. On a success, a target takes half the bludgeoning damage, but is neither pushed nor knocked prone.'

