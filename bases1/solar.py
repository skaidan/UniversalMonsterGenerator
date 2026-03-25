# bases1/solar.py
"""
Solar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=solar
"""
from creature_base import GlobalCreatureBaseClass


class Solar(GlobalCreatureBaseClass):
    """
    Large celestial creature - Solar
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 243, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 22, 'CON': 26, 'INT': 25, 'WIS': 25, 'CHAR': 30, 'armor_class': 21, 'alignment': 'lawful good Armor Class  21 (natural armor) Hit Points  243 (18d10 + 144) Speed  50 ft.', 'legendary': False, 'size': 'Large', 'type': 'celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['angelic_weapons', 'multiattack', 'greatsword', 'slaying_longbow', 'flying_sword', 'healing_touch_(4/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def angelic_weapons(self) -> str:
        """The solar's weapon attacks are magical. When the solar hits with any weapon, the weapon deals an extra 6d8 radiant damage (included in the attack).Divine Awareness. The solar knows if it hears a lie.I"""
        return "The solar's weapon attacks are magical. When the solar hits with any weapon, the weapon deals an extra 6d8 radiant damage (included in the attack).Divine Awareness. The solar knows if it hears a lie.I"

    def multiattack_attack(self) -> str:
        """The solar makes two greatsword attacks."""
        return 'The solar makes two greatsword attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +15 to hit, reach 5 ft., one target. Hit: 22 (4d6 + 8) slashing damage plus 27 (6d8) radiant damage."""
        return 'Melee Weapon Attack: +15 to hit, reach 5 ft., one target. Hit: 22 (4d6 + 8) slashing damage plus 27 (6d8) radiant damage.'

    def slaying_longbow_attack(self) -> str:
        """Ranged Weapon Attack: +13 to hit, range 150/600 ft., one target. Hit: 15 (2d8 + 6) piercing damage plus 27 (6d8) radiant damage. If the target is a creature that has 100 hit points or fewer, it must succeed on a DC 15 Constitution saving throw or die."""
        return 'Ranged Weapon Attack: +13 to hit, range 150/600 ft., one target. Hit: 15 (2d8 + 6) piercing damage plus 27 (6d8) radiant damage. If the target is a creature that has 100 hit points or fewer, it must succeed on a DC 15 Constitution saving throw or die.'

    def flying_sword_attack(self) -> str:
        """The solar releases its greatsword to hover magically in an unoccupied space within 5 feet of it. If the solar can see the sword, the solar can mentally command it as a bonus action to fly up to 50 feet and either make one attack against a target or return to the solar's hands. If the hovering sword is targeted by any effect, the solar is considered to be holding it. The hovering sword falls if the solar dies."""
        return "The solar releases its greatsword to hover magically in an unoccupied space within 5 feet of it. If the solar can see the sword, the solar can mentally command it as a bonus action to fly up to 50 feet and either make one attack against a target or return to the solar's hands. If the hovering sword is targeted by any effect, the solar is considered to be holding it. The hovering sword falls if the solar dies."

    def healing_touch_(4/day)_attack(self) -> str:
        """The solar touches another creature. The target magically regains 40 (8d8 + 4) hit points and is freed from any curse, disease, poison, blindness, or deafness."""
        return 'The solar touches another creature. The target magically regains 40 (8d8 + 4) hit points and is freed from any curse, disease, poison, blindness, or deafness.'

