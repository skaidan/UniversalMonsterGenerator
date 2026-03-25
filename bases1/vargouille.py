# bases1/vargouille.py
"""
Vargouille creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vargouille
"""
from creature_base import GlobalCreatureBaseClass


class Vargouille(GlobalCreatureBaseClass):
    """
    Tiny Fiend creature - Vargouille
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 14, 'CON': 14, 'INT': 4, 'WIS': 7, 'CHAR': 2, 'armor_class': 12, 'alignment': 'typically Chaotic Evil Armor Class  12 Hit Points  18 (4d4 + 8) Speed  5 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'Fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'abyssal_curse', 'stunning_shriek_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage plus 10 (3d6) poison damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage plus 10 (3d6) poison damage.'

    def abyssal_curse_attack(self) -> str:
        """The vargouille targets one incapacitated Humanoid within 5 feet of it. The target must succeed on a DC 12 Charisma saving throw or become cursed. The cursed target loses 1 point of Charisma after each hour, as its head takes on fiendish aspects. The curse doesn't advance while the target is in sunlight or the area of a daylight spell; don't count that time. When the cursed target's Charisma becomes 2, it dies, and its head tears from its body and becomes a new vargouille. Casting remove curse, greater restoration, or a similar spell on the target before the transformation is complete can end the curse. Doing so undoes the changes made to the target by the curse."""
        return "The vargouille targets one incapacitated Humanoid within 5 feet of it. The target must succeed on a DC 12 Charisma saving throw or become cursed. The cursed target loses 1 point of Charisma after each hour, as its head takes on fiendish aspects. The curse doesn't advance while the target is in sunlight or the area of a daylight spell; don't count that time. When the cursed target's Charisma becomes 2, it dies, and its head tears from its body and becomes a new vargouille. Casting remove curse, greater restoration, or a similar spell on the target before the transformation is complete can end the curse. Doing so undoes the changes made to the target by the curse."

    def stunning_shriek_(recharge_5–6)_attack(self) -> str:
        """The vargouille shrieks. Each Humanoid and Beast within 30 feet of the vargouille and able to hear it must succeed on a DC 12 Wisdom saving throw or be frightened of the vargouille until the end of the vargouille's next turn. While frightened in this way, a target is stunned. If a target's saving throw is successful or the effect ends for it, the target is immune to the Stunning Shriek of all vargouilles for 1 hour."""
        return "The vargouille shrieks. Each Humanoid and Beast within 30 feet of the vargouille and able to hear it must succeed on a DC 12 Wisdom saving throw or be frightened of the vargouille until the end of the vargouille's next turn. While frightened in this way, a target is stunned. If a target's saving throw is successful or the effect ends for it, the target is immune to the Stunning Shriek of all vargouilles for 1 hour."

