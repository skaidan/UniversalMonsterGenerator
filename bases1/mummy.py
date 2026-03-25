# bases1/mummy.py
"""
Mummy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mummy
"""
from creature_base import GlobalCreatureBaseClass


class Mummy(GlobalCreatureBaseClass):
    """
    Medium undead creature - Mummy
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 8, 'CON': 15, 'INT': 6, 'WIS': 10, 'CHAR': 12, 'armor_class': 11, 'alignment': 'lawful evil Armor Class  11 (natural armor) Hit Points  58 (9d8 + 18) Speed  20 ft. STR 16 (+3) DEX 8 (-1) CON 15 (+2) INT 6 (-2) WIS 10 (+0) CHA 12 (+1) Saving Throws  Wis +2 Damage Vulnerabilities  fire Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'rotting_fist', 'dreadful_glare']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The mummy can use its Dreadful Glare and makes one attack with its rotting fist."""
        return 'The mummy can use its Dreadful Glare and makes one attack with its rotting fist.'

    def rotting_fist_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) necrotic damage. If the target is a creature, it must succeed on a DC 12 Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) necrotic damage. If the target is a creature, it must succeed on a DC 12 Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic."

    def dreadful_glare_attack(self) -> str:
        """The mummy targets one creature it can see within 60 feet of it. If the target can see the mummy, it must succeed on a DC 11 Wisdom saving throw against this magic or become frightened until the end of the mummy's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all mummies (but not mummy lords) for the next 24 hours."""
        return "The mummy targets one creature it can see within 60 feet of it. If the target can see the mummy, it must succeed on a DC 11 Wisdom saving throw against this magic or become frightened until the end of the mummy's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all mummies (but not mummy lords) for the next 24 hours."

