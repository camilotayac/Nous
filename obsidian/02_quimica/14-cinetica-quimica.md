# Cinética química

## Introducción

Aunque todos los procesos químicos transcurren hasta alcanzar el equilibrio, pocos lo hacen con la misma rapidez. La [**cinética química**]{#sec-cinetica-quimica}, el área que estudia las velocidades de las reacciones, nació de la observación de que la afinidad no basta para predecir un resultado: a comienzos del siglo XIX Berthollet sostuvo que los productos podían descomponerse en masa, mientras Proust defendía proporciones fijas, y el debate reveló que la dirección de una transformación depende de las condiciones dinámicas [@brock2015, cap. 5].

La formulación cuantitativa llegó en 1863, cuando los noruegos Guldberg y Waage enunciaron la ley de acción de masas: la velocidad de una reacción es proporcional al producto de las concentraciones de los reactivos. Publicada en noruego, la idea fue ignorada hasta los años ochenta del mismo siglo, cuando la nueva fisicoquímica, que emergía hacia 1850 con escuelas como la de Bunsen, la integró al marco teórico de la disciplina [@brock2015, cap. 5].

La pregunta doble de la química se asemeja a la de un viaje: ¿hasta dónde llegará la reacción y cuánto tardará? El equilibrio responde la primera y la dinámica de reacciones responde la segunda. Muchas transformaciones termodinámicamente posibles son tan lentas que parecen no ocurrir: una mezcla de hidrógeno y oxígeno puede permanecer inalterada a temperatura ambiente hasta que una chispa la enciende [@atkins2015, cap. 3].

La velocidad de una reacción depende del estado físico de los reactivos, de la concentración, de la temperatura y de la presencia de catalizadores [@brown2012, sec. 14.1]. Este capítulo desarrolla, en ese orden, la definición de velocidad, las leyes de velocidad y sus formas integradas, la vida media, el efecto de la temperatura con la ecuación de Arrhenius, los mecanismos de reacción y la catálisis, cuya conexión con el equilibrio se retoma en el capítulo 15 [@brown2012, sec. 14.7].

## Los factores que afectan la velocidad de reacción

Los reactivos reaccionan con velocidades características: unas reacciones, como las precipitaciones en disolución, son casi instantáneas, mientras otras, como la corrosión del hierro y la descomposición de los alimentos, tardan meses o años [@brown2012, sec. 14.1]. Pauling resume que la velocidad depende de la composición, de la forma física, de la intimidad de la mezcla, de la temperatura, de la presión, de las concentraciones, de la irradiación y de la presencia de otras sustancias [@pauling1988, sec. 16-1].

La superficie expuesta de los sólidos manda en su reactividad: el cinc en polvo se disuelve en ácido mucho más deprisa que una barra, y un propelente de perclorato potásico con carbón quema más rápido cuanto más finas son sus partículas [@pauling1988, sec. 16-1]. La **reacción homogénea** transcurre en una sola fase y la **reacción heterogénea** en las interfaces entre fases, donde el contacto entre especies es la variable decisiva [@brown2012, sec. 14.1].

La intimidad del contacto pesa tanto como la superficie: dos líquidos inmiscibles reaccionan solo en su interfase, de modo que agitar la mezcla y acrecentar el área de contacto acelera la transformación [@pauling1988, sec. 16-1]. En las reacciones con sólidos la concentración del sólido no figura en la ley de velocidad, pues la reacción ocurre sobre su superficie, y por ello la finura del polvo equivale a disponer de más sitios de reacción [@brown2012, sec. 14.1].

La concentración actúa aumentando la frecuencia de colisiones, y la temperatura eleva la fracción de colisiones eficaces, de modo que la constante de velocidad depende de ella; un [**catalizador**]{#sec-catalizador} acelera la reacción sin consumirse y no desplaza la posición de equilibrio [@brown2012, sec. 14.1; @pauling1988, sec. 16-5; @atkins2015, cap. 3]. Ciertas transformaciones se aceleran además por irradiación: una **reacción fotoquímica**, como la del cloro con el hidrógeno, se inicia por la luz [@pauling1988, sec. 16-1].

La **reacción homogénea** típica se estudia en un **termostato**, que mantiene la temperatura constante mientras se sigue la presión o la concentración [@pauling1988, sec. 16-1]. La comparación sistemática de estos factores revela que la concentración es el eje cuantitativo del análisis: de ella dependen la velocidad instantánea y la forma de la ley de velocidad que se desarrolla a continuación.

## Velocidad de reacción y estequiometría

La [**velocidad de reacción**]{#sec-velocidad-reaccion} se define como el aumento de la concentración de un producto, o la disminución de la de un reactivo, por unidad de tiempo, y se expresa ordinariamente en moles por litro por segundo [@brown2012, sec. 14.2]. La **velocidad promedio** corresponde a un segmento de la curva concentración-tiempo, mientras la **velocidad instantánea** es la pendiente de la tangente en un punto de esa curva [@brown2012, sec. 14.2].

Un ejemplo clásico es la hidrólisis del C₄H₉Cl, cuya concentración se sigue por titulación: de las pendientes de las tangentes se estima que la velocidad instantánea vale 1,9 × 10⁻⁴ M/s al inicio del proceso y desciende a 1,1 × 10⁻⁴ M/s a los 300 segundos, porque queda menos reactivo [@brown2012, Sample Exercise 14.2].

Antes de comparar velocidades de especies distintas hay que tener en cuenta la estequiometría: en 2HI → H₂ + I₂, por cada dos moles de HI desaparecidos se forma un mol de H₂ y uno de I₂, de modo que la velocidad de desaparición del HI duplica la de aparición del I₂. La definición general divide cada cambio de concentración entre el coeficiente estequiométrico de la especie [@brown2012, sec. 14.2].

$$\text{velocidad} = -\frac{1}{a}\frac{\Delta[A]}{\Delta t} = -\frac{1}{b}\frac{\Delta[B]}{\Delta t} = \frac{1}{c}\frac{\Delta[C]}{\Delta t} = \frac{1}{d}\frac{\Delta[D]}{\Delta t}$$ {#eq-velocidad-estequiometrica}

En la ecuación @eq-velocidad-estequiometrica, a, b, c y d son los coeficientes estequiométricos de la reacción aA + bB → cC + dD; Δ[A]/Δt mide el cambio de molaridad de cada especie en el intervalo Δt; los signos menos convierten en positivas las velocidades de desaparición de los reactivos, y los cocientes 1/a, 1/b, 1/c y 1/d igualan las velocidades por unidad de reacción [@brown2012, sec. 14.2]. Cuando todos los coeficientes valen uno, los cuatro términos coinciden.

Las velocidades se miden con el método más cómodo para cada sistema: la presión de un gas en un recipiente cerrado, la absorbancia de una disolución coloreada o la conductividad de una disolución iónica. Las especies coloreadas se siguen con un **espectrómetro** aplicando la **ley de Beer**, A = εbc, que liga la absorbancia A con la concentración de la especie absorbente [@brown2012, sec. 14.2].

En las reacciones gaseosas con cambio en el número de moles, un manómetro basta, como en el estudio del dimetiléter midiendo la presión total a tiempos fijos [@pauling1988, Example 16-1]. La **velocidad inicial**, la velocidad instantánea justo al comenzar la reacción, es especialmente útil porque en ese instante las concentraciones de productos son despreciables y no enturbian el análisis [@brown2012, sec. 14.3].

## Ley de velocidad y orden de reacción

La [**ley de velocidad**]{#sec-ley-velocidad} expresa la velocidad de una reacción en función de las concentraciones de los reactivos y de una [**constante de velocidad**]{#sec-constante-velocidad} k: rate = k[A]ᵐ[B]ⁿ. Los exponentes m y n, llamados [**orden de reacción**]{#sec-orden-reaccion} respecto de cada reactivo, no guardan relación necesaria con los coeficientes estequiométricos y deben determinarse experimentalmente; su suma es el [**orden global de reacción**]{#sec-orden-global-reaccion} [@brown2012, sec. 14.3].

$$\text{velocidad} = k[A]^{m}[B]^{n}$$ {#eq-ley-velocidad}

En la ecuación @eq-ley-velocidad, k es la constante de velocidad, característica de cada reacción a una temperatura dada y con unidades que dependen del orden global, s⁻¹ para orden uno y M⁻¹ s⁻¹ para orden dos; [A] y [B] son las molaridades de los reactivos, y m y n son los órdenes parciales, por lo común números enteros o mitades, que indican cuántas veces se multiplica la velocidad al duplicar la concentración correspondiente [@brown2012, sec. 14.3].

El orden es empírico: el N₂O₅ se descompone con ley rate = k[N₂O₅] aunque su ecuación balanceada lleva coeficiente dos, y la reacción 2NO + 2H₂ → N₂ + 2H₂O sigue rate = k[NO]²[H₂], de tercer orden global [@brown2012, sec. 14.3]. Para descubrirlo se mide la velocidad inicial en series de experimentos que varían una concentración a la vez, el **método de las velocidades iniciales** [@brown2012, sec. 14.3].

Un ejemplo que fija ideas: la reacción NH₄⁺(aq) + NO₂⁻(aq) → N₂(g) + 2H₂O(l) resultó de primer orden en cada reactivo, con k = 2,7 × 10⁻⁴ M⁻¹ s⁻¹ y ley rate = k[NH₄⁺][NO₂⁻] [@brown2012, Table 14.2]. En el ejercicio del texto, la reacción A + B → C dio rate = k[A]², independiente de B, con k = 4,0 × 10⁻³ M⁻¹ s⁻¹, y con [A] = 0,050 M la velocidad vale 1,0 × 10⁻⁵ M/s [@brown2012, Sample Exercise 14.6].

No todas las leyes son tan sencillas: la cloración del cloroformo, CHCl₃ + Cl₂ → CCl₄ + HCl, sigue rate = k[CHCl₃][Cl₂]^1/2, de orden global tres medios, con la constante medida en M^(−1/2) s⁻¹ [@brown2012, sec. 14.3]. La reacción del monóxido de nitrógeno con hidrógeno, de orden tres, presenta en cambio k = 1,2 M⁻² s⁻¹ [@brown2012, Practice Exercise 14.6].

La constante k no depende de las concentraciones, pero sí de la temperatura, como mostrará la ecuación de Arrhenius, y de la presencia de un catalizador, que la modifica al rebajar la energía de activación [@brown2012, sec. 14.5]. Las leyes de velocidad diferenciales describen un instante; para conocer las concentraciones a tiempos largos se integran, como se hace en la sección siguiente.

## Variación de la concentración con el tiempo

Las leyes integradas convierten la velocidad instantánea en una relación entre concentración y tiempo. Para una reacción de primer orden, rate = k[A], el cálculo integral da ln[A]ₜ = −kt + ln[A]₀, con ln el logaritmo natural; el gráfico de ln[A] frente a t es entonces una recta de pendiente −k [@brown2012, sec. 14.4].

$$\ln[A]_{t} = -kt + \ln[A]_{0}$$ {#eq-primer-orden-integrada}

En la ecuación @eq-primer-orden-integrada, [A]ₜ es la molaridad del reactivo en el instante t y [A]₀ su molaridad inicial; t es el tiempo transcurrido y k la constante de velocidad, con unidades de s⁻¹ o de año⁻¹ según la escala; el producto kt es adimensional, de modo que ln[A]ₜ decrece linealmente con el tiempo [@brown2012, sec. 14.4]. La vida media, definida más adelante, no depende de la concentración inicial en el primer orden.

La **isomerización** del metilisocianuro, CH₃NC → CH₃CN, a 199 °C, es un reordenamiento estructural de primer orden con k = 5,1 × 10⁻⁵ s⁻¹; su gráfica de ln[CH₃NC] frente al tiempo es rectilínea y su vida media vale 13 600 s, unas 3,78 horas [@brown2012, sec. 14.4]. El decaimiento radiactivo es el ejemplo natural del mismo formalismo: la **constante de desintegración** de un núclido es la constante de velocidad de primer orden del proceso [@pauling1988, sec. 16-2].

Con la forma integrada se calculan concentraciones futuras: un insecticida que se hidroliza con k = 1,45 año⁻¹ deja al cabo de un año el 24% de la concentración inicial de 5,0 × 10⁻⁷ g/cm³, es decir 1,2 × 10⁻⁷ g/cm³, y para que caiga hasta 3,0 × 10⁻⁷ g/cm³ bastan 0,35 años [@brown2012, Sample Exercise 14.7]. Estos cálculos se extienden en la sección del ejemplo resuelto a las edades geológicas.

Para segundo orden, rate = k[A]², la integración produce la ecuación siguiente, en la que 1/[A]ₜ y t se relacionan linealmente con pendiente k, a diferencia del logaritmo del primer orden; la linealidad de esa representación es la prueba experimental del orden dos [@brown2012, sec. 14.4].

$$\frac{1}{[A]_{t}} = kt + \frac{1}{[A]_{0}}$$ {#eq-segundo-orden-integrada}

En la ecuación @eq-segundo-orden-integrada, [A]ₜ y [A]₀ son las molaridades al tiempo t y al comienzo, k es la constante de segundo orden, en M⁻¹ s⁻¹, y la ordenada al origen 1/[A]₀ permite verificar los datos experimentales; a diferencia del primer orden, la vida media depende de la concentración inicial [@brown2012, sec. 14.4]. La descomposición del NO₂ a 300 °C, con rate = k[NO₂]² y k = 0,543 M⁻¹ s⁻¹, es el ejemplo canónico del texto [@brown2012, sec. 14.4].

El segundo orden admite comprobaciones elegantes: si se duplica el volumen del recipiente, la concentración baja a la mitad y la velocidad se reduce a la cuarta parte, de modo que el tiempo para un cambio dado se duplica [@pauling1988, Example 16-5]. Cuando un reactivo está en enorme exceso, su concentración apenas cambia y el segundo orden se disfraza de **pseudoprimer orden**, como en el acetato de etilo con hidróxido de sodio [@pauling1988, Example 16-7].

Algunas reacciones son de orden cero: su velocidad es constante mientras quede reactivo, como cuando la etapa lenta es la descomposición de las moléculas adsorbidas sobre una superficie totalmente cubierta [@brown2012, sec. 14.4]. La ley integrada, [A]ₜ = −kt + [A]₀, produce una recta de pendiente −k al representar [A] frente a t [@brown2012, sec. 14.4].

$$[A]_{t} = -kt + [A]_{0}$$ {#eq-orden-cero-integrada}

En la ecuación @eq-orden-cero-integrada, la velocidad de desaparición de A es constante, k tiene unidades de M/s, y el gráfico de [A]ₜ contra t corta el eje horizontal en el tiempo t = [A]₀/k [@brown2012, sec. 14.4]. El orden se reconoce por la linealidad de cada representación: ln[A] frente a t para el primero, 1/[A] frente a t para el segundo y [A] sin transformar para el orden cero [@brown2012, sec. 14.4].

La [**vida media**]{#sec-vida-media} t½ es el tiempo necesario para que la concentración de un reactivo caiga a la mitad [@brown2012, sec. 14.4]. En el primer orden vale t½ = 0,693/k: el insecticida da 0,478 años y el C₄H₉Cl unos 340 s, k ≈ 2,0 × 10⁻³ s⁻¹ [@brown2012, sec. 14.4 y Sample Exercise 14.9]. El bromuro de metilo estratosférico tiene t½ = 0,8 ± 0,1 años y en diez años queda un 2 × 10⁻⁴ de lo emitido [@brown2012, Chemistry and Life, sec. 14.4].

$$t_{1/2} = \frac{0,693}{k}$$ {#eq-vida-media-primer-orden}

En la ecuación @eq-vida-media-primer-orden, t½ es el tiempo necesario para que [A] caiga a la mitad de su valor inicial, 0,693 es el logaritmo natural de dos y k la constante de primer orden [@brown2012, sec. 14.4]. Como k no depende de la concentración, la vida media tampoco: cada semivida adicional reduce la concentración a la mitad de la anterior, propiedad que caracteriza experimentalmente al primer orden [@brown2012, sec. 14.4].

El mismo criterio aplicado a la ecuación del segundo orden da t½ = 1/(k[A]₀): la vida media crece según disminuye la concentración inicial, de modo que el NO₂ tarda menos en reducirse a la mitad cuando empieza más concentrado [@brown2012, sec. 14.4]. Pauling lo formula diciendo que la vida media de una reacción de segundo orden es inversamente proporcional a la concentración inicial [@pauling1988, Example 16-6].

$$t_{1/2} = \frac{1}{k[A]_{0}}$$ {#eq-vida-media-segundo-orden}

En la ecuación @eq-vida-media-segundo-orden, t½ depende de k y de la molaridad inicial [A]₀: cada vez que la concentración inicial se duplica, la semivida se reduce a la mitad [@brown2012, sec. 14.4]. Esta dependencia distingue el segundo orden del primero y es la base de la datación por carbono-14, que cierra el apartado con su aplicación más célebre [@pauling1988, Example 16-3].

La madera vieja del Monte Mazama, en Oregón, emite 6,90 cuentas por minuto y gramo frente a 15,3 de la madera recién cortada; de la razón 0,451 y la constante de primer orden k = 1,20 × 10⁻⁴ año⁻¹, derivada de la vida media de 5760 años, se deduce una edad de 6640 años para la erupción [@pauling1988, Example 16-3]. El método ilustra cómo la cinética de primer orden ordena el tiempo geológico.

## Temperatura, colisiones y energía de activación

La temperatura acelera casi todas las reacciones: como regla empírica general, la velocidad se duplica por cada 10 °C de aumento, aunque la regla es aproximada, pues el incremento exacto depende de la energía de activación [@pauling1988, sec. 16-4]. Las luciérnagas, cuyos destellos químicos se suceden más deprisa en las noches cálidas, ilustran la sensibilidad biológica de la velocidad a la temperatura [@atkins2015, cap. 3].

El [**modelo de colisiones**]{#sec-modelo-colisiones} explica el origen de esa sensibilidad: para que ocurra la reacción, las moléculas deben chocar con orientación adecuada y con energía suficiente [@brown2012, sec. 14.5]. En la reacción H₂ + I₂ → 2HI, cada molécula experimenta unos 10¹⁰ colisiones por segundo, pero solo 1 de cada 10¹³ colisiones resulta eficaz a temperatura ambiente [@brown2012, sec. 14.5].

La orientación importa porque los enlaces se forman en direcciones concretas: el átomo de cloro debe golpear el extremo del NOCl para que Cl + NOCl → Cl₂ + NO se complete, y cualquier otra geometría rebota sin reacción. Este requisito geométrico es el [**factor de orientación**]{#sec-factor-orientacion} [@brown2012, sec. 14.5].

La energía importa todavía más: las moléculas deben superar una barrera formando el [**complejo activado**]{#sec-complejo-activado}, una asociación transitoria en la que los enlaces están a medio romper y a medio formar, llamada [**estado de transición**]{#sec-estado-transicion} en el punto de máxima energía [@brown2012, sec. 14.5]. En la isomerización del metilisocianuro, el enlace C–N se rompe parcialmente mientras se forma el enlace C–C del acetonitrilo, y la cima del perfil corresponde a esa configuración intermedia [@brown2012, sec. 14.5].

La [**energía de activación**]{#sec-energia-activacion} es la energía mínima que deben poseer las moléculas que colisionan para formar el complejo activado; cada reacción tiene la suya característica [@brown2012, sec. 14.5]. Solo las colisiones cuya energía supera esa barrera producen producto: el resto rebota, como una pelota que no alcanza la cima de la colina para rodar al valle vecino [@brown2012, sec. 14.5].

La fracción de moléculas con energía suficiente la da la [**distribución de Boltzmann**]{#sec-distribucion-boltzmann}: cuanto mayor es la temperatura, más moléculas superan la barrera, porque la cola de la distribución se extiende hacia energías altas [@pauling1988, sec. 16-4]. Cuantitativamente, esa fracción vale f = e^(−Ea/RT), donde Ea aparece en julios por mol, R es la constante de los gases y T la temperatura absoluta [@brown2012, sec. 14.5].

$$f = e^{\frac{-E_{a}}{RT}}$$ {#eq-fraccion-energia}

En la ecuación @eq-fraccion-energia, f es la fracción de moléculas cuya energía alcanza o supera Ea, Ea es la energía de activación en julios por mol, R la constante de los gases con valor 8,314 J/(mol·K) y T la temperatura absoluta en kelvin [@brown2012, sec. 14.5]. Cuando T crece, el exponente negativo se acerca a cero y f aumenta, aunque Ea, fija para cada reacción, no cambie [@brown2012, sec. 14.5].

Con Ea = 100 kJ/mol, f vale 3,9 × 10⁻¹⁸ a 300 K y 1,4 × 10⁻¹⁷ a 310 K: un aumento de diez grados multiplica la fracción 3,6 veces, más que el factor dos de la regla empírica, lo que confirma su carácter aproximado [@brown2012, sec. 14.5]. La clara de huevo, que coagula unas cincuenta veces más deprisa al subir 10 °C, muestra cuán variable es el factor real [@pauling1988, sec. 16-4].

## La ecuación de Arrhenius

Svante Arrhenius, doctor en 1884 y premio Nobel de química en 1903, publicó en 1889 las ecuaciones de velocidad que llevan su nombre, y la literatura mayoritaria fecha la energía de activación en ese año [@pauling1988, sec. 16-4]. Brown, en cambio, sitúa la sugerencia en 1888, cuando Arrhenius acababa de consolidar junto con van 't Hoff y Ostwald la revista Zeitschrift für physikalische Chemie [@brown2012, sec. 14.5].

La [**ecuación de Arrhenius**]{#sec-ecuacion-arrhenius} resume cómo k combina la frecuencia de colisiones favorables y la fracción de Boltzmann: cuanto menor es la energía de activación, mayor es la constante de velocidad a una temperatura dada [@brown2012, sec. 14.5]. Su forma exponencial explica por qué pequeñas variaciones de temperatura transforman radicalmente las velocidades.

$$k = A\,e^{\frac{-E_{a}}{RT}}$$ {#eq-arrhenius}

En la ecuación @eq-arrhenius, k es la constante de velocidad, A el [**factor de frecuencia**]{#sec-factor-frecuencia}, que incluye el número de colisiones con orientación favorable por segundo, Ea la energía de activación en julios por mol, R la constante de los gases y T la temperatura en kelvin [@brown2012, sec. 14.5]. El exponente −Ea/RT hace que k crezca con T y que una Ea menor multiplique k de forma exponencial [@brown2012, sec. 14.5].

Logaritmando se obtiene una recta: ln k = ln A − Ea/RT, de modo que representar ln k frente a 1/T da una línea de pendiente −Ea/R [@brown2012, sec. 14.5]. Pauling lo aplica a la reacción H₂ + I₂ → 2HI: la pendiente del gráfico, −21,6 en el eje de 1000/T, arroja Ea = 180 kJ/mol; como la transformación directa difiere de la inversa en 10 kJ/mol de entalpía, la reacción 2HI → H₂ + I₂ necesita 190 kJ/mol [@pauling1988, Example 16-8, sec. 16-4].

$$\ln k = \ln A - \frac{E_{a}}{RT}$$ {#eq-arrhenius-lineal}

En la ecuación @eq-arrhenius-lineal, ln A es la ordenada al origen, Ea/R la pendiente negativa y 1/T la abscisa; con dos puntos (k₁, T₁) y (k₂, T₂) se elimina ln A y queda ln(k₂/k₁) = (Ea/R)(1/T₁ − 1/T₂), forma de dos temperaturas muy usada para predecir constantes [@brown2012, sec. 14.5]. El ejercicio resuelto del texto determina así Ea = 160 kJ/mol para la isomerización del metilisocianuro y predice k = 2,2 × 10⁻² s⁻¹ a 280 °C [@brown2012, Sample Exercise 14.11 y Practice Exercise 14.11].

Las energías de activación obedecen a patrones empíricos razonables: en las reacciones exotérmicas con dos enlaces rotos, Ea ronda el 30% de la suma de las energías de los enlaces que se rompen, como en H₂ + I₂; cuando se rompe un enlace y se forma otro, Ea es del orden del 8% de la energía del enlace roto [@pauling1988, sec. 16-4]. Estas reglas solo aproximan; el camino seguro es el gráfico de Arrhenius [@brown2012, Sample Exercise 14.11].

El paso siguiente examina cómo se descompone una reacción global en etapas elementales y cómo la ley de velocidad delata la etapa lenta del mecanismo [@brown2012, sec. 14.6]. Con ello se conecta la constante medida con las moléculas que realmente chocan, y se prepara el terreno para entender la catálisis.

## Mecanismos de reacción

Un [**mecanismo de reacción**]{#sec-mecanismo-reaccion} es la secuencia de pasos elementales que conduce de los reactivos a los productos. La reacción NO₂ + CO → NO + CO₂ parece simple, pero su ley medida, rate = k[NO₂]², no contiene [CO]: en un solo paso debería ser k[NO₂][CO], de modo que el proceso transcurre forzosamente en dos etapas [@brown2012, sec. 14.6].

Cada [**reacción elemental**]{#sec-reaccion-elemental} es un paso individual en el que las moléculas se reorganizan directamente, y su [**molecularidad**]{#sec-molecularidad} es el número de moléculas que participan: una [**reacción unimolecular**]{#sec-reaccion-unimolecular}, dos una [**reacción bimolecular**]{#sec-reaccion-bimolecular} y tres una [**reacción termolecular**]{#sec-reaccion-termolecular}, esta última rara por exigir tres colisiones simultáneas [@brown2012, sec. 14.6]. El orden coincide con la molecularidad solo en las etapas elementales, no en la reacción global.

La ley de velocidad de una etapa elemental se escribe con las concentraciones de sus reactivos y exponentes iguales a la molecularidad: para O₃ → O₂ + O, rate = k[O₃]; para O₃ + Cl → ClO + O₂, rate = k[O₃][Cl]; para 2NO → N₂O₂, rate = k[NO]² [@brown2012, Sample Exercise 14.12].

Los productos de una etapa que se consumen en otra son **intermedio de reacción**: el átomo de oxígeno del ozono y el NO₃ del óxido de nitrógeno no figuran en las ecuaciones globales porque se forman y se gastan dentro del mecanismo [@brown2012, sec. 14.6]. A diferencia del estado de transición, efímero, los intermedios son especies con vida propia y detectable [@brown2012, sec. 14.6].

El ejemplo del NO₂ ilustra la jerarquía: el primer paso, NO₂ + NO₂ → NO₃ + NO, es lento y bimolecular; el segundo, NO₃ + CO → NO₂ + CO₂, es rápido. Como el paso lento consume casi todo el NO₂ disponible, la velocidad global queda gobernada por él, rate = k[NO₂]², y el CO, que solo participa en la etapa rápida, desaparece de la ley [@brown2012, sec. 14.6].

Esa etapa dominante es el [**paso determinante de la velocidad**]{#sec-paso-determinante-velocidad}: la reacción global no puede ser más rápida que su eslabón más lento, como una fila que avanza al ritmo de su puesto más lento [@brown2012, sec. 14.6]. Cuando el paso lento viene después de un equilibrio rápido, la concentración de su reactivo se introduce mediante la constante del equilibrio previo, y cuando conduce el primer paso, la ley predicha coincide con la medida.

La reacción H₂ + Br₂ → 2HBr exhibe la ley rate = k[H₂][Br₂]^1/2, imposible en un solo paso de cuatro moléculas. El mecanismo en cadena la explica: el Br₂ se disocia en dos átomos de bromo, un átomo de bromo arranca un hidrógeno del H₂ formando HBr y un átomo de hidrógeno, que a su vez reacciona con Br₂ regenerando el átomo de bromo; la cadena termina cuando dos átomos de bromo se recombinan [@pauling1988, sec. 16-7; @brown2012, Sample Exercise 14.13].

Esta propagación autosostenida es una [**reacción en cadena**]{#sec-reaccion-cadena}, concepto central en la cinética de las explosiones: la **explosión térmica** de H₂ + Cl₂ libera calor que acelera la propia reacción, mientras la **explosión de cadena ramificada** de H₂ + O₂ multiplica los portadores en cada paso y crece exponencialmente [@pauling1988, sec. 16-7]. La **combustión espontánea** de trapos impregnados de aceite ilustra el caso térmico: la oxidación lenta acumula calor y enciende sin llama externa [@pauling1988, sec. 16-7].

El mecanismo con equilibrio rápido previo se ve en 2NO + Br₂ → 2NOBr: el paso rápido NO + Br₂ ⇌ NOBr₂ establece la concentración del intermedio, y el paso lento NOBr₂ + NO → 2NOBr da rate = k₂(k₁/k₋₁)[NO]²[Br₂], que reproduce la ley experimental de tercer orden [@brown2012, sec. 14.6].

El análisis mecánico no es un lujo: explica los órdenes fraccionarios como el de H₂ + Br₂, por qué un reactivo puede brillar por su ausencia en la ley de velocidad y por qué los catalizadores abren caminos alternativos de menor barrera [@brown2012, sec. 14.6]. Con ello se llega a la catálisis, el último gran factor de la velocidad.

## Catálisis y enzimas {#sec-enzimas}

Un **catalizador** acelera una reacción sin sufrir un cambio neto: aparece entre los reactivos al comienzo y se regenera al final, de modo que no figura en la ecuación global [@brown2012, sec. 14.7]. Los caracteres chinos que forman la palabra catalizador describen a una casamentera, que une a los reactivos sin consumirse, y no existe un catalizador universal para todas las reacciones [@atkins2015, cap. 3].

La [**catálisis homogénea**]{#sec-catalisis-homogenea} ocurre cuando el catalizador comparte la fase con los reactivos: la descomposición del peróxido de hidrógeno, lentísima sin ayuda, es acelerada por el ion bromuro en medio ácido, que reacciona formando Br₂ acuoso; el Br₂ formado reacciona después con más H₂O₂ y regenera el Br⁻ [@brown2012, sec. 14.7]. El Br₂ es un intermedio de reacción, porque se forma durante el curso del proceso, mientras el Br⁻ es el catalizador, porque está presente desde el inicio [@brown2012, sec. 14.7].

El catalizador modifica el factor exponencial de la ecuación de Arrhenius: abre un mecanismo alternativo con menor energía de activación o mejora la orientación de las colisiones, y por eso pequeñas cantidades producen efectos enormes [@brown2012, sec. 14.7]. Pauling ilustra el principio con la producción industrial de tolueno desde el metilciclohexano, inviable comercialmente hasta hallar una mezcla de óxidos que acelerara la reacción; el catalizador interactúa sobre todo con el complejo activado y disminuye la barrera [@pauling1988, sec. 16-5].

La [**catálisis heterogénea**]{#sec-catalisis-heterogenea} emplea un catalizador sólido sobre el que se adsorben los reactivos gaseosos o líquidos: la adsorción los concentra y debilita sus enlaces, y los productos se desorben dejando la superficie libre [@brown2012, sec. 14.7]. La **hidrogenación** del etileno con níquel, paladio o platino y la descomposición del ácido fórmico sobre óxido de cinc pertenecen a esta clase de procesos [@brown2012, sec. 14.7].

La aplicación más visible es el **convertidor catalítico**: los gases de escape tocan el catalizador solo entre 100 y 400 ms, pero en ese lapso el 96% de los hidrocarburos y del monóxido de carbono se oxidan a CO₂ y H₂O, y las emisiones de óxidos de nitrógeno se reducen un 76% [@brown2012, sec. 14.7]. El dispositivo consume el 35% del platino, el 65% del paladio y el 95% del rodio usados anualmente en el mundo [@brown2012, sec. 14.7].

La naturaleza supera al laboratorio con las **enzimas**, proteínas de masa entre 10 000 y un millón de umas, selectivas hasta la especificidad absoluta: la catalasa de la sangre y el hígado descompone el H₂O₂ biológicamente nocivo en agua y oxígeno [@brown2012, sec. 14.7]. El [**número de recambio**]{#sec-numero-recambio} de un [**sitio activo**]{#sec-sitio-activo} oscila entre 10³ y 10⁷ eventos por segundo, y las enzimas multiplican la constante de velocidad de una reacción un millón de veces o más frente a un catalizador simple [@brown2012, sec. 14.7].

El [**sustrato**]{#sec-sustrato} se une al **sitio activo** por complementariedad de forma, el **modelo de llave y cerradura**: solo la llave correcta entra en la cerradura [@brown2012, sec. 14.7]. Las sustancias que bloquean ese encaje, como ciertos venenos nerviosos, el plomo y el mercurio, actúan como **inhibidor enzimático** y detienen la catálisis que el organismo necesita [@brown2012, sec. 14.7].

Pauling formaliza la cinética enzimática con la ecuación de Michaelis-Menten: la enzima E y el sustrato S se combinan en el [**complejo enzima-sustrato**]{#sec-complejo-enzima-sustrato} ES, que se descompone en producto o en E y S; cuando [S] es pequeña, la velocidad es proporcional a [S], y cuando [S] es grande, la enzima se satura y la velocidad tiende a un máximo [@pauling1988, sec. 16-6]. La curva de crecimiento de un mutante de Neurospora frente al ácido p-aminobenzoico reproduce esa forma de saturación [@pauling1988, sec. 16-6].

Muchas enzimas activas requieren dos piezas: la **apoenzima**, proteína sin actividad, y la **coenzima**, con frecuencia una vitamina; la cistationinuria, enfermedad por una apoenzima alterada, mejora con dosis de piridoxina, la vitamina B₆, de unas cien veces la ingesta diaria de 1 mg, que desplazan el equilibrio hacia la enzima activa [@pauling1988, sec. 16-6].

La **fijación de nitrógeno**, la conversión del N₂ atmosférico en compuestos asimilables por las plantas, corre por cuenta de la nitrogenasa, una **metaloenzima** de bacterias de las raíces de leguminosas cuyo cofactor FeMo contiene siete átomos de hierro y uno de molibdeno unidos por azufre [@brown2012, sec. 14.7]. Sin esa enzima, la vida como la conocemos no existiría [@brown2012, sec. 14.7].

El epílogo lo pone Atkins: la vida es la encarnación de la catálisis, pues cada reacción del metabolismo está afinada por enzimas que la aceleran sin desplazar el equilibrio [@atkins2015, cap. 3]. Este capítulo ha abierto la dinámica química; el capítulo 15 la cerrará formalmente con el equilibrio, del que la cinética es la antesala.

## Ejemplo resuelto: descomposición del ácido fórmico

El siguiente ejemplo integrador reúne la cinética de primer orden, la catálisis heterogénea, la estequiometría de gases y la termoquímica del capítulo 5. El ácido fórmico gaseoso se descompone según HCOOH(g) → CO₂(g) + H₂(g); a 838 K, la curva de presión parcial frente al tiempo muestra que la presión inicial de 3,00 × 10² torr se reduce a la mitad, 1,50 × 10² torr, a los 6,60 × 10² segundos [@brown2012, Sample Integrative Exercise].

A partir de la vida media se obtiene la constante de primer orden: k = 0,693/660 s = 1,05 × 10⁻³ s⁻¹ [@brown2012, Sample Integrative Exercise]. Representar la concentración en moles por litro, en lugar de la presión, no cambia el valor de k, porque sus unidades son s⁻¹ y la vida media es independiente de las unidades de concentración [@brown2012, Sample Integrative Exercise].

El óxido de cinc sólido acelera la descomposición: su superficie actúa como catalizador heterogéneo que rebaja la energía de activación [@brown2012, Sample Integrative Exercise]. La estequiometría produce dos moles de gas por cada mol de ácido, así que la presión final duplicará la inicial hasta 600 torr; con V = 436 cm³ y T = 838 K, la ecuación del gas ideal del capítulo 10 da n = PV/RT ≈ 5,0 × 10⁻³ mol de gas [@brown2012, Sample Integrative Exercise].

El calor estándar de formación del ácido fórmico gaseoso vale −378,6 kJ/mol; combinándolo con el del CO₂, −393,5 kJ/mol según el Apéndice C, el ΔH° de la reacción resulta −14,9 kJ/mol, exotérmico [@brown2012, Sample Integrative Exercise y Apéndice C]. Como la energía de activación vale 184 kJ/mol, el perfil de energía muestra una enorme cima asimétrica, con el estado de transición muy por encima de reactivos y productos, que la catálisis ayuda a rebajar [@brown2012, Sample Integrative Exercise].

## Preguntas y ejercicios

Los siguientes ejercicios, inspirados en la tipología de @brown2012 (2012), cap. 14 y @pauling1988 (1988), cap. 16, se resuelven aplicando únicamente los conceptos y datos desarrollados en este capítulo, con cambios de valores y de contextos respecto de las fuentes; el solucionario paso a paso aparece en la sección siguiente.

La descomposición del pentóxido de dinitrógeno, 2N₂O₅ → 4NO₂ + O₂, transcurre con desaparición del N₂O₅ a 2,4 × 10⁻⁴ M/s. Calcula las velocidades de aparición del NO₂ y del O₂ y verifica con la ecuación @eq-velocidad-estequiometrica que las tres describen la misma velocidad de reacción.

En la hidrólisis del C₄H₉Cl se registran las molaridades 0,100 a t = 0, 0,0640 a t = 100 s y 0,0450 a t = 200 s. Calcula la velocidad promedio en cada intervalo y explica por qué la velocidad instantánea a los 50 s es mayor que a los 150 s.

Para la reacción A + B → C se obtienen las velocidades iniciales 1,2 × 10⁻³ M/s con [A] = 0,30 M y [B] = 0,20 M; 2,4 × 10⁻³ M/s con [A] = 0,60 M y [B] = 0,20 M; y 4,8 × 10⁻³ M/s con [A] = 0,30 M y [B] = 0,40 M. Determina la ley de velocidad, el valor y las unidades de k, y la velocidad cuando [A] = 0,15 M y [B] = 0,10 M.

La reacción NH₄⁺(aq) + NO₂⁻(aq) → N₂(g) + 2H₂O(l) tiene k = 2,7 × 10⁻⁴ M⁻¹ s⁻¹ a cierta temperatura. Calcula la velocidad cuando [NH₄⁺] = 0,200 M y [NO₂⁻] = 0,300 M, y explica qué le ocurre a la velocidad si se duplica cada concentración por separado y si se duplican ambas a la vez.

Un insecticida se hidroliza en el suelo con k = 0,115 año⁻¹ siguiendo una cinética de primer orden. ¿Qué fracción del insecticida queda a los dos años y cuál es su vida media? Expresa el resultado como porcentaje de la cantidad inicial e interpreta los hallazgos con las ecuaciones @eq-primer-orden-integrada y @eq-vida-media-primer-orden.

El NO₂ se descompone a 300 °C con k = 0,543 M⁻¹ s⁻¹ y orden dos. Si [NO₂]₀ = 0,0800 M, calcula con la ecuación @eq-segundo-orden-integrada el tiempo necesario para que la concentración caiga hasta 0,0100 M, y compara esa semivida con la que tendría la reacción si fuera de primer orden con la misma k.

Una reacción de orden cero sobre una superficie metálica tiene k = 2,5 × 10⁻³ M/s y [A]₀ = 0,500 M. Calcula [A] a los 40 s y el tiempo de agotamiento total del reactivo, apoyándote en la ecuación @eq-orden-cero-integrada, y justifica por qué la velocidad no decae al consumirse el reactivo.

La isomerización del metilisocianuro tiene Ea = 160 kJ/mol y k = 5,1 × 10⁻⁵ s⁻¹ a 199 °C (472 K). Con la forma de dos temperaturas de la ecuación @eq-arrhenius-lineal, estima la constante de velocidad a 510 K y comenta por qué la constante aumenta con la temperatura.

Un mecanismo propuesto para 2NO + F₂ → 2NOF consta de las etapas 2NO → N₂O₂ (lenta, con constante k₁) y N₂O₂ + F₂ → 2NOF (rápida). Deduce la ley de velocidad global, identifica el intermedio y explica por qué la concentración de F₂ no aparece en la ley.

En la descomposición del H₂O₂ catalizada por Br⁻, el ion bromuro reacciona primero formando Br₂ acuoso y el Br₂ generado reacciona después con más H₂O₂, con balance total 2H₂O₂ → 2H₂O + O₂. Identifica el catalizador y el intermedio, justifica la distinción y explica con la ecuación @eq-arrhenius por qué el catalizador acelera la reacción.

## Solucionario

Para la primera pregunta, la estequiometría 2N₂O₅ → 4NO₂ + O₂ fija la velocidad común: dividiendo la desaparición del N₂O₅ entre el coeficiente dos, velocidad = 1,2 × 10⁻⁴ M/s; el NO₂ aparece cuatro veces más deprisa, a 4,8 × 10⁻⁴ M/s, y el O₂ a 1,2 × 10⁻⁴ M/s. La comprobación con la ecuación @eq-velocidad-estequiometrica: (1/2)(2,4 × 10⁻⁴) = (1/4)(4,8 × 10⁻⁴) = 1,2 × 10⁻⁴ M/s.

Para la segunda pregunta, la velocidad promedio entre 0 y 100 s es (0,100 − 0,0640)/100 = 3,6 × 10⁻⁴ M/s, y entre 100 y 200 s, (0,0640 − 0,0450)/100 = 1,9 × 10⁻⁴ M/s. La caída refleja que, con menos reactivo, las colisiones eficaces son menos frecuentes, y por eso la tangente a la curva en t = 50 s es más inclinada que la de t = 150 s.

Para la tercera pregunta, comparando el segundo experimento con el primero, al duplicar [A] con [B] fija la velocidad se duplica: primer orden en A; comparando el tercero con el primero, al duplicar [B] la velocidad se cuadruplica: segundo orden en B. Entonces k = 1,2 × 10⁻³/(0,30 × 0,040) = 0,10 M⁻² s⁻¹, y con [A] = 0,15 M y [B] = 0,10 M, velocidad = 0,10 × 0,15 × 0,010 = 1,5 × 10⁻⁴ M/s.

Para la cuarta pregunta, con la ley velocidad = k[NH₄⁺][NO₂⁻], se tiene velocidad = 2,7 × 10⁻⁴ × 0,200 × 0,300 = 1,62 × 10⁻⁵ ≈ 1,6 × 10⁻⁵ M/s. Duplicar [NH₄⁺] o [NO₂⁻] por separado duplica la velocidad, y duplicar ambas a la vez la cuadruplica, porque el producto de las dos concentraciones se multiplica por cuatro.

Para la quinta pregunta, de la ecuación @eq-primer-orden-integrada, fracción = e^(−0,115 × 2) = e^(−0,230) = 0,79, y de la ecuación @eq-vida-media-primer-orden, t½ = 0,693/0,115 = 6,0 años. La constancia de la semivida caracteriza al primer orden: en cada intervalo de seis años queda la mitad del insecticida, sin importar cuánto haya.

Para la sexta pregunta, de la ecuación @eq-segundo-orden-integrada, 1/0,0100 − 1/0,0800 = 87,5 M⁻¹ = kt, y con k = 0,543 M⁻¹ s⁻¹, t = 87,5/0,543 = 161 s. La semivida inicial del segundo orden, 1/(0,543 × 0,0800) = 23,0 s, es fija en el primer orden hipotético, pero crece en el segundo orden según la concentración cae, lo que distingue ambos casos.

Para la séptima pregunta, con orden cero, [A] = 0,500 − (2,5 × 10⁻³)(40) = 0,400 M, y el agotamiento ocurre cuando [A] = 0: t = 0,500/2,5 × 10⁻³ = 200 s. La velocidad constante se explica porque la superficie metálica permanece saturada de reactivo mientras quede gas, de modo que el número de moléculas que reaccionan por segundo no cambia.

Para la octava pregunta, con Ea/R = 160 000/8,314 = 1,92 × 10⁴ K, ln(k₂/5,1 × 10⁻⁵) = 1,92 × 10⁴ × (1/472 − 1/510) = 3,04; entonces k₂ = 5,1 × 10⁻⁵ × e³,⁰⁴ ≈ 1,1 × 10⁻³ s⁻¹. Subir la temperatura 38 grados multiplica la constante por veinte porque la fracción de colisiones que supera la barrera crece exponencialmente.

Para la novena pregunta, el primer paso, lento y bimolecular, determina la velocidad global: rate = k₁[NO]², y el F₂, que solo participa en la etapa rápida, no figura en la ley. El N₂O₂ es el intermedio, pues se forma en la primera etapa y se consume en la segunda sin aparecer en la ecuación global 2NO + F₂ → 2NOF.

Para la décima pregunta, el Br⁻ está presente desde el inicio y se regenera al final, de modo que es el catalizador; el Br₂ se forma y luego se consume, de modo que es el intermedio; ninguno figura en el balance global. Según la ecuación @eq-arrhenius, el catalizador abre un mecanismo con menor energía de activación, lo que aumenta exponencialmente k y con ella la velocidad, sin alterar la posición de equilibrio.

## Resumen

La cinética química estudia la velocidad de las reacciones y sus factores: estado físico, superficie de contacto, concentración, temperatura y catalizadores; las reacciones homogéneas transcurren en una sola fase y las heterogéneas en las interfaces [@brown2012, sec. 14.1; @pauling1988, sec. 16-1]. La velocidad instantánea se define con la estequiometría y se mide por presión, absorbancia u otros métodos [@brown2012, sec. 14.2].

La ley de velocidad rate = k[A]ᵐ[B]ⁿ resume la dependencia con la concentración; m, n y k son empíricos, y el orden global fija las unidades de k [@brown2012, sec. 14.3]. Las formas integradas y las vidas medias distinguen los órdenes: t½ = 0,693/k para el primer orden y t½ = 1/(k[A]₀) para el segundo [@brown2012, sec. 14.4].

La temperatura actúa a través de la fracción de Boltzmann, y la ecuación de Arrhenius, k = Ae^(−Ea/RT), con su forma lineal ln k = ln A − Ea/RT, permite medir la energía de activación desde pendientes o con dos temperaturas [@brown2012, sec. 14.5; @pauling1988, sec. 16-4]. Los mecanismos descomponen la reacción en etapas elementales con molecularidades y un paso determinante; los intermedios se forman y se consumen, y los órdenes fraccionarios denuncian mecanismos en cadena [@brown2012, sec. 14.6; @pauling1988, sec. 16-7].

Los catalizadores rebajan la energía de activación sin consumirse, en catálisis homogénea, heterogénea o enzimática; el convertidor catalítico, las enzimas con sus sitios activos y la nitrogenasa ilustran la escala del fenómeno [@brown2012, sec. 14.7]. La cinética confluye así con el equilibrio: las velocidades directa e inversa son las dos caras de una misma moneda dinámica.
