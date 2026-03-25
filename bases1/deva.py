# bases1/deva.py
"""
Deva creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deva
"""
from creature_base import GlobalCreatureBaseClass


class Deva(GlobalCreatureBaseClass):
    """
    Medium celestial creature - Deva
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 18, 'CON': 18, 'INT': 17, 'WIS': 20, 'CHAR': 20, 'armor_class': 17, 'alignment': 'lawful good Armor Class  17 (natural armor) Hit Points  136 (16d8 + 64) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['angelic_weapons', 'multiattack', 'mace', 'healing_touch_(3/day)', 'change_shape']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def angelic_weapons(self) -> str:
        """The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra 4d8 radiant damage (included in the attack).Innate Spellcasting. The deva's spellcasting ability is"""
        return "The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra 4d8 radiant damage (included in the attack).Innate Spellcasting. The deva's spellcasting ability is"

    def multiattack_attack(self) -> str:
        """The deva makes two melee attacks."""
        return 'The deva makes two melee attacks.'

    def mace_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage plus 18 (4d8) radiant damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage plus 18 (4d8) radiant damage.'

    def healing_touch_(3/day)_attack(self) -> str:
        """The deva touches another creature. The target magically regains 20 (4d8 + 2) hit points and is freed from any curse, disease, poison, blindness, or deafness."""
        return 'The deva touches another creature. The target magically regains 20 (4d8 + 2) hit points and is freed from any curse, disease, poison, blindness, or deafness.'

    def change_shape_attack(self) -> str:
        """The deva magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the deva's choice). In a new form, the deva retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and special senses are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks."""
        return "The deva magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the deva's choice). In a new form, the deva retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and special senses are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks."

