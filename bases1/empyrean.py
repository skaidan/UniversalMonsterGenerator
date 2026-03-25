# bases1/empyrean.py
"""
Empyrean creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=empyrean
"""
from creature_base import GlobalCreatureBaseClass


class Empyrean(GlobalCreatureBaseClass):
    """
    Huge celestial (Titan) creature - Empyrean
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 313, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 21, 'CON': 30, 'INT': 21, 'WIS': 22, 'CHAR': 27, 'armor_class': 22, 'alignment': 'chaotic good (75 %) or neutral evil (25 %) Armor Class  22 (natural armor) Hit Points  313 (19d12 + 190) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'celestial (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'maul', 'bolt']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The empyrean's innate spellcasting ability is Charisma (spell save DC 23, +15 to hit with spell attacks).It can innately cast the following spells, requiring no material components:At will: greater re"""
        return "The empyrean's innate spellcasting ability is Charisma (spell save DC 23, +15 to hit with spell attacks).It can innately cast the following spells, requiring no material components:At will: greater re"

    def maul_attack(self) -> str:
        """Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 31 (6d6 + 10) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw or be stunned until the end of the empyrean's next turn."""
        return "Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 31 (6d6 + 10) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw or be stunned until the end of the empyrean's next turn."

    def bolt_attack(self) -> str:
        """Ranged Spell Attack: +15 to hit, range 600 ft., one target. Hit: 24 (7d6) damage of one of the following types (empyrean's choice): acid, cold, fire, force, lightning, radiant, or thunder."""
        return "Ranged Spell Attack: +15 to hit, range 600 ft., one target. Hit: 24 (7d6) damage of one of the following types (empyrean's choice): acid, cold, fire, force, lightning, radiant, or thunder."

