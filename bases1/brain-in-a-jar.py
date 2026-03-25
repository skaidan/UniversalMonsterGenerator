# bases1/brain-in-a-jar.py
"""
BrainInAJar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=brain-in-a-jar
"""
from creature_base import GlobalCreatureBaseClass


class BrainInAJar(GlobalCreatureBaseClass):
    """
    Small undead creature - BrainInAJar
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 55, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 3, 'CON': 15, 'INT': 19, 'WIS': 10, 'CHAR': 15, 'armor_class': 11, 'alignment': 'any alignment Armor Class  11 (natural armor) Hit Points  55 (10d6 + 20) Speed  0 ft.', 'legendary': False, 'size': 'Small', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['detect_sentience', 'chill_touch_(cantrip)', 'mind_blast_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def detect_sentience(self) -> str:
        """The brain can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a m"""
        return 'The brain can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a m'

    def chill_touch_(cantrip)_attack(self) -> str:
        """Ranged Spell Attack: +6 to hit, range 120 ft., one creature. Hit: 13 (3d8) necrotic damage, and the target can't regain hit points until the start of the brain's next turn. If the target is undead, it also has disadvantage on attack rolls against the brain until the end of the brain's next turn."""
        return "Ranged Spell Attack: +6 to hit, range 120 ft., one creature. Hit: 13 (3d8) necrotic damage, and the target can't regain hit points until the start of the brain's next turn. If the target is undead, it also has disadvantage on attack rolls against the brain until the end of the brain's next turn."

    def mind_blast_(recharge_5–6)_attack(self) -> str:
        """The brain magically emits psychic energy in a 60-foot cone. Each creature in that area must succeed on a DC 14 Intelligence saving throw or take 17 (3d8 + 4) psychic damage and be stunned for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The brain magically emits psychic energy in a 60-foot cone. Each creature in that area must succeed on a DC 14 Intelligence saving throw or take 17 (3d8 + 4) psychic damage and be stunned for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

