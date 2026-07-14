# Guía del Agente de IA para el Proyecto Presentación

Esta guía contiene la especificación técnica, las reglas de formato y las directrices de diseño para mantener y extender el proyecto de presentación de diapositivas interactivas. Está estructurada para ser interpretada directamente por asistentes de IA y agentes de codificación autónomos (skills de IA).

---

## 1. Arquitectura y Estructura del Proyecto

El proyecto consta de siete archivos principales que deben mantenerse sincronizados:
- **`tema.md`**: El archivo de origen del contenido en formato Markdown estructurado. Define el texto, la organización de diapositivas y el coloreado de elementos.
- **`presentacion.html`**: El archivo de visualización monolítico (HTML5, CSS3, Vanilla JS). Contiene las hojas de estilo y el motor de renderizado.
- **`instrucciones.md`** (este archivo): Las directrices de formato, comportamiento de la interfaz y reglas del agente.
- **`agente_latex_html_css.md`**: La guía específica y lista de verificación para validar de forma estricta la renderización de fórmulas (LaTeX), visualización de fracciones y alineación CSS.
- **`agente_ortografia.md`**: La guía específica y lista de verificación para la revisión ortográfica, acentuación y consistencia tipográfica de `tema.md`.
- **`pdf.js`**: El script de automatización en Node.js para generar de forma automatizada la versión PDF de las diapositivas usando Puppeteer.
- **`presentacion.pdf`**: El documento final exportado en formato de diapositiva horizontal A4, optimizado para impresión y distribución.
---

## 2. Especificación de tema.md (Estructura de Contenido)

Cualquier cambio en el contenido del archivo `tema.md` debe seguir el siguiente esquema de anotaciones:

### 2.1. Direccionamiento de Diapositiva (Etiquetas `@`)
- **Bloques con Scroll (`@N`)**: La etiqueta `@N` (donde `N` es un número secuencial, ej. `@1`, `@2`, `@3`) define un nuevo bloque central. Al navegar, la presentación realiza un scroll vertical y centra este bloque en pantalla.
- **Sub-pasos Acumulativos (`@N[letra]`)**: La etiqueta `@N[letra]` (ej. `@2a`, `@2b`, `@2c`) acumula contenido secuencialmente dentro del mismo bloque `N`.
  - **Comportamiento**: No realiza scroll. El nuevo contenido aparece debajo del anterior.
  - **Actualización Inteligente In-Place y Segmentación por Bloques**: Si un párrafo o fórmula en un sub-paso es una modificación directa o repetición de un elemento ya existente (por ejemplo, para reactivarlo, mantenerlo visible o añadir nuevos resaltadores y colores), este debe ser detectado (mediante análisis de similitud textual) y modificado/actualizado *in-situ* en el mismo elemento DOM. El propósito de volver a escribir un bloque previo no es duplicarlo, sino mantenerlo visible a foco completo (opacidad 1) en el paso activo aplicando los nuevos resaltados.
    - **Segmentación por Bloques**: Si el texto de una diapositiva contiene múltiples bloques o ecuaciones separados por doble barra inclinada (`// //`), el motor los separa en bloques lógicos virtuales y los asocia a slots de manera independiente. Esto evita duplicaciones de texto en pantalla y permite que un bloque se actualice (ej. aplicando un tachado) mientras el otro bloque (ej. la ecuación química) permanece visible de fondo.
  - **Foco**: Las celdas/párrafos de sub-pasos anteriores reducen su opacidad, manteniendo opacidad plena únicamente en el sub-paso activo en ese instante (o el elemento modificado más recientemente).

### 2.2. Reglas para Tablas Progresivas
Si las diapositivas de un sub-paso (ej. de `@2a` a `@2e`) inician con tuberías de tabla Markdown (`|`):
- **Estructura**: El motor de renderizado fusionará horizontalmente las columnas de cada paso de izquierda a derecha.
- **Cabecera (`thead`)**: La primera fila de cada sub-paso define el encabezado correspondiente en la tabla unificada.
- **Cuerpo (`tbody`)**: Las filas subsecuentes definen las celdas de datos en cada columna.
- **Animaciones**:
  - Al revelarse una columna, sus celdas se desplazan suavemente `12px` desde la derecha usando la curva `cubic-bezier(0.16, 1, 0.3, 1)`.
  - Se aplica un retraso escalonado (*stagger*) de `60ms` por fila (`fila * 60ms`) para lograr un efecto de barrido en cascada de arriba a abajo.
  - La columna activa tiene opacidad `1`, mientras que las columnas reveladas anteriormente se muestran atenuadas (opacidad `0.35` en el bloque activo).

### 2.3. Formato de Color y Resaltado (Paleta Paul Tol Muted)
Para destacar texto u operaciones matemáticas, se utilizan atajos especiales de Markdown con la siguiente sintaxis:
> [!IMPORTANT]
> Se utiliza obligatoriamente el carácter de dos puntos (`:`) en lugar de barra vertical (`|`) para evitar romper el análisis de celdas en el parser de tablas Markdown.

| Sintaxis | Elemento | Color Aplicado | Estilo / Uso |
| :--- | :--- | :--- | :--- |
| `{r:texto}` | Color de Texto | `#CC6677` (Rosa/Terracota) | Elementos tipo A, primeros pasos |
| `{g:texto}` | Color de Texto | `#117733` (Verde bosque) | Elementos tipo B, intermedios |
| `{b:texto}` | Color de Texto | `#332288` (Azul índigo) | Elementos tipo C o principales |
| `{y:texto}` | Color de Texto | `#999933` (Amarillo oliva) | Totales o resultados destacados |
| `[r:texto]` | Resaltador | Fondo translúcido rosa | Fondo sutil tipo acuarela |
| `[g:texto]` | Resaltador | Fondo translúcido verde | Fondo sutil tipo acuarela |
| `[b:texto]` | Resaltador | Fondo translúcido azul | Fondo sutil tipo acuarela |
| `[y:texto]` | Resaltador | Fondo translúcido ocre | Resaltador tradicional arena (`rgba(221, 204, 119, 0.22)`) |

### 2.4. Elemento Importante Persistente (% [texto])
- **Definición**: Una línea que inicia con el carácter `%` (ej. `% {r:C₆}{g:H₁₂}{b:O₆}`) declara una anotación o dato clave persistente en la barra lateral.
- **Comportamiento**: Se extrae durante el preprocesamiento de la diapositiva y se elimina del cuerpo del texto central.
- **Ubicación en UI**: Se renderiza de forma fija arriba a la derecha (`top: calc(5.0rem + 4cm); right: calc(5.5rem + 1.5cm);`), desplazado 1.5 cm a la izquierda y 4 cm hacia abajo respecto a la posición original alineada con el subtítulo (H2).
- **Persistencia**: El elemento permanece visible en pantalla a lo largo de las siguientes diapositivas y pasos de cálculo hasta que sea sobrescrito por un nuevo elemento `%`, o sea limpiado por completo usando la palabra reservada `%fin` o `% fin` (insensible a mayúsculas/minúsculas).
- **Formato**: Admite etiquetas internas de color y resaltado (ej. `{b:texto}`, `[y:texto]`) así como expresiones matemáticas de LaTeX envueltas en `$` (ej. `{b:$C_6H_{12}O_6$}`). El motor ejecuta tanto `formatText` como `parseMath` sobre este bloque.

### 2.5. Formato de Expresiones Matemáticas y Fórmulas Químicas
- **Definición**: Las expresiones matemáticas/químicas se pueden delimitar por caracteres `$` en ambos extremos (ej. `$ expresión $`) o se detectan automáticamente si contienen `_`, `/frac`, o `*`.
- **Subíndices**: Se utiliza la sintaxis estándar de LaTeX con números normales para fórmulas en modo matemático (ej. `C_6`, `H_{12}`). El parser convierte estos a etiquetas `<sub>` de forma automática.
- **Escritura de Fórmulas Químicas**: Toda fórmula o compuesto químico (ej. `C_6H_{12}O_6`, `CO_2`) debe escribirse siempre utilizando la sintaxis de LaTeX delimitada por caracteres `$` en ambos extremos (ej. `$C_6H_{12}O_6$`, `$CO_2$`), tanto en bloques matemáticos independientes como en medio de párrafos de texto plano o preguntas.
- **Fracciones `/frac`**: Se utiliza `/frac{numerador}{denominador}` (con barra inclinada `/` en vez de contrabarra `\`).
- **Tachado y Cancelación `\sout` o `/sout`**: Se utiliza para tachar y cancelar términos en las fórmulas matemáticas (ej. `\sout{g C_6H_{12}O_6}`). El parser lo traduce a una etiqueta HTML `<span class="sout-cancel">` con las siguientes características técnicas obligatorias:
  - **Alineación**: Debe usar `display: inline-block` con `vertical-align: baseline` (en lugar de `display: inline`) para asegurar que el navegador cree una caja de formato (bounding box) estable para aplicar transformaciones CSS (`transform`) y dibujar la diagonal, manteniendo la perfecta alinementación de la línea de texto base (baseline) respecto a las variables matemáticas de la fórmula.
  - **Línea Diagonal (Vectorial)**: Se renderiza como un elemento `::after` absoluto que abarca la caja de texto. Su línea diagonal en color rojo (`var(--c-red)`) de `3.5px` de grosor relativo se define mediante un gráfico vectorial en línea (`background-image` con un SVG que dibuja una línea de `(0, 100)` a `(100, 0)` con `preserveAspectRatio="none"`). Esto evita la borrosidad y los defectos de rasterizado típicos de los degradados lineales (`linear-gradient`) al imprimir a PDF.
  - **Atenuación**: El texto cancelado se atenúa a `var(--ink-faint)` (gris claro) para restarle peso visual.
  - **Animación e Impresión**: Se conserva el efecto de trazado dinámico de izquierda a derecha usando una transformación de escala (`transform: scaleX(0) -> scaleX(1)`). En impresión/PDF, la animación debe desactivarse (`animation: none !important; transform: none !important;` en `@media print`) para evitar que la página se capture antes de terminar de dibujarse y se exporte invisible.

### 2.6. Salto de Línea (//)
- **Definición**: La secuencia de dos barras inclinadas (`//`) en cualquier parte del texto o anotaciones declares en el tema (incluyendo comentarios `%`) se interpreta como un salto de línea.
- **Comportamiento**: El motor de renderizado debe reemplazar todas las ocurrencias del token `//` con la etiqueta `<br>` en el HTML final.

---

## 3. Especificación Técnica de presentacion.html

Cualquier agente de IA que trabaje sobre las hojas de estilo o los scripts en `presentacion.html` debe respetar estrictamente las siguientes constantes físicas y comportamientos:

### 3.1. Estilo Libro Electrónico (Paperwhite / E-Reader)
- **Fondo**: Blanco puro (`#FFFFFF`) con una textura de papel sutil aplicada a través de un SVG de ruido fractal en línea como `background-image` en CSS.
- **Tinta**: Escala de grises neutros y negro para simular tinta electrónica:
    - Activo completo: `#000000`
    - Contenido intermedio: `#444444`
    - Atenuado/Pasado: `#888888`
- **Tipografía (Híbrida Moderna)**: La tipografía base para el cuerpo de texto (`.sub-step`) y las celdas del cuerpo de las tablas (`.paragraph-block tbody tr td`) es `Helvetica` (Sans-Serif) para garantizar máxima legibilidad digital en datos y lectura fluida. La tipografía `EB Garamond` (Serif) se utiliza exclusivamente para firmas, encabezados e interfaces de usuario (`#header-h1`, `#header-h2`, `#author-tag`, `#progress-label`), combinando elegancia literaria y claridad técnica.
- **Tamaño de Letra Homogéneo**: Tanto los párrafos de texto (`.sub-step`) como las celdas del cuerpo de las tablas (`.paragraph-block tbody tr td`) deben usar un tamaño de `1.38rem` para garantizar la uniformidad visual del libro electrónico.
- **Ancho Útil y Centrado Horizontal**: `min(900px, 88vw)` con un padding de `3rem` en el track. Todo el contenido principal (bloques, párrafos, fórmulas y tablas) debe estar centrado tanto vertical como horizontalmente (`text-align: center` y alineación flex centrada).
- **Máscara de Bordes**: Un degradado lineal superior e inferior (`#mask`) en el viewport difumina el scroll del texto en los extremos para un efecto orgánico.
- **Firma del Autor**: Texto vertical ("Camilo Tayac") fijo en la posición inferior izquierda (`left: 5.5rem; bottom: 12vh`), rotado a -90 grados con tipografía `EB Garamond` en mayúsculas.
- **Anotación Marginal (%)**: El contenedor `#header-info` (clase `.info-text`) se posiciona fijo en `top: calc(5.0rem + 4cm); right: calc(5.5rem + 1.5cm);` con tipografía `Helvetica`, tamaño `1.38rem` (homogéneo con el texto principal), alineado a la derecha y opacidad `0.80` (cuando está visible), animándose de forma suavizada (`400ms`). Se oculta en dispositivos móviles.

### 3.2. Centrado Vertical Físico (JS Math)
El bloque activo debe posicionarse en el centro exacto de la pantalla.
- El contenedor principal `#track` se mantiene fijo arriba (`position: fixed; top: 0; left: 50%`).
- El scroll vertical del track se calcula en tiempo real en JS mediante la fórmula:
  $$translateY = Y_{centro\_pantalla} - (Y_{bloque\_activo} + \frac{Height_{bloque\_activo}}{2})$$
  Donde $Y_{bloque\_activo}$ es el `offsetTop` del bloque y $Y_{centro\_pantalla}$ es `window.innerHeight / 2`.

### 3.3. Transición Visual de Foco (Desenfoque y Escala)
Los bloques inactivos no modifican su tamaño de fuente (`font-size`) para evitar el rediseño del flujo de texto, sino que se transforman usando `transform: scale()`, filtros de desenfoque (`filter: blur`) y cambios de opacidad:
- **Bloque Activo**: `scale(1)` — Opacidad `1`
- **Bloque Anterior Inmediato (`past-1`)**: `scale(0.82)` — Desenfoque `blur(0.3px)` — Opacidad `0.3`
- **Segundo Bloque Anterior (`past-2`)**: `scale(0.70)` — Desenfoque `blur(0.6px)` — Opacidad `0.15`
- **Bloques Anteriores Lejanos (`past-far`)**: `scale(0.60)` — Desenfoque `blur(1px)` — Opacidad `0.05`
- **Bloques Siguiente Inmediato y Futuro (`next-1` / `future`)**: `scale(0.82)` / `scale(0.70)` — Opacidad `0` (Completamente invisibles con `pointer-events: none` para evitar spoilers del siguiente paso).
- **Constante de Tiempo**: Todas las transiciones de scroll y foco visual deben durar exactamente **900ms** utilizando la curva `cubic-bezier(0.25, 0.46, 0.45, 0.94)`.

### 3.4. Cabeceras Dinámicas (H1 y H2)
Los encabezados `#` (H1) y `##` (H2) son leídos por el script y removidos del cuerpo del texto del bloque:
- **H1**: Se posiciona de forma fija arriba a la izquierda (`top: 2.2rem; left: 5.5rem`).
- **H2**: Se posiciona de forma fija arriba a la derecha (`top: 2.2rem; right: 5.5rem`).
- **Estilo**: EB Garamond, tamaño `0.95rem`, espaciado entre letras `0.22em`, mayúsculas, opacidad `0.85`.
- **Transición**: Animación de fundido (*fade-in / fade-out*) de `400ms` al cambiar el encabezado activo.

### 3.5. Barra de Progreso
- Se ubica en la parte inferior central (`#bottom-ui`).
- Muestra una barra horizontal de color neutro y una etiqueta de texto con el porcentaje calculado de forma precisa según el número de sub-pasos completados sobre el total general.

### 3.6. Expresiones Matemáticas y Fracciones
- **Renderizado de Fracciones (`.fraction`)**:
  - Las fracciones se muestran en vertical. El numerador se divide del denominador mediante un borde inferior (`border-bottom: 1.5px solid #000000`).
  - Si una fracción está vacía o contiene solo espacios en sus llaves (ej. `/frac{    }{    }`), el motor de renderizado le asigna la clase `.empty-fraction` y le aplica un ancho mínimo de `6rem` (`96px`), forzando que se visualice una línea horizontal de división larga y visible que indique que la fracción está pendiente de completarse.

---

## 4. Lógica de Navegación por Teclado y Táctil

El motor de navegación debe responder a los siguientes eventos:
- **Avanzar**:
  - Tecla de flecha derecha (`ArrowRight`), flecha abajo (`ArrowDown`) o barra espaciadora (`Space`).
  - Clic o toque táctil en el lado derecho de la pantalla (zona igual o mayor al 35% del ancho de la ventana, `x >= 35vw`).
- **Retroceder**:
  - Tecla de flecha izquierda (`ArrowLeft`) o flecha arriba (`ArrowUp`).
  - Clic o toque táctil en el lado izquierdo de la pantalla (zona menor al 35% del ancho de la ventana, `x < 35vw`).
- **Exclusiones**: Se debe ignorar la navegación táctil si el usuario está realizando una selección de texto activa o si hace clic en un enlace (`a`) o botón (`button`).
- **Control de Paso**:
  - Si el grupo activo tiene sub-pasos no revelados, avanzar revela el siguiente sub-paso.
  - Si todos los sub-pasos del grupo activo están visibles, avanzar realiza el scroll al siguiente bloque.
  - El comportamiento inverso se aplica al retroceder.

---

## 5. Criterios de Diseño UX y Carga Cognitiva

El diseño visual de la presentación equilibra la **carga cognitiva extraña** (ruido visual) y la **carga cognitiva relevante** (contexto) mediante la visibilidad periférica de diapositivas adyacentes:

### 5.1. Relación de Señal/Ruido (Visual Peeking)
- **Foco (Señal)**: El bloque central activo tiene opacidad `1`, escala `scale(1)` y texto en negro nítido (`#000000`).
- **Contexto (Ruido controlado)**: Los bloques superiores (`past-1`, `past-2`) actúan como anclas visuales atenuadas y difuminadas. Esto ayuda al lector a retener el hilo conductor (de dónde viene) y reduce la carga cognitiva.
  - Para evitar que compitan con la señal principal y sobre todo **evitar spoilers de los siguientes pasos**, los bloques futuros (`next-1` y `future`) se configuran con opacidad `0` y `pointer-events: none`, siendo completamente invisibles hasta que se activan.

### 5.2. Adaptabilidad a Dispositivos y Orientaciones

1. **Prevención de Spoilers en Fórmulas (Configuración por Defecto)**:
   - Para que el usuario no visualice respuestas o desarrollos antes de tiempo, los bloques siguientes (`next-1` y `future`) deben mantenerse siempre con opacidad `0` y `pointer-events: none`.
2. **Contexto de Bloques Pasados**:
   - Mantener las diapositivas pasadas visibles pero atenuadas (`past-1` a `0.3`, `past-2` a `0.15`) para proveer un ancla del camino recorrido.
3. **Optimización Móvil (Celulares y Tablets)**:
   - **Celulares en Modo Vertical (Portrait, `< 768px`)**: Debe mostrarse una pantalla fija de advertencia (`#rotation-warning`) con animación instructiva que indique al usuario girar su dispositivo a horizontal. El contenido principal debe permanecer oculto para evitar spoilers y cortes.
   - **Celulares en Modo Horizontal (Landscape, `max-height: 480px`)**:
     - El espacio vertical es crítico. Se debe priorizar el bloque activo, ocultando los bloques pasados lejanos y futuros para evitar desbordes.
     - Se reduce el tamaño de letra de `.sub-step` y de las celdas de las tablas a `1.15rem` y la altura de línea a `1.5`.
     - Se disminuye el padding vertical de `.paragraph-block` a `0.6rem` y el del track.
     - Se reposicionan las cabeceras fijas (`top: 0.8rem`, tamaño `0.8rem`).
     - Se ocultan la firma vertical (`#author-tag`) y la anotación marginal (`.info-text`) para liberar espacio vertical.
   - **Tabletas y Dispositivos Medianos (Portrait y Landscape)**:
     - El contenido se centra horizontal y verticalmente de forma óptima.
     - En orientación vertical (`portrait`, e.g. `< 1024px`), se oculta la anotación marginal (`.info-text`) para que no compita ni se solape con el texto de los bloques. En orientación horizontal se muestra de forma normal.

---

## 6. Exportación y Generación de PDF

El proyecto incluye soporte nativo y automatizado para generar un documento PDF de la presentación con orientación horizontal (Landscape) en tamaño A4. Este PDF se compila paso a paso para simular la progresión de la presentación en pantalla.

### 6.1. Hojas de Estilo para Impresión (`@media print`)
El motor de visualización en `presentacion.html` contiene reglas CSS específicas para garantizar un formato idéntico al modo pantalla y evitar desbordamientos de página:
- **Márgenes de Página**: Se define la directiva `@page { size: A4 landscape; margin: 0; }` para que la textura de fondo cubra toda la página (Full Bleed).
- **Ocultamiento de UI y Elementos Fijos**: Oculta la barra de progreso, máscaras de degradado, atajos de navegación y elementos de posición fija globales (`#mask`, `#bottom-ui`, `#author-tag`, `.header-text`, `.info-text`) mediante `display: none !important`.
- **Estructura del Contenedor**: El contenedor `#track` debe cambiar su visualización a `display: block !important` (reemplazando el comportamiento flex de pantalla) para asegurar que el navegador respete de forma estricta los saltos de página.
- **Control de Dimensiones y Salto de Página**: Cada bloque de diapositiva (`.paragraph-block`) tiene:
  - `page-break-after: always` y `break-after: page` para iniciar cada paso en una página nueva.
  - `height: 209mm !important` y `max-height: 209mm !important` con `overflow: hidden !important` para ajustarse perfectamente al alto físico A4 (210mm) con tolerancia a sub-píxeles, evitando páginas extra en blanco.
  - `position: relative !important` para servir de ancla a sus cabeceras e informaciones locales.
- **Opacidades de Progresión**: Para replicar el foco de pantalla, se aplican reglas específicas de opacidad en impresión:
  - `.paragraph-block .sub-step.revealed` y `.td-wrapper.revealed` se atenúan a `opacity: 0.35 !important`.
  - El sub-paso activo `.sub-step.revealed.latest` y `.td-wrapper.revealed.latest` se muestran con `opacity: 1 !important`.
- **Preservación de Resaltados (`.hl-`)**:
  - Para asegurar que los resaltados de color se impriman en el PDF, las clases `.hl-red`, `.hl-green`, `.hl-blue`, y `.hl-yellow` deben tener `display: inline-block; vertical-align: baseline;` y las directivas `-webkit-print-color-adjust: exact` y `print-color-adjust: exact;`.
  - En la sección `@media print`, los fondos translúcidos (`rgba()`) de los resaltados se reemplazan por **colores hexadecimales sólidos y opacos** (ej. `#FADBD8` para rojo, `#FCF3CF` para amarillo) para evitar que el renderizado de impresión del navegador los elimine o los lave a color blanco.
- **Componentes Locales de Impresión**: Cada bloque contiene copias absolutas locales de la interfaz de usuario para evitar problemas de duplicación de elementos fijos:
  - `.print-header`: Cabeceras (H1 y H2) alineadas absolutamente a `top: 2.2rem; left: 5.5rem; right: 5.5rem`.
  - `.print-info`: El comentario lateral de datos de anotación (`%`) posicionado absolutamente arriba a la derecha.
  - `.print-author`: La firma del autor vertical posicionada a `left: 5.5rem; bottom: 12vh` y rotada a `-90deg` para replicar exactamente la firma en pantalla.

### 6.2. Preparación Dinámica de Impresión (`prepareForPrint()`)
Cuando la presentación se prepara para imprimir (llamada por Puppeteer):
1. **Reconstrucción del DOM**: Se gather-an todos los sub-pasos individuales de la secuencia (12 pasos en total).
2. Se limpia el track (`track.innerHTML = ''`) y se crea una diapositiva (`.paragraph-block`) por cada paso.
3. Cada diapositiva de paso se renderiza en la versión exacta de su progreso (revelando elementos y aplicando la clase `.latest` al elemento de ese paso), clonando el comportamiento en pantalla de forma estática en 12 páginas.

### 6.3. Generación Automatizada vía Node.js (`pdf.js`)
Para compilar y exportar la presentación directamente a `presentacion.pdf` mediante línea de comandos:
1. **Requisito**: Tener instalado `puppeteer` en el directorio (`npm install puppeteer`).
2. **Ejecución**: Ejecutar el comando `node pdf.js`.
3. **Mecanismo**: El script levanta un navegador sin interfaz (headless), abre `presentacion.html`, espera a que la estructura cargue, evalúa `window.prepareForPrint()` en el contexto del navegador para reconstruir las 12 páginas, configura un viewport horizontal de 1920x1080 y exporta el archivo PDF con márgenes de `0px`.

### 6.4. Sincronización Obligatoria del PDF
Cada vez que un agente de IA realice cambios en el contenido de `tema.md` o en la estructura, estilos o scripts de `presentacion.html`, es **obligatorio** que ejecute `node pdf.js` para compilar y actualizar `presentacion.pdf`. Esto garantiza que los formatos HTML y PDF estén siempre sincronizados y reflejen los mismos contenidos.


