# bases1/dryad.py
"""
Dryad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dryad
"""
from creature_base import GlobalCreatureBaseClass


class Dryad(GlobalCreatureBaseClass):
    """
    Medium fey creature - Dryad
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 12, 'CON': 11, 'INT': 14, 'WIS': 15, 'CHAR': 18, 'armor_class': 11, 'alignment': 'neutral Armor Class  11 (16 with  barkskin ) Hit Points  22 (5d8) Speed  30 ft. STR 10 (+0) DEX 12 (+1) CON 11 (+0) INT 14 (+2) WIS 15 (+2) CHA 18 (+4) Skills  Perception +4', 'legendary': False, 'size': 'Medium', 'type': 'fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'club', 'fey_charm']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast the following spells, requiring no material components:At will: druidcraft3/day each: entangle, good"""
        return "The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast the following spells, requiring no material components:At will: druidcraft3/day each: entangle, good"

    def club_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit (+6 to hit with shillelagh), reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage, or 8 (1d8 + 4) bludgeoning damage with shillelagh."""
        return 'Melee Weapon Attack: +2 to hit (+6 to hit with shillelagh), reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage, or 8 (1d8 + 4) bludgeoning damage with shillelagh.'

    def fey_charm_attack(self) -> str:
        """The dryad targets one humanoid or beast that she can see within 30 feet of her. If the target can see the dryad, it must succeed on a DC 14 Wisdom saving throw or be magically charmed. The charmed creature regards the dryad as a trusted friend to be heeded and protected. Although the target isn't under the dryad's control, it takes the dryad's requests or actions in the most favorable way it can. Each time the dryad or its allies do anything harmful to the target, it can repeat the saving throw, ending the effect on itself on a success. Otherwise, the effect lasts 24 hours or until the dryad dies, is on a different plane of existence from the target, or ends the effect as a bonus action. If a target's saving throw is successful, the target is immune to the dryad's Fey Charm for the next 24 hours. The dryad can have no more than one humanoid and up to three beasts charmed at a time."""
        return "The dryad targets one humanoid or beast that she can see within 30 feet of her. If the target can see the dryad, it must succeed on a DC 14 Wisdom saving throw or be magically charmed. The charmed creature regards the dryad as a trusted friend to be heeded and protected. Although the target isn't under the dryad's control, it takes the dryad's requests or actions in the most favorable way it can. Each time the dryad or its allies do anything harmful to the target, it can repeat the saving throw, ending the effect on itself on a success. Otherwise, the effect lasts 24 hours or until the dryad dies, is on a different plane of existence from the target, or ends the effect as a bonus action. If a target's saving throw is successful, the target is immune to the dryad's Fey Charm for the next 24 hours. The dryad can have no more than one humanoid and up to three beasts charmed at a time."

