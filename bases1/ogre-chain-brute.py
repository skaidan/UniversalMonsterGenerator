# bases1/ogre-chain-brute.py
"""
OgreChainBrute creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ogre-chain-brute
"""
from creature_base import GlobalCreatureBaseClass


class OgreChainBrute(GlobalCreatureBaseClass):
    """
    Large Giant creature - OgreChainBrute
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 59, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 8, 'CON': 16, 'INT': 5, 'WIS': 7, 'CHAR': 7, 'armor_class': 11, 'alignment': 'typically Chaotic Evil Armor Class  11 (hide armor) Hit Points  59 (7d10 + 21) Speed  40 ft. STR 19 (+4) DEX 8 (-1) CON 16 (+3) INT 5 (-3) WIS 7 (-2) CHA 7 (-2) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fist', 'chain_smash_(recharge_6)', 'chain_sweep']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.'

    def chain_smash_(recharge_6)_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage, and the target must make a DC 14 Constitution saving throw or be stunned for 1 minute. The target repeats the saving throw if it takes damage and at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage, and the target must make a DC 14 Constitution saving throw or be stunned for 1 minute. The target repeats the saving throw if it takes damage and at the end of each of its turns, ending the effect on itself on a success.'

    def chain_sweep_attack(self) -> str:
        """The ogre swings its chain, and every creature within 10 feet of it must make a DC 14 Dexterity saving throw. On a failed saving throw, a creature takes 8 (1d8 + 4) bludgeoning damage and is knocked prone. On a successful save, the creature takes half as much damage and isn't knocked prone."""
        return "The ogre swings its chain, and every creature within 10 feet of it must make a DC 14 Dexterity saving throw. On a failed saving throw, a creature takes 8 (1d8 + 4) bludgeoning damage and is knocked prone. On a successful save, the creature takes half as much damage and isn't knocked prone."

