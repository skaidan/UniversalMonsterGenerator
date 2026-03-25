# bases1/rakshasa.py
"""
Rakshasa creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rakshasa
"""
from creature_base import GlobalCreatureBaseClass


class Rakshasa(GlobalCreatureBaseClass):
    """
    Medium fiend creature - Rakshasa
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 110, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 17, 'CON': 18, 'INT': 13, 'WIS': 16, 'CHAR': 20, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (natural armor) Hit Points  110 (13d8 + 52) Speed  40 ft. STR 14 (+2) DEX 17 (+3) CON 18 (+4) INT 13 (+1) WIS 16 (+3) CHA 20 (+5) Skills  Deception +10', 'legendary': False, 'size': 'Medium', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['limited_magic_immunity', 'multiattack', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def limited_magic_immunity(self) -> str:
        """The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has advantage on saving throws against all other spells and magical effects.Innate Spellcasting. T"""
        return "The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has advantage on saving throws against all other spells and magical effects.Innate Spellcasting. T"

    def multiattack_attack(self) -> str:
        """The rakshasa makes two claw attacks."""
        return 'The rakshasa makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage, and the target is cursed if it is a creature. The magical curse takes effect whenever the target takes a short or long rest, filling the target's thoughts with horrible images and dreams. The cursed target gains no benefit from finishing a short or long rest. The curse lasts until it is lifted by a remove curse spell or similar magic."""
        return "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage, and the target is cursed if it is a creature. The magical curse takes effect whenever the target takes a short or long rest, filling the target's thoughts with horrible images and dreams. The cursed target gains no benefit from finishing a short or long rest. The curse lasts until it is lifted by a remove curse spell or similar magic."

