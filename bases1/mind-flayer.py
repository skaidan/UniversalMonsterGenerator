# bases1/mind-flayer.py
"""
MindFlayer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mind-flayer
"""
from creature_base import GlobalCreatureBaseClass


class MindFlayer(GlobalCreatureBaseClass):
    """
    Medium aberration creature - MindFlayer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 71, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 12, 'CON': 12, 'INT': 19, 'WIS': 17, 'CHAR': 17, 'armor_class': 15, 'alignment': 'lawful evil Armor Class  15 (breastplate) Hit Points  71 (13d8 + 13) Speed  30 ft. STR 11 (+0) DEX 12 (+1) CON 12 (+1) INT 19 (+4) WIS 17 (+3) CHA 17 (+3) Saving Throws  Int +7', 'legendary': False, 'size': 'Medium', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'tentacles', 'extract_brain', 'mind_blast_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The mind flayer has advantage on saving throws against spells and other magical effects.Innate Spellcasting (Psionics). The mind flayer's innate spellcasting ability is Intelligence (spell save DC 15)"""
        return "The mind flayer has advantage on saving throws against spells and other magical effects.Innate Spellcasting (Psionics). The mind flayer's innate spellcasting ability is Intelligence (spell save DC 15)"

    def tentacles_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 15 (2d10 + 4) psychic damage. If the target is Medium or smaller, it is grappled (escape DC 15) and must succeed on a DC 15 Intelligence saving throw or be stunned until this grapple ends."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 15 (2d10 + 4) psychic damage. If the target is Medium or smaller, it is grappled (escape DC 15) and must succeed on a DC 15 Intelligence saving throw or be stunned until this grapple ends.'

    def extract_brain_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one incapacitated humanoid grappled by the mind flayer. Hit: The target takes 55 (10d10) piercing damage. If this damage reduces the target to 0 hit points, the mind flayer kills the target by extracting and devouring its brain."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one incapacitated humanoid grappled by the mind flayer. Hit: The target takes 55 (10d10) piercing damage. If this damage reduces the target to 0 hit points, the mind flayer kills the target by extracting and devouring its brain.'

    def mind_blast_(recharge_5–6)_attack(self) -> str:
        """The mind flayer magically emits psychic energy in a 60-foot cone. Each creature in that area must succeed on a DC 15 Intelligence saving throw or take 22 (4d8 + 4) psychic damage and be stunned for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The mind flayer magically emits psychic energy in a 60-foot cone. Each creature in that area must succeed on a DC 15 Intelligence saving throw or take 22 (4d8 + 4) psychic damage and be stunned for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

