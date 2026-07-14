# Guía de Verificación del Agente: LaTeX, HTML y CSS (Universal)

Esta guía contiene las especificaciones de diseño, reglas del parser y criterios de aceptación para verificar que el renderizador matemático en `presentacion.html` compile y visualice de manera óptima las expresiones de **Química, Física y Matemáticas**.

---

## 1. Especificaciones de Expresiones por Dominio

El motor matemático de la presentación es universal y debe validar la correcta interpretación de las siguientes nomenclaturas:

### 1.1. Química (Fórmulas y Estequiometría)
* **Sintaxis de Subíndices**:
  - Dígitos Simples sin llaves: `C_6` -> `C<sub>6</sub>`
  - Dígitos Múltiples con llaves: `H_{12}` -> `H<sub>12</sub>`
  - Soporte de Subíndices Unicode heredados: `C_₆` -> `C<sub>6</sub>`
* **Estilo Visual**: Todas las fórmulas químicas deben representarse obligatoriamente en modo matemático LaTeX (`$ ... $`), mostrándose siempre en fuente Serif e itálica (`EB Garamond`) para mantener la consistencia en toda la presentación.

### 1.2. Física (Constantes, Unidades y Potencias)
* **Sintaxis de Superíndices**:
  - Exponentes simples: `c^2` -> `c<sup>2</sup>`
  - Exponentes agrupados o negativos: `10^{-3}` -> `10<sup>-3</sup>`
* **Operador de Producto**:
  - El asterisco `*` debe compilar a un signo de multiplicación elegante: ` &times; ` (ej. `m * c^2` -> `m &times; c<sup>2</sup>`).
* **Espaciado de Unidades**: Se deben preservar los espacios literales entre magnitudes y unidades (ej. `350 g` o `1.94 mol`).

### 1.3. Matemáticas (Ecuaciones Complejas)
* **Fracciones**:
  - Soporte dual para barra inclinada `/frac{num}{den}` y estándar LaTeX con contrabarra `\frac{num}{den}`.
  - Las fracciones con contenido en blanco o espacios (ej. `\frac{    }{    }`) deben activar la clase `.empty-fraction` para forzar un ancho mínimo de `6rem` (`96px`) y dibujar una línea de división clara.
* **Radicales / Raíz Cuadrada**:
  - `\sqrt{x}` o `/sqrt{x}` deben compilar al símbolo radical `&radic;` con una línea superior CSS: `&radic;<span style="border-top: 1.5px solid #000; padding-top: 1px;">x</span>`.
* **Operadores y Letras Griegas**:
  - Más-menos: `\pm` o `/pm` -> ` &plusmn; `
  - Punto central: `\cdot` o `/cdot` -> ` &middot; `
  - Multiplicación explícita: `\times` o `/times` -> ` &times; `
  - Delta minúscula: `\delta` o `/delta` -> `&delta;`
  - Delta mayúscula: `\Delta` o `/Delta` -> `&Delta;`

---

## 2. Plan de Pruebas Manuales (Casos de Control)

Para validar el renderizado, inserta temporalmente las siguientes expresiones en `tema.md` y verifica su aspecto en el navegador:

### Caso A: Estequiometría y Conversión (Química)
* **Entrada**: `$ [r:350 g C_6H_{12}O_6] * \frac{1 mol C_6H_{12}O_6}{180 g C_6H_{12}O_6} $`
* **Resultado Esperado**:
  - Resaltador rosa sutil de fondo sobre todo el primer término.
  - Subíndices químicos (`6`, `12`, `6`) del mismo tamaño y correctamente alineados en la parte inferior de las letras.
  - Línea horizontal de la fracción abarcando exactamente el ancho de los datos.
  - Asterisco reemplazado por la cruz de multiplicar (`×`).
  - Sin símbolos `$` visibles.

### Caso B: Ecuación de Energía de Einstein (Física)
* **Entrada**: `$ E = m * c^2 $`
* **Resultado Esperado**:
  - El exponente `2` posicionado como superíndice arriba del nivel de la `c`.
  - Espacio uniforme a los lados del igual (`=`) y del signo de multiplicación (`×`).

### Caso C: Fórmula Cuadrática General (Matemáticas)
* **Entrada**: `$ x = \frac{-b \pm \sqrt{b^2 - 4 * a * c}}{2 * a} $`
* **Resultado Esperado**:
  - Una fracción grande bien estructurada.
  - El símbolo de raíz cuadrada con una línea superior que cubra exactamente el término `b² - 4 × a × c`.
  - El exponente `2` elevado sobre la variable `b`.
  - El operador de más-menos (`±`) renderizado correctamente.
  - Signo de multiplicación (`×`) en los productos.

---

## 3. Checklist de Verificación para el Agente (Código y Estilos)

### HTML & CSS ([presentacion.html](file:///Users/tayac/Documents/GitHub/Presentacion/2/presentacion.html))
- [ ] `.math-expression` usa la tipografía `'EB Garamond', serif` con estilo `italic`.
- [ ] `.math-expression sub` tiene `font-size: 0.65em; vertical-align: sub;` y no dobla subíndices unicode si se mezclan.
- [ ] `.math-expression sup` tiene `font-size: 0.65em; vertical-align: super;`.
- [ ] `.fraction.empty-fraction` aplica un `min-width: 6rem;`.
- [ ] `.numerator` aplica un `border-bottom: 1.5px solid #000000; width: 100%;` para la barra fraccionaria.
- [ ] `.sout-cancel` tiene `position: relative; display: inline-block; vertical-align: baseline; color: var(--ink-faint);` y dibuja una línea diagonal de cancelación mediante un pseudo-elemento `::after` con una línea SVG vectorial en el fondo (evitando gradientes lineales pixelados en impresión).
- [ ] Las clases de resaltado `.hl-red`, `.hl-green`, `.hl-blue`, y `.hl-yellow` tienen `display: inline-block; vertical-align: baseline;` con las directivas `-webkit-print-color-adjust: exact` y `print-color-adjust: exact` para asegurar que el navegador pinte sus fondos de color.
- [ ] En la sección `@media print` del archivo CSS, los resaltadores cambian a **colores de fondo Hexadecimales sólidos y opacos** (`#FADBD8`, `#D4EFDF`, `#D6EAF8`, `#FCF3CF`) para evitar desvanecimientos.
- [ ] En la sección `@media print`, la animación de `.sout-cancel::after` se deshabilita (`animation: none !important; transform: none !important;`) para garantizar el renderizado inmediato de la diagonal.

### Motor JS ([presentacion.html](file:///Users/tayac/Documents/GitHub/Presentacion/3/presentacion.html))
- [ ] La función `parseMath` ejecuta `text.trim().replace(/\r/g, '')` antes de validar la coincidencia de los delimitadores `$`.
- [ ] Las expresiones de sub/superíndices y radicales soportan llaves anidadas (ej. `_{12}` en `$C_6H_{12}O_6$`) mediante patrones robustos `([^{}]*(?:\{[^{}]*\}[^{}]*)*)`.
- [ ] La expresión de `sout` tiene el prefijo de barra opcional `/[\/\\]?sout/` para tolerar escapes consumidos por compiladores de JavaScript.
- [ ] El motor de slots realiza una segmentación de las diapositivas en bloques virtuales independientes dividiéndolas por los saltos de párrafo dobles (`// //`), evitando duplicaciones de texto y logrando una transición inteligente in-place.

### Exportación a PDF ([pdf.js](file:///Users/tayac/Documents/GitHub/Presentacion/3/pdf.js))
- [ ] El script inicia Puppeteer con la bandera `--allow-file-access-from-files` para evitar fallos de CORS al hacer `fetch('tema.md')` localmente bajo el protocolo `file://`.
- [ ] Se ejecuta `node pdf.js` tras modificar el contenido o estilos para actualizar `presentacion.pdf`.
- [ ] Se verifica que `presentacion.pdf` se genera sin errores en la terminal y que refleja fielmente la presentación en HTML.

