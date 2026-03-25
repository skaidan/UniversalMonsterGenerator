# bases1/ultroloth.py
"""
Ultroloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ultroloth
"""
from creature_base import GlobalCreatureBaseClass


class Ultroloth(GlobalCreatureBaseClass):
    """
    Medium fiend (Yugoloth) creature - Ultroloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 153, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 16, 'CON': 18, 'INT': 18, 'WIS': 15, 'CHAR': 19, 'armor_class': 19, 'alignment': 'neutral evil Armor Class  19 (natural armor) Hit Points  153 (18d8 + 72) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'longsword', 'hypnotic_gaze', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The ultroloth's innate spellcasting ability is Charisma (spell save DC 17). The ultroloth can innately cast the following spells, requiring no material components:At will: alter self, clairvoyance, da"""
        return "The ultroloth's innate spellcasting ability is Charisma (spell save DC 17). The ultroloth can innately cast the following spells, requiring no material components:At will: alter self, clairvoyance, da"

    def multiattack_attack(self) -> str:
        """The ultroloth can use its Hypnotic Gaze and makes three melee attacks."""
        return 'The ultroloth can use its Hypnotic Gaze and makes three melee attacks.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.'

    def hypnotic_gaze_attack(self) -> str:
        """The ultroloth's eyes sparkle with opalescent light as it targets one creature it can see within 30 feet of it. If the target can see the ultroloth, the target must succeed on a DC 17 Wisdom saving throw against this magic or be charmed until the end of the ultroloth's next turn. The charmed target is stunned. If the target's saving throw is successful, the target is immune to the ultroloth's gaze for the next 24 hours."""
        return "The ultroloth's eyes sparkle with opalescent light as it targets one creature it can see within 30 feet of it. If the target can see the ultroloth, the target must succeed on a DC 17 Wisdom saving throw against this magic or be charmed until the end of the ultroloth's next turn. The charmed target is stunned. If the target's saving throw is successful, the target is immune to the ultroloth's gaze for the next 24 hours."

    def teleport_attack(self) -> str:
        """The ultroloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."""
        return 'The ultroloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see.'

