#!/usr/bin/env python3
"""
Script to regenerate monster classes in bases1/ from AiDeDd scraper
"""

import os
from imports.aidedd_scraper import scrape_monster

# List of monster names to regenerate (from original bases1 files)
MONSTER_NAMES = [
    'aarakocra', 'aberrant-spirit', 'abjurer-wizard', 'aboleth', 'abominable-yeti',
    'acererak', 'acolyte', 'adult-amethyst-dragon', 'adult-black-dragon',
    'adult-blue-dracolich', 'adult-blue-dragon', 'adult-brass-dragon',
    'adult-bronze-dragon', 'adult-copper-dragon', 'adult-crystal-dragon',
    'adult-deep-dragon', 'adult-emerald-dragon', 'adult-gold-dragon',
    'adult-green-dragon', 'adult-kruthik', 'adult-moonstone-dragon',
    'adult-oblex', 'adult-red-dragon', 'adult-sapphire-dragon',
    'adult-silver-dragon', 'adult-topaz-dragon', 'adult-white-dragon',
    'air-elemental-myrmidon', 'air-elemental', 'alhoon', 'alkilith', 'allip',
    'allosaurus', 'alustriel-silverhand', 'amethyst-dragon-wyrmling', 'amnizu',
    'ancient-amethyst-dragon', 'ancient-black-dragon', 'ancient-blue-dragon',
    'ancient-brass-dragon', 'ancient-bronze-dragon', 'ancient-copper-dragon',
    'ancient-crystal-dragon', 'ancient-deep-dragon', 'ancient-dragon-turtle',
    'ancient-emerald-dragon', 'ancient-gold-dragon', 'ancient-green-dragon',
    'ancient-moonstone-dragon', 'ancient-red-dragon', 'ancient-sapphire-dragon',
    'ancient-sea-serpent', 'ancient-shadow', 'ancient-silver-dragon',
    'ancient-topaz-dragon', 'ancient-white-dragon', 'androsphinx',
    'angry-sorrowsworn', 'animated-armor', 'animated-breath', 'ankheg',
    'ankylosaurus', 'annis-hag', 'ape', 'apprentice-wizard', 'arcanaloth',
    'archdruid', 'archer', 'archmage', 'armanite', 'asmodeus', 'assassin-vine',
    'assassin', 'astral-dreadnought', 'aurak-draconian', 'aurochs',
    'autumn-eladrin', 'avatar-of-death', 'awakened-shrub', 'awakened-tree',
    'axe-beak', 'azer', 'baalzebul', 'baaz-draconian', 'babau', 'baboon',
    'badger', 'bael', 'bag-jelly', 'balhannoth', 'balor', 'banderhobb',
    'bandit-captain', 'bandit', 'banshee', 'baphomet', 'barbed-devil',
    'bard', 'barghest', 'barlgura', 'barrowghast', 'basilisk', 'bat',
    'bearded-devil', 'beast-of-the-land', 'beast-of-the-sea', 'beast-of-the-sky',
    'behir', 'beholder-zombie', 'beholder', 'bel', 'belaphoss', 'belial',
    'berbalang', 'berserker', 'bestial-spirit', 'bheur-hag', 'black-abishai',
    'black-bear', 'black-dragon-wyrmling', 'black-gauntlet-of-bane',
    'black-pudding', 'blackguard', 'blink-dog', 'blood-hawk', 'blue-abishai',
    'blue-dragon-wyrmling', 'blue-slaad', 'boar', 'bodak', 'boggle',
    'bone-devil', 'bone-naga', 'boneclaw', 'bozak-draconian', 'brain-in-a-jar',
    'brass-dragon-wyrmling', 'bronze-dragon-wyrmling', 'brown-bear',
    'bugbear-chief', 'bugbear', 'bulette', 'bulezau', 'bullywug-knight',
    'bullywug', 'cadaver-collector', 'cairnwight', 'cambion', 'camel',
    'canoloth', 'carrion-crawler', 'cat', 'catoblepas', 'cave-fisher',
    'celestial-spirit', 'centaur', 'chain-devil', 'champion', 'chasme',
    'chimera', 'chitine', 'choker', 'choldrith', 'chromatic-greatwyrm', 'chuul',
    'cinder-hulk', 'clay-golem', 'cloaker', 'clockwork-iron-cobra',
    'cloud-giant-destiny-gambler', 'cloud-giant-of-evil-air',
    'cloud-giant-smiling-one', 'cloud-giant', 'cockatrice', 'commoner',
    'conjurer-wizard', 'constrictor-snake', 'construct-spirit',
    'copper-dragon-wyrmling', 'corpse-flower', 'couatl', 'crab',
    'cradle-of-the-cloud-scion', 'cradle-of-the-fire-scion',
    'cradle-of-the-frost-scion', 'cradle-of-the-hill-scion',
    'cradle-of-the-stone-scion', 'cradle-of-the-storm-scion', 'cranium-rat',
    'crawling-claw', 'crocodile', 'crokek-toeck', 'crystal-dragon-wyrmling',
    'cult-fanatic', 'cultist', 'cyclops', 'dancing-item', 'dao',
    'darkling-elder', 'darkling', 'darkmantle', 'death-dog',
    'death-giant-reaper', 'death-giant-shrouded-one', 'death-kiss',
    'death-knight', 'death-s-head-of-bhaal', 'death-slaad', 'death-tyrant',
    'deathlock-mastermind', 'deathlock-wight', 'deathlock', 'deep-dragon-wyrmling',
    'deep-gnome-svirfneblin', 'deep-rothe', 'deep-scion', 'deer', 'demilich',
    'demogorgon', 'derro-savant', 'derro', 'deva', 'devilroot', 'devourer',
    'dhergoloth', 'dire-troll', 'dire-wolf', 'dispater', 'displacer-beast',
    'diviner-wizard', 'djinni', 'dolphin-delighter', 'dolphin', 'doppelganger',
    'dracohydra', 'draconian-dreadnought', 'draconian-foot-soldier',
    'draconian-infiltrator', 'draconian-mage', 'draconian-mastermind',
    'draconic-shard', 'draconic-spirit', 'draegloth', 'draft-horse',
    'dragon-blessed', 'dragon-chosen', 'dragon-speaker', 'dragon-turtle-wyrmling',
    'dragon-turtle', 'dragonblood-ooze', 'dragonbone-golem',
    'dragonborn-of-bahamut', 'dragonborn-of-sardior', 'dragonborn-of-tiamat',
    'dragonflesh-abomination', 'dragonflesh-grafter', 'dragonnel',
    'drake-companion', 'dretch', 'drider', 'drow-arachnomancer',
    'drow-elite-warrior', 'drow-favored-consort', 'drow-house-captain',
    'drow-inquisitor', 'drow-mage', 'drow-matron-mother',
    'drow-priestess-of-lolth', 'drow-shadowblade', 'drow', 'druid', 'dryad',
    'duergar-despot', 'duergar-kavalrachni', 'duergar-mind-master',
    'duergar-soulblade', 'duergar-stone-guard', 'duergar-warlord',
    'duergar-xarrorn', 'duergar', 'duodrone', 'dust-hulk', 'dust-mephit',
    'dybbuk', 'eagle', 'earth-elemental-myrmidon', 'earth-elemental',
    'echo-of-demogorgon', 'efreeti', 'eidolon', 'elder-brain-dragon',
    'elder-brain', 'elder-oblex', 'elder-tempest', 'elemental-spirit',
    'elephant', 'elk', 'emerald-dragon-wyrmling', 'empyrean', 'enchanter-wizard',
    'erinyes', 'ettercap', 'ettin-ceremorph', 'ettin', 'evoker-wizard',
    'expert-lvl-1', 'expert-lvl-2', 'expert-lvl-3', 'expert-lvl-4',
    'expert-lvl-5', 'expert-lvl-6', 'eyedrake', 'faerie-dragon',
    'female-steeder', 'fensir-devourer', 'fensir-skirmisher', 'fey-spirit',
    'fiendish-spirit', 'fierna', 'firbolg-primeval-warden', 'firbolg-wanderer',
    'fire-elemental-myrmidon', 'fire-elemental', 'fire-giant-dreadnought',
    'fire-giant-forgecaller', 'fire-giant-of-evil-fire', 'fire-giant',
    'fire-hellion', 'fire-snake', 'firegaunt', 'firenewt-warlock-of-imix',
    'firenewt-warrior', 'fist-of-bane', 'flail-snail', 'flameskull',
    'flesh-colossus', 'flesh-golem', 'flind', 'flumph', 'flying-snake',
    'flying-sword', 'fomorian-deep-crawler', 'fomorian-noble',
    'fomorian-warlock-of-the-dark', 'fomorian', 'fox', 'fraz-urb-luu', 'frog',
    'froghemoth', 'frost-druid', 'frost-giant-everlasting-one',
    'frost-giant-ice-shaper', 'frost-giant-of-evil-water', 'frost-giant',
    'frost-salamander', 'frostmourn', 'fury-of-kostchtchie', 'galeb-duhr',
    'gargantua', 'gargoyle', 'gas-spore', 'gauth', 'gazer', 'gelatinous-cube',
    'gem-greatwyrm', 'gem-stalker', 'geryon', 'ghast', 'ghost-dragon', 'ghost',
    'ghoul', 'giant-ape', 'giant-badger', 'giant-bat', 'giant-boar',
    'giant-centipede', 'giant-constrictor-snake', 'giant-crab',
    'giant-crocodile', 'giant-eagle', 'giant-elk', 'giant-fire-beetle',
    'giant-frog', 'giant-goat', 'giant-goose', 'giant-hyena', 'giant-lizard',
    'giant-lynx', 'giant-octopus', 'giant-owl', 'giant-ox',
    'giant-poisonous-snake', 'giant-ram', 'giant-rat', 'giant-scorpion',
    'giant-sea-horse', 'giant-shark', 'giant-spider', 'giant-strider',
    'giant-toad', 'giant-two-headed-goat', 'giant-vulture', 'giant-walrus',
    'giant-wasp', 'giant-weasel', 'giant-wolf-spider', 'gibbering-mouther',
    'giff', 'gigant', 'girallon', 'githyanki-gish', 'githyanki-kith-rak',
    'githyanki-knight', 'githyanki-supreme-commander', 'githyanki-warrior',
    'githzerai-anarch', 'githzerai-enlightened', 'githzerai-monk',
    'githzerai-zerth', 'glabrezu', 'gladiator', 'glasya', 'gnoll-fang-of-yeenoghu',
    'gnoll-flesh-gnawer', 'gnoll-hunter', 'gnoll-pack-lord', 'gnoll-witherling',
    'gnoll', 'goat', 'goblin-boss', 'goblin', 'gold-dragon-wyrmling',
    'goliath-giant-kin', 'gorgon', 'goristro', 'gray-ooze', 'gray-render',
    'gray-slaad', 'graz-zt', 'green-abishai', 'green-dragon-wyrmling',
    'green-hag', 'green-slaad', 'grell', 'grick-alpha', 'grick', 'griffon',
    'grimlock', 'grinning-cat', 'grung-elite-warrior', 'grung-wildling',
    'grung', 'guard-drake', 'guard', 'guardian-naga', 'gynosphinx',
    'halaster-blackcloak', 'half-ogre', 'half-red-dragon-veteran', 'hare',
    'harpy', 'hawk', 'hell-hound', 'hellfire-engine', 'hellwasp', 'helmed-horror',
    'hezrou', 'hill-giant-avalancher', 'hill-giant', 'hippogriff', 'hoard-mimic',
    'hoard-scarab', 'hobgoblin-captain', 'hobgoblin-devastator',
    'hobgoblin-iron-shadow', 'hobgoblin-warlord', 'hobgoblin', 'hollow-dragon',
    'homunculus-servant', 'homunculus', 'hook-horror', 'horned-devil', 'howler',
    'hungry-sorrowsworn', 'hunter-shark', 'hutijin', 'hydra', 'hydroloth',
    'hyena', 'ice-devil', 'ice-mephit', 'iggwilv-the-witch-queen',
    'illusionist-wizard', 'imix', 'imp', 'intellect-devourer', 'invisible-stalker',
    'iron-consul', 'iron-golem', 'jackal', 'jackalwere', 'jarlaxle-baenre',
    'juiblex', 'kapak-draconian', 'kender-skirmisher', 'kenku', 'ki-rin',
    'killer-whale', 'knight', 'knucklehead-trout', 'kobold-dragonshield',
    'kobold-inventor', 'kobold-scale-sorcerer', 'kobold', 'korred',
    'kraken-priest', 'kraken', 'kruthik-hive-lord', 'kuo-toa-archpriest',
    'kuo-toa-whip', 'kuo-toa', 'laeral-silverhand', 'lamia', 'lemure',
    'leucrotta', 'leviathan', 'levistus', 'lich', 'lightning-hulk', 'lion',
    'liondrake', 'lizard-king-queen', 'lizard', 'lizardfolk-shaman',
    'lizardfolk', 'lonely-sorrowsworn', 'lord-soth', 'lost-sorrowsworn', 'mage',
    'magma-mephit', 'magmin', 'male-steeder', 'mammon', 'mammoth', 'manes',
    'manshoon', 'manticore', 'marid', 'marilith', 'martial-arts-adept', 'marut',
    'master-of-souls', 'master-sage', 'master-thief', 'mastiff', 'maurezhi',
    'maw-demon', 'maw-of-yeenoghu', 'meazel', 'medusa', 'meenlock',
    'mephistopheles', 'merfolk', 'merregon', 'merrenoloth', 'merrow',
    'metallic-greatwyrm', 'mezzoloth', 'mighty-servant-of-leuk-o', 'miirym',
    'mimic', 'mind-flayer', 'mindwitness', 'minor-air-elemental',
    'minor-earth-elemental', 'minor-fire-elemental', 'minor-water-elemental',
    'minotaur-skeleton', 'minotaur', 'mist-hulk', 'moloch', 'molydeus',
    'monodrone', 'moonstone-dragon-wyrmling', 'morkoth', 'mountain-goat',
    'mouth-of-grolantor', 'mud-hulk', 'mud-mephit', 'muiral', 'mule',
    'mummified-warrior', 'mummy-lord', 'mummy', 'myconid-adult',
    'myconid-sovereign', 'myconid-sprout', 'nabassu', 'nagpa', 'nalfeshnee',
    'narzugon', 'necromancer-wizard', 'necromite-of-myrkul', 'needle-blight',
    'neogi-hatchling', 'neogi-master', 'neogi', 'neothelid', 'night-blade',
    'night-hag', 'nightmare', 'nightwalker', 'nilbog', 'nothic', 'nupperibo',
    'nycaloth', 'oblex-spawn', 'ochre-jelly', 'octopus', 'ogre-battering-ram',
    'ogre-bolt-launcher', 'ogre-chain-brute', 'ogre-howdah', 'ogre-zombie',
    'ogre', 'ogremoch', 'oinoloth', 'olhydra', 'oni', 'orc-blade-of-ilneval',
    'orc-claw-of-luthic', 'orc-eye-of-gruumsh', 'orc-hand-of-yurtrus',
    'orc-red-fang-of-shargaas', 'orc-war-chief', 'orc', 'orcus', 'orog',
    'orthon', 'otyugh', 'owl', 'owlbear', 'ox', 'panther', 'pegasus',
    'pentadrone', 'peryton', 'phase-spider', 'phoenix', 'piercer',
    'pit-fiend', 'pixie', 'planetar', 'plesiosaurus', 'poisonous-snake',
    'polar-bear', 'pony', 'priest', 'pseudodragon', 'pteranodon',
    'purple-worm', 'quadrone', 'quaggoth-spore-servant', 'quaggoth', 'quasit',
    'quetzalcoatlus', 'quickling', 'quipper', 'rakshasa', 'rat', 'raven',
    'reaper-of-bhaal', 'red-abishai', 'red-dragon-wyrmling', 'red-slaad',
    'redcap', 'reef-manta-ray', 'reef-shark', 'regisaur', 'remorhaz',
    'retriever', 'revenant', 'rhinoceros', 'riding-horse', 'rime-hulk', 'roc',
    'roper', 'rot-troll', 'rothe', 'rug-of-smothering', 'runic-colossus',
    'rust-monster', 'rutterkin', 'saber-toothed-tiger', 'sage',
    'sahuagin-baron', 'sahuagin-priestess', 'sahuagin', 'salamander',
    'sapphire-dragon-wyrmling', 'satyr', 'scarecrow', 'scion-of-grolantor',
    'scion-of-memnor', 'scion-of-skoraeus', 'scion-of-stronmaus',
    'scion-of-surtur', 'scion-of-thrym', 'scorpion', 'scout', 'sea-hag',
    'sea-horse', 'sea-spawn', 'seal', 'shadar-kai-gloom-weaver',
    'shadar-kai-shadow-dancer', 'shadar-kai-soul-monger', 'shadow-demon',
    'shadow-mastiff-alpha', 'shadow-mastiff', 'shadow-spirit', 'shadow',
    'shambling-mound', 'shield-guardian', 'shoosuva', 'shrieker', 'sibriex',
    'silver-dragon-wyrmling', 'sivak-draconian', 'skeletal-knight', 'skeleton',
    'skulk', 'skull-lasher-of-myrkul', 'skull-lord', 'slaad-tadpole',
    'slithering-tracker', 'smoke-mephit', 'solar', 'spawn-of-kyuss',
    'spectator', 'specter', 'spectral-cloud', 'spellcaster-lvl-1',
    'spellcaster-lvl-2', 'spellcaster-lvl-3', 'spellcaster-lvl-4',
    'spellcaster-lvl-5', 'spellcaster-lvl-6', 'sperm-whale', 'spider',
    'spined-devil', 'spirit-naga', 'spirit-troll', 'spotted-lion',
    'spring-eladrin', 'sprite', 'spy', 'stalker-of-baphomet', 'star-spawn-grue',
    'star-spawn-hulk', 'star-spawn-larva-mage', 'star-spawn-mangler',
    'star-spawn-seer', 'steam-mephit', 'steel-defender', 'steel-predator',
    'stench-kow', 'stirge', 'stone-cursed', 'stone-giant-dreamwalker',
    'stone-giant-of-evil-earth', 'stone-giant-rockspeaker', 'stone-giant',
    'stone-golem', 'storm-crab', 'storm-giant-quintessent',
    'storm-giant-tempest-caller', 'storm-giant', 'storm-herald',
    'strahd-von-zarovich', 'succubus', 'summer-eladrin', 'swarm-of-bats',
    'swarm-of-cranium-rats', 'swarm-of-insects', 'swarm-of-poisonous-snakes',
    'swarm-of-quippers', 'swarm-of-rats', 'swarm-of-ravens',
    'swarm-of-rot-grubs', 'swashbuckler', 'sword-wraith-commander',
    'sword-wraith-warrior', 'tabaxi-hunter', 'tabaxi-minstrel', 'tanarukk',
    'tarrasque', 'tempest-spirit', 'thorny-vegepygmy', 'thri-kreen', 'thug',
    'tiamat', 'tiger', 'tiny-servant', 'titanothere', 'titivilus', 'tlincalli',
    'topaz-dragon-wyrmling', 'tortle-druid', 'tortle', 'transmuter-wizard',
    'trapper', 'treant', 'tribal-warrior', 'triceratops', 'tridrone',
    'troglodyte', 'troll-amalgam', 'troll-mutate', 'troll', 'twig-blight',
    'tyrannosaurus-rex', 'ulitharid', 'ultroloth', 'umber-hulk', 'undead-spirit',
    'unicorn', 'uthgardt-shaman', 'vajra-safahr', 'vampire-spawn', 'vampire',
    'vampiric-mist', 'vargouille', 'vecna-the-archlich', 'vegepygmy-chief',
    'vegepygmy', 'vellynne-harpell', 'velociraptor', 'venerable-shadow',
    'venom-troll', 'veteran', 'vine-blight', 'violet-fungus', 'vrock',
    'vulture', 'walrus', 'war-priest', 'warhorse-skeleton', 'warhorse',
    'warlock-of-the-archfey', 'warlock-of-the-fiend', 'warlock-of-the-great-old-one',
    'warlord', 'warrior-lvl-1', 'warrior-lvl-2', 'warrior-lvl-3',
    'warrior-lvl-4', 'warrior-lvl-5', 'warrior-lvl-6', 'wastrilith',
    'water-elemental-myrmidon', 'water-elemental', 'water-weird', 'weasel',
    'were-bat', 'werebear', 'wereboar', 'wererat', 'weretiger', 'werewolf',
    'wersten-kern', 'white-abishai', 'white-dragon-wyrmling', 'wight',
    'wild-dog-alpha', 'wild-dog', 'wildfire-spirit', 'will-o--wisp',
    'winged-kobold', 'winter-eladrin', 'winter-wolf', 'wolf', 'wood-woad',
    'worg', 'wraith', 'wretched-sorrowsworn', 'wyvern', 'xorn',
    'xvart-warlock-of-raxivort', 'xvart', 'yagnoloth', 'yan-c-bin', 'yeenoghu',
    'yellow-musk-creeper', 'yellow-musk-zombie', 'yeth-hound', 'yeti',
    'yochlol', 'young-amethyst-dragon', 'young-black-dragon', 'young-blue-dragon',
    'young-brass-dragon', 'young-bronze-dragon', 'young-copper-dragon',
    'young-crystal-dragon', 'young-deep-dragon', 'young-dragon-turtle',
    'young-emerald-dragon', 'young-gold-dragon', 'young-green-dragon',
    'young-kruthik', 'young-moonstone-dragon', 'young-red-dragon',
    'young-red-shadow-dragon', 'young-remorhaz', 'young-sapphire-dragon',
    'young-sea-serpent', 'young-silver-dragon', 'young-topaz-dragon',
    'young-white-dragon', 'yuan-ti-abomination', 'yuan-ti-anathema',
    'yuan-ti-broodguard', 'yuan-ti-malison', 'yuan-ti-mind-whisperer',
    'yuan-ti-nightmare-speaker', 'yuan-ti-pit-master', 'yuan-ti-pureblood',
    'zaratan', 'zargon-the-returner', 'zariel', 'zombie', 'zuggtmoy'
]

def generate_monster_class(name: str, data: dict) -> str:
    """Generate Python class code for a monster"""
    class_name = ''.join(word.capitalize() for word in name.split('-'))
    
    # Extract data
    size = data.get('size', 'Medium')
    creature_type = data.get('type', 'Unknown').split(',')[0].strip()
    alignment = data.get('type', 'Unknown').split(',')[1].strip() if ',' in data.get('type', '') else 'Unaligned'
    
    stats = {
        "hit_points": data.get('hit_points', 10),
        "min_level": 1,
        "level": 1,
        "STR": data.get('STR', 10),
        "DEX": data.get('DEX', 10),
        "CON": data.get('CON', 10),
        "INT": data.get('INT', 10),
        "WIS": data.get('WIS', 10),
        "CHAR": data.get('CHA', 10),
        "armor_class": data.get('armor_class', 10),
        "alignment": alignment,
        "legendary": False,
        "size": size,
        "type": creature_type,
        "challenge": data.get('challenge', '0'),
        "saving_throws": data.get('saving_throws'),
        "skills": data.get('skills'),
        "damage_resistances": data.get('damage_resistances'),
        "damage_immunities": data.get('damage_immunities'),
        "condition_immunities": data.get('condition_immunities'),
        "senses": data.get('senses'),
        "languages": data.get('languages'),
        "hit_points_up": [1, 1, 1],
        "STR_up": [1, 1, 0],
        "DEX_up": [0, 1, 0],
        "CON_up": [0, 0, 1],
        "INT_up": [1, 0, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 0],
        "abilities": [],
    }
    
    # Abilities
    abilities = []
    for trait in data.get('traits', []):
        ability_name = trait['name'].lower().replace(' ', '_').replace("'", "")
        abilities.append(ability_name)
    
    for action in data.get('actions', []):
        action_name = action['name'].lower().replace(' ', '_').replace("'", "")
        abilities.append(action_name)
    
    stats["abilities"] = abilities
    
    # Generate code
    code = f'''# bases1/{name}.py
"""
{class_name} creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo={name}
"""
from creature_base import GlobalCreatureBaseClass


class {class_name}(GlobalCreatureBaseClass):
    """
    {size} {creature_type} creature - {class_name}
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {stats!r}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
'''
    
    # Add trait methods
    for trait in data.get('traits', []):
        method_name = trait['name'].lower().replace(' ', '_').replace("'", "")
        desc = trait['description']
        code += f'''
    def {method_name}(self) -> str:
        """{desc}"""
        return {desc!r}
'''
    
    # Add action methods
    for action in data.get('actions', []):
        method_name = action['name'].lower().replace(' ', '_').replace("'", "") + '_attack'
        desc = action['description']
        code += f'''
    def {method_name}(self) -> str:
        """{desc}"""
        return {desc!r}
'''
    
    code += '''
'''
    return code

def main():
    os.makedirs('bases1', exist_ok=True)
    
    for name in MONSTER_NAMES:
        print(f"Scraping {name}...")
        data = scrape_monster(name)
        if data:
            code = generate_monster_class(name, data)
            filepath = f'bases1/{name}.py'
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"Generated {filepath}")
        else:
            print(f"Failed to scrape {name}")

if __name__ == "__main__":
    main()