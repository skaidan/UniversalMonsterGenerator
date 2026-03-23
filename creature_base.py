# creature_base.py
import re
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple


def normalize_abilities(abilities: List[str]) -> List[str]:
    """
    Normalize abilities:
      - "Flying", "Flying"          → "Flying 2"
      - "Flying 2", "Flying"        → "Flying 3"
      - "Flying 2", "Flying 3"      → "Flying 5"
      - "Flying 10", "Flying 3"     → "Flying 13"
    Then sort by base name (case‑insensitive) and then by count descending.
    """
    counts: Dict[str, int] = {}

    for a in abilities:
        if not isinstance(a, str):
            continue
        match = re.match(r"^(.+?)(?:\s+(\d+))?$", a.strip())
        if not match:
            base_name = a.strip()
            n = 1
        else:
            base_name = match.group(1).strip()
            n_str = match.group(2)
            n = int(n_str) if n_str is not None else 1

        counts[base_name] = counts.get(base_name, 0) + n

    # Sort by name (case‑insensitive), then by count descending
    items: List[Tuple[str, int]] = sorted(
        counts.items(),
        key=lambda x: (x[0].lower(), -x[1]),
    )

    result: List[str] = []
    for name, total in items:
        if total == 1:
            result.append(name)
        else:
            result.append(f"{name} {total}")

    return result


@dataclass
class GlobalCreatureBaseClass:
    hit_points: int
    min_level: int
    level: int
    STR: int
    DEX: int
    CON: int
    INT: int
    WIS: int
    CHAR: int
    armor_class: int
    alignment: str
    legendary: bool
    size: str
    type: str
    hit_points_up: List[int]
    STR_up: List[int]
    DEX_up: List[int]
    CON_up: List[int]
    INT_up: List[int]
    WIS_up: List[int]
    CHAR_up: List[int]
    abilities: List[str]

    def __post_init__(self) -> None:
        # Validate numeric stats
        for name in [
            "hit_points",
            "min_level",
            "STR",
            "DEX",
            "CON",
            "INT",
            "WIS",
            "CHAR",
            "armor_class",
        ]:
            value = getattr(self, name)
            if not isinstance(value, int):
                raise TypeError(f"{name} must be int, got {type(value).__name__}")
            if value <= 0:
                raise ValueError(f"{name} must be positive, got {value}")

        # Validate level (must be >= min_level)
        if not isinstance(self.level, int):
            raise TypeError(f"level must be int, got {type(self.level).__name__}")
        if self.level < self.min_level:
            raise ValueError(
                f"level ({self.level}) must be >= min_level ({self.min_level})"
            )

        # Validate string fields
        for name in ["alignment", "size", "type"]:
            value = getattr(self, name)
            if not isinstance(value, str):
                raise TypeError(f"{name} must be str, got {type(value).__name__}")
            if not value:
                raise ValueError(f"{name} cannot be empty")

        # Validate legendary
        if not isinstance(self.legendary, bool):
            raise TypeError(f"legendary must be bool, got {type(self.legendary).__name__}")

        # Validate _up fields (arrays with specific constraints)
        up_field_names = [
            "hit_points_up",
            "STR_up",
            "DEX_up",
            "CON_up",
            "INT_up",
            "WIS_up",
            "CHAR_up",
        ]
        
        # Get reference length from hit_points_up
        hit_points_up = getattr(self, "hit_points_up")
        if not isinstance(hit_points_up, list):
            raise TypeError("hit_points_up must be list")
        
        reference_length = len(hit_points_up)
        
        # Validate all _up arrays have same length and correct values
        for name in up_field_names:
            value = getattr(self, name)
            if not isinstance(value, list):
                raise TypeError(f"{name} must be list, got {type(value).__name__}")
            
            # Check length
            if len(value) != reference_length:
                raise ValueError(f"{name} must have same length as hit_points_up ({reference_length}), got {len(value)}")
            
            # Check each value
            for i, v in enumerate(value):
                if not isinstance(v, int):
                    raise TypeError(f"{name}[{i}] must be int, got {type(v).__name__}")
                
                if name == "hit_points_up":
                    # hit_points_up: 1 to 10% of initial hit_points
                    max_hp_up = max(1, int(self.hit_points * 0.1))
                    if not (1 <= v <= max_hp_up):
                        raise ValueError(
                            f"hit_points_up[{i}] must be between 1 and {max_hp_up} (10% of {self.hit_points}), got {v}"
                        )
                else:
                    # Other _up arrays: 0 to 2
                    if not (0 <= v <= 2):
                        raise ValueError(f"{name}[{i}] must be between 0 and 2, got {v}")
        
        # Validate column sums for non-hit_points arrays = 2
        for i in range(reference_length):
            column_sum = sum(
                getattr(self, name)[i] 
                for name in up_field_names 
                if name != "hit_points_up"
            )
            if column_sum != 2:
                raise ValueError(
                    f"Sum of column {i} in _up arrays (excluding hit_points_up) must be 2, got {column_sum}"
                )

        if not isinstance(self.abilities, list):
            raise TypeError("abilities must be a list of strings")
        for i, a in enumerate(self.abilities):
            if not isinstance(a, str):
                raise TypeError(
                    f"abilities[{i}] must be string, got {type(a).__name__}"
                )

        # Normalize and deduplicate abilities
        self.abilities = normalize_abilities(self.abilities)

    def to_dict(self) -> dict:
        """
        Convert to JSON‑serializable dict.
        """
        return asdict(self)

    def to_json_str(self, **kwargs) -> str:
        """
        Serialize to JSON string.
        """
        import json

        return json.dumps(self.to_dict(), **kwargs)

    def to_json_file(self, path: str, **kwargs) -> None:
        """
        Serialize to a JSON file.
        """
        import json

        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, **kwargs)
