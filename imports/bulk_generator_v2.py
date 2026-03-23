#!/usr/bin/env python3
"""
Enhanced Bulk Monster Generator
Scrapes all monsters from AiDeDd and creates/updates creature classes in bases1/
Intelligently handles abilities and updates existing classes
"""

import os
import sys
import re
import time
import ast
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from typing import List, Dict, Set, Optional
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from imports.aidedd_scraper import scrape_monster


def normalize_class_name(monster_name: str) -> str:
    """Convert monster name to valid Python class name"""
    parts = monster_name.split('-')
    return ''.join(word.capitalize() for word in parts)


def normalize_ability_name(ability_name: str) -> str:
    """Convert ability name to valid Python method name
    
    Examples:
        'Keen Smell' -> 'keen_smell'
        'Legendary Resistance' -> 'legendary_resistance'
    """
    # Remove special characters and convert to snake_case
    name = re.sub(r'[^a-zA-Z\s]', '', ability_name)
    name = name.strip().lower().replace(' ', '_')
    return name


def extract_abilities_from_scraped_data(monster_data: Dict) -> List[Dict[str, str]]:
    """Extract structured ability data from scraped monster data
    
    Returns list of dicts with 'name' and 'description' keys
    """
    abilities = []
    
    # Extract traits that were populated by the scraper
    if 'traits' in monster_data and monster_data['traits']:
        for item in monster_data['traits']:
            if isinstance(item, dict):
                if 'name' in item and 'description' in item:
                    # Validates both name and description exist
                    abilities.append({
                        'name': item['name'],
                        'description': item['description']
                    })
            elif isinstance(item, str):
                # Parse simple string format: "Name. Description"
                match = re.match(r'([^.]+)\.\s*(.*)', item)
                if match:
                    name = match.group(1).strip()
                    desc = match.group(2).strip()
                    if name and desc:
                        abilities.append({
                            'name': name,
                            'description': desc
                        })
    
    return abilities


def read_existing_class(filepath: Path) -> Optional[Dict]:
    """Read and parse an existing creature class file
    
    Returns dict with class info or None if file doesn't exist
    """
    if not filepath.exists():
        return None
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        return {
            'content': content,
            'exists': True
        }
    except Exception as e:
        print(f"    Warning: Could not read {filepath}: {e}")
        return {'exists': False, 'error': str(e)}


def generate_ability_methods(abilities: List[Dict[str, str]]) -> str:
    """Generate Python method code for creature abilities"""
    
    if not abilities:
        return ""
    
    methods = ""
    for ability in abilities:
        method_name = normalize_ability_name(ability['name'])
        desc = ability['description'].replace('"', '\\"')
        
        methods += f'''
    def {method_name}(self) -> str:
        """{ability['name']}: {desc[:100]}..."""
        return "{desc}"
'''
    
    return methods


def generate_creature_class(monster_name: str, monster_data: Dict, abilities: List[Dict[str, str]]) -> str:
    """Generate Python code for a creature class"""
    
    class_name = normalize_class_name(monster_name)
    
    # Extract data with safe defaults
    hit_points = monster_data.get('hit_points', 10)
    armor_class = monster_data.get('armor_class', 10)
    size = monster_data.get('size', 'Medium')
    creature_type = monster_data.get('type', 'Beast')
    alignment = monster_data.get('alignment', 'Unaligned')
    
    str_score = monster_data.get('STR', 10)
    dex_score = monster_data.get('DEX', 10)
    con_score = monster_data.get('CON', 10)
    int_score = monster_data.get('INT', 10)
    wis_score = monster_data.get('WIS', 10)
    cha_score = monster_data.get('CHA', 10)
    
    # Calculate min_level based on challenge rating
    challenge = monster_data.get('challenge', {}).get('rating', '0')
    challenge_num = float(challenge.split('/')[0]) if isinstance(challenge, str) else challenge
    min_level = max(1, int(challenge_num) + 1)
    
    # Calculate hit_points_up (max of 1, or 10% of HP)
    hp_up_max = max(1, int(hit_points * 0.1))
    
    # Create _up arrays that guarantee column sums = 2
    hit_points_up = [hp_up_max] * 3
    
    # Distribute ability increases based on scores
    ability_scores = [
        ('STR', str_score),
        ('DEX', dex_score),
        ('CON', con_score),
        ('INT', int_score),
        ('WIS', wis_score),
        ('CHA', cha_score)
    ]
    
    # Sort by score (highest first)
    sorted_abilities = sorted(ability_scores, key=lambda x: -x[1])
    
    # Create base arrays
    str_up = [0, 0, 0]
    dex_up = [0, 0, 0]
    con_up = [0, 0, 0]
    int_up = [0, 0, 0]
    wis_up = [0, 0, 0]
    cha_up = [0, 0, 0]
    
    ability_arrays = {
        'STR': str_up,
        'DEX': dex_up,
        'CON': con_up,
        'INT': int_up,
        'WIS': wis_up,
        'CHA': cha_up
    }
    
    # Fill columns to sum = 2
    col_0_abilities = sorted_abilities[0:2]
    col_1_abilities = sorted_abilities[2:4]
    col_2_abilities = sorted_abilities[4:6]
    
    for ability_name, _ in col_0_abilities:
        ability_arrays[ability_name][0] += 1
    
    for ability_name, _ in col_1_abilities:
        ability_arrays[ability_name][1] += 1
    
    for ability_name, _ in col_2_abilities:
        ability_arrays[ability_name][2] += 1
    
    # Generate ability method code
    ability_methods = generate_ability_methods(abilities)
    
    # Build abilities list for __init__
    ability_names = [normalize_ability_name(a['name']) for a in abilities]
    
    code = f'''# bases1/{monster_name}.py
"""
{class_name} creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo={monster_name}
"""
from creature_base import GlobalCreatureBaseClass


class {class_name}(GlobalCreatureBaseClass):
    """
    {class_name} creature
    Size: {size}, Type: {creature_type}
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {{
        "hit_points": {hit_points},
        "min_level": {min_level},
        "level": {min_level},
        "STR": {str_score},
        "DEX": {dex_score},
        "CON": {con_score},
        "INT": {int_score},
        "WIS": {wis_score},
        "CHAR": {cha_score},
        "armor_class": {armor_class},
        "alignment": "{alignment}",
        "legendary": False,
        "size": "{size}",
        "type": "{creature_type}",
        "hit_points_up": {hit_points_up},
        "STR_up": {str_up},
        "DEX_up": {dex_up},
        "CON_up": {con_up},
        "INT_up": {int_up},
        "WIS_up": {wis_up},
        "CHAR_up": {cha_up},
        "abilities": [],
    }}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Add creature-specific abilities
{f"        self.abilities.extend([{', '.join(repr(a) for a in ability_names)}])" if ability_names else "        # No special abilities"}
{ability_methods}
'''
    
    return code


def update_existing_class(filepath: Path, monster_name: str, monster_data: Dict, abilities: List[Dict[str, str]]) -> bool:
    """Update an existing creature class with new ability information
    
    Returns True if successfully updated, False otherwise
    """
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # If abilities list is empty, don't update
        if not abilities:
            return False
        
        # Extract the class name
        class_name = normalize_class_name(monster_name)
        
        # Find the __init__ method
        init_pattern = r'(    def __init__\(self, \*args, \*\*kwargs\) -> None:\n        super\(\)\.__init__\(\*args, \*\*kwargs\)\n)'
        
        # Generate ability initialization code
        ability_names = [normalize_ability_name(a['name']) for a in abilities]
        ability_init = f"self.abilities.extend([{', '.join(repr(a) for a in ability_names)}])"
        
        # Replace or insert ability initialization
        if 'self.abilities.append' in content or 'self.abilities.extend' in content:
            # Update existing abilities
            content = re.sub(
                r'(def __init__.*?:\n.*?super\(\).__init__\(.*?\)\n)(.*?self\.abilities\.[^\n]+)',
                f'\\1        {ability_init}',
                content,
                flags=re.DOTALL
            )
        else:
            # Insert abilities after super().__init__
            content = re.sub(
                init_pattern,
                f'\\1        {ability_init}\n',
                content
            )
        
        # Generate and append ability methods
        ability_methods = generate_ability_methods(abilities)
        
        if ability_methods:
            # Add methods before the last line (or at end)
            content = content.rstrip() + ability_methods + '\n'
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        return True
    
    except Exception as e:
        print(f"    Error updating {filepath}: {e}")
        return False


def get_all_monster_names() -> Set[str]:
    """Extract all monster names from the monsters filter page (all filters checked)"""
    url = "https://www.aidedd.org/dnd-filters/monsters.php"
    
    print("[1/4] Fetching monster list from AiDeDd with Category/Type/Size/Source enabled...")
    try:
        # Force all filter values (all sources too) to retrieve full monster set
        payload = {
            'Filtre1[]': ['M', 'A', 'P'],  # Category: Monsters, Beasts, NPC
            'Filtre2[]': ['Humanoid', 'Aberration', 'Beast', 'Celestial', 'Construct', 'Dragon',
                          'Elemental', 'Fey', 'Fiend', 'Giant', 'Monstrosity', 'Ooze', 'Plant', 'Undead'],
            'Filtre3[]': ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan'],
            'source[]': ['base', 'ftod', 'motm', 'gog', 'rule', 'adv', 'nono'],
            'nivMin': '-1',
            'nivMax': '30',
            'filtrer': 'FILTER'
        }

        req = Request(url, data=urlencode(payload, doseq=True).encode('utf-8'),
                      headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8', errors='ignore')

        pattern = r'monstres\.php\?vo=([^"&\s]+)'
        matches = re.findall(pattern, html)

        monsters = sorted(set(matches))
        print(f"✓ Found {len(monsters)} unique monsters")
        return monsters

    except Exception as e:
        print(f"✗ Error fetching monster list: {e}")
        print("  Falling back to default GET mode...")
        try:
            with urlopen(url, timeout=30) as response:
                html = response.read().decode('utf-8', errors='ignore')

            pattern = r'monstres\.php\?vo=([^"&\s]+)'
            matches = re.findall(pattern, html)
            monsters = sorted(set(matches))
            print(f"✓ Found {len(monsters)} unique monsters (fallback)")
            return monsters
        except Exception as fallback_e:
            print(f"✗ Fallback error: {fallback_e}")
            return set()


def main():
    print("="*70)
    print("ENHANCED BULK MONSTER GENERATOR - AiDeDd to Python Classes")
    print("="*70)
    
    # Get all monster names
    monsters = get_all_monster_names()
    if not monsters:
        print("✗ Could not retrieve monster list")
        return
    
    bases1_dir = Path(__file__).parent.parent / "bases1"
    bases1_dir.mkdir(exist_ok=True)
    
    print(f"\n[2/4] Scraping and generating/updating classes...")
    
    created = 0
    updated = 0
    failed = 0
    skipped = 0
    
    # Reserved files to skip
    reserved = {'base1_a.py', 'base1_b.py', 'base2_a.py', 'base2_b.py', 
                'base3_a.py', 'base3_b.py', '__init__.py'}
    
    for i, monster_name in enumerate(monsters, 1):
        class_name = normalize_class_name(monster_name)
        class_file = bases1_dir / f"{monster_name}.py"
        
        # Skip reserved files
        if class_file.name in reserved:
            skipped += 1
            continue
        
        try:
            # Scrape monster data
            monster_data = scrape_monster(monster_name)
            
            if not monster_data:
                failed += 1
                continue
            
            # Extract abilities from scraped data
            abilities = extract_abilities_from_scraped_data(monster_data)
            hp = monster_data.get('hit_points', '?')
            
            # Check if file exists
            if class_file.exists():
                # Try to update with new abilities
                if update_existing_class(class_file, monster_name, monster_data, abilities):
                    print(f"  [{i:3d}/{len(monsters)}] ↻ {class_name} ({hp} HP) - updated with abilities")
                    updated += 1
                else:
                    print(f"  [{i:3d}/{len(monsters)}] ✓ {class_name} ({hp} HP) - exists (no abilities)")
                    skipped += 1
            else:
                # Create new class
                code = generate_creature_class(monster_name, monster_data, abilities)
                with open(class_file, 'w') as f:
                    f.write(code)
                
                ability_count = len(abilities)
                print(f"  [{i:3d}/{len(monsters)}] ✓ {class_name} ({hp} HP) - created ({ability_count} abilities)")
                created += 1
            
            # Rate limiting
            time.sleep(0.3)
        
        except Exception as e:
            print(f"  [{i:3d}/{len(monsters)}] ✗ {class_name} ({str(e)[:35]})")
            failed += 1
            time.sleep(0.3)
    
    print(f"\n[3/4] Summary")
    print("-"*70)
    print(f"  ✓ Created:  {created}")
    print(f"  ↻ Updated:  {updated}")
    print(f"  ✓ Exist:    {skipped}")
    print(f"  ✗ Failed:   {failed}")
    print(f"  Total:      {len(monsters)}")
    
    print(f"\n[4/4] Classes generated/updated in: bases1/")


if __name__ == "__main__":
    main()
