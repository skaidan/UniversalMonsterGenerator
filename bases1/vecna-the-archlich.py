# bases1/vecna-the-archlich.py
"""
VecnaTheArchlich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vecna-the-archlich
"""
from creature_base import GlobalCreatureBaseClass


class VecnaTheArchlich(GlobalCreatureBaseClass):
    """
    Medium Undead (Wizard) creature - VecnaTheArchlich
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 272, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 16, 'CON': 18, 'INT': 22, 'WIS': 24, 'CHAR': 16, 'armor_class': 18, 'alignment': 'Lawful Evil Armor Class  18 (natural armor) Hit Points  272 (32d8 + 128) Speed  30 ft. STR 14 (+2) DEX 16 (+3) CON 18 (+4) INT 22 (+6) WIS 24 (+7) CHA 16 (+3) Saving Throws  Con +12', 'legendary': False, 'size': 'Medium', 'type': 'Undead (Wizard)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(5/day)', 'multiattack', 'afterthought', 'flight_of_the_damned_(recharge_5–6)', 'rotten_fate', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(5/day)(self) -> str:
        """If Vecna fails a saving throw, he can choose to succeed instead.Special Equipment. Vecna carries a magic dagger named Afterthought. In the hands of anyone other than Vecna, Afterthought is a +2 dagger"""
        return 'If Vecna fails a saving throw, he can choose to succeed instead.Special Equipment. Vecna carries a magic dagger named Afterthought. In the hands of anyone other than Vecna, Afterthought is a +2 dagger'

    def multiattack_attack(self) -> str:
        """Vecna uses Flight of the Damned (if available), Rotten Fate, or Spellcasting. He then makes two attacks with Afterthought."""
        return 'Vecna uses Flight of the Damned (if available), Rotten Fate, or Spellcasting. He then makes two attacks with Afterthought.'

    def afterthought_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 7 (1d4 + 5) piercing damage plus 9 (2d8) necrotic damage. If the target is a creature, it is afflicted by entropic magic, taking 9 (2d8) necrotic damage at the start of each of its turns. Immediately after taking this damage on its turn, the target can make a DC 20 Constitution saving throw, ending the effect on itself on a success. Until it succeeds on this save, the afflicted target can't regain hit points."""
        return "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 7 (1d4 + 5) piercing damage plus 9 (2d8) necrotic damage. If the target is a creature, it is afflicted by entropic magic, taking 9 (2d8) necrotic damage at the start of each of its turns. Immediately after taking this damage on its turn, the target can make a DC 20 Constitution saving throw, ending the effect on itself on a success. Until it succeeds on this save, the afflicted target can't regain hit points."

    def flight_of_the_damned_(recharge_5–6)_attack(self) -> str:
        """Vecna conjures a torrent of flying, spectral entities that fill a 120-foot cone and pass through all creatures in that area before dissipating. Each creature in that area must make a DC 22 Constitution saving throw. On a failed save, the creature takes 36 (8d8) necrotic damage and is frightened of Vecna for 1 minute. On a successful save, the creature takes half as much damage and isn't frightened. A frightened creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return "Vecna conjures a torrent of flying, spectral entities that fill a 120-foot cone and pass through all creatures in that area before dissipating. Each creature in that area must make a DC 22 Constitution saving throw. On a failed save, the creature takes 36 (8d8) necrotic damage and is frightened of Vecna for 1 minute. On a successful save, the creature takes half as much damage and isn't frightened. A frightened creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

    def rotten_fate_attack(self) -> str:
        """Vecna causes necrotic magic to engulf one creature he can see within 120 feet of himself. The target must make a DC 22 Constitution saving throw, taking 96 (8d8 + 60) necrotic damage on a failed save, or half as much damage on a successful one. A Humanoid killed by this magic rises as a zombie at the start of Vecna's next turn and acts immediately after Vecna in the initiative order. The zombie is under Vecna's control."""
        return "Vecna causes necrotic magic to engulf one creature he can see within 120 feet of himself. The target must make a DC 22 Constitution saving throw, taking 96 (8d8 + 60) necrotic damage on a failed save, or half as much damage on a successful one. A Humanoid killed by this magic rises as a zombie at the start of Vecna's next turn and acts immediately after Vecna in the initiative order. The zombie is under Vecna's control."

    def spellcasting_attack(self) -> str:
        """Vecna casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 22):"""
        return 'Vecna casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 22):'

