# bases1/mummy-lord.py
"""
MummyLord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mummy-lord
"""
from creature_base import GlobalCreatureBaseClass


class MummyLord(GlobalCreatureBaseClass):
    """
    Medium undead creature - MummyLord
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 97, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 17, 'INT': 11, 'WIS': 18, 'CHAR': 16, 'armor_class': 17, 'alignment': 'lawful evil Armor Class  17 (natural armor) Hit Points  97 (13d8 + 39) Speed  20 ft. STR 18 (+4) DEX 10 (+0) CON 17 (+3) INT 11 (+0) WIS 18 (+4) CHA 16 (+3) Saving Throws  Con +8', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'rotting_fist', 'dreadful_glare']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The mummy lord has advantage on saving throws against spells and other magical effects.Rejuvenation. A destroyed mummy lord gains a new body in 24 hours if its heart is intact, regaining all its hit p"""
        return 'The mummy lord has advantage on saving throws against spells and other magical effects.Rejuvenation. A destroyed mummy lord gains a new body in 24 hours if its heart is intact, regaining all its hit p'

    def multiattack_attack(self) -> str:
        """The mummy can use its Dreadful Glare and makes one attack with its rotting fist."""
        return 'The mummy can use its Dreadful Glare and makes one attack with its rotting fist.'

    def rotting_fist_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage plus 21 (6d6) necrotic damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic."""
        return "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage plus 21 (6d6) necrotic damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic."

    def dreadful_glare_attack(self) -> str:
        """The mummy lord targets one creature it can see within 60 feet of it. If the target can see the mummy lord, it must succeed on a DC 16 Wisdom saving throw against this magic or become frightened until the end of the mummy's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all mummies and mummy lords for the next 24 hours."""
        return "The mummy lord targets one creature it can see within 60 feet of it. If the target can see the mummy lord, it must succeed on a DC 16 Wisdom saving throw against this magic or become frightened until the end of the mummy's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all mummies and mummy lords for the next 24 hours."

