# bases1/jackalwere.py
"""
Jackalwere creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=jackalwere
"""
from creature_base import GlobalCreatureBaseClass


class Jackalwere(GlobalCreatureBaseClass):
    """
    Medium humanoid (Shapechanger) creature - Jackalwere
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 15, 'CON': 11, 'INT': 13, 'WIS': 11, 'CHAR': 10, 'armor_class': 12, 'alignment': 'chaotic evil Armor Class  12 Hit Points  18 (4d8) Speed  40 ft. STR 11 (+0) DEX 15 (+2) CON 11 (+0) INT 13 (+1) WIS 11 (+0) CHA 10 (+0) Skills  Deception +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Shapechanger)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'bite_(jackal_or_hybrid_form_only)', 'scimitar_(human_or_hybrid_form_only)', 'sleep_gaze']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The jackalwere can use its action to polymorph into a specific Medium human or a jackal-humanoid hybrid, or back into its true form (that of a Small jackal). Other than its size, its statistics are th"""
        return 'The jackalwere can use its action to polymorph into a specific Medium human or a jackal-humanoid hybrid, or back into its true form (that of a Small jackal). Other than its size, its statistics are th'

    def bite_(jackal_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def scimitar_(human_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.'

    def sleep_gaze_attack(self) -> str:
        """The jackalwere gazes at one creature it can see within 30 feet of it. The target must make a DC 10 Wisdom saving throw. On a failed save, the target succumbs to a magical slumber, falling unconscious for 10 minutes or until someone uses an action to shake the target awake. A creature that successfully saves against the effect is immune to this jackalwere's gaze for the next 24 hours. Undead and creatures immune to being charmed aren't affected by it."""
        return "The jackalwere gazes at one creature it can see within 30 feet of it. The target must make a DC 10 Wisdom saving throw. On a failed save, the target succumbs to a magical slumber, falling unconscious for 10 minutes or until someone uses an action to shake the target awake. A creature that successfully saves against the effect is immune to this jackalwere's gaze for the next 24 hours. Undead and creatures immune to being charmed aren't affected by it."

