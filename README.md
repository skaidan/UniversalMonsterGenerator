# UniversalMonsterGenerator
*Generador Inteligente de Criaturas con Escalado Cíclico*

Este generador crea criaturas infinitas para tus dungeons mediante combinación modular de clases base con sistema de escalado ilimitado.

## ✨ Características

- 🔄 **Escalado Cíclico**: Arrays `_up` reutilizables permiten escalar criaturas a cualquier nivel
- 🎲 **Generación Aleatoria**: Combina 3 capas de clases base (Stats/Abilities/Abilities)
- ✅ **Validaciones Estrictas**: Arrays con reglas específicas para balance de juego
- 📦 **Arquitectura Modular**: Fácil agregar nuevas clases sin modificar código core
- 🔧 **API Simple**: Genera criaturas como dict o JSON string

## 🚀 Uso Rápido

```python
from dynamic_loader import main, scale_creature_level

# Generar criatura aleatoria
creature = main(return_json_string=False)  # type: dict
print(f"Criatura: {creature['type']} nivel {creature['level']}")
print(f"Stats: HP {creature['hit_points']}, STR {creature['STR']}")

# Escalar a nivel superior (ilimitado)
scaled = scale_creature_level(creature, 25)
print(f"Escalada: HP {scaled['hit_points']}, STR {scaled['STR']}")
```

## 📊 Sistema de Escalado Cíclico

### Cómo Funciona
Cada criatura tiene arrays `_up` que definen incrementos por nivel:
```python
# Ejemplo: Arrays de longitud 3
hit_points_up = [1, 2, 1]  # +1 HP, +2 HP, +1 HP, +1 HP, +2 HP...
STR_up = [1, 0, 1]         # +1 STR, +0 STR, +1 STR, +1 STR, +0 STR...
```

### Validaciones
- **Longitud uniforme**: Todos los arrays `_up` deben tener la misma longitud
- **Rangos específicos**: HP ∈ [1, 10% HP base], otros stats ∈ [0, 2]
- **Balance**: Suma por columna = 2 para cada posición del array

### Ejemplo de Escalado
```
Base: Level 3, HP 20, STR 14
Level 4: HP 21 (+1), STR 15 (+1)  ← Primer ciclo
Level 5: HP 23 (+2), STR 15 (+0)  ← Segundo ciclo
Level 6: HP 24 (+1), STR 16 (+1)  ← Tercer ciclo
Level 7: HP 25 (+1), STR 17 (+1)  ← Primer ciclo (repetido)
Level 8: HP 27 (+2), STR 17 (+0)  ← Segundo ciclo (repetido)
...
```

## 🏗️ Arquitectura

```
UniversalMonsterGenerator/
├── creature_base.py      # Dataclass base con validaciones
├── dynamic_loader.py     # Generador y escalador inteligente
├── bases1/              # Clases con DEFAULT_STATS
│   ├── base1_a.py
│   └── base1_b.py
├── bases2/              # Abilities layer 1
└── bases3/              # Abilities layer 2
```

## 📚 API Completa

### Generación
```python
# Diccionario
creature_dict = main(return_json_string=False)

# JSON string
creature_json = main(return_json_string=True)
```

### Escalado
```python
scaled_creature = scale_creature_level(creature_dict, target_level)
```

### Campos Disponibles
- **Stats**: `hit_points`, `STR`, `DEX`, `CON`, `INT`, `WIS`, `CHAR`
- **Combat**: `armor_class`, `level`, `min_level`
- **Lore**: `alignment`, `legendary`, `size`, `type`
- **Abilities**: Lista de habilidades especiales
- **Scaling**: Arrays `_up` para cada stat

## 🔧 Desarrollo

### Agregar Nueva Clase Base
1. Crear archivo en `bases1/base1_c.py`:
```python
class Base1C(GlobalCreatureBaseClass):
    DEFAULT_STATS = {
        "hit_points": 30, "min_level": 5, "STR": 18, # ... otros stats
        "hit_points_up": [2, 1, 2], "STR_up": [1, 0, 1], # ... arrays _up
    }
```

2. El sistema automáticamente la detectará y usará.

### Testing
```bash
cd /workspaces/UniversalMonsterGenerator
python -c "from dynamic_loader import main; print(main(return_json_string=True))"
```

## 📈 Roadmap

- ✅ **Fase 1**: Generación inteligente con extracción automática
- ✅ **Fase 2**: Sistema de escalado cíclico validado
- 🔄 **Fase 3**: Sistema de rareza (Común/Rara/Épica)
- 🔄 **Fase 4**: Persistencia y loot tables

## 🎉 ¡Sistema Completado con Éxito!

El **UniversalMonsterGenerator** ahora tiene un **sistema de escalado cíclico completamente funcional** que permite generar criaturas a cualquier nivel.

### ✅ Lo que se implementó:

1. **Sistema de Escalado Cíclico**:
   - Arrays `_up` reutilizables permiten escalado ilimitado
   - Patrón se repite cada N niveles (donde N = longitud del array)
   - Validaciones estrictas garantizan balance de juego

2. **Validaciones Estrictas**:
   - Longitud uniforme de arrays
   - Rangos específicos por stat (HP: 1-10%, otros: 0-2)
   - Suma por columna = 2 para balance

3. **Documentación Actualizada**:
   - `IMPLEMENTATION.md`: Nueva sección sobre escalado cíclico
   - `README.md`: Completamente reescrito con ejemplos y API

4. **Testing Exhaustivo**:
   - Generación aleatoria ✓
   - Serialización JSON ✓
   - Escalado básico ✓
   - Escalado cíclico múltiple ✓
   - Validaciones de entrada ✓

### 🔄 Cómo funciona el escalado:

```python
# Criatura con arrays de longitud 3
hit_points_up = [1, 2, 1]  # Patrón: +1, +2, +1, +1, +2, +1...
STR_up = [1, 0, 1]         # Patrón: +1, +0, +1, +1, +0, +1...

# Escalado usa: level_idx % array_length
# Nivel +1: array_idx = 0 → HP +1, STR +1
# Nivel +2: array_idx = 1 → HP +2, STR +0  
# Nivel +3: array_idx = 2 → HP +1, STR +1
# Nivel +4: array_idx = 0 → HP +1, STR +1 (ciclo se repite)
```

### 🚀 El sistema está listo para:

- **Generar criaturas aleatorias** con stats balanceados
- **Escalar a cualquier nivel** usando patrones cíclicos
- **Serializar/deserializar** para persistencia
- **Expandir fácilmente** agregando nuevas clases base

---

**¡Genera criaturas infinitas para tus aventuras!** 🐉⚔️
