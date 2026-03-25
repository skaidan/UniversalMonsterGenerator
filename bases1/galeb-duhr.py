# bases1/galeb-duhr.py
"""
GalebDuhr creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=galeb-duhr
"""
from creature_base import GlobalCreatureBaseClass


class GalebDuhr(GlobalCreatureBaseClass):
    """
    Medium elemental creature - GalebDuhr
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 14, 'CON': 20, 'INT': 11, 'WIS': 12, 'CHAR': 11, 'armor_class': 16, 'alignment': 'neutral Armor Class  16 (natural armor) Hit Points  85 (9d8 + 45) Speed  15 ft. (30 ft. when rolling', 'legendary': False, 'size': 'Medium', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'slam', 'animate_boulders_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the galeb duhr remains motionless, it is indistinguishable from a normal boulder.Rolling Charge. If the galeb duhr rolls at least 20 feet straight toward a target and then hits it with a slam at"""
        return 'While the galeb duhr remains motionless, it is indistinguishable from a normal boulder.Rolling Charge. If the galeb duhr rolls at least 20 feet straight toward a target and then hits it with a slam at'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage.'

    def animate_boulders_(1/day)_attack(self) -> str:
        """The galeb duhr magically animates up to two boulders it can see within 60 feet of it. A boulder has statistics like those of a galeb duhr, except it has Intelligence 1 and Charisma 1, it can't be charmed or frightened, and it lacks this action option. A boulder remains animated as long as the galeb duhr maintains concentration, up to 1 minute (as if concentrating on a spell)."""
        return "The galeb duhr magically animates up to two boulders it can see within 60 feet of it. A boulder has statistics like those of a galeb duhr, except it has Intelligence 1 and Charisma 1, it can't be charmed or frightened, and it lacks this action option. A boulder remains animated as long as the galeb duhr maintains concentration, up to 1 minute (as if concentrating on a spell)."

