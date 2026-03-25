# bases1/chain-devil.py
"""
ChainDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chain-devil
"""
from creature_base import GlobalCreatureBaseClass


class ChainDevil(GlobalCreatureBaseClass):
    """
    Medium fiend (Devil) creature - ChainDevil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 18, 'INT': 11, 'WIS': 12, 'CHAR': 14, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (natural armor) Hit Points  85 (10d8 + 40) Speed  30 ft. STR 18 (+4) DEX 15 (+2) CON 18 (+4) INT 11 (+0) WIS 12 (+1) CHA 14 (+2) Saving Throws  Con +7', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'chain', 'animate_chains_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The devil makes two attacks with its chains."""
        return 'The devil makes two attacks with its chains.'

    def chain_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) slashing damage. The target is grappled (escape DC 14) if the devil isn't already grappling a creature. Until this grapple ends, the target is restrained and takes 7 (2d6) piercing damage at the start of each of its turns."""
        return "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) slashing damage. The target is grappled (escape DC 14) if the devil isn't already grappling a creature. Until this grapple ends, the target is restrained and takes 7 (2d6) piercing damage at the start of each of its turns."

    def animate_chains_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """Up to four chains the devil can see within 60 feet of it magically sprout razor-edged barbs and animate under the devil's control, provided that the chains aren't being worn or carried. Each animated chain is an object with AC 20, 20 hit points, resistance to piercing damage, and immunity to psychic and thunder damage. When the devil uses Multiattack on its turn, it can use each animated chain to make one additional chain attack. An animated chain can grapple one creature of its own but can't make attacks while grappling. An animated chain reverts to its inanimate state if reduced to 0 hit points or if the devil is incapacitated or dies."""
        return "Up to four chains the devil can see within 60 feet of it magically sprout razor-edged barbs and animate under the devil's control, provided that the chains aren't being worn or carried. Each animated chain is an object with AC 20, 20 hit points, resistance to piercing damage, and immunity to psychic and thunder damage. When the devil uses Multiattack on its turn, it can use each animated chain to make one additional chain attack. An animated chain can grapple one creature of its own but can't make attacks while grappling. An animated chain reverts to its inanimate state if reduced to 0 hit points or if the devil is incapacitated or dies."

