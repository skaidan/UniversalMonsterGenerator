# dynamic_loader.py
import os
import importlib.util
import random
from typing import Union


def load_classes_from_dir(directory: str) -> dict[str, type]:
    """
    Load all classes defined in .py files under a directory.
    """
    classes = {}

    for filename in os.listdir(directory):
        if not filename.endswith(".py") or filename == "__init__.py":
            continue

        module_name = os.path.splitext(filename)[0]
        path = os.path.join(directory, filename)

        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:
            print(f"Warning: skipping {filename} due to import error: {exc}")
            continue

        for attr_name in dir(module):
            obj = getattr(module, attr_name)
            if isinstance(obj, type) and obj.__module__ == module.__name__:
                classes[filename] = obj

    return classes


def create_dynamic_class(base_classes: list[type], name: str = "DynamicCreature") -> type:
    """
    Create a runtime class that inherits from base_classes.
    No custom __init__ – relies on GlobalCreatureBaseClass.dataclass.
    """
    return type(name, tuple(base_classes), {})


def combine_class_names(base1: type, base2: type) -> str:
    """Combine two class names into a single creature name."""
    return f"{base1.__name__}{base2.__name__}"


def main(
    return_json_string: bool = False,
) -> Union[dict, str]:
    """
    Build a random DynamicCreature by:
    1. Selecting two classes from bases1
    2. Extracting stats from the first selected class's DEFAULT_STATS
    3. Creating the dynamic creature with a mixed name
    4. Collecting abilities from both selected classes
    """
    DIR1 = "bases1"

    classes_dir1 = load_classes_from_dir(DIR1)

    if not classes_dir1:
        raise ValueError("Directory bases1 does not contain any classes")

    base1 = random.choice(list(classes_dir1.values()))
    base2 = random.choice(list(classes_dir1.values()))

    print(f"Base1: {base1.__name__}")
    print(f"Base2: {base2.__name__}")

    creature_name = combine_class_names(base1, base2)
    DynamicCreature = create_dynamic_class(
        [base1, base2],
        name=creature_name,
    )

    print(f"Creature name: {DynamicCreature.__name__}")
    print("MRO:")
    for cls in DynamicCreature.mro():
        print(f"  {cls.__name__}")

    # Extract stats from base1's DEFAULT_STATS
    stats = getattr(base1, "DEFAULT_STATS", None)
    if stats is None:
        raise ValueError(
            f"Base1 class {base1.__name__} must define DEFAULT_STATS class attribute"
        )

    # Combine abilities from the two selected Base1 classes
    abilities = []
    for cls in (base1, base2):
        base_stats = getattr(cls, "DEFAULT_STATS", None)
        if base_stats is None:
            raise ValueError(
                f"Base1 class {cls.__name__} must define DEFAULT_STATS class attribute"
            )
        abilities.extend(base_stats.get("abilities", []))

    # Fill defaults for optional stats if missing
    stats.setdefault("abilities", [])

    # Create creature with extracted stats from the first selected class,
    # but collect abilities from both selected classes.
    creature = DynamicCreature(
        hit_points=stats["hit_points"],
        min_level=stats["min_level"],
        level=stats["level"],
        STR=stats["STR"],
        DEX=stats["DEX"],
        CON=stats["CON"],
        INT=stats["INT"],
        WIS=stats["WIS"],
        CHAR=stats["CHAR"],
        armor_class=stats["armor_class"],
        alignment=stats["alignment"],
        legendary=stats["legendary"],
        size=stats["size"],
        type=stats["type"],
        hit_points_up=stats["hit_points_up"],
        STR_up=stats["STR_up"],
        DEX_up=stats["DEX_up"],
        CON_up=stats["CON_up"],
        INT_up=stats["INT_up"],
        WIS_up=stats["WIS_up"],
        CHAR_up=stats["CHAR_up"],
        abilities=abilities,
    )

    print("\nCreature:")
    print(creature)
    print("Abilities:", creature.abilities)

    # To JSON‑ready dict
    creature_dict = creature.to_dict()

    if return_json_string:
        import json

        return json.dumps(creature_dict, indent=2, ensure_ascii=False)

    return creature_dict


if __name__ == "__main__":
    result = main(return_json_string=True)
    print("\n=== JSON Output ===")
    print(result)


def create_creature_from_dict(
    creature_data: dict,
    level: int | None = None,
) -> dict:
    """
    Create a creature from a dictionary of creature data.
    
    Args:
        creature_data: Dictionary containing all creature attributes
        level: Optional level to override the creature's level. 
               Must be >= creature_data["min_level"]
    
    Returns:
        Dictionary representation of the created creature
    
    Raises:
        ValueError: If level < min_level or required fields are missing
        TypeError: If data types are incorrect
    """
    from creature_base import GlobalCreatureBaseClass
    
    # Create a dynamic creature class (simplified single-base inheritance)
    CreatureClass = type("LoadedCreature", (GlobalCreatureBaseClass,), {})
    
    # Override level if provided
    if level is not None:
        creature_data = {**creature_data, "level": level}
    
    # Create the creature instance from the dictionary
    creature = CreatureClass(**creature_data)
    
    return creature.to_dict()


def create_creature_from_json(
    json_string: str,
    level: int | None = None,
) -> dict:
    """
    Create a creature from a JSON string.
    
    Args:
        json_string: JSON string containing creature data
        level: Optional level to override the creature's level
    
    Returns:
        Dictionary representation of the created creature
    
    Raises:
        json.JSONDecodeError: If JSON is invalid
        ValueError: If level < min_level or required fields are missing
        TypeError: If data types are incorrect
    """
    import json
    
    creature_data = json.loads(json_string)
    return create_creature_from_dict(creature_data, level=level)


def scale_creature_level(
    creature_data: dict,
    target_level: int,
) -> dict:
    """
    Scale a creature to a target level using the _up arrays cyclically.
    
    The scaling arrays are used cyclically: if an array has length N and we need
    to scale K levels, we use array[i % N] for each scaling step i.
    
    Args:
        creature_data: Dictionary containing creature data
        target_level: Target level to scale to (must be >= min_level)
    
    Returns:
        Dictionary with scaled creature data
    
    Raises:
        ValueError: If target_level < min_level
    """
    if target_level < creature_data["min_level"]:
        raise ValueError(
            f"target_level ({target_level}) must be >= min_level ({creature_data['min_level']})"
        )
    
    # Calculate how many levels to scale
    levels_to_scale = target_level - creature_data["min_level"]
    
    if levels_to_scale == 0:
        # No scaling needed, just update level
        return {**creature_data, "level": target_level}
    
    # Get the _up arrays
    up_arrays = {
        "hit_points": creature_data["hit_points_up"],
        "min_level": creature_data["min_level_up"],
        "STR": creature_data["STR_up"],
        "DEX": creature_data["DEX_up"],
        "CON": creature_data["CON_up"],
        "INT": creature_data["INT_up"],
        "WIS": creature_data["WIS_up"],
        "CHAR": creature_data["CHAR_up"],
    }
    
    # Get array lengths (all should be the same due to validation)
    array_length = len(up_arrays["hit_points"])
    
    # Create scaled creature data
    scaled_data = creature_data.copy()
    scaled_data["level"] = target_level
    
    # Apply scaling for each level using cyclic indexing
    for level_idx in range(levels_to_scale):
        # Use modulo to cycle through the array
        array_idx = level_idx % array_length
        
        # Scale hit_points
        scaled_data["hit_points"] += up_arrays["hit_points"][array_idx]
        
        # Scale other stats
        for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHAR"]:
            scaled_data[stat] += up_arrays[stat][array_idx]
    
    return scaled_data


def create_scaled_creature_from_dict(
    creature_data: dict,
    level: int,
) -> dict:
    """
    Create a creature from dict data and scale it to the specified level.
    
    Args:
        creature_data: Dictionary containing creature data
        level: Target level for the creature
    
    Returns:
        Dictionary representation of the scaled creature
    """
    # First create the base creature
    base_creature = create_creature_from_dict(creature_data, level=creature_data["level"])
    
    # Then scale it to the target level
    scaled_creature = scale_creature_level(base_creature, level)
    
    return scaled_creature


def create_scaled_creature_from_json(
    json_string: str,
    level: int,
) -> dict:
    """
    Create a creature from JSON string and scale it to the specified level.
    
    Args:
        json_string: JSON string containing creature data
        level: Target level for the creature
    
    Returns:
        Dictionary representation of the scaled creature
    """
    import json
    
    creature_data = json.loads(json_string)
    return create_scaled_creature_from_dict(creature_data, level)
