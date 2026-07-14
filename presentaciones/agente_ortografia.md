# Guía de Verificación del Agente: Ortografía y Consistencia Tipográfica (tema.md)

Esta guía contiene la lista de verificación y las reglas ortográficas que deben validarse de manera estricta en el contenido de [tema.md](file:///Users/tayac/Documents/GitHub/Presentacion/2/tema.md) y en su literal sincronizado en el HTML.

---

## 1. Reglas Ortográficas y Léxicas

Cualquier revisión del contenido debe contrastarse contra las siguientes reglas ortográficas del español:

### 1.1. Acentuación y Tildes
* **Interrogaciones**: Las preguntas que abren con `¿` deben llevar tilde diacrítica en sus pronombres/adverbios interrogativos:
  - `¿Cuántos...?` (Correcto) vs `¿Cuantos...?` (Incorrecto)
  - `¿Cómo...?` (Correcto) vs `¿Como...?` (Incorrecto)
  - `¿Cuál...?` (Correcto) vs `¿Cual...?` (Incorrecto)
* **Terminología Científica**:
  - **Conversión**: Siempre lleva tilde en la 'o' (`conversión`).
  - **Mol / Moles**: La palabra `mol` es aguda terminada en consonante distinta de 'n' o 's', no lleva tilde. Su plural `moles` es grave terminada en 's', tampoco lleva tilde.
  - **Molar / Molecular**: Palabras agudas terminadas en 'r', no llevan tilde.

### 1.2. Capitalización (Mayúsculas)
* **Títulos y Subtítulos (`#` y `##`)**:
  - Deben escribirse con mayúscula inicial en la primera palabra del título.
  - Si el título incluye dos puntos, la palabra inmediatamente posterior a los dos puntos debe iniciar con mayúscula (estilo de títulos del proyecto):
    * `## Paso 2: Factor de conversión` (Correcto)
    * `## Paso 2: factor de conversión` (Incorrecto)
* **Elementos Químicos**: Los símbolos químicos deben seguir estrictamente la nomenclatura de la IUPAC (primera letra en mayúscula, segunda en minúscula si la hay):
  - `C` (Carbono), `H` (Hidrógeno), `O` (Oxígeno), `Na` (Sodio).
  - Evitar fórmulas en minúsculas en LaTeX (ej. `$c_6$` es incorrecto; debe ser `$C_6$`).

### 1.3. Abreviaturas y Unidades de Medida (Sistema Internacional)
* **Gramos**: La abreviatura oficial y única de gramo es **`g`** (en minúscula, sin punto).
  - `350 g` (Correcto)
  - `350 gr`, `350 grs.`, `350 g.` (Incorrectos)
* **Moles**: La unidad de cantidad de sustancia es **`mol`** (tanto para singular como plural en la notación de unidades).
  - `1.94 mol` o `1 mol` (Correcto en notación de unidad física)
  - *Nota*: En lenguaje natural se puede escribir "moles" (`¿Cuántos moles hay...`), pero como unidad al lado de un número va `mol` (`1.94 mol`).
* **Masa Molar**: Se abrevia como **`g/mol`**.
* **Espaciado**: Debe dejarse obligatoriamente un espacio duro o espacio normal entre el número y la unidad:
  - `350 g` (Correcto) vs `350g` (Incorrecto)

---

## 2. Consistencia en Fórmulas (Uso de LaTeX)

Todas las fórmulas y compuestos químicos deben escribirse en formato LaTeX utilizando el delimitador de bloque matemático `$`:
* **Regla General**: Se prohíbe el uso de subíndices Unicode (como `₆`, `₁₂`) en los nombres de compuestos químicos. Todos los compuestos deben ir envueltos en `$` para que el motor matemático aplique el formato y espaciado correspondiente:
  - `¿Cuántos moles hay en $350 g$ de $C_6H_{12}O_6$?` (Correcto)
  - `¿Cuántos moles hay en $350 g$ de C₆H₁₂O₆?` (Incorrecto)
* **Subíndices LaTeX**: Usa únicamente subíndices de LaTeX (`_` y `_{}`) dentro de los bloques `$`:
  - `$ C_6H_{12}O_6 $` (Correcto)
  - `$ C_₆H_{₁₂}O_₆ $` (Incorrecto)

---

## 3. Checklist de Verificación de Ortografía para tema.md

Antes de finalizar cualquier edición de contenido, el agente debe verificar:
- [ ] ¿Todas las preguntas interrogativas (`¿...?`) tienen tildes en sus partículas de pregunta?
- [ ] ¿Se utiliza `conversión` con tilde?
- [ ] ¿Se utiliza `g` y `mol` (y no `gr`, `grs` o `moles` como unidad)?
- [ ] ¿Hay un espacio entre las cifras y sus unidades correspondientes (ej. `350 g`)?
- [ ] ¿La primera letra tras los dos puntos en los títulos de paso (`## Paso X: ...`) inicia con mayúscula?
- [ ] ¿Todas las fórmulas y compuestos químicos de tema.md están escritos en sintaxis LaTeX y envueltos en `$` (evitando subíndices Unicode)?
- [ ] ¿Se sincronizaron exactamente estos cambios en el literal `temaMarkdown` de `presentacion.html`?
