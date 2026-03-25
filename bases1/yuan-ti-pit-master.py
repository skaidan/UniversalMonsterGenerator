# bases1/yuan-ti-pit-master.py
"""
YuanTiPitMaster creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-pit-master
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiPitMaster(GlobalCreatureBaseClass):
    """
    Medium Monstrosity (Warlock) creature - YuanTiPitMaster
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 88, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 13, 'INT': 14, 'WIS': 12, 'CHAR': 16, 'armor_class': 14, 'alignment': 'typically Neutral Evil Armor Class  14 (natural armor) Hit Points  88 (16d8 + 16) Speed  30 ft. STR 16 (+3) DEX 14 (+2) CON 13 (+1) INT 14 (+2) WIS 12 (+1) CHA 16 (+3) Saving Throws  Wis +4', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity (Warlock)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'bite', 'spectral_fangs', 'merrshaulks_slumber_(1/day)', 'spellcasting_(yuan-ti_form_only)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the yuan-ti's darkvision.Magic Resistance. The yuan-ti has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the yuan-ti's darkvision.Magic Resistance. The yuan-ti has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The yuan-ti makes three Bite attacks or two Spectral Fangs attacks."""
        return 'The yuan-ti makes three Bite attacks or two Spectral Fangs attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) poison damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) poison damage.'

    def spectral_fangs_attack(self) -> str:
        """Ranged Spell Attack: +6 to hit, range 120 ft., one target. Hit: 16 (3d8 + 3) poison damage."""
        return 'Ranged Spell Attack: +6 to hit, range 120 ft., one target. Hit: 16 (3d8 + 3) poison damage.'

    def merrshaulks_slumber_(1/day)_attack(self) -> str:
        """The yuan-ti targets up to five creatures that it can see within 60 feet of it. Each target must succeed on a DC 13 Constitution saving throw or fall into a magical sleep and be unconscious for 10 minutes. A sleeping target awakens if it takes damage or if someone uses an action to shake or slap it awake. This magical sleep has no effect on a creature immune to being charmed."""
        return 'The yuan-ti targets up to five creatures that it can see within 60 feet of it. Each target must succeed on a DC 13 Constitution saving throw or fall into a magical sleep and be unconscious for 10 minutes. A sleeping target awakens if it takes damage or if someone uses an action to shake or slap it awake. This magical sleep has no effect on a creature immune to being charmed.'

    def spellcasting_(yuan-ti_form_only)_attack(self) -> str:
        """The yuan-ti casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 14):"""
        return 'The yuan-ti casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 14):'

