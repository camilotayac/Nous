# Termodinámica química

## Introducción

Los capítulos 14 y 15 describieron cuándo se alcanza el equilibrio y con qué rapidez, pero no explicaron por qué algunas reacciones ocurren por sí solas y otras exigen un aporte externo de energía [@brown2012, sec. 19.1]. Esa pregunta, la más profunda de la química, encuentra respuesta en la termodinámica, ciencia nacida del estudio de las máquinas de vapor y consolidada por Rudolf Clausius, Ludwig Boltzmann y Josiah Willard Gibbs en el siglo XIX [@brock2015, cap. 5].

Este capítulo formaliza los dos grandes principios que gobiernan todo cambio natural: el primero fija la cantidad de energía, que se conserva, y el segundo su calidad, que se degrada [@atkins2015, cap. 3]. Con ellos se construirá la **energía libre de Gibbs** (@sec-energia-libre-gibbs), el criterio unificado de espontaneidad que conecta la entalpía del capítulo 11 con la constante de equilibrio del capítulo 15 [@pauling1988, cap. 11; @brown2012, sec. 19.5].

## Procesos espontáneos y no espontáneos

Un [**proceso espontáneo**]{#sec-procesos-espontaneos} es aquel que ocurre por sí solo bajo un conjunto dado de condiciones, sin necesidad de intervención externa [@chang2022, sec. 17.1; @brown2012, sec. 19.1]. La espontaneidad no implica rapidez: la combustión del metano es espontánea y, sin embargo, exige una chispa que supere la barrera cinética descrita en el capítulo 14 [@chang2022, sec. 17.1]. El carácter espontáneo se refiere solo a la dirección termodinámica del cambio [@brown2012, sec. 19.1].

Un **proceso no espontáneo** es aquel que no ocurre bajo las condiciones especificadas, aunque pueda volverse espontáneo al cambiarlas [@chang2022, sec. 17.1]. Una cascada cae cuesta abajo pero jamás remonta su curso, el azúcar se disuelve en el café sin reaparecer como cristal y el calor fluye de lo caliente a lo frío [@chang2022, sec. 17.1]. Ningún proceso puede ser espontáneo en ambos sentidos bajo las mismas condiciones [@chang2022, sec. 17.1].

La intuición de que lo espontáneo debe liberar energía se apoya en casos como la combustión del metano, CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l), con ΔH° = −890.4 kJ/mol, o la neutralización H⁺(aq) + OH⁻(aq) → H₂O(l), con ΔH° = −56.2 kJ/mol [@chang2022, sec. 17.1]. Sin embargo, la fusión del hielo, H₂O(s) → H₂O(l), es espontánea por encima de 0 °C pese a su ΔH° = +6.01 kJ/mol [@chang2022, sec. 17.1]. También la disolución del nitrato de amonio en agua procede sola siendo endotérmica [@chang2022, sec. 17.1].

La descomposición del óxido de mercurio(II), 2HgO(s) → 2Hg(l) + O₂(g), con ΔH° = 90.7 kJ/mol, resulta no espontánea a temperatura ambiente pero espontánea al calentar [@chang2022, sec. 17.1]. La conclusión es doble: la exotermicidad favorece la espontaneidad sin garantizarla, y una reacción endotérmica puede ser espontánea [@chang2022, sec. 17.1]. Para decidir hace falta una nueva magnitud termodinámica, la entropía [@chang2022, sec. 17.1].

## Entropía y dispersión de la energía

La [**entropía**]{#sec-entropia}, simbolizada S, mide cuán dispersa está la energía de un sistema entre las distintas formas en que puede contenerla [@chang2022, sec. 17.2]. Una taza de agua caliente posee entropía por la repartición de su energía entre los estados traslacionales, rotacionales y vibracionales de sus moléculas, y al enfriarse esa energía se dispersa entre muchos más estados de las moléculas de aire [@chang2022, sec. 17.2]. Mayores dispersión y número de estados accesibles implican mayor entropía [@chang2022, sec. 17.2].

La versión estadística de la entropía parte de los **microestados**, cada disposición específica y equiprobable de las partículas de un sistema [@chang2022, sec. 17.2]. Para cuatro moléculas distribuidas entre dos compartimentos iguales existen once microestados: uno con todas a la izquierda, cuatro con tres a un lado, y seis con dos en cada lado [@chang2022, sec. 17.2]. La distribución de dos y dos es la más probable porque admite seis realizaciones, y al crecer el número de moléculas esa distribución domina abrumadoramente [@chang2022, sec. 17.2].

$$S = k_B \ln W$$ {#eq-entropia-boltzmann}

En la ecuación de Boltzmann (@eq-entropia-boltzmann), S es la entropía del estado, W el número de microestados accesibles al sistema y k_B la **constante de Boltzmann**, cuyo valor es 1.38 × 10⁻²³ J/K [@chang2022, sec. 17.2; @pauling1988, sec. 10-4]. Como la entropía depende del logaritmo natural, cada multiplicación de W por diez suma una cantidad fija de entropía [@chang2022, sec. 17.2]. Esta ecuación, grabada en la tumba de Boltzmann en Viena, convierte la probabilidad en una propiedad termodinámica del estado [@brown2012, sec. 19.3].

$$ΔS = k_B \ln \frac{W_f}{W_i}$$ {#eq-ds-microestados}

Para un proceso entre un estado inicial y uno final, la variación de entropía (@eq-ds-microestados) depende solo del cociente de microestados, Wf/Wi, porque la entropía es función de estado como la entalpía [@chang2022, sec. 17.2]. Si el estado final ofrece más microestados que el inicial, ΔS > 0 y la entropía del sistema aumenta [@chang2022, sec. 17.2]. Boltzmann formuló esta identidad hacia 1870, antes del desarrollo de la teoría cuántica, manejando solo cocientes de multiplicidades [@pauling1988, sec. 10-4].

Conviene anticipar una discrepancia de lenguaje entre las fuentes: Brock y Pauling describen la entropía como desorden molecular que crece de sólido a gas [@brock2015, cap. 5; @pauling1988, sec. 10-4], mientras Chang la define como dispersión de la energía [@chang2022, sec. 17.2] y Atkins como degradación de su calidad [@atkins2015, cap. 3]. Las tres formulaciones describen la misma magnitud con lentes distintos: el desorden molecular, la dispersión energética y la calidad degradada son facetas equivalentes del aumento de W [@atkins2015, cap. 3].

## Cambios de entropía en la materia

Las transiciones de fase ilustran el crecimiento de microestados: al fundirse un sólido, las partículas abandonan los puntos fijos de la red y multiplican sus posiciones posibles, y al vaporizarse el aumento es todavía mayor porque el gas ocupa mucho más espacio [@chang2022, sec. 17.2]. Así, la entropía crece de sólido a líquido y de líquido a gas a temperatura constante [@brown2012, sec. 19.2]. El valor por mol de la vaporización resulta casi constante para muchos líquidos, hecho que resume la **regla de Trouton** con un cociente de unos 84 J/K·mol entre la entalpía de vaporización y el punto de ebullición absoluto [@pauling1988, sec. 10-3].

La disolución suele aumentar la entropía del sistema porque mezcla y, para electrolitos, disociación crean más partículas y más arreglos [@chang2022, sec. 17.2]. La hidratación actúa en sentido contrario: las moléculas de agua se ordenan alrededor de los iones y disminuyen su número de disposiciones [@chang2022, sec. 17.2; @brown2012, sec. 19.3]. Para iones pequeños y muy cargados como Al³⁺ y Fe³⁺, la pérdida por hidratación puede superar la ganancia por mezcla y disociación, dejando un ΔS global negativo [@chang2022, sec. 17.2].

El calentamiento también eleva la entropía: al aumentar la temperatura, las energías traslacional, rotacional y vibracional se reparten entre más niveles cuánticos accesibles [@chang2022, sec. 17.2; @brown2012, sec. 19.3]. La complejidad molecular influye del mismo modo: el etano supera al metano en entropía por sus mayores posibilidades de rotación y vibración, y el neón supera al helio porque su mayor masa estrecha la separación de niveles [@chang2022, sec. 17.2; @brown2012, sec. 19.4]. En sólidos, el diamante, más ordenado, tiene menor entropía estándar que el grafito [@chang2022, sec. 17.2].

La entropía admite valores absolutos, a diferencia de la energía y la entalpía, y por ello se tabula como **entropía estándar molar (S°)**, la entropía de un mol de sustancia pura a 1 atm y normalmente 25 °C [@chang2022, sec. 17.2; @brown2012, sec. 19.4]. Todos los valores de S° son positivos, mientras que la entalpía de formación de los elementos en su forma estable se fija arbitrariamente en cero [@chang2022, sec. 17.2]. Las unidades usuales son J/K·mol, y el uso de julios en lugar de kilojulios refleja la pequeñez de estos valores [@chang2022, sec. 17.2].

Un mol de gas perfecto que se expande en un sistema aislado, como al abrir la llave entre dos bulbos de la figura 19.2 de Brown, ilustra el segundo principio en su forma más simple: al duplicar el volumen, ΔS = R ln 2 = 5.764 J/K·mol [@pauling1988, sec. 10-4; @brown2012, sec. 19.2]. La energía potencial del mercurio que cae entre dos bulbos se convierte en energía térmica, aumentando también la entropía [@pauling1988, sec. 10-4]. Todo cambio macroespontáneo en un sistema aislado va acompañado de un aumento de W y, con él, de entropía [@pauling1988, sec. 10-4].

## La segunda ley de la termodinámica

La **segunda ley de la termodinámica** afirma que la entropía del universo aumenta en todo proceso espontáneo y permanece constante en uno reversible [@chang2022, sec. 17.3; @brown2012, sec. 19.2]. La entropía total se descompone en la del sistema y la de su entorno, de modo que la ley se escribe ΔS_univ = ΔS_sys + ΔS_surr > 0 [@chang2022, sec. 17.3; @brown2012, sec. 19.2]. La ley no impone restricciones sobre los signos individuales: el sistema puede perder entropía siempre que el entorno gane más [@brown2012, sec. 19.2].

$$ΔS_{univ} = ΔS_{sys} + ΔS_{surr}$$ {#eq-ds-universo}

En la ecuación de la segunda ley (@eq-ds-universo), ΔS_univ es la variación de entropía del universo, suma de la del sistema, ΔS_sys, y la de los alrededores, [**ΔS_surr**]{#sec-calculo-delta-s} [@chang2022, sec. 17.3]. La espontaneidad exige ΔS_univ > 0, mientras que ΔS_univ = 0 define el proceso reversible ideal e inalcanzable en la práctica [@pauling1988, sec. 10-6]. Para el sistema considerado aislado, la ley se reduce al aumento de su propia entropía, como en la expansión de un gas [@brown2012, sec. 19.2; @pauling1988, sec. 10-4].

$$ΔS_{surr} = -\frac{ΔH_{sys}}{T}$$ {#eq-ds-entorno}

La contribución del entorno a temperatura constante se calcula con la ecuación (@eq-ds-entorno), donde ΔH_sys es la entalpía del proceso en el sistema y T la temperatura absoluta de los alrededores [@brown2012, sec. 19.4; @chang2022, sec. 17.3]. Un proceso exotérmico cede calor al entorno y eleva su entropía, mientras uno endotérmico la reduce [@brown2012, sec. 19.4]. Esta relación convierte a todo calor liberado en un aumento de desorden fuera del sistema, independiente de lo que ocurra dentro [@brown2012, sec. 19.4].

En la síntesis de amoníaco, ΔH° = −92.38 kJ y ΔS° = −198.3 J/K: a 298 K el entorno gana ΔS_surr = 92 380/298 = +310 J/K, frente a la pérdida del sistema [@brown2012, sec. 19.4]. El balance del universo resulta +310 − 198.3 = +112 J/K, positivo y, por tanto, espontáneo a 25 °C [@brown2012, sec. 19.4]. A 773 K, en cambio, el entorno gana solo 92 380/773 = +119 J/K y el balance queda −79 J/K, no espontáneo [@brown2012, sec. 19.6]. La temperatura decide el signo porque el término −ΔH/T pierde magnitud al calentar [@brown2012, sec. 19.4].

## La tercera ley y las entropías absolutas

La **tercera ley de la termodinámica** establece que la entropía de un cristal perfecto puro tiende a cero cuando la temperatura tiende al cero absoluto [@brown2012, sec. 19.3; @chang2022, sec. 17.3; @pauling1988, sec. 10-9]. En un cristal a 0 K, los átomos ocupan posiciones perfectamente definidas sin movimiento térmico y existe un único microestado, de modo que S = k_B ln 1 = 0 [@brown2012, sec. 19.3]. Al calentar, la vibración de las partículas alrededor de sus posiciones de red multiplica los microestados y la entropía crece [@brown2012, sec. 19.3].

La tercera ley permite medir entropías absolutas por calorimetría, integrando los calores absorbidos desde el cero absoluto hasta la temperatura de interés [@chang2022, sec. 17.3; @brown2012, sec. 19.4]. La mecánica cuántica introduce un matiz: incluso en el estado más bajo el oscilador conserva una energía residual de vibración, la **energía del punto cero**, igual a ½hν [@pauling1988, sec. 10-13]. En cristales, la capacidad calorífica decrece con la temperatura según la **teoría de Debye**, que predice una proporcionalidad con T³ a bajas temperaturas [@pauling1988, sec. 10-16].

$$ΔS^\circ = \sum n\,S^\circ(\text{productos}) - \sum m\,S^\circ(\text{reactivos})$$ {#eq-ds-reaccion}

La entropía estándar de una reacción se calcula con la ecuación (@eq-ds-reaccion), donde n y m son los coeficientes estequiométricos y S° las entropías estándar molares de productos y reactivos [@chang2022, sec. 17.3; @brown2012, sec. 19.4]. Para la síntesis de amoníaco, N₂(g) + 3H₂(g) → 2NH₃(g), la resta de los valores tabulados da ΔS° = −198.3 J/K, signo negativo porque cuatro moles gaseosos se convierten en dos [@brown2012, sec. 19.4]. El signo de ΔS° se predice cualitativamente contando moles gaseosos, aunque moléculas más complejas pueden compensar parcialmente la reducción [@brown2012, sec. 19.4].

Las entropías estándar aumentan sistemáticamente hacia abajo en un grupo de la tabla periódica: en el grupo 4A valen 2.43 J/K·mol para el diamante, 18.81 para el silicio, 31.09 para el germanio y 51.818 para el estaño [@brown2012, sec. 19.4]. La mayor masa atómica estrecha los niveles de energía y multiplica las formas de repartirla [@chang2022, sec. 17.2]. Un caso límite lo ofrece la **entropía residual**: Koehler y Giauque midieron en 1958 un valor residual de 10.13 J/K·mol en el ClO₃F cristalino, atribuible a la congelación del desorden de orientación molecular [@pauling1988, cap. 10].

## Energía libre de Gibbs {#sec-energia-libre-gibbs}

La segunda ley exige analizar el universo, un objeto incómodo para el laboratorio, pero en 1876 Gibbs reorganizó el balance para concentrarlo todo en el sistema [@brock2015, cap. 5]. A temperatura y presión constantes, el cambio de entropía del universo resulta igual a −ΔG/T, donde G es la **energía libre de Gibbs**, una nueva función de estado definida como G = H − TS [@chang2022, sec. 17.4; @pauling1988, sec. 10-2]. Así, observar el sistema basta para decidir la espontaneidad [@chang2022, sec. 17.4; @brown2012, sec. 19.5; @pauling1988, sec. 11-1].

$$ΔG = ΔH - TΔS$$ {#eq-energia-libre}

En la ecuación de la energía libre (@eq-energia-libre), ΔG es la variación de energía libre del sistema a temperatura constante, ΔH su entalpía y ΔS su entropía [@chang2022, sec. 17.4]. La energía libre tiene unidades de energía porque H y TS las tienen, y comparte con ellos el carácter de función de estado [@chang2022, sec. 17.4]. El signo de ΔG resume la segunda ley: negativo para el proceso espontáneo, positivo para el no espontáneo y cero en el **equilibrio termodinámico**, donde no hay cambio neto [@chang2022, sec. 17.4; @brown2012, sec. 19.5; @pauling1988, sec. 11-1].

El nombre «libre» alude a la fracción de energía convertible en trabajo: en un proceso espontáneo, la disminución de G es la máxima cantidad de trabajo útil que puede extraerse [@brown2012, sec. 19.5]. Lewis y Randall difundieron esta interpretación en su tratado de 1923, que unificó la notación termodinámica dispersa de los primeros textos [@brock2015, cap. 5]. Para un proceso no espontáneo, ΔG mide el trabajo mínimo que debe invertirse para forzarlo [@brown2012, sec. 19.5].

La energía libre decrece a lo largo de toda reacción espontánea hasta alcanzar un mínimo en el equilibrio, análogamente a la energía potencial de una roca que rueda cuesta abajo hasta el valle [@brown2012, sec. 19.5]. Si el recipiente se carga con N₂ y H₂, el sistema evoluciona hacia el amoníaco descendiendo en G; si se carga con amoníaco puro, desciende descomponiéndolo, y ambos caminos terminan en el mismo valle [@brown2012, sec. 19.5]. El mínimo de la función G define, pues, la posición de equilibrio calculada en el capítulo 15 [@brown2012, sec. 19.5; @pauling1988, sec. 11-1].

Para reacciones bajo estados estándar, la **energía libre estándar de formación (ΔG°f)** se define como el cambio de G al formar un mol de compuesto desde sus elementos en sus estados estándar, tomando cero para los elementos en su forma más estable [@chang2022, sec. 17.4; @brown2012, sec. 19.5]. La energía libre estándar de una reacción se combina con las reglas de Hess del capítulo 11, restando las formaciones de los reactivos a las de los productos [@chang2022, sec. 17.4]. En la combustión del grafito, C(grafito) + O₂(g) → CO₂(g), el resultado se reduce directamente a ΔG°f(CO₂) porque las formaciones del carbono y del oxígeno valen cero [@chang2022, sec. 17.4].

## Energía libre y temperatura

Los signos de ΔH y ΔS se combinan en cuatro casos que la tabla recoge, y solo dos de ellos son incondicionales [@brown2012, sec. 19.6; @chang2022, sec. 17.4]. La temperatura decide los restantes porque el término −TΔS crece en magnitud al calentar, mientras ΔH y ΔS apenas varían [@brown2012, sec. 19.6].

| Signo de ΔH | Signo de ΔS | Espontaneidad |
| :---: | :---: | :--- |
| − | + | Espontánea a toda temperatura |
| + | − | No espontánea a ninguna temperatura |
| − | − | Espontánea solo a temperaturas bajas |
| + | + | Espontánea solo a temperaturas altas |

La tabla reproduce el contenido de la tabla 19.3 de Brown y de la 17.4 de Chang: cuando ΔH y ΔS tienen signos opuestos, la espontaneidad es independiente de T y el signo de ΔG queda fijado [@brown2012, sec. 19.6; @chang2022, sec. 17.4]. Cuando comparten signo, la competencia entre ΔH y TΔS se resuelve con la temperatura [@chang2022, sec. 17.4]. La fusión del hielo ocupa la última fila: endotérmica y con aumento de desorden, se vuelve espontánea por encima de 0 °C [@brown2012, sec. 19.1].

El punto de ebullición normal ofrece una aplicación directa: en él, líquido y vapor puros coexisten a 1 atm, Q = 1 y ΔG° = 0, de modo que [**la temperatura de transición**]{#sec-temperatura-transicion} vale T_b = ΔH°/ΔS° [@brown2012, sec. 19.7]. Para el tetracloruro de carbono, la estimación con valores a 298 K reproducen de cerca el punto de ebullición experimental de 76.5 °C, y la pequeña desviación refleja la suposición de ΔH° y ΔS° constantes con la temperatura [@brown2012, sec. 19.7]. La regla de Trouton explica por qué esa estimación funciona: el cociente ΔH_vap/ΔS_vap se mantiene en torno a 84 J/K·mol [@pauling1988, sec. 10-3].

El proceso de Haber exhibe la sensibilidad térmica de la energía libre con datos ya conocidos: ΔH° = −92.38 kJ y ΔS° = −198.3 J/K [@brown2012, sec. 19.6]. A 298 K, ΔG° = −92.38 − 298(−0.1983) = −33.3 kJ, espontáneo bajo condiciones estándar; a 773 K, ΔG° = −92.38 − 773(−0.1983) = +61 kJ, no espontáneo [@brown2012, sec. 19.6]. El signo negativo de ΔS° hace que −TΔS° crezca con la temperatura y enfríe la fuerza impulsora hacia el amoníaco [@brown2012, sec. 19.6]. Esta es la razón termodinámica del dilema industrial ya descrito en el capítulo 15 [@pauling1988, sec. 11-5].

## Energía libre bajo condiciones no estándar

Las reacciones reales no transcurren con todos los participantes en sus estados estándar, y la energía libre debe corregirse con el cociente de reacción Q del capítulo 15 [@brown2012, sec. 19.7]. La relación, derivable del potencial químico, se escribe ΔG = ΔG° + RT ln Q [@chang2022, sec. 17.5; @pauling1988, sec. 11-5]. Cuando Q vale 1, el logaritmo se anula y ΔG coincide con ΔG°, caso que se da en el punto de ebullición normal [@brown2012, sec. 19.7].

$$ΔG = ΔG^\circ + RT \ln Q$$ {#eq-dg-no-estandar}

En la ecuación de la energía libre no estándar (@eq-dg-no-estandar), R es la constante de los gases, T la temperatura absoluta, ΔG° la energía libre estándar y Q el cociente de reacción evaluado con las presiones parciales en atmósferas y las concentraciones en molaridad [@brown2012, sec. 19.7]. La energía libre se expresa en kJ por mol de reacción como está escrita, de modo que «por mol» significa por cada mol de N₂, tres de H₂ y dos de NH₃ en el proceso de Haber [@brown2012, sec. 19.7]. Las unidades de R deben elegirse coherentes con las de ΔG° [@brown2012, sec. 19.7].

Para el proceso de Haber a 25 °C con presiones de 1.0 atm de N₂, 3.0 atm de H₂ y 0.50 atm de NH₃, el cociente vale Q = (0.50)²/((1.0)(3.0)³) = 0.00926 [@brown2012, sec. 19.7]. Con ΔG° = −33.3 kJ/mol, RT ln Q = 8.314 × 298 × ln(0.00926) = −11.6 kJ/mol, y la energía libre resulta ΔG = −44.9 kJ/mol [@brown2012, sec. 19.7]. La presión elevada del reactivo y la reducida del producto aumentan la fuerza impulsora hacia el amoníaco, exactamente lo que predice el principio de Le Châtelier [@brown2012, sec. 19.7].

Si, en cambio, la mezcla contiene 0.50 atm de N₂, 0.75 atm de H₂ y 2.0 atm de NH₃, el cociente sube a Q = 18.96 y RT ln Q = +7.3 kJ/mol, dando ΔG = −26.0 kJ/mol [@brown2012, sec. 19.7]. El exceso de producto reduce la fuerza impulsora sin invertirla: la reacción sigue avanzando hacia el equilibrio, pero con menos ímpetu [@brown2012, sec. 19.7]. A medida que Q se acerca a K, el término RT ln Q compensa a ΔG° y la diferencia tiende a cero [@brown2012, sec. 19.7].

## Energía libre y constante de equilibrio

En el equilibrio, ΔG = 0 y Q = K, de modo que la ecuación (@eq-dg-no-estandar) se transforma en el puente termodinámico del capítulo 15 [@brown2012, sec. 19.7]. La relación [**ΔG° = −RT ln K**]{#sec-delta-g-equilibrio}, una de las más importantes de la química, liga la constante de equilibrio con la energía libre estándar, no con la energía libre actual del sistema que varía durante la reacción [@chang2022, sec. 17.5]. Para gases se emplea Kp y para disoluciones Kc, sin que sólidos, líquidos puros ni disolventes aparezcan en la expresión [@brown2012, sec. 19.7; @chang2022, sec. 17.5].

$$ΔG^\circ = -RT \ln K$$ {#eq-dg-equilibrio}

La ecuación de la energía libre y la constante (@eq-dg-equilibrio) implica que un ΔG° negativo produce ln K positivo y, por tanto, K > 1: cuanto más negativa la energía libre, mayor la constante [@brown2012, sec. 19.7]. Un ΔG° positivo, en cambio, da K < 1 y favorece los reactivos [@brown2012, sec. 19.7]. Esto explica cuantitativamente la tabla de magnitud de K del capítulo 15, donde la posición del equilibrio quedaba fijada por el valor de la constante [@brown2012, sec. 19.7; @chang2022, sec. 17.5].

$$K = e^{-ΔG^\circ / (RT)}$$ {#eq-k-dg}

La forma exponencial de la constante (@eq-k-dg) permite calcular K a partir de ΔG° sin medir concentraciones, lo que resulta indispensable para reacciones cuyos equilibrios son extremos [@brown2012, sec. 19.7]. Si ΔG° es muy positivo, como en la formación del óxido nítrico, N₂(g) + O₂(g) → 2NO(g), con ΔG° = 173.3 kJ, la constante resulta del orden de 10⁻³¹ y la concentración de NO en equilibrio es imperceptible [@chang2022, sec. 17.5]. Medir directamente una constante tan pequeña es prácticamente imposible, y por eso se obtiene de ΔG° [@chang2022, sec. 17.5].

Para la síntesis de amoníaco a 25 °C, con ΔG° = −33.3 kJ, la constante vale K = e^{33 300/(8.314 × 298)} = e^{13.44} = 6.8 × 10⁵, un valor enorme que favorece al producto [@brown2012, sec. 19.7]. La tabla 15.2 del capítulo 15 mostraba cómo este equilibrio tan favorable a baja temperatura se erosiona al calentar, coherente con los +61 kJ de ΔG° a 773 K [@brown2012, sec. 19.7]. En el sentido inverso, la reacción H₂ + I₂ ⇌ 2HI tiene una constante medible experimentalmente, y su ΔG° se calcula después con la ecuación (@eq-dg-equilibrio) [@chang2022, sec. 17.5].

La energía libre como criterio unificado cierra el círculo iniciado en el capítulo 15: la posición del equilibrio, la dirección del cambio para un Q dado y el efecto de la temperatura sobre K derivan todos de un único principio [@atkins2015, cap. 3; @brown2012, sec. 19.7; @chang2022, sec. 17.5]. La entalpía, que los químicos del siglo XIX creían suficiente, resulta solo la mitad de la historia [@atkins2015, cap. 3]. Los químicos modernos saben que las reacciones «ruedan cuesta arriba en entropía», no cuesta abajo en entalpía, aunque ambos criterios coincidan en la mayoría de los casos [@atkins2015, cap. 3].

## Ejemplo resuelto: el proceso de Haber bajo la lente termodinámica

El problema integra las herramientas del capítulo: para N₂(g) + 3H₂(g) ⇌ 2NH₃(g), se sabe que ΔH° = −92.38 kJ y ΔS° = −198.3 J/K, valores que se suponen constantes con la temperatura [@brown2012, sec. 19.6]. Se pide calcular la energía libre estándar a 298 K y a 773 K, la constante de equilibrio a 25 °C y la energía libre cuando las presiones parciales son 1.0 atm de N₂, 3.0 atm de H₂ y 0.50 atm de NH₃ [@brown2012, sec. 19.6-19.7].

La energía libre a 298 K se obtiene de la ecuación (@eq-energia-libre): ΔG° = −92.38 − 298(−0.1983) = −33.3 kJ, y a 773 K resulta −92.38 − 773(−0.1983) = +61 kJ [@brown2012, sec. 19.6]. Las unidades del producto TΔS° deben convertirse a kJ para sumarlas a ΔH° [@brown2012, sec. 19.6]. El cambio de signo entre ambas temperaturas revela que la mezcla estándar produce amoníaco espontáneamente a 25 °C pero se descompone a 773 K [@brown2012, sec. 19.6].

La constante de equilibrio a 25 °C se calcula despejando K en la ecuación (@eq-k-dg): K = e^{33 300/(8.314 × 298)} = e^{13.44} = 6.8 × 10⁵ [@brown2012, sec. 19.7]. La energía libre debe expresarse en julios para cancelar las unidades de R, y el resultado es una constante enorme que favorece abrumadoramente al amoníaco [@brown2012, sec. 19.7]. Los valores de K a 300–600 °C de la tabla 15.2 confirman la caída térmica de este equilibrio [@brown2012, sec. 19.7].

Para las condiciones no estándar, el cociente de reacción vale Q = (0.50)²/((1.0)(3.0)³) = 0.00926 [@brown2012, sec. 19.7]. Con la ecuación (@eq-dg-no-estandar), RT ln Q = 8.314 × 298 × ln(0.00926) = −11.6 kJ/mol, y ΔG = −33.3 + (−11.6) = −44.9 kJ/mol [@brown2012, sec. 19.7]. La presión del reactivo H₂ por encima del estándar y la del producto NH₃ por debajo profundizan la fuerza impulsora [@brown2012, sec. 19.7].

La coherencia con Le Châtelier cierra el análisis: aumentar un reactivo y disminuir un producto desplaza la reacción hacia la derecha, y la energía libre no estándar cuantifica exactamente ese desplazamiento [@brown2012, sec. 19.7]. El mismo sistema admite tres lecturas complementarias, la cinética del capítulo 14, la posición de equilibrio del capítulo 15 y la termodinámica de este capítulo, que convergen en la misma predicción [@atkins2015, cap. 3].

## Preguntas y ejercicios

Los ejercicios de este capítulo, inspirados en @brown2012 (2012), cap. 19; @chang2022 (2022), cap. 17; @pauling1988 (1988), caps. 10-11; @atkins2015 (2015), cap. 3, combinan la clasificación de espontaneidad, el signo y el cálculo de entropías, el balance del universo, los cuatro casos de temperatura y el puente entre energía libre y constante de equilibrio.

Primer ejercicio: la descomposición del óxido de mercurio(II), 2HgO(s) → 2Hg(l) + O₂(g), tiene ΔH° = 90.7 kJ/mol [@chang2022, sec. 17.1]. Explica por qué esta reacción endotérmica resulta no espontánea a temperatura ambiente y espontánea al calentar, y justifica por qué la mera exotermicidad no basta para predecir la dirección de un cambio [@chang2022, sec. 17.1].

Segundo ejercicio: predice el signo de ΔS para condensar vapor de agua, cristalizar sacarosa desde una disolución sobresaturada, calentar hidrógeno de 60 a 80 °C y sublimar hielo seco, razonando en cada caso con el número de microestados [@chang2022, sec. 17.2]. Indica además cuál de los cuatro procesos presenta el mayor aumento absoluto de entropía [@chang2022, sec. 17.2].

Tercer ejercicio: un mol de gas perfecto se expande en un sistema aislado desde un volumen V hasta 5V al abrir una llave entre dos recipientes [@pauling1988, sec. 10-4]. Calcula el aumento de entropía con la fórmula ΔS = R ln(V₂/V₁) y compara tu resultado con los 5.764 J/K·mol que se obtienen al duplicar el volumen [@pauling1988, sec. 10-4].

Cuarto ejercicio: cincuenta gramos de mercurio líquido se congelan a su punto normal de congelación, −38.9 °C, con entalpía molar de fusión ΔH_fus = 2.29 kJ/mol [@brown2012, sec. 19.2]. Calcula el cambio de entropía del sistema y explica por qué su signo es negativo aunque el proceso sea espontáneo [@brown2012, sec. 19.2].

Quinto ejercicio: 68.3 g de etanol gaseoso condensan a 78.3 °C, su punto normal de ebullición, con entalpía molar de vaporización 38.56 kJ/mol [@brown2012, sec. 19.2]. Determina el cambio de entropía del sistema y compara ese valor con el que predice la regla de Trouton para la vaporización [@brown2012, sec. 19.2; @pauling1988, sec. 10-3].

Sexto ejercicio: para la síntesis de amoníaco se conocen ΔH° = −92.38 kJ y ΔS° = −198.3 J/K [@brown2012, sec. 19.4]. Calcula la entropía ganada por el entorno a 298 K y a 773 K con la ecuación (@eq-ds-entorno), y establece con la ecuación (@eq-ds-universo) en cuál de las dos temperaturas el proceso es espontáneo [@brown2012, sec. 19.4].

Séptimo ejercicio: una reacción exotérmica con ΔS positivo es espontánea a toda temperatura, mientras una endotérmica con ΔS negativo jamás lo es [@brown2012, sec. 19.6]. Explica a qué temperaturas resultan espontáneas las dos combinaciones restantes, la de ΔH y ΔS negativos y la de ambos positivos, y justifica por qué el término TΔS inclina la balanza [@brown2012, sec. 19.6; @chang2022, sec. 17.4].

Octavo ejercicio: un mol de bromo líquido se vaporiza a su punto normal de ebullición, 58.8 °C, con ΔH_vap = 29.6 kJ/mol [@brown2012, sec. 19.2]. Indica si su entropía aumenta o disminuye y calcula ΔS_vap, comparando el resultado con la regla de Trouton [@brown2012, sec. 19.2; @pauling1988, sec. 10-3].

Noveno ejercicio: para la formación del óxido nítrico, N₂(g) + O₂(g) → 2NO(g), se conocen ΔH° = 180.7 kJ y ΔS° = 24.7 J/K [@brown2012, sec. 19.5]. Calcula ΔG° a 298 K, obtén la constante de equilibrio con la ecuación (@eq-k-dg) y explica por qué resulta preferible calcular K a partir de ΔG° que medirla experimentalmente [@brown2012, sec. 19.5; @chang2022, sec. 17.5].

Décimo ejercicio: una mezcla de 0.50 atm de N₂, 0.75 atm de H₂ y 2.0 atm de NH₃ se encuentra a 25 °C [@brown2012, sec. 19.7]. Con ΔG° = −33.3 kJ/mol, calcula el cociente de reacción, el término RT ln Q y la energía libre no estándar, y decide si la reacción avanza hacia los productos o hacia los reactivos [@brown2012, sec. 19.7].

## Solucionario

Primer ejercicio: la reacción es endotérmica y genera gas, de modo que ΔH > 0 y ΔS > 0, el cuarto caso de la tabla: espontánea solo a temperaturas altas [@chang2022, sec. 17.1]. A temperatura ambiente el término TΔS no compensa a ΔH y la descomposición no ocurre, pero al calentar la entropía gana el pulso [@chang2022, sec. 17.1]. La exotermicidad favorece la espontaneidad sin garantizarla, como prueban este ejemplo y el de la fusión del hielo [@chang2022, sec. 17.1].

Segundo ejercicio: condensar vapor reduce los microestados y da ΔS < 0; cristalizar sacarosa ordena las moléculas y también da ΔS < 0 [@chang2022, sec. 17.2]. Calentar el hidrógeno incrementa sus movimientos moleculares y da ΔS > 0, mientras sublimar hielo seco multiplica los arreglos al pasar a gas y da el mayor aumento absoluto [@chang2022, sec. 17.2]. La sublimación combina la ganancia de la fusión con la de la vaporización [@chang2022, sec. 17.2].

Tercer ejercicio: con V₂/V₁ = 5, ΔS = R ln 5 = 8.315 × 1.6094 = 13.38 J/K·mol, más del doble del valor para el doble de volumen [@pauling1988, sec. 10-4]. El logaritmo natural hace que el aumento de entropía crezca más lentamente que el volumen: quintuplicar el espacio no quintuplica la entropía [@pauling1988, sec. 10-4]. La espontaneidad de la expansión en un sistema aislado es una consecuencia directa del aumento de W [@pauling1988, sec. 10-4].

Cuarto ejercicio: la congelación es la inversa de la fusión, con q = −2.29 kJ/mol, y la cantidad de mercurio es 50.0/200.59 = 0.2493 mol [@brown2012, sec. 19.2]. El calor cedido vale −2.29 × 0.2493 = −0.571 kJ y, dividido entre la temperatura absoluta 234.25 K, da ΔS = −571/234.25 = −2.44 J/K [@brown2012, sec. 19.2]. El signo negativo es correcto porque el sistema se ordena, y la espontaneidad proviene del entorno, que gana los +2.44 J/K [@brown2012, sec. 19.2].

Quinto ejercicio: la masa de etanol equivale a 68.3/46.07 = 1.482 mol, y la condensación libera −38.56 × 1.482 = −57.16 kJ [@brown2012, sec. 19.2]. Dividido entre la temperatura absoluta 351.45 K, el cambio de entropía del sistema vale −57 160/351.45 = −162.6 J/K [@brown2012, sec. 19.2]. La regla de Trouton predeciría, para la vaporización inversa, unos +84 J/K·mol, y el valor obtenido, 162.6 J/K entre 1.482 mol, da 109.7 J/K·mol, superior por los enlaces de hidrógeno del etanol [@pauling1988, sec. 10-3].

Sexto ejercicio: el entorno gana ΔS_surr = −ΔH/T, de modo que a 298 K resultan 92 380/298 = +310 J/K y a 773 K, 92 380/773 = +119 J/K [@brown2012, sec. 19.4]. Sumando la pérdida del sistema, −198.3 J/K, el universo gana +112 J/K a 298 K y pierde −79 J/K a 773 K [@brown2012, sec. 19.4]. Solo la primera temperatura admite la síntesis espontánea bajo condiciones estándar, en pleno acuerdo con el ejemplo resuelto [@brown2012, sec. 19.4].

Séptimo ejercicio: con ΔH y ΔS negativos, el término −TΔS es positivo y compite con ΔH, de modo que la espontaneidad solo ocurre a temperaturas bajas, donde TΔS no supera a ΔH [@chang2022, sec. 17.4]. Con ambos positivos, −TΔS es negativo y requiere temperaturas altas para dominar el balance [@chang2022, sec. 17.4]. La temperatura actúa solo sobre el término TΔS, porque ΔH y ΔS cambian poco con ella [@brown2012, sec. 19.6].

Octavo ejercicio: la vaporización multiplica los microestados y ΔS debe ser positivo [@brown2012, sec. 19.2]. Con temperatura absoluta 331.95 K, ΔS_vap = 29 600/331.95 = 89.2 J/K·mol, próximo a los 84 J/K·mol de la regla de Trouton [@brown2012, sec. 19.2; @pauling1988, sec. 10-3]. La desviación moderada es típica de líquidos sin enlaces de hidrógeno pronunciados [@pauling1988, sec. 10-3].

Noveno ejercicio: ΔG° = 180.7 − 298(0.0247) = 173.3 kJ, muy positivo [@brown2012, sec. 19.5]. La constante resulta K = e^{−173 300/(8.314 × 298)} = e^{−69.9} = 4 × 10⁻³¹, un valor tan pequeño que los productos son indetectables en el equilibrio [@chang2022, sec. 17.5]. Medir una constante semejante por concentraciones es inviable, y por eso se obtiene de ΔG° [@chang2022, sec. 17.5].

Décimo ejercicio: el cociente vale Q = (2.0)²/((0.50)(0.75)³) = 4/0.211 = 18.96 [@brown2012, sec. 19.7]. Con RT ln Q = 8.314 × 298 × ln(18.96) = +7.3 kJ/mol, la energía libre resulta ΔG = −33.3 + 7.3 = −26.0 kJ/mol [@brown2012, sec. 19.7]. Como ΔG sigue siendo negativo, la reacción avanza hacia los productos, aunque con menor fuerza impulsora que en condiciones estándar [@brown2012, sec. 19.7].

## Resumen

La termodinámica distingue la cantidad de energía, que el primer principio conserva, de su calidad, que el segundo principio degrada [@atkins2015, cap. 3]. Un proceso espontáneo ocurre por sí solo bajo condiciones dadas, sin implicar rapidez, y la exotermicidad lo favorece sin garantizarlo [@chang2022, sec. 17.1]. La entropía mide la dispersión de la energía entre los microestados del sistema, según la ecuación de Boltzmann S = k_B ln W [@chang2022, sec. 17.2].

La segunda ley exige que la entropía del universo aumente en todo proceso espontáneo, con el entorno contribuyendo con ΔS_surr = −ΔH/T [@brown2012, sec. 19.4]. La tercera ley permite fijar entropías absolutas con el cero en el cristal perfecto a 0 K, y las entropías estándar de reacción se combinan restando reactivos de productos [@brown2012, sec. 19.4]. Los cuatro casos de signos de ΔH y ΔS determinan cuándo la temperatura decide la espontaneidad [@brown2012, sec. 19.6].

La energía libre de Gibbs, ΔG = ΔH − TΔS, condensa el balance del universo en el sistema: negativa para la espontaneidad, positiva contra ella y cero en el equilibrio [@chang2022, sec. 17.4]. Bajo condiciones no estándar, ΔG = ΔG° + RT ln Q corrige la energía libre con el cociente de reacción [@brown2012, sec. 19.7]. En el equilibrio, la relación ΔG° = −RT ln K conecta la termodinámica con la constante del capítulo 15 [@chang2022, sec. 17.5].

El proceso de Haber ilustra la potencia del marco: un solo par de valores de ΔH° y ΔS° predice espontaneidad, constante de equilibrio y efecto de la presión [@brown2012, sec. 19.6-19.7]. La caída de la constante con la temperatura, documentada en la tabla 15.2, y la mejora de la fuerza impulsora con la presión del reactivo emergen del mismo formalismo [@brown2012, sec. 19.7]. La termodinámica, en suma, reduce la química del cambio a un único principio de máximo desorden del universo [@atkins2015, cap. 3].
