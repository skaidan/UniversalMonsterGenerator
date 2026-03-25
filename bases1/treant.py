# bases1/treant.py
"""
Treant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=treant
"""
from creature_base import GlobalCreatureBaseClass


class Treant(GlobalCreatureBaseClass):
    """
    Huge plant creature - Treant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 138, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 8, 'CON': 21, 'INT': 12, 'WIS': 16, 'CHAR': 12, 'armor_class': 16, 'alignment': 'chaotic good Armor Class  16 (natural armor) Hit Points  138 (12d12 + 60) Speed  30 ft. STR 23 (+6) DEX 8 (-1) CON 21 (+5) INT 12 (+1) WIS 16 (+3) CHA 12 (+1) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Huge', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'multiattack', 'slam', 'rock', 'animate_trees_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the treant remains motionless, it is indistinguishable from a normal tree.Siege Monster. The treant deals double damage to objects and structures."""
        return 'While the treant remains motionless, it is indistinguishable from a normal tree.Siege Monster. The treant deals double damage to objects and structures.'

    def multiattack_attack(self) -> str:
        """The treant makes two slam attacks."""
        return 'The treant makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 16 (3d6 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 16 (3d6 + 6) bludgeoning damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +10 to hit, range 60/180 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage."""
        return 'Ranged Weapon Attack: +10 to hit, range 60/180 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage.'

    def animate_trees_(1/day)_attack(self) -> str:
        """The treant magically animates one or two trees it can see within 60 feet of it. These trees have the same statistics as a treant, except they have Intelligence and Charisma scores of 1, they can't speak, and they have only the Slam action option. An animated tree acts as an ally of the treant. The tree remains animate for 1 day or until it dies; until the treant dies or is more than 120 feet from the tree; or until the treant takes a bonus action to turn it back into an inanimate tree. The tree then takes root if possible."""
        return "The treant magically animates one or two trees it can see within 60 feet of it. These trees have the same statistics as a treant, except they have Intelligence and Charisma scores of 1, they can't speak, and they have only the Slam action option. An animated tree acts as an ally of the treant. The tree remains animate for 1 day or until it dies; until the treant dies or is more than 120 feet from the tree; or until the treant takes a bonus action to turn it back into an inanimate tree. The tree then takes root if possible."

