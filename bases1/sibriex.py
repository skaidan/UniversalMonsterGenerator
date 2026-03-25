# bases1/sibriex.py
"""
Sibriex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sibriex
"""
from creature_base import GlobalCreatureBaseClass


class Sibriex(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - Sibriex
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 150, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 3, 'CON': 23, 'INT': 25, 'WIS': 24, 'CHAR': 25, 'armor_class': 19, 'alignment': 'typically Chaotic Evil Armor Class  19 (natural armor) Hit Points  150 (12d12 + 72) Speed  0 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['contamination', 'multiattack', 'chain', 'spellcasting', 'squirt_bile', 'warp_creature']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def contamination(self) -> str:
        """The sibriex emits an aura of corruption 30 feet in every direction. Vegetation withers in the aura, and the ground in the aura is difficult terrain for other creatures. Any creature that starts its tu"""
        return 'The sibriex emits an aura of corruption 30 feet in every direction. Vegetation withers in the aura, and the ground in the aura is difficult terrain for other creatures. Any creature that starts its tu'

    def multiattack_attack(self) -> str:
        """The sibriex makes three Chain attacks, and it uses Squirt Bile."""
        return 'The sibriex makes three Chain attacks, and it uses Squirt Bile.'

    def chain_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 20 (2d12 + 7) force damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 20 (2d12 + 7) force damage.'

    def spellcasting_attack(self) -> str:
        """The sibriex casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 21):"""
        return 'The sibriex casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 21):'

    def squirt_bile_attack(self) -> str:
        """The sibriex targets one creature it can see within 120 feet of it. The target must succeed on a DC 20 Dexterity saving throw or take 31 (9d6) acid damage."""
        return 'The sibriex targets one creature it can see within 120 feet of it. The target must succeed on a DC 20 Dexterity saving throw or take 31 (9d6) acid damage.'

    def warp_creature_attack(self) -> str:
        """The sibriex targets up to three creatures it can see within 120 feet of it. Each target must make a DC 20 Constitution saving throw. On a successful save, a creature becomes immune to this sibriex's Warp Creature. On a failed save, the target is poisoned, which causes it to also gain 1 level of exhaustion. While poisoned in this way, the target must repeat the saving throw at the start of each of its turns. Three successful saves against the poison end it, and ending the poison removes any levels of exhaustion caused by it. Each failed save causes the target to gain another level of exhaustion. Once the target reaches 6 levels of exhaustion, it dies and instantly transforms into a living manes under the sibriex's control. The transformation of the body can be undone only by a wish spell."""
        return "The sibriex targets up to three creatures it can see within 120 feet of it. Each target must make a DC 20 Constitution saving throw. On a successful save, a creature becomes immune to this sibriex's Warp Creature. On a failed save, the target is poisoned, which causes it to also gain 1 level of exhaustion. While poisoned in this way, the target must repeat the saving throw at the start of each of its turns. Three successful saves against the poison end it, and ending the poison removes any levels of exhaustion caused by it. Each failed save causes the target to gain another level of exhaustion. Once the target reaches 6 levels of exhaustion, it dies and instantly transforms into a living manes under the sibriex's control. The transformation of the body can be undone only by a wish spell."

