"""
AiDeDd Monster Web Scraper
Scrapes monster data from https://www.aidedd.org/dnd/monstres.php?vo=<monster_name>
"""

import re
from typing import Optional, Dict, Any, List
from urllib.request import urlopen
from html.parser import HTMLParser


class MonsterHTMLParser(HTMLParser):
    """Custom HTML parser to extract monster stat blocks from AiDeDd pages"""
    
    def __init__(self):
        super().__init__()
        self.monster_data = {
            "name": None,
            "type": None,
            "size": None,
            "armor_class": None,
            "hit_points": None,
            "hit_dice": None,
            "speed": None,
            "STR": None,
            "DEX": None,
            "CON": None,
            "INT": None,
            "WIS": None,
            "CHA": None,
            "senses": None,
            "languages": None,
            "challenge": None,
            "traits": [],  # Special abilities/traits
            "actions": [],  # Combat actions
        }
        self.current_section = None
        self.in_h1 = False
        self.in_title = False
        self.text_buffer = ""
        self.last_strong = ""
        self.in_jaune = False
        self.current_trait = None
        self.current_trait_desc = ""
        
    def handle_starttag(self, tag: str, attrs: list):
        if tag == "h1":
            self.in_h1 = True
        elif tag == "div":
            for attr, value in attrs:
                if attr == "class" and "jaune" in value:
                    self.in_jaune = True
        elif tag == "strong" and self.in_jaune:
            self.text_buffer = ""
    
    def handle_endtag(self, tag: str):
        if tag == "h1":
            self.in_h1 = False
        elif tag == "strong" and self.in_jaune:
            self.last_strong = self.text_buffer.strip()
            self.text_buffer = ""
    
    def handle_data(self, data: str):
        if self.in_h1:
            self.monster_data["name"] = data.strip()
            self.in_h1 = False
        elif self.in_jaune:
            self.text_buffer += data
            
            # Parse type info (e.g., "Tiny beast, unaligned")
            if "type:" not in self.text_buffer.lower() and re.search(r"(Tiny|Small|Medium|Large|Huge|Gargantuan)", data):
                type_match = re.search(r"(Tiny|Small|Medium|Large|Huge|Gargantuan)\s+(.*?)(?=<|$)", data)
                if type_match:
                    size_creature = type_match.group(0)
                    parts = size_creature.split()
                    self.monster_data["size"] = parts[0]
                    self.monster_data["type"] = " ".join(parts[1:])
            
            # Parse Armor Class
            if self.last_strong == "Armor Class" and "AC" not in str(self.monster_data.get("armor_class")):
                ac_match = re.search(r"(\d+)", data)
                if ac_match:
                    self.monster_data["armor_class"] = int(ac_match.group(1))
            
            # Parse Hit Points
            if self.last_strong == "Hit Points":
                hp_match = re.search(r"(\d+)", data)
                dice_match = re.search(r"(\d+d\d+(?:\s*[+-]\s*\d+)?)", data)
                if hp_match:
                    self.monster_data["hit_points"] = int(hp_match.group(1))
                if dice_match:
                    self.monster_data["hit_dice"] = dice_match.group(1).replace(" ", "")
            
            # Parse Speed
            if self.last_strong == "Speed":
                self.monster_data["speed"] = data.strip()
            
            # Parse Ability Scores
            ability_pattern = r"(STR|DEX|CON|INT|WIS|CHA|CHAR)\s+(\d+)"
            for match in re.finditer(ability_pattern, data):
                ability = match.group(1)
                if ability == "CHAR":  # Normalize CHAR to CHA
                    ability = "CHA"
                score = int(match.group(2))
                self.monster_data[ability] = score
            
            # Parse Senses
            if self.last_strong == "Senses":
                self.monster_data["senses"] = data.strip().replace("Senses", "").strip()
            
            # Parse Languages
            if self.last_strong == "Languages":
                self.monster_data["languages"] = data.strip().replace("Languages", "").strip()
            
            # Parse Challenge
            if self.last_strong == "Challenge":
                challenge_match = re.search(r"(\d+(?:/\d+)?)\s+\((\d+)\s+XP\)", data)
                if challenge_match:
                    self.monster_data["challenge"] = {
                        "rating": challenge_match.group(1),
                        "xp": int(challenge_match.group(2))
                    }


def extract_traits_from_html(html: str) -> List[Dict[str, str]]:
    """Extract trait/ability information from monster HTML
    
    Looks for patterns like:
    <strong><em>Trait Name</em></strong>. Description text here.
    """
    traits = []
    
    # Pattern: <strong><em>Name</em></strong>. Description
    pattern = r'<strong><em>([^<]+)</em></strong>\.\s*([^<]+(?:<[^>]*>[^<]*)*)'
    
    for match in re.finditer(pattern, html):
        trait_name = match.group(1).strip()
        trait_desc = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        
        if trait_name and trait_desc:
            traits.append({
                'name': trait_name,
                'description': trait_desc[:200]  # Limit description length
            })
    
    return traits


def scrape_monster(monster_name: str) -> Optional[Dict[str, Any]]:
    """
    Scrape a monster from AiDeDd.
    
    Args:
        monster_name: The monster name (e.g., "badger")
    
    Returns:
        Dictionary with monster data or None if scraping fails
    """
    url = f"https://www.aidedd.org/dnd/monstres.php?vo={monster_name.lower()}"
    
    try:
        with urlopen(url, timeout=10) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
        
        parser = MonsterHTMLParser()
        parser.feed(html_content)
        
        # Extract traits and abilities from HTML
        # Look for special traits/abilities in the main content
        traits = extract_traits_from_html(html_content)
        if traits:
            parser.monster_data['traits'] = traits
        
        # Clean up the data
        result = {k: v for k, v in parser.monster_data.items() if v is not None and v != []}
        
        if result.get("name"):
            return result
        else:
            print(f"Warning: Could not extract monster data for '{monster_name}'")
            return None
            
    except Exception as e:
        print(f"Error scraping '{monster_name}': {e}")
        return None


def extract_ability_scores(data: str) -> Dict[str, int]:
    """Extract ability scores from raw text"""
    scores = {}
    pattern = r"(STR|DEX|CON|INT|WIS|CHA|CHAR)\s+(\d+)"
    
    for match in re.finditer(pattern, data):
        ability = match.group(1)
        if ability == "CHAR":
            ability = "CHA"
        scores[ability] = int(match.group(2))
    
    return scores


if __name__ == "__main__":
    # Test the scraper
    data = scrape_monster("badger")
    if data:
        print("✓ Successfully scraped badger data:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    else:
        print("✗ Failed to scrape badger data")
