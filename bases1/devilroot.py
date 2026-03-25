# bases1/devilroot.py
"""
Devilroot creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=devilroot
"""
from creature_base import GlobalCreatureBaseClass


class Devilroot(GlobalCreatureBaseClass):
    """
    Medium plant creature - Devilroot
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 105, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 11, 'CON': 17, 'INT': 12, 'WIS': 14, 'CHAR': 14, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (natural armour) Hit Points  105 (14d8 + 42) Speed  30 ft. STR 17 (+3) DEX 11 (+0) CON 17 (+3) INT 12 (+1) WIS 14 (+2) CHA 14 (+2) Saving Throws  Con +6', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'multiattack', 'fiendish_vine', 'fiendish_pollen_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the devilroot remains motionless, it is indistinguishable from an ordinary plant.Speak With Plants. The devilroot can communicate with plants and plant creatures as if they shared a language."""
        return 'While the devilroot remains motionless, it is indistinguishable from an ordinary plant.Speak With Plants. The devilroot can communicate with plants and plant creatures as if they shared a language.'

    def multiattack_attack(self) -> str:
        """The devilroot makes two melee attacks."""
        return 'The devilroot makes two melee attacks.'

    def fiendish_vine_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage. If the target is a creature, it must then succeed on a DC 16 Constitution saving throw or become poisoned and infected with a disease. Creatures immune to the poisoned condition are immune to this disease. While infected in this way, a target takes 5 (1d10) poison damage at the start of each of its turns. A target can repeat the saving throw at the end of each of its turns, ending both effects on itself on a success. Any effect that removes a disease ends both effects. If a creature infected with this desease dies, it sprouts 1d6 rooter motes that grow to full size in 7 days."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage. If the target is a creature, it must then succeed on a DC 16 Constitution saving throw or become poisoned and infected with a disease. Creatures immune to the poisoned condition are immune to this disease. While infected in this way, a target takes 5 (1d10) poison damage at the start of each of its turns. A target can repeat the saving throw at the end of each of its turns, ending both effects on itself on a success. Any effect that removes a disease ends both effects. If a creature infected with this desease dies, it sprouts 1d6 rooter motes that grow to full size in 7 days.'

    def fiendish_pollen_(recharge_5-6)_attack(self) -> str:
        """The devilroot releases toxic pollen in a 30-foot cone. Each creature in that area must make a DC 16 Constitution saving throw, taking 27 (5d10) poison damage on a failed save, or half as much damage on a successful one."""
        return 'The devilroot releases toxic pollen in a 30-foot cone. Each creature in that area must make a DC 16 Constitution saving throw, taking 27 (5d10) poison damage on a failed save, or half as much damage on a successful one.'

