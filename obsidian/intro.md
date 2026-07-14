# Introducción {.unnumbered}

## Cómo leer este libro

Los capítulos están organizados por materia. Cada uno puede leerse de forma independiente. Al final hay referencias bibliográficas.

## Convenciones

- `##` divide secciones dentro de un mismo tema
- `@exm-` son ejemplos
- `@tbl-` son tablas
- `@eq-` son ecuaciones

## Cómo escribir ecuaciones

### Ecuación básica

```
$$\text{Descripción} = \frac{a}{b}$$ {#eq-nombre}
```

### Texto largo — salto de línea

```
$$\substack{\text{Línea 1} \\ \text{Línea 2}} = \frac{a}{b}$$ {#eq-nombre}
```

### Referenciar en texto

`como se observa en la @eq-nombre` → renderiza como "Ecuación 2.1".

### Inline

- Concentración: `$[B]$`
- Unidades: `$M$`, `$s$`, `$\frac{M}{s}$`
- Símbolo griego: `$\Delta$`

### Prohibiciones

- **No usar** `\tag{N}` — no funciona en epub. Siempre `{#eq-label}`.
- **No usar** `\n` en `\text{}` — usar `\\` dentro de `\substack{}`.
