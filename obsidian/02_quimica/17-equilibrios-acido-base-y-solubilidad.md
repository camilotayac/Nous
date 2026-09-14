# Equilibrios ácido-base y de solubilidad: aplicaciones

## Introducción

Las herramientas cuantitativas del capítulo anterior, las constantes Ka y Kb y las escalas de pH y pOH, encuentran aquí su aplicación más rica en tres territorios de la química acuosa [@brown2012, cap. 17]. Las disoluciones amortiguadoras mantienen el pH casi inmóvil frente a la adición de ácidos o bases, las valoraciones convierten la neutralización en un método de medida y los equilibrios de solubilidad explican desde la caries dental hasta la separación de iones en el laboratorio [@chang2022, cap. 16]. Un denominador común recorre estos problemas: el principio de Le Châtelier aplicado a equilibrios gobernados por constantes [@pauling1988, sec. 14-6, 14-7].

La utilidad práctica de estos equilibrios es difícil de exagerar: la sangre humana depende de sistemas amortiguadores para permanecer cerca de pH 7.4, el diagnóstico digestivo emplea el sulfato de bario insoluble, y la identificación de desconocidos iónicos reposa sobre la precipitación selectiva [@chang2022, sec. 16.2, 16.5, 16.8; @brown2012, sec. 17.2, 17.7; @pauling1988, sec. 14-7]. El orden de exposición sigue la lógica del problema: primero el efecto del ion común, que gobierna tampones y solubilidad, después la valoración y sus indicadores, y finalmente el producto de solubilidad con sus factores y aplicaciones analíticas [@brown2012, cap. 17].

## El efecto del ion común

Una disolución que contiene dos solutos con un ion en común se comporta de manera distinta a la suma de sus partes: la presencia del ion compartido suprime la ionización del ácido o de la base débil, y el resultado es un desplazamiento predecible del equilibrio [@chang2022, sec. 16.1; @brown2012, sec. 17.1].

Si se disuelven simultáneamente ácido acético y acetato de sodio, ambos aportan iones acetato, y el exceso de estos iones desplaza el equilibrio de ionización del ácido hacia la izquierda, disminuyendo la concentración de iones hidrógeno [@chang2022, sec. 16.1]. El [**efecto del ion común**]{#sec-efecto-ion-comun} es, por tanto, un caso especial del principio de Le Châtelier, y desempeña un papel central en el pH de las disoluciones y en la solubilidad de las sales poco solubles [@chang2022, sec. 16.1; @brown2012, sec. 17.1].

La magnitud del desplazamiento se obtiene con la constante del ácido débil, cuyo valor no cambia por la presencia de la sal [@chang2022, sec. 16.1]. En una disolución 0.20 M de ácido acético, con Ka = 1.8 × 10⁻⁵, la ionización produce [H⁺] = 1.9 × 10⁻³ M y un pH de 2.72 [@chang2022, sec. 16.1].

Al añadir acetato de sodio hasta 0.30 M, el ion común reduce la concentración de hidrógeno a 1.2 × 10⁻⁵ M y eleva el pH a 4.92, casi dos unidades más alto [@chang2022, sec. 16.1]. La misma lógica vale para una base débil: el amoniaco 0.20 M con cloruro de amonio 0.30 M resulta menos básico que el amoniaco solo, porque el ion amonio común suprime la aceptación de protones [@chang2022, sec. 16.1].

Cuando las concentraciones del ácido débil y de su sal son razonablemente altas, superiores a 0.01 M, puede despreciarse tanto la ionización del ácido como la hidrólisis de la sal [@chang2022, sec. 16.1]. Esta aproximación permite usar las concentraciones iniciales directamente en la expresión de Ka, y conduce a una forma logarítmica especialmente cómoda [@chang2022, sec. 16.1]. La manipulación algebraica de la constante, tomando logaritmos negativos en ambos miembros, produce la ecuación que domina el cálculo de los tampones [@brown2012, sec. 17.1].

$$pH = pK_a + \log\frac{[\mathrm{A^-}]}{[\mathrm{HA}]},$$ {#eq-henderson-hasselbalch}

La expresión (ec. @eq-henderson-hasselbalch) relaciona el pH con el pKa del ácido débil, definido como el logaritmo negativo de su constante, y con el cociente entre las concentraciones de la base conjugada A⁻ y del ácido HA [@brown2012, sec. 17.2; @chang2022, sec. 16.1]. La variable [A⁻] representa la concentración molar del ion acetato o de cualquier base conjugada, [HA] la del ácido sin ionizar, y el logaritmo en base diez del cociente añade o resta fracciones de unidad al pKa [@brown2012, sec. 17.2]. Cuando ambas concentraciones se igualan, el logaritmo se anula y el pH coincide exactamente con el pKa, hecho que permite calibrar la escala con un solo parámetro [@brown2012, sec. 17.2].

La ecuación (ec. @eq-henderson-hasselbalch), conocida como [**ecuación de Henderson-Hasselbalch**]{#sec-henderson-hasselbalch}, es válida con independencia de la procedencia de la base conjugada, ya provenga del ácido solo o la suministren el ácido y su sal [@chang2022, sec. 16.1]. Los biólogos y bioquímicos que trabajan con tampones la emplean de forma rutinaria porque evita plantear tablas de equilibrio, y porque su forma logarítmica hace evidente la relación entre el pH y la proporción de las especies [@brown2012, sec. 17.2]. En los problemas de ion común suelen darse las concentraciones iniciales, y la validez de la aproximación se verifica comprobando que el grado de ionización permanece despreciable [@chang2022, sec. 16.1].

## Disoluciones amortiguadoras (tampones)

Las [**disoluciones amortiguadoras**]{#sec-soluciones-amortiguadoras}, también llamadas tampones o soluciones buffer, son mezclas de un ácido débil y su base conjugada, o de una base débil y su ácido conjugado, que resisten el cambio de pH al añadir cantidades moderadas de ácidos o bases fuertes [@brown2012, sec. 17.2; @chang2022, sec. 16.2; @pauling1988, sec. 14-7].

La resistencia no es mágica: el componente ácido consume los iones hidróxido añadidos y el componente básico consume los iones hidrógeno, de modo que la proporción entre ambas especies cambia apenas [@brown2012, sec. 17.2; @chang2022, sec. 16.2]. Una gota de ácido concentrado en un litro de agua pura multiplica la concentración de iones hidrógeno por 5000, mientras que en un tampón fosfato ese mismo aumento no llega al uno por ciento [@pauling1988, sec. 14-7].

La sangre ilustra la importancia biológica de los tampones, pues su pH normal, cercano a 7.4, solo cambia lentamente cuando se añade ácido o base [@pauling1988, sec. 14-7; @brown2012, sec. 17.2]. Entre las sustancias amortiguadoras del organismo figuran las proteínas del suero, con grupos ácidos y básicos capaces de combinarse con lo añadido, y el par carbónico-bicarbonato cuya concentración regula la respiración [@pauling1988, sec. 14-7; @brown2012, sec. 17.2]. En contraste, el jugo gástrico mantiene un pH cercano a 1.5, y el lavado de los riñones y los pulmones ajusta el sistema según las necesidades del cuerpo [@chang2022, sec. 16.2].

El cálculo del pH de un tampón es directo con la ecuación (ec. @eq-henderson-hasselbalch): un tampón 0.12 M en ácido benzoico y 0.20 M en benzoato de sodio, con pKa del ácido igual a 4.20, produce un pH de 4.42 [@brown2012, sec. 17.2]. El resultado puede obtenerse también con la tabla de equilibrio convencional, y ambas rutas coinciden porque la única diferencia es la forma de presentar los mismos términos algebraicos [@brown2012, sec. 17.2]. La preparación inversa, calcular la cantidad de sal necesaria para lograr un pH deseado, se resuelve despejando la concentración del conjugado en la misma expresión [@brown2012, sec. 17.2].

Pauling ilustra la neutralidad del punto medio con el par acético-acetato: cuando las concentraciones del ácido y de su sal son iguales, el pH coincide con el pKa del ácido, 4.7 para el acético [@pauling1988, sec. 14-7]. Variar la proporción desplaza el pH: una mezcla 1:5 de ácido y sal da pH 5.4, y una mezcla 5:1 da pH 4.0, de modo que eligiendo la proporción puede fijarse cualquier pH deseado en ese vecindario [@pauling1988, sec. 14-7]. El tampón fosfato, preparado con KH₂PO₄ y Na₂HPO₄·2H₂O, sirve para la región neutra con pH entre 5.3 y 8.0, y otros pares cubren rangos desde 1 hasta 13 [@pauling1988, sec. 14-7].

## Capacidad amortiguadora y rango de pH

Dos características distinguen a los tampones útiles: la [**capacidad amortiguadora**]{#sec-capacidad-amortiguadora}, cantidad de ácido o base que pueden neutralizar antes de que el pH cambie de forma apreciable, y el [**rango de pH**]{#sec-rango-ph} en el que actúan eficazmente; juntas definen la ventana de uso de cada tampón [@brown2012, sec. 17.2; @chang2022, sec. 16.2].

La capacidad depende de la cantidad de ácido y de base con que se preparó el tampón: dos disoluciones 1 M y 0.1 M en acetato tienen el mismo pH, pero la primera neutraliza diez veces más ácido o base antes de moverse [@brown2012, sec. 17.2]. La dilución por diez de un tampón reduce en el mismo factor la cantidad de ácido o base que puede absorber sin salirse del margen deseado [@pauling1988, sec. 14-7].

El rango de acción eficaz se centra en el pKa del ácido: el tampón resiste mejor cuando las concentraciones del ácido y de su base conjugada son semejantes, y su actuación se deteriora cuando un componente supera diez veces al otro, lo que delimita el margen práctico de trabajo [@brown2012, sec. 17.2].

Como el logaritmo de diez vale uno, los tampones tienen un margen útil de pH = pKa ± 1, de modo que la elección de un par amortiguador comienza por buscar un ácido cuyo pKa esté cerca del pH deseado [@brown2012, sec. 17.2]. Para un pH de 7.0 conviene, por ejemplo, el ácido hipocloroso, con pKa 7.5, y no el nitroso, cuyo pKa es de 3.35 [@brown2012, sec. 17.2].

La respuesta cuantitativa de un tampón a la adición de un ácido o una base fuerte se resuelve en dos pasos [@brown2012, sec. 17.2]. Primero se realiza un cálculo estequiométrico: el ácido fuerte reacciona por completo con la base conjugada del tampón, y la base fuerte con el ácido débil, siempre que no se rebase la capacidad [@brown2012, sec. 17.2]. Después se introduce la nueva composición en la ecuación (ec. @eq-henderson-hasselbalch), obteniendo el pH con las cantidades ya ajustadas [@brown2012, sec. 17.2].

Esta estrategia revela la magnitud de la protección: un tampón de 0.300 mol de ácido acético y 0.300 mol de acetato en un litro, con pH 4.74, pasa a 4.80 al añadir 0.020 mol de hidróxido de sodio, mientras que la misma cantidad de base eleva el pH del agua pura desde 7 hasta 12.30 [@brown2012, sec. 17.2]. La diferencia se entiende recordando que el agua no tiene reserva alguna de ácido débil que consuma el hidróxido [@brown2012, sec. 17.2]. El mismo razonamiento vale para la adición de un ácido fuerte, que el tampón convierte en una pequeña variación de la proporción [@brown2012, sec. 17.2].

## Valoraciones ácido-base {#sec-valoraciones}

Una [**valoración ácido-base**]{#sec-valoraciones-acido-base} determina la concentración de un ácido o de una base haciendo reaccionar la disolución problema con una disolución de concentración conocida, añadida con una bureta hasta completar la neutralización [@chang2022, sec. 16.3; @brown2012, sec. 17.3]. La relación estequiométrica entre el volumen gastado y la concentración del titulante permite calcular los moles de analito, y de ahí su molaridad [@chang2022, sec. 16.3]. La reacción entre un ácido fuerte y una base fuerte es esencialmente completa: los iones hidrógeno y los iones hidróxido se neutralizan entre sí formando agua [@chang2022, sec. 16.3].

El progreso de la valoración se representa con la [**curva de valoración**]{#sec-curva-valoracion}, gráfica del pH frente al volumen de disolución añadida, cuya forma depende de las fuerzas relativas de las especies [@brown2012, sec. 17.3]. En la valoración de un ácido fuerte con una base fuerte el pH inicial es bajo, crece lentamente, y salta bruscamente en las inmediaciones del [**punto de equivalencia**]{#sec-punto-equivalencia}, el momento en que el número de moles de base añadida es exactamente el estequiométricamente equivalente al ácido presente [@brown2012, sec. 17.3; @chang2022, sec. 16.3]. Para un par fuerte-fuerte, el pH en el punto de equivalencia es 7, porque la sal formada no se hidroliza [@brown2012, sec. 17.3].

Cuando el ácido es débil, la curva cambia de aspecto: el pH inicial es más alto que el de un ácido fuerte de la misma concentración, el salto cerca del punto de equivalencia es menor, y el pH en ese punto supera 7, pues el anión de la sal formada es una base débil que se hidroliza [@brown2012, sec. 17.3]. La valoración del ácido acético 0.100 M con hidróxido de sodio 0.100 M alcanza el punto de equivalencia en un pH de 8.72, por ejemplo [@brown2012, sec. 17.3].

Cuanto más débil es el ácido, más pronunciadas se vuelven estas diferencias, hasta el punto de que resulta prácticamente imposible localizar el punto de equivalencia cuando el pKa es 10 o mayor, porque el cambio de pH es demasiado pequeño y gradual [@brown2012, sec. 17.3].

La simetría se completa con la valoración de una base débil con un ácido fuerte, cuyo punto de equivalencia cae por debajo de 7 porque el ion amonio u otro ácido conjugado libera protones [@brown2012, sec. 17.3]. La titulación del amoniaco 0.100 M con ácido clorhídrico 0.100 M termina en pH 5.28, valor que exige un indicador que cambie de color en esa zona ácida [@brown2012, sec. 17.3]. En todos los casos, el pH de cada etapa se calcula combinando primero la estequiometría de la neutralización y después el equilibrio de las especies que quedan en disolución [@brown2012, sec. 17.3].

Los ácidos polipróticos y las bases polibásicas, cuando sus etapas de neutralización están suficientemente separadas, producen curvas de valoración con varios puntos de equivalencia [@brown2012, sec. 17.3]. El ácido carbónico, por ejemplo, muestra dos saltos de pH, correspondientes a la neutralización sucesiva de sus dos protones [@brown2012, sec. 17.3]. La curva de valoración del ácido fosfórico con una base fuerte, que Pauling emplea para explicar los tampones, exhibe igualmente dos puntos de inflexión netos [@pauling1988, sec. 14-7].

## Indicadores ácido-base

Un **indicador ácido-base** es un ácido orgánico débil cuya forma sin ionizar, HIn, tiene un color distinto al de su base conjugada, In⁻, de modo que el color de la disolución revela el pH [@chang2022, sec. 16.4; @brown2012, sec. 17.3]. El equilibrio HIn ⇌ H⁺ + In⁻ se desplaza con el pH: en medio ácido predomina la forma sin ionizar y en medio básico la ionizada [@chang2022, sec. 16.4].

El [**punto final**]{#sec-punto-final} es el instante en que el indicador cambia de color, y para que la valoración sea exacta debe coincidir con el punto de equivalencia, lo que exige elegir un indicador cuyo cambio de color ocurra en el salto brusco de la curva [@chang2022, sec. 16.4; @brown2012, sec. 17.3].

El criterio de elección cuantitativo es sencillo: el pKa del indicador debe aproximarse al pH del punto de equivalencia de la valoración [@pauling1988, sec. 14-6; @chang2022, sec. 16.4; @brown2012, sec. 17.3]. Para un ácido fuerte frente a una base fuerte, cuyo punto de equivalencia está en pH 7, casi cualquier indicador con pKa entre 4 y 10 produce un error menor del 0.2%, porque la curva es tan vertical que diferentes indicadores cambian a volúmenes casi idénticos [@pauling1988, sec. 14-6]. La fenolftaleína, con pKa de 9, es la elección clásica para un ácido débil como el acético, cuyo punto de equivalencia se sitúa en pH 8.87 por la hidrólisis del acetato [@pauling1988, sec. 14-6].

| Indicador | Rango o pKa | Valoración típica |
| :--- | :--- | :--- |
| Naranja de metilo | pKa 3.8 | Base débil con ácido fuerte [@pauling1988, sec. 14-6] |
| Rojo de metilo | 4.2 a 6.0 | Base débil con ácido fuerte [@brown2012, sec. 17.3] |
| Tornasol, azul de bromotimol | pKa ~ 7 | Ácido fuerte con base fuerte [@pauling1988, sec. 14-6] |
| Fenolftaleína | 8.3 a 10.0 | Ácido débil con base fuerte [@brown2012, sec. 17.3] |
| Timolftaleína | pKa 10 | Ácido fuerte con base fuerte [@pauling1988, sec. 14-6] |

La elección incorrecta produce errores sistemáticos: valorar ácido acético 0.100 M con hidróxido de sodio 0.100 M empleando rojo de metilo daría un cambio de color en pH de 4.2 a 6.0, mucho antes del punto de equivalencia de 8.72 [@brown2012, sec. 17.3]. La fenolftaleína, en cambio, cambia entre 8.3 y 10.0, justo en la zona de salto abrupto del pH [@brown2012, sec. 17.3]. Para la valoración inversa, amoniaco con ácido clorhídrico, el punto de equivalencia de 5.28 convierte al rojo de metilo en la elección natural, y a la fenolftaleína en una elección desafortunada [@brown2012, sec. 17.3].

## Ácidos polipróticos: etapas sucesivas y su valoración

El capítulo anterior introdujo los **ácidos polipróticos** y la regla de que el pH de sus disoluciones puede estimarse con la primera constante, pero el tratamiento completo de las especies exige considerar cada etapa por separado [@chang2022, sec. 15.8; @brown2012, sec. 16.6]. El ácido carbónico se ioniza en dos pasos, el primero con constante Ka1 y el segundo con Ka2, y el ion que es base conjugada en la primera etapa actúa como ácido en la segunda [@chang2022, sec. 15.8]. El ácido fosfórico, con tres hidrógenos ionizables, presenta tres constantes sucesivas que disminuyen marcadamente [@chang2022, sec. 15.8].

La jerarquía de las constantes simplifica los cálculos: cuando Ka1 es mucho mayor que Ka2, la concentración de iones hidrógeno proviene casi por completo de la primera ionización, y la concentración de la especie producida en la segunda etapa resulta numéricamente igual a Ka2 [@chang2022, sec. 15.8; @brown2012, sec. 16.6].

Para el ácido oxálico 0.10 M, cuya primera constante es 6.5 × 10⁻², la ecuación cuadrática completa da [H⁺] = 0.054 M, y la concentración del ion oxalato, C₂O₄²⁻, coincide con Ka2, 6.1 × 10⁻⁵ M [@chang2022, sec. 15.8]. La aproximación de una sola etapa fallaría aquí porque el 54% del ácido se ioniza, excediendo con mucho la regla del 5% [@chang2022, sec. 15.8].

En una disolución de ácido fosfórico, las constantes decrecientes 7.5 × 10⁻³, 6.2 × 10⁻⁸ y 4.8 × 10⁻¹³ implican que la especie no ionizada es la más abundante, y solo el propio ácido y los iones H⁺ y H₂PO₄⁻ presentan concentración apreciable [@chang2022, sec. 15.8; @brown2012, sec. 16.6]. Para el ácido carbónico en disolución saturada de dióxido de carbono a 0.1 atmósferas, 0.0037 M [@brown2012, sec. 16.6], la segunda etapa apenas contribuye al pH, y el ion carbonato queda fijado por Ka2, 5.6 × 10⁻¹¹ M [@brown2012, sec. 16.6]. Estos cálculos escalonados preparan el terreno para interpretar las curvas de valoración con múltiples puntos de equivalencia [@brown2012, sec. 17.3].

## El producto de solubilidad (Kps)

Los equilibrios de solubilidad abordan una pregunta que las reglas cualitativas de preferencia no pueden responder: cuánto de un compuesto iónico poco soluble realmente se disuelve [@chang2022, sec. 16.5]. Una disolución saturada de cloruro de plata en contacto con el sólido constituye un equilibrio heterogéneo, y la actividad del sólido puro se toma como uno, de modo que la constante de equilibrio del proceso AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq) se reduce al producto de las concentraciones iónicas [@chang2022, sec. 16.5]. Esta constante recibe el nombre de [**producto de solubilidad**]{#sec-producto-solubilidad}, Kps, y su expresión general eleva cada concentración al coeficiente estequiométrico [@chang2022, sec. 16.5; @brown2012, sec. 17.4; @pauling1988, sec. 13-5].

$$K_{ps} = [\mathrm{M^{y+}}]^x [\mathrm{X^{x-}}]^y,$$ {#eq-kps}

La ecuación (ec. @eq-kps) resume el producto de solubilidad para la sal general AxBy que se disocia en x cationes M^{y+} e y aniones X^{x-} [@chang2022, sec. 16.5; @brown2012, sec. 17.4; @pauling1988, sec. 13-5]. Cada concentración molar se eleva al número de iones de esa especie que produce una unidad fórmula, y el valor resultante, característico de cada sal a 25 °C, indica la solubilidad: cuanto menor es Kps, menos soluble es el compuesto [@chang2022, sec. 16.5]. Las comparaciones directas entre Kps solo son honestas para sales de estequiometría semejante, como AgCl y ZnS, o CaF₂ y Fe(OH)₂ [@chang2022, sec. 16.5].

La **solubilidad molar** expresa la concentración de la disolución saturada en moles por litro, y la solubilidad en gramos por litro, y ambas se convierten entre sí con la masa molar [@chang2022, sec. 16.5]. Del Kps del bromuro de plata, 7.7 × 10⁻¹³, se obtiene una solubilidad molar de 8.8 × 10⁻⁷ M, pues cada unidad disuelta produce un ion de cada especie [@chang2022, sec. 16.5]. En la dirección contraria, la solubilidad del sulfato de calcio, 0.67 g/L, conduce a un Kps de 2.4 × 10⁻⁵ después de convertir a moles [@chang2022, sec. 16.5].

La utilidad práctica de estos equilibrios es inmediata: el esmalte dental se compone de hidroxiapatita, Ca₅(PO₄)₃OH, cuya disolución en medio ácido produce la caries, mientras que el sulfato de bario insoluble y opaco a los rayos X permite diagnosticar el tubo digestivo [@chang2022, sec. 16.5].

La preparación industrial del carbonato de sodio y la formación de estalactitas y estalagmitas de carbonato de calcio son procesos de precipitación regidos por los mismos productos [@chang2022, sec. 16.5]. Pauling añade una observación pionera: el yodo se disuelve mucho mejor en disoluciones de yoduro porque forma el ion triyoduro, y el perclorato de potasio es menos soluble en presencia de su propio ion [@pauling1988, sec. 13-5].

## El producto iónico y la predicción de precipitación

Las concentraciones de una disolución que no está en equilibrio se comparan con el producto de solubilidad mediante el [**producto iónico**]{#sec-producto-ionico}, Q, que tiene la misma forma que Kps pero usa las concentraciones iniciales [@chang2022, sec. 16.5; @brown2012, sec. 17.6]. Para la mezcla de una disolución de iones plata con otra de iones cloruro, la expresión es Q = [Ag⁺]₀[Cl⁻]₀, donde el subíndice cero recuerda que no son concentraciones de equilibrio [@chang2022, sec. 16.5].

Si Q es menor que Kps la disolución no está saturada y no precipita nada; si es igual, está exactamente saturada y existe equilibrio; y si es mayor, está sobresaturada y se forma precipitado hasta que el producto iónico vuelve a igualar a Kps [@chang2022, sec. 16.5; @brown2012, sec. 17.6].

$$Q = [\mathrm{Ag^+}]_0 [\mathrm{Cl^-}]_0,$$ {#eq-q-kps}

El criterio (ec. @eq-q-kps) sintetiza la predicción de precipitación en una sola comparación: cuando el producto iónico excede al producto de solubilidad, la precipitación ocurre [@chang2022, sec. 16.5]. La condición de saturación se alcanza cuando Q iguala a Kps, y ninguna cantidad de sólido adicional puede disolverse [@chang2022, sec. 16.5]. Este umbral cuantitativo convierte la precipitación en una herramienta de separación, pues los iones pueden aislarse eligiendo un reactivo que forme con ellos sales de solubilidades muy distintas [@brown2012, sec. 17.6; @chang2022, sec. 16.6].

En una disolución que contiene iones plata y plomo, por ejemplo, la adición lenta de iones cloruro precipita primero el cloruro de plata, cuyo Kps es de 1.8 × 10⁻¹⁰, mientras que el cloruro de plomo, con Kps mucho mayor, permanece en disolución [@brown2012, sec. 17.6]. La concentración de cloruro necesaria para iniciar cada precipitación se calcula despejando en la expresión del producto: la sal menos soluble comienza antes y agota el ion común [@brown2012, sec. 17.6]. Así, la plata puede separarse cuantitativamente del plomo controlando la adición del reactivo precipitante [@brown2012, sec. 17.6].

Conviene registrar una discrepancia entre las tablas de las fuentes: Chang emplea un Kps de 1.6 × 10⁻¹⁰ para el cloruro de plata [@chang2022, sec. 16.5], mientras que Brown cita 1.8 × 10⁻¹⁰ [@brown2012, sec. 17.6]. La diferencia afecta solo a la segunda cifra significativa y no altera el orden de precipitación, pues el cloruro de plata es mucho menos soluble que el de plomo con cualquiera de las dos cifras [@brown2012, sec. 17.6]. Por coherencia con cada procedimiento, el capítulo emplea el valor de Brown en el ejemplo de separación plata-plomo y el de Chang en los cálculos de precipitación fraccionada [@brown2012, sec. 17.6; @chang2022, sec. 16.6].

## Factores que alteran la solubilidad: ion común, pH e iones complejos

El efecto del ion común, introducido para los ácidos, actúa también sobre la solubilidad de las sales: la adición de un ion compartido desplaza el equilibrio de disolución hacia el sólido y reduce la cantidad disuelta [@chang2022, sec. 16.7; @brown2012, sec. 17.5; @pauling1988, sec. 13-5]. El cloruro de plata, cuya solubilidad en agua pura es de 1.9 × 10⁻³ g/L, se disuelve solo 3.6 × 10⁻⁶ g/L en una disolución 6.5 × 10⁻³ M de nitrato de plata, porque el ion plata común deprime la disolución [@chang2022, sec. 16.7]. El valor de Kps permanece inalterado en ambos casos, pues es una constante de equilibrio, mientras que la solubilidad sí depende del entorno [@chang2022, sec. 16.7].

El pH del medio altera la solubilidad de las sales cuyos aniones son bases conjugadas de ácidos débiles [@chang2022, sec. 16.7; @brown2012, sec. 17.5]. El hidróxido de magnesio, con Kps de 1.2 × 10⁻¹¹, tiene una disolución saturada de pH 10.45, y su solubilidad aumenta cuando el pH es menor porque los iones hidrógeno consumen el anión hidróxido [@chang2022, sec. 16.7]. De modo análogo, el sulfuro de cobre(II) se disuelve mejor en medio ácido porque el ion sulfuro captura protones, mientras que la solubilidad del cloruro de plata no cambia con el pH, pues el ion cloruro es la base conjugada de un ácido fuerte [@chang2022, sec. 16.7].

Los [**iones complejos**]{#sec-iones-complejos} forman una tercera vía para aumentar la solubilidad: un catión metálico se combina con bases de Lewis y retira el ion metálico de la disolución, desplazando el equilibrio hacia la disolución del sólido [@chang2022, sec. 16.7; @brown2012, sec. 17.5]. La tendencia a formar estos complejos se mide con la [**constante de formación**]{#sec-constante-formacion}, Kf, que cuantifica la estabilidad del ion complejo frente a su disociación [@chang2022, sec. 16.7; @brown2012, sec. 17.5]. La formación del complejo tetraminocobre(II), por ejemplo, explica que el hidróxido de cobre precipite primero al añadir amoniaco y se redisuelva después en exceso del mismo reactivo [@chang2022, sec. 16.7].

$$K_f = \frac{[\mathrm{Cu(NH_3)_4^{2+}}]}{[\mathrm{Cu^{2+}}][\mathrm{NH_3}]^4},$$ {#eq-kf}

La expresión (ec. @eq-kf) define la constante de formación para el complejo Cu(NH₃)₄²⁺: en el numerador figura la concentración del ion complejo y en el denominador el producto de la concentración del catión libre por la del ligando elevada a cuatro, su coeficiente estequiométrico [@chang2022, sec. 16.7].

El valor muy grande de Kf indica que el complejo es muy estable y que la concentración de iones cobre libres en el equilibrio es extremadamente pequeña [@chang2022, sec. 16.7]. Un caso cuantitativamente impresionante es el cloruro de plata: su solubilidad molar en agua pura es 1.3 × 10⁻⁵ M, pero en amoniaco 1.0 M alcanza 0.045 M gracias a la formación de Ag(NH₃)₂⁺, una multiplicación por más de tres mil [@chang2022, sec. 16.7].

Ciertos hidróxidos, llamados [**amfóteros**]{#sec-amfoteros}, reaccionan tanto con ácidos como con bases, y su solubilidad crece en ambos extremos del pH [@chang2022, sec. 16.7; @brown2012, sec. 17.5]. El hidróxido de aluminio, el de plomo(II), el de cromo(III), el de zinc y el de cadmio pertenecen a esta clase [@chang2022, sec. 16.7]. El aumento de solubilidad del Al(OH)₃ en medio básico se debe a la formación del ion complejo Al(OH)₄⁻, donde el hidróxido actúa como ácido de Lewis y el ion hidróxido como base de Lewis [@chang2022, sec. 16.7; @brown2012, sec. 17.5].

## Precipitación fraccionada y análisis cualitativo

La [**precipitación fraccionada**]{#sec-precipitacion} separa iones de solubilidades distintas precipitándolos uno tras otro con la adición controlada de un reactivo común [@chang2022, sec. 16.6; @brown2012, sec. 17.6]. En una disolución que contiene iones cloruro y bromuro, ambos 0.020 M, la adición lenta de nitrato de plata inicia primero la precipitación del bromuro de plata, cuyo Kps de 7.7 × 10⁻¹³ exige superar apenas [Ag⁺] = 3.9 × 10⁻¹¹ M, mientras que el cloruro de plata, con Kps de 1.6 × 10⁻¹⁰, necesita [Ag⁺] = 8.0 × 10⁻⁹ M [@chang2022, sec. 16.6]. Entre esos dos límites, el ion bromuro precipita casi por completo mientras el cloruro permanece en disolución [@chang2022, sec. 16.6].

La eficacia de la separación es cuantificable: cuando la concentración de plata alcanza el umbral del cloruro, quedan solo 0.48% de los iones bromuro originales, es decir, 99.52% han precipitado como bromuro de plata [@chang2022, sec. 16.6]. El procedimiento se generaliza a más de dos iones siempre que sus sales presenten productos de solubilidad suficientemente distintos [@chang2022, sec. 16.6; @brown2012, sec. 17.6]. Así, los haluros de plata precipitan en el orden yoduro, bromuro, cloruro, de menor a mayor Kps [@chang2022, sec. 16.6].

El [**análisis cualitativo**]{#sec-analisis-cualitativo} aprovecha estas diferencias para identificar los iones presentes en una muestra desconocida, mediante un esquema sistemático de precipitación y separación de cationes en cinco grupos [@chang2022, sec. 16.8; @brown2012, sec. 17.7]. El primer grupo precipita con ácido clorhídrico diluido, pues solo los iones Ag⁺, Hg₂²⁺ y Pb²⁺ forman cloruros insolubles; los demás permanecen en disolución [@chang2022, sec. 16.8; @brown2012, sec. 17.7]. El segundo grupo se precipita con sulfuro de hidrógeno en medio ácido, donde la concentración del ion sulfuro es mínima, y solo los sulfuros menos solubles, como Bi₂S₃, CdS, CuS, HgS y SnS, se depositan [@chang2022, sec. 16.8; @brown2012, sec. 17.7].

Al hacer básica la disolución con hidróxido de sodio, el equilibrio del sulfuro se desplaza y precipitan los sulfuros más solubles, CoS, FeS, MnS, NiS y ZnS, junto con los hidróxidos de aluminio y de cromo [@chang2022, sec. 16.8; @brown2012, sec. 17.7]. El cuarto grupo se separa con carbonato de sodio, que precipita los iones Ba²⁺, Ca²⁺ y Sr²⁺ como carbonatos, y en el quinto quedan solo los iones Na⁺, K⁺ y NH₄⁺ [@chang2022, sec. 16.8; @brown2012, sec. 17.7].

La presencia de amonio se confirma porque el hidróxido de sodio libera amoniaco gaseoso, detectado por su olor o por el viraje del papel de tornasol, y los metales alcalinos por la [**prueba de llama**]{#sec-prueba-llama}, que da color amarillo al sodio, violeta al potasio y verde al cobre [@chang2022, sec. 16.8; @brown2012, sec. 17.7].

La secuencia no es arbitraria, pues cada etapa debe eliminar por completo los iones del grupo anterior para no contaminar los siguientes [@chang2022, sec. 16.8; @brown2012, sec. 17.7]. Si el clorhídrico no eliminara todo el plomo del primer grupo, por ejemplo, este precipitaría después como sulfuro y falsearía el diagnóstico [@chang2022, sec. 16.8]. Los reactivos se eligen para precipitar el menor número de cationes posible, garantizando así que cada grupo quede definido por un reactivo específico [@chang2022, sec. 16.8].

## Ejemplo resuelto

Se prepara un tampón disolviendo 0.200 mol de ácido acético y 0.200 mol de acetato de sodio en agua hasta completar 0.500 L de disolución, y se agregan después 10.0 mL de hidróxido de sodio 2.0 M; el objetivo es observar cuánto se mueve el pH frente a esa adición [@brown2012, sec. 17.2].

La primera parte del cálculo es estequiométrica: los 0.020 mol de iones hidróxido reaccionan por completo con el ácido débil, consumiendo 0.020 mol de ácido acético y generando 0.020 mol adicionales de acetato [@brown2012, sec. 17.2]. Tras la reacción quedan 0.180 mol de ácido y 0.220 mol de base conjugada en un volumen total de 0.510 L, y como el volumen se cancela en el cociente, puede trabajarse con moles [@brown2012, sec. 17.2].

La segunda parte es el equilibrio: introduciendo las cantidades ajustadas en la ecuación (ec. @eq-henderson-hasselbalch) con pKa del acético igual a 4.74, el pH resulta 4.74 + log(0.220/0.180) = 4.83 [@brown2012, sec. 17.2]. El cambio respecto del tampón original, con pH 4.74, es de solo 0.09 unidades, pese a haber añadido una cantidad de base que en agua pura produciría un efecto mucho mayor [@brown2012, sec. 17.2]. Si los mismos 0.020 mol de hidróxido se disolvieran en 0.510 L de agua pura, la concentración de iones hidróxido sería 0.039 M, el pOH 1.41 y el pH 12.59 [@brown2012, sec. 17.2].

La comparación entre 4.83 y 12.59 condensa toda la teoría de este capítulo: el tampón absorbe el impacto del hidróxido convirtiéndolo en acetato, mientras que el agua carece de reserva alguna [@brown2012, sec. 17.2]. La capacidad del tampón se agotaría solo si se añadiera tanto hidróxido que el ácido acético se consumiera por completo [@brown2012, sec. 17.2]. El ejemplo ilustra además la estrategia general de dos pasos, estequiometría primero y equilibrio después, que gobierna también las valoraciones [@brown2012, sec. 17.2].

## Preguntas y ejercicios

Los ejercicios de esta sección se inspiran en la tipología de @brown2012 (cap. 17), @chang2022 (cap. 16) y @pauling1988 (caps. 13-14); los valores, las especies y los contextos numéricos son originales de este libro, y cada resultado del solucionario ha sido verificado por re-resolución independiente.

Calcule el pH de una disolución 0.25 M de ácido acético y el de otra disolución que sea 0.25 M en ácido acético y 0.40 M en acetato de sodio, empleando para ambas la constante Ka = 1.8 × 10⁻⁵, y compare los resultados con lo que predice la ecuación (ec. @eq-henderson-hasselbalch) [@chang2022, sec. 16.1].

Prepare un tampón disolviendo 0.150 mol de amoniaco y 0.150 mol de cloruro de amonio en un litro de agua y añada después 0.030 mol de ácido clorhídrico, indicando qué reacción consume el ácido añadido y calculando el pH final con la ecuación (ec. @eq-henderson-hasselbalch), sabiendo que el pKb del amoniaco es 4.74 [@brown2012, sec. 17.2; @chang2022, sec. 16.1].

Determine el rango de pH en el que un tampón de ácido láctico-lactato resulta eficaz, sabiendo que la constante Ka del ácido láctico es de 1.4 × 10⁻⁴, y explique por qué fuera de ese margen la resistencia al cambio se deteriora [@brown2012, sec. 17.2].

Compare dos tampones de acetato, uno 2.0 M en ácido acético y 2.0 M en acetato de sodio y otro 0.20 M en ambos componentes, calculando el pH de cada uno y discutiendo cuál neutralizará más ácido o base antes de cambiar su pH de forma apreciable [@chang2022, sec. 16.2].

Calcule el pH en el punto de equivalencia de la valoración de 30.0 mL de ácido fórmico 0.10 M con hidróxido de potasio 0.10 M, considerando que la sal formada se hidroliza como base débil y empleando la relación Kb = Kw/Ka derivada en el capítulo anterior [@chang2022, sec. 16.3; @brown2012, sec. 17.3].

Un indicador tiene una constante de ionización de 2.0 × 10⁻⁶, con su forma no ionizada de un color y la ionizada de otro; calcule el pKa del indicador y el pH al que mostrará el cambio de color, y explique el criterio para elegirlo en una valoración [@chang2022, sec. 16.4].

Determine las concentraciones de equilibrio de las principales especies de una disolución 0.10 M de ácido fosfórico, resolviendo la primera etapa con la ecuación cuadrática completa y aplicando la regla de que la especie de la segunda etapa iguala a Ka2 cuando Ka1 domina [@chang2022, sec. 15.8].

Calcule el producto de solubilidad del cromato de plomo(II) a partir de su solubilidad, 4.5 × 10⁻⁵ g/L, convirtiendo primero a moles por litro con la masa molar de 323.2 g/mol y elevando después al cuadrado la solubilidad molar de la sal [@chang2022, sec. 16.5].

Calcule la solubilidad del bromuro de plata en agua pura y en una disolución 0.0010 M de bromuro de sodio, empleando Kps = 7.7 × 10⁻¹³, y exprese ambos resultados en gramos por litro para comparar el efecto del ion común observado [@chang2022, sec. 16.7].

Una disolución contiene iones cloruro y bromuro, ambos 0.020 M, y sobre ella se añade lentamente nitrato de plata; calcule la concentración de iones plata necesaria para iniciar la precipitación de cada haluro y el porcentaje de bromuro que permanece sin precipitar cuando comienza a precipitar el cloruro [@chang2022, sec. 16.6].

## Solucionario

La disolución 0.25 M de ácido acético solo plantea la cuadrática x²/(0.25 − x) = 1.8 × 10⁻⁵, cuya aproximación x = 2.1 × 10⁻³ M verifica la regla del 5%, y conduce a pH = 2.67 [@chang2022, sec. 16.1]. Con acetato de sodio 0.40 M, el ion común suprime la ionización y la ecuación (ec. @eq-henderson-hasselbalch) da pH = 4.74 + log(0.40/0.25) = 4.94 [@chang2022, sec. 16.1]. El ion común eleva el pH en más de dos unidades al desplazar el equilibrio hacia la izquierda [@brown2012, sec. 17.1].

El ácido clorhídrico añadido, 0.030 mol, reacciona con el amoniaco del tampón y lo convierte en ion amonio, dejando 0.120 mol de la base y 0.180 mol del ácido conjugado [@brown2012, sec. 17.2]. El pKa del ion amonio vale 14.00 − 4.74 = 9.26, y el pH final es 9.26 + log(0.120/0.180) = 9.08, apenas 0.18 unidades por debajo del pH inicial de 9.26 [@brown2012, sec. 17.2]. En agua pura, los mismos 0.030 mol de ácido producirían un pH de 1.52; el tampón los absorbe casi sin moverse [@brown2012, sec. 17.2].

El pKa del ácido láctico es −log(1.4 × 10⁻⁴) = 3.85, y el rango eficaz del tampón abarca pH = 3.85 ± 1, es decir, de 2.85 a 4.85 [@brown2012, sec. 17.2]. Fuera de ese margen, un componente supera al otro en más de un factor diez, el logaritmo del cociente crece o decrece más de una unidad y la resistencia al cambio se pierde [@brown2012, sec. 17.2]. Por eso los manuales recomiendan elegir el par cuyo pKa esté a menos de una unidad del pH que se desea fijar [@brown2012, sec. 17.2].

Ambos tampones tienen pH 4.74, porque el pH solo depende del cociente de concentraciones y en los dos el cociente vale uno [@chang2022, sec. 16.2; @brown2012, sec. 17.2]. El tampón 2.0 M posee, sin embargo, una capacidad amortiguadora diez veces mayor, pues contiene diez veces más moles de ácido y de base capaces de absorber las adiciones [@chang2022, sec. 16.2]. La capacidad depende de las cantidades absolutas de reserva, y la resistencia relativa al pH del cociente [@pauling1988, sec. 14-7].

En el punto de equivalencia, 30.0 mL de ácido fórmico 0.10 M han reaccionado con el mismo volumen de hidróxido de potasio 0.10 M, formando formiato de potasio 0.050 M en el volumen doblado [@brown2012, sec. 17.3]. La base conjugada del fórmico tiene Kb = 1.0 × 10⁻¹⁴ / 1.8 × 10⁻⁴ = 5.6 × 10⁻¹¹, y la hidrólisis produce [OH⁻] = 1.7 × 10⁻⁶ M, de donde pOH = 5.78 y pH = 8.22 [@brown2012, sec. 17.3]. El pH supera 7 porque el formiato es una base débil, igual que sucede con cualquier sal de ácido débil y base fuerte [@brown2012, sec. 17.3].

El pKa del indicador es −log(2.0 × 10⁻⁶) = 5.70, y el cambio de color ocurre en ese pH, donde las formas HIn e In⁻ se igualan [@chang2022, sec. 16.4]. El indicador resulta idóneo para valoraciones cuyo punto de equivalencia caiga cerca de 5.70, como la de una base débil con un ácido fuerte, y desaconsejable cuando el salto de pH ocurra en otra zona [@chang2022, sec. 16.4]. El color observado depende del desplazamiento del equilibrio HIn ⇌ H⁺ + In⁻ por el pH del medio [@brown2012, sec. 17.3].

Para el ácido fosfórico 0.10 M, la primera etapa plantea x² + 7.5 × 10⁻³ x − 7.5 × 10⁻⁴ = 0, cuya raíz positiva es x = 0.024 M, pues la aproximación simple excedería la regla del 5% [@chang2022, sec. 15.8]. Entonces [H⁺] = [H₂PO₄⁻] = 0.024 M, el pH vale 1.62, y la concentración de HPO₄²⁻ iguala a Ka2 = 6.2 × 10⁻⁸ M [@chang2022, sec. 15.8]. La tercera especie, PO₄³⁻, queda en concentraciones insignificantes por la pequeñez de Ka3 [@chang2022, sec. 15.8].

La solubilidad molar del cromato de plomo(II) es 4.5 × 10⁻⁵ g/L ÷ 323.2 g/mol = 1.4 × 10⁻⁷ M, y su producto de solubilidad, siendo la sal 1:1, es el cuadrado, 2.0 × 10⁻¹⁴ [@chang2022, sec. 16.5]. Convertir la solubilidad en gramos por litro a moles por litro es el paso indispensable, pues Kps se define con concentraciones molares [@chang2022, sec. 16.5]. La pequeñez del resultado confirma que el cromato de plomo es una sal muy poco soluble [@chang2022, sec. 16.5].

En agua pura, la solubilidad molar del bromuro de plata es √(7.7 × 10⁻¹³) = 8.8 × 10⁻⁷ M, que multiplicada por la masa molar de 187.8 g/mol da 1.7 × 10⁻⁴ g/L [@chang2022, sec. 16.7]. En bromuro de sodio 0.0010 M, el ion común reduce la solubilidad a 7.7 × 10⁻¹⁰ M, es decir, 1.4 × 10⁻⁷ g/L, casi mil veces menor [@chang2022, sec. 16.7]. La comparación muestra que el ion común desplaza el equilibrio hacia la izquierda sin alterar el valor de Kps [@chang2022, sec. 16.7].

Para el bromuro de plata, la precipitación se inicia cuando [Ag⁺] = 7.7 × 10⁻¹³ / 0.020 = 3.9 × 10⁻¹¹ M, y para el cloruro cuando [Ag⁺] = 1.6 × 10⁻¹⁰ / 0.020 = 8.0 × 10⁻⁹ M [@chang2022, sec. 16.6]. En el intervalo entre ambos umbrales, manteniendo la concentración de plata por debajo de 8.0 × 10⁻⁹ M, el bromuro precipita casi por entero [@chang2022, sec. 16.6]. Cuando el cloruro empieza a precipitar, el bromuro restante es 7.7 × 10⁻¹³ / 8.0 × 10⁻⁹ = 9.6 × 10⁻⁵ M, el 0.48% del valor inicial, de modo que 99.52% del bromuro ya se ha separado [@chang2022, sec. 16.6].

## Resumen

El efecto del ion común mostró cómo un ion compartido por dos solutos suprime la ionización del ácido o la base débil, y dio lugar a la ecuación de Henderson-Hasselbalch, que liga el pH con el pKa y con el cociente de las concentraciones del par conjugado [@chang2022, sec. 16.1; @brown2012, sec. 17.2].

Los tampones, mezclas de un ácido débil con su base conjugada, resisten el cambio de pH gracias a esa reserva de especies, y su capacidad y su rango eficaz, pH = pKa ± 1, guían su diseño [@brown2012, sec. 17.2]. Las valoraciones convierten la neutralización en medida, y sus curvas revelan la fuerza de las especies y la posición del punto de equivalencia [@brown2012, sec. 17.3].

Los indicadores, ácidos débiles coloreados, señalan el punto final cuando su pKa coincide con el pH de equivalencia, criterio central para elegir entre fenolftaleína y rojo de metilo [@pauling1988, sec. 14-6; @brown2012, sec. 17.3]. Los ácidos polipróticos se tratan por etapas, con la regla de que la segunda especie iguala a Ka2 cuando la primera constante domina, y sus curvas muestran varios puntos de equivalencia [@chang2022, sec. 15.8; @brown2012, sec. 17.3]. El producto de solubilidad cuantificó la disolución de las sales poco solubles, y su comparación con el producto iónico decide si precipita un sólido [@chang2022, sec. 16.5].

La solubilidad se altera con el ion común, con el pH cuando el anión es base conjugada de un ácido débil, y con la formación de iones complejos, cuya constante de formación explica redisolución de precipitados como el cloruro de plata en amoniaco [@chang2022, sec. 16.7]. La precipitación fraccionada y el análisis cualitativo en cinco grupos aplican estas ideas a la separación e identificación de cationes [@chang2022, sec. 16.6, 16.8]. Este arsenal de equilibrios deja preparado el terreno para la termodinámica, que explicará por qué estos procesos ocurren en la dirección que ocurren [@brown2012, cap. 17].
