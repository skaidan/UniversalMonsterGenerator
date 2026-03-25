# bases1/kobold-inventor.py
"""
KoboldInventor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kobold-inventor
"""
from creature_base import GlobalCreatureBaseClass


class KoboldInventor(GlobalCreatureBaseClass):
    """
    Small Humanoid creature - KoboldInventor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 15, 'CON': 12, 'INT': 8, 'WIS': 7, 'CHAR': 8, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 Hit Points  13 (3d6 + 3) Speed  30 ft. STR 7 (-2) DEX 15 (+2) CON 12 (+1) INT 8 (-1) WIS 7 (-2) CHA 8 (-1) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'dagger', 'sling', 'weapon_invention', '&nbsp;_1-_acid', '&nbsp;_2-_alchemists_fire', '&nbsp;_3-_basket_of_centipedes', '&nbsp;_4-_green_slime_pot', '&nbsp;_5-_rot_grub_pot', '&nbsp;_6-_scorpion_on_a_stick', '&nbsp;_7-_skunk_in_a_cage', '&nbsp;_8-_wasp_nest_in_a_bag']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated.Sunlight Sensitivity. While in su"""
        return "The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated.Sunlight Sensitivity. While in su"

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def sling_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.'

    def weapon_invention_attack(self) -> str:
        """The kobold uses one of the following options (choose one or roll a d8); the kobold can use each one no more than once per day:"""
        return 'The kobold uses one of the following options (choose one or roll a d8); the kobold can use each one no more than once per day:'

    def &nbsp;_1-_acid_attack(self) -> str:
        """The kobold hurls a flask of acid. Ranged Weapon Attack: +4 to hit, range 5/20 ft., one target. Hit: 7 (2d6) acid damage."""
        return 'The kobold hurls a flask of acid. Ranged Weapon Attack: +4 to hit, range 5/20 ft., one target. Hit: 7 (2d6) acid damage.'

    def &nbsp;_2-_alchemists_fire_attack(self) -> str:
        """The kobold throws a flask of alchemist's fire. Ranged Weapon Attack: +4 to hit, range 5/20 ft., one target. Hit: 2 (1d4) fire damage at the start of each of the target's turns. The target can end this damage by using its action to make a DC 10 Dexterity check to extinguish the flames."""
        return "The kobold throws a flask of alchemist's fire. Ranged Weapon Attack: +4 to hit, range 5/20 ft., one target. Hit: 2 (1d4) fire damage at the start of each of the target's turns. The target can end this damage by using its action to make a DC 10 Dexterity check to extinguish the flames."

    def &nbsp;_3-_basket_of_centipedes_attack(self) -> str:
        """The kobold throws a small basket into a 5-foot-square space within 20 feet of it. A swarm of insects (centipedes) with 11 hit points emerges from the basket and rolls initiative. At the end of each of the swarm's turns, there's a 50 percent chance that the swarm disperses."""
        return "The kobold throws a small basket into a 5-foot-square space within 20 feet of it. A swarm of insects (centipedes) with 11 hit points emerges from the basket and rolls initiative. At the end of each of the swarm's turns, there's a 50 percent chance that the swarm disperses."

    def &nbsp;_4-_green_slime_pot_attack(self) -> str:
        """The kobold throws a clay pot full of green slime at the target, and it breaks open on impact. Ranged Weapon Attack: +4 to hit, range 5/20 ft., one target. Hit: 5 (1d10) acid damage, and the target is covered in slime until a creature uses its action to scrape or wash the slime off. A target covered in the slime takes 5 (1d10) acid damage at the start of each of its turns."""
        return 'The kobold throws a clay pot full of green slime at the target, and it breaks open on impact. Ranged Weapon Attack: +4 to hit, range 5/20 ft., one target. Hit: 5 (1d10) acid damage, and the target is covered in slime until a creature uses its action to scrape or wash the slime off. A target covered in the slime takes 5 (1d10) acid damage at the start of each of its turns.'

    def &nbsp;_5-_rot_grub_pot_attack(self) -> str:
        """The kobold throws a clay pot into a 5-foot-square space within 20 feet of it, and it breaks open on impact. A swarm of rot grubs (in this book) emerges from the shattered pot and remains a hazard in that square."""
        return 'The kobold throws a clay pot into a 5-foot-square space within 20 feet of it, and it breaks open on impact. A swarm of rot grubs (in this book) emerges from the shattered pot and remains a hazard in that square.'

    def &nbsp;_6-_scorpion_on_a_stick_attack(self) -> str:
        """The kobold makes a melee attack with a scorpion tied to the end of a 5-foot-long pole. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the target must make a DC 9 Constitution saving throw, taking 4 (1d8) poison damage on a failed save, or half as much damage on a successful one."""
        return 'The kobold makes a melee attack with a scorpion tied to the end of a 5-foot-long pole. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the target must make a DC 9 Constitution saving throw, taking 4 (1d8) poison damage on a failed save, or half as much damage on a successful one.'

    def &nbsp;_7-_skunk_in_a_cage_attack(self) -> str:
        """The kobold releases a skunk into an unoccupied space within 5 feet of it. The skunk has a walking speed of 20 feet, AC 10, 1 hit point, and no effective attacks. It rolls initiative and, on its turn, uses its action to spray musk at a random creature within 5 feet of it. The target must succeed on a DC 9 Constitution saving throw, or it retches and is incapacitated for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. A creature that doesn't need to breathe or is immune to poison automatically succeeds on the saving throw. Once the skunk has sprayed its musk, it can't do so again until it finishes a short or long rest."""
        return "The kobold releases a skunk into an unoccupied space within 5 feet of it. The skunk has a walking speed of 20 feet, AC 10, 1 hit point, and no effective attacks. It rolls initiative and, on its turn, uses its action to spray musk at a random creature within 5 feet of it. The target must succeed on a DC 9 Constitution saving throw, or it retches and is incapacitated for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. A creature that doesn't need to breathe or is immune to poison automatically succeeds on the saving throw. Once the skunk has sprayed its musk, it can't do so again until it finishes a short or long rest."

    def &nbsp;_8-_wasp_nest_in_a_bag_attack(self) -> str:
        """The kobold throws a small bag into a 5-foot-square space within 20 feet of it. A swarm of insects (wasps) with 11 hit points emerges from the bag and rolls initiative. At the end of each of the swarm's turns, there's a 50 percent chance that the swarm disperses."""
        return "The kobold throws a small bag into a 5-foot-square space within 20 feet of it. A swarm of insects (wasps) with 11 hit points emerges from the bag and rolls initiative. At the end of each of the swarm's turns, there's a 50 percent chance that the swarm disperses."

