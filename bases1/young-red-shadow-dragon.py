# bases1/young-red-shadow-dragon.py
"""
YoungRedShadowDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-red-shadow-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungRedShadowDragon(GlobalCreatureBaseClass):
    """
    Large dragon creature - YoungRedShadowDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 178, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 21, 'INT': 14, 'WIS': 11, 'CHAR': 19, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (natural armor) Hit Points  178 (17d10 + 85) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['living_shadow', 'multiattack', 'bite', 'claw', 'shadow_breath_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def living_shadow(self) -> str:
        """While in dim light or darkness, the dragon has resistance to damage that isn't force, psychic, or radiant.Shadow Stealth. While in dim light or darkness, the dragon can take the Hide action as a bonus"""
        return "While in dim light or darkness, the dragon has resistance to damage that isn't force, psychic, or radiant.Shadow Stealth. While in dim light or darkness, the dragon can take the Hide action as a bonus"

    def multiattack_attack(self) -> str:
        """The dragon makes three attacks: one with its bite and two with its claws."""
        return 'The dragon makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 3 (1d6) necrotic damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 3 (1d6) necrotic damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.'

    def shadow_breath_(recharge_5–6)_attack(self) -> str:
        """The dragon exhales shadowy fire in a 30-foot cone. Each creature in that area must make a DC 18 Dexterity saving throw, taking 56 (16d6) necrotic damage on a failed save, or half as much damage on a successful one. A humanoid reduced to 0 hit points by this damage dies, and an undead shadow rises from its corpse and acts immediately after the dragon in the initiative count. The shadow is under the dragon's control."""
        return "The dragon exhales shadowy fire in a 30-foot cone. Each creature in that area must make a DC 18 Dexterity saving throw, taking 56 (16d6) necrotic damage on a failed save, or half as much damage on a successful one. A humanoid reduced to 0 hit points by this damage dies, and an undead shadow rises from its corpse and acts immediately after the dragon in the initiative count. The shadow is under the dragon's control."

