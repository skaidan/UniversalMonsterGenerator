# bases1/tiamat.py
"""
Tiamat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tiamat
"""
from creature_base import GlobalCreatureBaseClass


class Tiamat(GlobalCreatureBaseClass):
    """
    Gargantuan fiend creature - Tiamat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 615, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 10, 'CON': 30, 'INT': 26, 'WIS': 26, 'CHAR': 28, 'armor_class': 25, 'alignment': 'chaotic evil Armor Class  25 (natural armor) Hit Points  615 (30d20 + 300) Speed  60 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['discorporation', 'multiattack', 'claw', 'tail', 'frightful_presence']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def discorporation(self) -> str:
        """When Tiamat drops to 0 hit points or dies, her body is destroyed but her essence travels back to her domain in the Nine Hells, and she is unable to take physical form for a time.Innate Spellcasting (3"""
        return 'When Tiamat drops to 0 hit points or dies, her body is destroyed but her essence travels back to her domain in the Nine Hells, and she is unable to take physical form for a time.Innate Spellcasting (3'

    def multiattack_attack(self) -> str:
        """Tiamat can use her Frightful Presence. She then makes three attacks: two with her claws and one with her tail."""
        return 'Tiamat can use her Frightful Presence. She then makes three attacks: two with her claws and one with her tail.'

    def claw_attack(self) -> str:
        """Weapon Attack: + 19 to hit, reach 15 ft., one target. Hit: 24 (4d6 + 10) slashing damage."""
        return 'Weapon Attack: + 19 to hit, reach 15 ft., one target. Hit: 24 (4d6 + 10) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: + 19 to hit, reach 25 ft., one target. Hit: 28 (4d8 + 10) piercing damage."""
        return 'Melee Weapon Attack: + 19 to hit, reach 25 ft., one target. Hit: 28 (4d8 + 10) piercing damage.'

    def frightful_presence_attack(self) -> str:
        """Each creature of Tiamat's choice that is within 240 feet of Tiamat and aware of her must succeed on a DC 26 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to Tiamat's Frightful Presence for the next 24 hours."""
        return "Each creature of Tiamat's choice that is within 240 feet of Tiamat and aware of her must succeed on a DC 26 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to Tiamat's Frightful Presence for the next 24 hours."

