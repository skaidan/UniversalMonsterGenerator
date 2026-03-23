# Universal Monster Generator - Roadmap

## Visión General
Un generador dinámico de monstruos que combina múltiples bases de características para crear criaturas únicas con habilidades emergentes.

## Arquitectura
- **Bases1**: Proporciona estadísticas base (HP, atributos, AC)
- **Bases2 & Bases3**: Contribuyen habilidades especiales
- **dynamic_loader**: Orquesta la combinación inteligente de clases

## Próximas Iteraciones

### v1.0 - MVP Actual
- ✅ Sistema de herencia múltiple con MRO
- ✅ Normalización y deduplicación de abilities
- ✅ Serialización a JSON

### v1.1 - Extracción Inteligente de Atributos
- 🔄 Las clases Base1 definen valores por defecto para stats
- 🔄 dynamic_loader extrae automáticamente stats de Base1
- 🔄 dynamic_loader agrega abilities de Base1, Base2, Base3

### v1.2 - Generación Procedural Avanzada
- Modificadores por nivel
- Escalado de habilidades
- Balance de mecánicas

### v2.0 - Sistema de Rareza
- Criaturas comunes, raras, épicas
- Loot y drops asociados
- Puntos de poder

## Hitos Críticos
| Fase | Objetivo | Status |
|------|----------|--------|
| Definición de arquitectura | Sistema de herencia limpio | ✅ Completado |
| Base de datos de componentes | Clases base con valores | 🔄 En progreso |
| Generador inteligente | Extracción automática de stats | 🔄 En progreso |
