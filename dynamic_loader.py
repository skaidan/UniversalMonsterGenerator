# dynamic_loader.py
import os
import importlib.util
import random


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
        spec.loader.exec_module(module)

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


def main(
    return_json_string: bool = False,
) -> Union[dict, str]:
    """
    Build a random DynamicCreature and return its data as JSON‑ready dict
    (or as JSON string if `return_json_string=True`).
    """
    DIR1 = "bases1"
    DIR2 = "bases2"
    DIR3 = "bases3"

    classes_dir1 = load_classes_from_dir(DIR1)
    classes_dir2 = load_classes_from_dir(DIR2)
    classes_dir3 = load_classes_from_dir(DIR3)

    if not (classes_dir1 and classes_dir2 and classes_dir3):
        raise ValueError("At least one directory does not contain any classes")

    base1 = random.choice(list(classes_dir1.values()))
    base2 = random.choice(list(classes_dir2.values()))
    base3 = random.choice(list(classes_dir3.values()))

    print(f"Base1: {base1.__name__}")
    print(f"Base2: {base2.__name__}")
    print(f"Base3: {base3.__name__}")

    DynamicCreature = create_dynamic_class(
        [base1, base2, base3],
        name="DynamicCreature",
    )

    print("MRO:")
    for cls in DynamicCreature.mro():
        print(f"  {cls.__name__}")

    creature = DynamicCreature(
        hit_points=20,
        min_level=3,
        STR=14,
        DEX=12,
        CON=16,
        INT=10,
        WIS=11,
        CHAR=8,
        armor_class=15,
        abilities=[],  # components will add their abilities
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
