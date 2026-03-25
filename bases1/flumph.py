# bases1/flumph.py
"""
Flumph creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flumph
"""
from creature_base import GlobalCreatureBaseClass


class Flumph(GlobalCreatureBaseClass):
    """
    Small aberration creature - Flumph
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 15, 'CON': 10, 'INT': 14, 'WIS': 14, 'CHAR': 11, 'armor_class': 12, 'alignment': 'lawful good Armor Class  12 Hit Points  7 (2d6) Speed  5 ft.', 'legendary': False, 'size': 'Small', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['advanced_telepathy', 'tendrils', 'stench_spray_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def advanced_telepathy(self) -> str:
        """The flumph can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy.Prone Deficiency. If the flumph is knoc"""
        return "The flumph can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy.Prone Deficiency. If the flumph is knoc"

    def tendrils_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage plus 2 (1d4) acid damage. At the end of each of its turns, the target must make a DC 10 Constitution saving throw, taking 2 (1d4) acid damage on a failure or ending the recurring acid damage on a success. A lesser restoration spell cast on the target also ends the recurring acid damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage plus 2 (1d4) acid damage. At the end of each of its turns, the target must make a DC 10 Constitution saving throw, taking 2 (1d4) acid damage on a failure or ending the recurring acid damage on a success. A lesser restoration spell cast on the target also ends the recurring acid damage.'

    def stench_spray_(1/day)_attack(self) -> str:
        """Each creature in a 15-foot cone originating from the flumph must succeed on a DC 10 Dexterity saving throw or be coated in a foul-smelling liquid. A coated creature exudes a horrible stench for 1d4 hours. The coated creature is poisoned as long as the stench lasts, and other creatures are poisoned while within 5 feet of the coated creature. A creature can remove the stench on itself by using a short rest to bathe in water, alcohol, or vinegar."""
        return 'Each creature in a 15-foot cone originating from the flumph must succeed on a DC 10 Dexterity saving throw or be coated in a foul-smelling liquid. A coated creature exudes a horrible stench for 1d4 hours. The coated creature is poisoned as long as the stench lasts, and other creatures are poisoned while within 5 feet of the coated creature. A creature can remove the stench on itself by using a short rest to bathe in water, alcohol, or vinegar.'

