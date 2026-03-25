# bases1/cambion.py
"""
Cambion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cambion
"""
from creature_base import GlobalCreatureBaseClass


class Cambion(GlobalCreatureBaseClass):
    """
    Medium fiend creature - Cambion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 82, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 18, 'CON': 16, 'INT': 14, 'WIS': 12, 'CHAR': 16, 'armor_class': 19, 'alignment': 'any evil alignment Armor Class  19 (scale mail) Hit Points  82 (11d8 + 33) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fiendish_blessing', 'multiattack', 'spear', 'fire_ray', 'fiendish_charm']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fiendish_blessing(self) -> str:
        """The AC of the cambion includes its Charisma bonus.Innate Spellcasting. The cambion's spellcasting ability is Charisma (spell save DC 14). The cambion can innately cast the following spells, requiring """
        return "The AC of the cambion includes its Charisma bonus.Innate Spellcasting. The cambion's spellcasting ability is Charisma (spell save DC 14). The cambion can innately cast the following spells, requiring "

    def multiattack_attack(self) -> str:
        """The cambion makes two melee attacks or uses its Fire Ray twice."""
        return 'The cambion makes two melee attacks or uses its Fire Ray twice.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 7 (1d6 + 4) piercing damage, or 8 (1d8 + 4) piercing damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage."""
        return 'Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 7 (1d6 + 4) piercing damage, or 8 (1d8 + 4) piercing damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage.'

    def fire_ray_attack(self) -> str:
        """Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 10 (3d6) fire damage."""
        return 'Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 10 (3d6) fire damage.'

    def fiendish_charm_attack(self) -> str:
        """One humanoid the cambion can see within 30 feet of it must succeed on a DC 14 Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the cambion's spoken commands. If the target suffers any harm from the cambion or another creature or receives a suicidal command from the cambion, the target can repeat the saving throw, ending the effect on itself on a success. If a target's saving throw is successful, or if the effect ends for it, the creature is immune to the cambion's Fiendish Charm for the next 24 hours."""
        return "One humanoid the cambion can see within 30 feet of it must succeed on a DC 14 Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the cambion's spoken commands. If the target suffers any harm from the cambion or another creature or receives a suicidal command from the cambion, the target can repeat the saving throw, ending the effect on itself on a success. If a target's saving throw is successful, or if the effect ends for it, the creature is immune to the cambion's Fiendish Charm for the next 24 hours."

