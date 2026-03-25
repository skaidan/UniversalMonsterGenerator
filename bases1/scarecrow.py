# bases1/scarecrow.py
"""
Scarecrow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scarecrow
"""
from creature_base import GlobalCreatureBaseClass


class Scarecrow(GlobalCreatureBaseClass):
    """
    Medium construct creature - Scarecrow
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 36, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 13, 'CON': 11, 'INT': 10, 'WIS': 10, 'CHAR': 13, 'armor_class': 11, 'alignment': 'chaotic evil Armor Class  11 Hit Points  36 (8d8) Speed  30 ft. STR 11 (+0) DEX 13 (+1) CON 11 (+0) INT 10 (+0) WIS 10 (+0) CHA 13 (+1) Damage Vulnerabilities  fire Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'multiattack', 'claw', 'terrifying_glare']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the scarecrow remains motionless, it is indistinguishable from an ordinary, inanimate scarecrow."""
        return 'While the scarecrow remains motionless, it is indistinguishable from an ordinary, inanimate scarecrow.'

    def multiattack_attack(self) -> str:
        """The scarecrow makes two claw attacks."""
        return 'The scarecrow makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage. If the target is a creature, it must succeed on a DC 11 Wisdom saving throw or be frightened until the end of the scarecrow's next turn."""
        return "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage. If the target is a creature, it must succeed on a DC 11 Wisdom saving throw or be frightened until the end of the scarecrow's next turn."

    def terrifying_glare_attack(self) -> str:
        """The scarecrow targets one creature it can see within 30 feet of it. If the target can see the scarecrow, the target must succeed on a DC 11 Wisdom saving throw or be magically frightened until the end of the scarecrow's next turn. The frightened target is paralyzed."""
        return "The scarecrow targets one creature it can see within 30 feet of it. If the target can see the scarecrow, the target must succeed on a DC 11 Wisdom saving throw or be magically frightened until the end of the scarecrow's next turn. The frightened target is paralyzed."

