# bases1/demogorgon.py
"""
Demogorgon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=demogorgon
"""
from creature_base import GlobalCreatureBaseClass


class Demogorgon(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - Demogorgon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 464, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 14, 'CON': 26, 'INT': 20, 'WIS': 17, 'CHAR': 25, 'armor_class': 22, 'alignment': 'Chaotic Evil Armor Class  22 (natural armor) Hit Points  464 (32d12 + 256) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'multiattack', 'tentacle', 'gaze', '&nbsp;_1-2:_beguiling_gaze', '&nbsp;_3-4:_confusing_caze', '&nbsp;_5-6:_hypnotic_caze', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If Demogorgon fails a saving throw, he can choose to succeed instead.Magic Resistance. Demogorgon has advantage on saving throws against spells and other magical effects.Two Heads. Demogorgon has adva"""
        return 'If Demogorgon fails a saving throw, he can choose to succeed instead.Magic Resistance. Demogorgon has advantage on saving throws against spells and other magical effects.Two Heads. Demogorgon has adva'

    def multiattack_attack(self) -> str:
        """Demogorgon makes two Tentacle attacks. He can replace one attack with a use of Gaze."""
        return 'Demogorgon makes two Tentacle attacks. He can replace one attack with a use of Gaze.'

    def tentacle_attack(self) -> str:
        """Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 28 (3d12 + 9) force damage. If the target is a creature, it must succeed on a DC 23 Constitution saving throw, or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if its hit point maximum is reduced to 0."""
        return 'Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 28 (3d12 + 9) force damage. If the target is a creature, it must succeed on a DC 23 Constitution saving throw, or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if its hit point maximum is reduced to 0.'

    def gaze_attack(self) -> str:
        """Demogorgon turns his magical gaze toward one creature he can see within 120 feet of him. The target must succeed on a DC 23 Wisdom saving throw or suffer one of the following effects (choose one or roll a d6):"""
        return 'Demogorgon turns his magical gaze toward one creature he can see within 120 feet of him. The target must succeed on a DC 23 Wisdom saving throw or suffer one of the following effects (choose one or roll a d6):'

    def &nbsp;_1-2:_beguiling_gaze_attack(self) -> str:
        """The target is stunned until the start of Demogorgon's next turn or until Demogorgon is no longer within line of sight."""
        return "The target is stunned until the start of Demogorgon's next turn or until Demogorgon is no longer within line of sight."

    def &nbsp;_3-4:_confusing_caze_attack(self) -> str:
        """The target suffers the effect of the confusion spell without making a saving throw. The effect lasts until the start of Demogorgon's next turn. Demogorgon doesn't need to concentrate on the spell."""
        return "The target suffers the effect of the confusion spell without making a saving throw. The effect lasts until the start of Demogorgon's next turn. Demogorgon doesn't need to concentrate on the spell."

    def &nbsp;_5-6:_hypnotic_caze_attack(self) -> str:
        """The target is charmed by Demogorgon until the start of Demogorgon's next turn. Demogorgon chooses how the charmed target uses its action, reaction, and movement."""
        return "The target is charmed by Demogorgon until the start of Demogorgon's next turn. Demogorgon chooses how the charmed target uses its action, reaction, and movement."

    def spellcasting_attack(self) -> str:
        """Demogorgon casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 23):"""
        return 'Demogorgon casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 23):'

