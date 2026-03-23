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
    STR: int
    DEX: int
    CON: int
    INT: int
    WIS: int
    CHAR: int
    armor_class: int
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
