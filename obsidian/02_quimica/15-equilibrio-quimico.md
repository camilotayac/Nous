# Equilibrio químico

## Introducción

Las reacciones químicas estudiadas en los capítulos anteriores se presentaron, en general, como procesos que consumen por completo los reactivos. Sin embargo, la mayoría de las reacciones son reversibles: transcurren en ambos sentidos hasta alcanzar un estado que parece estático, pero que en realidad es dinámico [@brown2012, sec. 15.1]. Ese estado se denomina [**equilibrio químico**]{#sec-equilibrio-quimico}, y la disciplina que lo describe constituye el puente entre la cinética del capítulo 14 y la termodinámica del capítulo 18 [@brock2015, cap. 5].

En el equilibrio, las velocidades de las reacciones directa e inversa se igualan y las concentraciones de todas las especies permanecen constantes mientras no se alteren las condiciones externas [@brown2012, sec. 15.1]. Este capítulo desarrolla la ley de acción de masas, la constante de equilibrio, el cociente de reacción y el principio de Le Châtelier, culminando en el análisis del proceso Haber–Bosch, el ejemplo industrial más célebre de aplicación de estos conceptos [@pauling1988, cap. 11].

## La naturaleza dinámica del equilibrio

Cuando se colocan N₂ y H₂ en un recipiente cerrado, la reacción no consume todo el nitrógeno; al cabo del tiempo conviven los tres gases con concentraciones invariables [@brown2012, sec. 15.1]. La causa de esta aparente quietud es que las moléculas de amoníaco se descomponen a la misma velocidad con que se forman: el sistema está en equilibrio dinámico, no estático, porque los flujos opuestos continúan activos a nivel molecular [@atkins2015, cap. 3].

Los químicos del siglo XIX estudiaron estos sistemas mucho antes de que Fritz Haber los explotara industrialmente. En 1864, Cato Guldberg y Peter Waage postularon la **ley de acción de masas**, que relaciona las concentraciones de reactivos y productos en el equilibrio mediante una expresión que depende solo de la estequiometría de la reacción [@brown2012, sec. 15.2]. Esta ley se convirtió en la herramienta cuantitativa que gobierna todos los equilibrios, desde los acuosos hasta los industriales [@brock2015, cap. 5].

Un equilibrio solo se alcanza y sostiene en un sistema cerrado a temperatura constante [@brown2012, sec. 15.1]. Si el sistema pierde materia o cambia su temperatura, la constancia de concentraciones se rompe y el sistema evoluciona hacia un nuevo equilibrio [@chang2022, sec. 14.1]. Esta sensibilidad a las condiciones externas será la clave del principio de Le Châtelier, que se estudia más adelante en este capítulo [@pauling1988, sec. 11-8].

## La ley de acción de masas

Para la reacción general aA + bB ⇌ dD + eE, la ley de acción de masas define la [**constante de equilibrio**]{#sec-constante-equilibrio} Kc como el cociente de los productos de las concentraciones molares de productos y reactivos, cada una elevada a su coeficiente estequiométrico [@brown2012, sec. 15.2; @chang2022, p. 599]:

$$K_c = \frac{[D]^d [E]^e}{[A]^a [B]^b}$$ {#eq-ley-accion-masas}

En esta expresión, [A], [B], [D] y [E] son las concentraciones molares en el equilibrio de las especies A, B, D y E, respectivamente, y los exponentes a, b, d y e reproducen los coeficientes de la ecuación balanceada [@brown2012, sec. 15.2]. El corchete indica molaridad o presión parcial según el tipo de constante de que se trate, y la expresión resultante se evalúa únicamente en el estado de equilibrio [@chang2022, sec. 14.2].

Para el proceso de Haber, N₂(g) + 3H₂(g) ⇌ 2NH₃(g), la expresión toma la forma Kc = [NH₃]²/([N₂][H₂]³) [@brown2012, sec. 15.2]. La constante es adimensional en la práctica termodinámica porque cada concentración se interpreta como una actividad, es decir, un cociente de la concentración real entre el estado estándar de 1 M [@chang2022, p. 636]. Esta convención, que se detalla en la sección de actividades, permite comparar constantes entre sí sin fricciones de unidades [@pauling1988, sec. 11-5].

## La constante en términos de presiones parciales

Cuando todas las especies son gaseosas, resulta más cómodo expresar el equilibrio con presiones parciales en lugar de molaridades [@brown2012, sec. 15.2]. La **constante de equilibrio en presiones parciales (Kp)** se define con la misma forma algebraica que Kc, pero sustituyendo cada concentración por su presión parcial en atmósferas [@chang2022, sec. 14.2]:

$$K_p = K_c (RT)^{\Delta n}$$ {#eq-kp-kc}

Aquí, R es la constante de los gases cuyo valor debe elegirse en las unidades que igualen las de las presiones y temperaturas empleadas, T es la temperatura absoluta en kelvin y Δn = (d + e) − (a + b) es la diferencia entre los moles gaseosos de productos y reactivos de la ecuación balanceada [@chang2022, sec. 14.2]. Si Δn es cero, Kp y Kc coinciden numéricamente [@brown2012, sec. 15.2].

Para el proceso de Haber, Δn = 2 − 4 = −2, y la conversión exige dividir Kc por (RT)² [@brown2012, sec. 15.2]. A 573 K, un valor de Kp = 4.34 × 10⁻³ corresponde a Kc = 9.60, dato de la tabla 15.2 de Brown que se retomará en los ejercicios [@brown2012, sec. 15.2]. La relación entre ambas constantes solo es válida para gases ideales, hipótesis razonable a presiones moderadas [@chang2022, sec. 14.2].

## Equilibrios homogéneos y heterogéneos

Un [**equilibrio homogéneo**]{#sec-equilibrio-homogeneo} es aquel en el que todas las especies reactivas se encuentran en la misma fase, como ocurre con las disoluciones acuosas o las mezclas gaseosas [@brown2012, sec. 15.4]. En cambio, un [**equilibrio heterogéneo**]{#sec-equilibrio-heterogeneo} involucra sustancias en más de una fase, como la descomposición del carbonato de calcio, CaCO₃(s) ⇌ CaO(s) + CO₂(g) [@chang2022, p. 639].

La expresión de la constante para equilibrios heterogéneos omite los sólidos y líquidos puros porque su concentración es constante e independiente de la cantidad presente [@brown2012, sec. 15.4]. Para la descomposición del carbonato de calcio, la constante se reduce a Kc = [CO₂] [@chang2022, pp. 639-640]. Este resultado explica que, a temperatura fija, la presión de CO₂ en equilibrio con el sólido no dependa de cuánto CaCO₃ haya: esa [**presión de disociación**]{#sec-presion-disociacion} característica, medida en atmósferas, es una propiedad del compuesto a la temperatura dada [@pauling1988, sec. 11-7].

## Actividades y el estado estándar

La termodinámica formal expresa la constante de equilibrio en términos de [**actividad**]{#sec-actividad}, una magnitud adimensional que mide la concentración o presión de cada especie relativa a su estado estándar [@chang2022, p. 636]. Para solutos, la actividad es la razón entre la molaridad real y el estado estándar de 1 M; para gases, la razón entre la presión parcial y el estado estándar de 1 atm [@chang2022, p. 636].

La actividad de un sólido o líquido puro es exactamente 1, razón por la cual estas fases desaparecen de la expresión de la constante [@chang2022, p. 639]. Aunque en los cálculos elementales se usan molaridades y atmósferas sin cocientes explícitos, esta convención justifica que las constantes se traten como números sin unidades, práctica difundida en los textos modernos [@brown2012, sec. 15.2]. La adopción de actividades permite además combinar reacciones y manipular constantes sin ambigüedad dimensional.

## La magnitud de la constante y la posición del equilibrio

La magnitud de la constante definida por la ley de acción de masas (@eq-ley-accion-masas) indica la **posición del equilibrio**, es decir, el lado de la ecuación que predomina en la mezcla final [@brown2012, sec. 15.3]. Una constante muy grande, como K ≈ 10⁹ para la formación de fosgeno, COCl₂ ⇌ CO + Cl₂, señala que el equilibrio «se encuentra a la derecha»: los productos dominan [@brown2012, sec. 15.3]. Una constante muy pequeña, en cambio, indica que el equilibrio se encuentra a la izquierda, con los reactivos casi intactos [@chang2022, sec. 14.2].

Conviene no confundir velocidad con posición: un valor extremo de K no dice nada sobre la rapidez con que se alcanza el equilibrio [@brown2012, sec. 15.3]. Así, la reacción del hidrógeno con el oxígeno tiene una constante enorme y, sin embargo, no transcurre en condiciones ordinarias por su elevada barrera de activación [@atkins2015, cap. 3]. La cinética del capítulo 14 y la posición de equilibrio son propiedades independientes del mismo sistema [@atkins2015, cap. 3].

## La manipulación algebraica de las constantes

Las constantes de equilibrio obedecen tres reglas algebraicas que facilitan el trabajo con reacciones combinadas [@brown2012, sec. 15.2]. Si se invierte una ecuación, la nueva constante es el recíproco de la original; si se multiplica la ecuación por un factor n, la constante se eleva a la potencia n [@chang2022, sec. 14.2]. Estas reglas se deducen directamente de la estructura de la expresión de la ley de acción de masas.

Para el equilibrio 2NO₂ ⇌ N₂O₄, con Kc = 4.63 × 10⁻³ a 25 °C, la reacción inversa N₂O₄ ⇌ 2NO₂ tiene constante 1/4.63 × 10⁻³ = 216, y la ecuación a la mitad, NO₂ ⇌ ½ N₂O₄, presenta constante √(4.63 × 10⁻³) = 0.0680 [@chang2022, sec. 14.2]. La tercera regla se aplica a los **equilibrios múltiples**: si una reacción es suma de otras dos, su constante es el producto de las constantes parciales [@chang2022, sec. 14.2]. El ácido carbónico, H₂CO₃, ilustra este caso en su disociación diprótica, cuya constante global se compone de las dos etapas sucesivas [@chang2022, sec. 14.2].

## Constante de equilibrio y cinética

El equilibrio dinámico admite una interpretación cinética directa: en el equilibrio, la velocidad directa y la inversa se igualan, de modo que Kc resulta ser el cociente de las constantes de velocidad, Kc = kf/kr [@brown2012, sec. 15.2]. Esta igualdad deriva de igualar las velocidades de avance y retroceso escritas con sus leyes de velocidad [@chang2022, sec. 14.2].

Para el equilibrio N₂O₄ ⇌ 2NO₂, con Kc = 0.212 y kr = 4.72 × kf, el cociente confirma el valor de la constante [@brown2012, sec. 15.2]. La relación kf/kr explica también por qué un catalizador, que acelera por igual ambos sentidos al reducir la energía de activación, no altera la posición de equilibrio [@chang2022, sec. 14.2]. Solo los cambios de temperatura modifican kf y kr de forma distinta, y con ello el valor de K, cuestión que se retoma con la ecuación de van't Hoff [@brown2012, sec. 15.2].

## El cociente de reacción y la dirección del cambio

Antes de alcanzar el equilibrio, los valores instantáneos de las concentraciones definen el [**cociente de reacción**]{#sec-cociente-reaccion} Qc, expresión de la misma forma que la constante de equilibrio pero evaluada en cualquier momento del proceso y no únicamente en el equilibrio [@brown2012, sec. 15.6]. Su utilidad práctica reside en compararlo con la constante para anticipar hacia dónde evolucionará el sistema antes de que ocurra ningún cambio observable [@chang2022, sec. 14.4].

$$Q_c = \frac{[D]^d [E]^e}{[A]^a [B]^b}$$ {#eq-cociente-reaccion}

La comparación de Qc con Kc dictamina el sentido del cambio espontáneo [@brown2012, sec. 15.6]. Si Qc < Kc, el cociente debe crecer y la reacción avanza hacia los productos; si Qc > Kc, el sistema se desplaza hacia los reactivos; si Qc = Kc, el sistema está en equilibrio [@chang2022, sec. 14.4]. Esta regla funciona también con presiones parciales usando Qp y Kp [@brown2012, sec. 15.6].

En la reacción del capítulo 15 de Brown, N₂ + 3H₂ ⇌ 2NH₃ a 472 °C con Kp = 2.79 × 10⁻⁵, si las presiones iniciales son 14.76, 4.92 y 0.332 atm para H₂, N₂ y NH₃, el cociente supera a la constante y la mezcla debe desplazarse hacia los reactivos [@brown2012, sec. 15.7]. El cálculo del cociente evita, por tanto, experimentar a ciegas: predice la dirección antes de que ocurra cualquier cambio [@chang2022, sec. 14.4].

## El método de la tabla de equilibrio

El cálculo de K a partir de concentraciones de equilibrio, o de concentraciones desconocidas a partir de K, se organiza con el [**método de la tabla de equilibrio (ICE)**]{#sec-metodo-ice}, cuyas siglas provienen de initial, change y equilibrium [@chang2022, sec. 14.4]. La tabla registra las concentraciones iniciales, el cambio estequiométrico x y las concentraciones finales expresadas en términos de x [@chang2022, sec. 14.4].

En la síntesis del ioduro de hidrógeno, H₂ + I₂ ⇌ 2HI, si se parte de 1.000 × 10⁻³ M de H₂ y 2.000 × 10⁻³ M de I₂, el cambio de concentración x resta de ambos reactivos y suma 2x al producto [@brown2012, sec. 15.5]. La concentración final de HI, medida experimentalmente como 1.87 × 10⁻³ M, fija x = 9.35 × 10⁻⁴ M y permite despejar las concentraciones restantes [@brown2012, sec. 15.5]. Este problema completo se resuelve en el ejemplo resuelto del capítulo [@brown2012, sec. 15.5].

Cuando la constante es pequeña y x resulta mucho menor que las concentraciones iniciales, la aproximación x despreciable simplifica la ecuación cuadrática [@chang2022, sec. 14.4]. La regla práctica acepta la aproximación si x es inferior a un 5 % de la concentración inicial, criterio que se verifica siempre después de calcular x [@chang2022, sec. 14.4].

## Cálculo de concentraciones en equilibrio

Conocida la constante, el método de la tabla permite predecir las concentraciones de equilibrio a partir de las iniciales [@brown2012, sec. 15.6]. La estrategia general consiste en plantear la expresión de K con las concentraciones finales en función de x, resolver la ecuación resultante y comprobar que la solución es físicamente admisible [@chang2022, sec. 14.4].

Cuando K es moderada, la ecuación es cuadrática y se elige la raíz positiva que mantiene todas las concentraciones positivas [@brown2012, sec. 15.6]. En la descomposición del pentacloruro de fósforo, PCl₅ ⇌ PCl₃ + Cl₂, la aplicación de este procedimiento a 250 °C, donde Kp = 1.05, produce una raíz razonable y otra descartable [@chang2022, sec. 14.2]. Las presiones parciales se resuelven de forma análoga trabajando con presiones en lugar de molaridades [@brown2012, sec. 15.6].

## El principio de Le Châtelier

El [**principio de Le Châtelier**]{#sec-principio-le-chatelier} resume la respuesta de un sistema en equilibrio ante cualquier [**perturbación del equilibrio**]{#sec-perturbacion-equilibrio}, entendida como un cambio externo de concentración, presión o temperatura: el sistema se desplaza en el sentido que tiende a contrarrestar el cambio impuesto [@brown2012, sec. 15.7]. Formulado por Henri Le Châtelier en 1884, este principio centraliza cualitativamente todos los efectos de concentración, presión y temperatura [@chang2022, sec. 14.5].

Cuando se añade un reactivo a una mezcla en equilibrio, el sistema consume parte del exceso desplazándose hacia los productos; cuando se retira un producto, el avance compensa la pérdida [@brown2012, sec. 15.7]. Este comportamiento explica, por ejemplo, que la remoción continua de amoníaco en el proceso industrial de Haber arrastre la reacción casi hasta la derecha [@brown2012, sec. 15.7]. Cada perturbación redefine los valores del cociente de reacción (@eq-cociente-reaccion), dejando intacta la constante mientras la temperatura no cambie [@chang2022, sec. 14.5].

## Efectos de la presión y el volumen

La compresión de un sistema gaseoso en equilibrio aumenta todas las presiones parciales y favorece el lado de la ecuación con menor número de moles gaseosos [@brown2012, sec. 15.7]. En la síntesis de amoníaco, donde cuatro moles gaseosos se convierten en dos, el aumento de presión desplaza el equilibrio hacia el amoníaco, y por eso el proceso emplea presiones de 200 a 600 atm [@brown2012, sec. 15.7]. La expansión produce el efecto opuesto [@chang2022, sec. 14.5].

Si la ecuación presenta el mismo número de moles gaseosos a ambos lados, la presión no altera la posición de equilibrio [@pauling1988, sec. 11-8; @brown2012, sec. 15.7]. La adición de un gas inerte a volumen constante tampoco cambia las presiones parciales de los reactivos y, por tanto, no perturba el equilibrio [@brown2012, sec. 15.7; @chang2022, sec. 14.5]. Todos estos efectos dejan la constante de equilibrio inalterada (@eq-ley-accion-masas): solo modifican las presiones parciales de las especies [@brown2012, sec. 15.7].

## El efecto de la temperatura y la ecuación de van't Hoff

La temperatura es la única variable que modifica el valor de la constante de equilibrio [@brown2012, sec. 15.7]. Para una reacción exotérmica, el calor puede considerarse producto: calentar desplaza el equilibrio hacia los reactivos y reduce K; para una endotérmica ocurre lo contrario [@chang2022, sec. 14.5]. En el equilibrio N₂F₄(g) ⇌ 2NF₂(g), con ΔH° = +38.5 kJ/mol, el calor aparece como reactivo y, al calentar, el sistema se desplaza hacia la derecha [@chang2022, sec. 14.5].

La dependencia cuantitativa de la constante con la temperatura la proporciona la [**ecuación de van't Hoff**]{#sec-ecuacion-vant-hoff}, una relación logarítmica que liga los valores de K a dos temperaturas con la entalpía de reacción, y cuya deducción se apoyará en la termodinámica que se formaliza en el capítulo 18 [@pauling1988, sec. 11-6]:

$$\ln \frac{K_2}{K_1} = -\frac{\Delta H^\circ}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$ {#eq-vant-hoff-equilibrio}

En la ecuación de van't Hoff (@eq-vant-hoff-equilibrio), K₁ y K₂ son las constantes de equilibrio a las temperaturas absolutas T₁ y T₂, ΔH° es la entalpía estándar de reacción y R es la constante de los gases en las unidades coherentes con la energía [@pauling1988, sec. 11-6]. Para el proceso de Haber, ΔH° = −107.3 kJ/mol a 800 K, y la ecuación predice que K disminuye al elevar la temperatura, en concordancia con los valores de la tabla 15.2 de Brown [@pauling1988, sec. 11-6].

## Catalizadores y equilibrio

Un catalizador acelera por igual las reacciones directa e inversa, de modo que reduce el tiempo necesario para alcanzar el equilibrio sin alterar su posición [@brown2012, sec. 15.7]. La constante K y las concentraciones finales permanecen idénticas; solo cambia la velocidad de llegada [@chang2022, sec. 14.5]. Esta propiedad distingue nítidamente el efecto catalítico del efecto térmico [@atkins2015, cap. 3].

La ausencia de efecto sobre el equilibrio no resta importancia al catalizador: sin él, muchas reacciones favorables serían impracticables por su lentitud [@brown2012, sec. 15.7]. En la síntesis industrial de amoníaco, el hierro con óxidos metálicos desarrollado por Carl Bosch hace posible una velocidad aceptable a 400-500 °C, temperatura a la que el equilibrio aún conserva un rendimiento útil [@brown2012, sec. 15.7]. La patente de un «catalizador superior» que prometiera mayor conversión en equilibrio sería rechazable por definición [@brown2012, sec. 15.7].

## El proceso Haber–Bosch

El **proceso de Haber**, desarrollado por Fritz Haber en 1912 y escalado industrialmente por Carl Bosch, fija el nitrógeno atmosférico como amoníaco mediante la reacción N₂(g) + 3H₂(g) ⇌ 2NH₃(g) [@brown2012, sec. 15.2]. Las condiciones industriales combinan unos 500 °C y presiones de 200 a 600 atm sobre un catalizador de hierro [@brown2012, sec. 15.2]. El amoníaco se retira continuamente por licuefacción a −33 °C, punto de ebullición muy superior a los del nitrógeno y el hidrógeno, y los gases restantes se reciclan [@brown2012, sec. 15.7].

Para el equilibrio gaseoso con K en atmósferas recíprocas, Pauling calcula que a 500 °C una mezcla estequiométrica produce 0.25 % de amoníaco a 1 atm y 46.6 % a 500 atm [@pauling1988, sec. 11-5]. La observación industrial confirma la lección del principio de Le Châtelier: el alto rendimiento exige alta presión, y la alta temperatura, que perjudica a K, se tolera solo para mantener una velocidad viable [@atkins2015, cap. 3]. Esta tensión entre posición y velocidad ilustra el arte de la química industrial [@atkins2015, cap. 3].

## Ejemplo resuelto: cálculo de la constante con la tabla de equilibrio

Se colocan 1.000 × 10⁻³ mol de H₂ y 2.000 × 10⁻³ mol de I₂ en un matraz de 1.000 L a 448 °C [@brown2012, sec. 15.5]. Al alcanzar el equilibrio, la concentración de HI medida es 1.87 × 10⁻³ M [@brown2012, sec. 15.5]. Se pide calcular Kc para la reacción H₂(g) + I₂(g) ⇌ 2HI(g) [@brown2012, sec. 15.5].

La tabla de equilibrio registra concentraciones iniciales 1.000 × 10⁻³ y 2.000 × 10⁻³ M para H₂ e I₂, cambios de −x y −x, y un cambio de +2x para el HI, cuyos valores finales quedan en función de x [@brown2012, sec. 15.5]. Como el HI final mide 1.87 × 10⁻³ M = 2x, se obtiene x = 9.35 × 10⁻⁴ M [@brown2012, sec. 15.5]. Las concentraciones finales de los reactivos son, por tanto, 1.000 × 10⁻³ − 9.35 × 10⁻⁴ = 6.5 × 10⁻⁵ M y 2.000 × 10⁻³ − 9.35 × 10⁻⁴ = 1.065 × 10⁻³ M [@brown2012, sec. 15.5].

La sustitución en la expresión de la constante produce Kc = (1.87 × 10⁻³)² / ((6.5 × 10⁻⁵)(1.065 × 10⁻³)) [@brown2012, sec. 15.5]. El numerador vale 3.4969 × 10⁻⁶ y el denominador 6.9225 × 10⁻⁸, de modo que Kc = 50.5 [@brown2012, sec. 15.5]. La constante se reporta como 51, valor consistente con la magnitud esperada para esta reacción a 448 °C [@brown2012, sec. 15.5]. La comprobación confirma además que ambas concentraciones finales son positivas y que el equilibrio favorece moderadamente a los productos [@chang2022, sec. 14.4].

## Preguntas y ejercicios

Los ejercicios de este capítulo, inspirados en @brown2012 (2012), cap. 15; @chang2022 (2022), cap. 14; @pauling1988 (1988), cap. 11, combinan la escritura de expresiones de equilibrio, la conversión entre Kc y Kp, el cálculo con tablas de equilibrio, la comparación del cociente de reacción con la constante y las predicciones cualitativas del principio de Le Châtelier.

Primer ejercicio: escribe la expresión de Kc para la combustión del amoníaco, 4NH₃(g) + 5O₂(g) ⇌ 4NO(g) + 6H₂O(g), construye después la expresión equivalente de Kp con presiones parciales e indica el valor de Δn que permite convertir una constante en la otra [@brown2012, sec. 15.2].

Segundo ejercicio: para el proceso de Haber, N₂(g) + 3H₂(g) ⇌ 2NH₃(g), cuya constante Kc vale 9.60 a 573 K, convierte la constante a Kp usando R = 0.08206 L·atm/(mol·K) y compara el resultado numérico con el valor reportado en la tabla 15.2 de Brown [@brown2012, sec. 15.2].

Tercer ejercicio: en un matraz de 1.00 L a 448 °C se mezclan H₂ e I₂ con concentraciones iniciales 2.00 × 10⁻³ y 4.00 × 10⁻³ M, y en el equilibrio se encuentra [HI] = 3.00 × 10⁻³ M [@brown2012, sec. 15.5]. Calcula Kc para H₂ + I₂ ⇌ 2HI [@brown2012, sec. 15.5].

Cuarto ejercicio: a 250 °C, la descomposición PCl₅(g) ⇌ PCl₃(g) + Cl₂(g) tiene Kp = 1.05 [@chang2022, sec. 14.4]. Una mezcla con presiones parciales 0.200, 0.300 y 0.100 atm de PCl₅, PCl₃ y Cl₂ no está en equilibrio [@chang2022, sec. 14.4]. Calcula el cociente de reacción y predice la dirección del cambio [@chang2022, sec. 14.4].

Quinto ejercicio: el sulfuro de amonio, NH₄HS(s), se descompone según NH₄HS(s) ⇌ NH₃(g) + H₂S(g) [@chang2022, sec. 14.2]. En un recipiente cerrado que contiene solo el sólido al inicio, la presión total en el equilibrio es 0.500 atm [@chang2022, sec. 14.2]. Determina Kp del equilibrio heterogéneo, razonando por qué las presiones parciales de los dos gases deben ser iguales [@brown2012, sec. 15.2].

Sexto ejercicio: en la reacción 2NO(g) ⇌ N₂(g) + O₂(g), cuya constante Kc vale 2.4 × 10³, se parte de una concentración inicial de NO de 0.175 M [@brown2012, sec. 15.6]. Construye la tabla de equilibrio, resuelve la ecuación para x y calcula la concentración final de NO, comprobando que la raíz elegida deja concentraciones positivas [@brown2012, sec. 15.6].

Séptimo ejercicio: para la reacción exotérmica 4NH₃(g) + 5O₂(g) ⇌ 4NO(g) + 6H₂O(g) con ΔH° = −904.4 kJ [@brown2012, sec. 15.7], predice el sentido del desplazamiento al añadir O₂, al aumentar la temperatura, al aumentar el volumen del recipiente y al añadir un catalizador [@brown2012, sec. 15.7].

Octavo ejercicio: la tabla 15.2 de Brown reporta Kp = 4.34 × 10⁻³ a 300 °C y Kp = 4.51 × 10⁻⁵ a 450 °C para el proceso de Haber [@brown2012, sec. 15.7]. Explica qué revelan estos valores sobre el signo de ΔH° y sobre la conveniencia de operar a baja temperatura [@brown2012, sec. 15.7].

Noveno ejercicio: para el equilibrio 2NO₂(g) ⇌ N₂O₄(g), Kc = 4.63 × 10⁻³ a 25 °C [@chang2022, p. 632]. Escribe las constantes de la reacción inversa N₂O₄ ⇌ 2NO₂ y de la reacción a la mitad NO₂ ⇌ ½ N₂O₄, aplicando las reglas de inversión y potencias [@chang2022, sec. 14.2].

Décimo ejercicio: el óxido de plata se descompone según 2Ag₂O(s) ⇌ 4Ag(s) + O₂(g) [@pauling1988, sec. 11-7]. A 400 °C, la presión de oxígeno en equilibrio es 0.145 atm, y a 426 °C, 0.21 atm [@pauling1988, sec. 11-7]. Establece si la plata expuesta al aire a 400 °C se oxida o se mantiene metálica, sabiendo que el aire contiene 0.21 atm de O₂ [@pauling1988, sec. 11-7].

## Solucionario

Primer ejercicio: la expresión de Kc es [NO]⁴[H₂O]⁶/([NH₃]⁴[O₂]⁵), y la de Kp reemplaza cada corchete por su presión parcial [@brown2012, sec. 15.2]. Como los moles gaseosos de productos suman 10 y los de reactivos 9, Δn = 1 y Kp = Kc(RT) [@chang2022, sec. 14.2].

Segundo ejercicio: con Δn = −2, la relación de conversión (@eq-kp-kc) da Kp = 9.60 × (0.08206 × 573)⁻² [@chang2022, sec. 14.2]. El producto RT vale 47.02, su cuadrado 2211, y el cociente 9.60/2211 = 4.34 × 10⁻³ [@brown2012, sec. 15.2]. El resultado coincide con el valor tabulado, validando la conversión [@brown2012, sec. 15.2].

Tercer ejercicio: la tabla da [HI] = 2x = 3.00 × 10⁻³, de modo que x = 1.50 × 10⁻³ M [@brown2012, sec. 15.5]. Las concentraciones finales de H₂ e I₂ son 2.00 × 10⁻³ − 1.50 × 10⁻³ = 5.0 × 10⁻⁴ M y 4.00 × 10⁻³ − 1.50 × 10⁻³ = 2.50 × 10⁻³ M [@brown2012, sec. 15.5]. La constante resulta (3.00 × 10⁻³)² / ((5.0 × 10⁻⁴)(2.50 × 10⁻³)) = 9.00 × 10⁻⁶ / 1.25 × 10⁻⁶ = 7.2 [@brown2012, sec. 15.5].

Cuarto ejercicio: el cociente de reacción vale Qp = (0.300)(0.100)/(0.200) = 0.15 [@chang2022, sec. 14.4]. Como 0.15 < 1.05, el cociente debe crecer y la reacción avanza hacia los productos hasta que Qp iguale a Kp [@chang2022, sec. 14.4]. El desplazamiento neto aumenta las presiones de PCl₃ y Cl₂ a costa de la de PCl₅ [@chang2022, sec. 14.4].

Quinto ejercicio: al descomponerse el sólido, cada mol de NH₃ va acompañado de un mol de H₂S, de modo que sus presiones parciales son iguales [@chang2022, sec. 14.2]. Con presión total 0.500 atm, cada gas aporta 0.250 atm [@chang2022, sec. 14.2]. La constante vale Kp = (0.250)(0.250) = 0.0625 [@chang2022, sec. 14.2].

Sexto ejercicio: la tabla de equilibrio registra NO inicial 0.175, cambio −2x, y N₂ y O₂ de 0 a x [@brown2012, sec. 15.6]. La expresión Kc = x²/(0.175 − 2x)² = 2.4 × 10³, al tomar raíz cuadrada, da x/(0.175 − 2x) = 48.99 [@brown2012, sec. 15.6]. Resolviendo, x = 8.586 − 97.98x, de donde 98.98x = 8.586 y x = 8.66 × 10⁻² M [@brown2012, sec. 15.6]. La concentración final de NO es 0.175 − 0.1732 = 1.8 × 10⁻³ M [@brown2012, sec. 15.6].

Séptimo ejercicio: añadir O₂ desplaza el equilibrio hacia la derecha, consumiendo el exceso de reactivo [@brown2012, sec. 15.7]. Al ser la reacción exotérmica, calentar favorece los reactivos y desplaza el equilibrio hacia la izquierda [@brown2012, sec. 15.7]. Aumentar el volumen favorece el lado con más moles gaseosos, que aquí es el de los productos (10 frente a 9), de modo que la expansión desplaza el equilibrio hacia la derecha [@brown2012, sec. 15.7]. El catalizador, por su parte, no altera la posición del equilibrio [@chang2022, sec. 14.5].

Octavo ejercicio: al elevar la temperatura de 300 a 450 °C, Kp cae de 4.34 × 10⁻³ a 4.51 × 10⁻⁵, un factor de cien [@brown2012, sec. 15.7]. Como el calor disminuye la constante, la reacción es exotérmica y ΔH° es negativo [@brown2012, sec. 15.7]. La baja temperatura favorece el rendimiento, pero exige un catalizador para que la velocidad siga siendo viable [@brown2012, sec. 15.7].

Noveno ejercicio: la inversión da K = 1/4.63 × 10⁻³ = 216 [@chang2022, sec. 14.2]. Multiplicar la ecuación por un medio eleva la constante a ½, de modo que K′ = √(4.63 × 10⁻³) = 0.0680 [@chang2022, sec. 14.2]. Las tres formulaciones describen el mismo sistema y sus constantes se relacionan por estas reglas [@chang2022, sec. 14.2].

Décimo ejercicio: la constante del equilibrio heterogéneo es Kp = P(O₂), sin participación de los sólidos [@pauling1988, sec. 11-7]. A 400 °C, la presión de disociación es 0.145 atm, inferior a los 0.21 atm del aire [@pauling1988, sec. 11-7]. El cociente de reacción Q = 0.21 supera a K = 0.145, de modo que la reacción avanza hacia la izquierda y la plata se oxida a 400 °C; solo por encima de 426 °C la presión de disociación iguala la del aire y el óxido se descompone [@pauling1988, sec. 11-7].

## Resumen

El equilibrio químico es un estado dinámico en el que las velocidades directa e inversa se igualan y las concentraciones permanecen constantes [@brown2012, sec. 15.1]. La ley de acción de masas define la constante de equilibrio Kc como el cociente de concentraciones elevadas a sus coeficientes estequiométricos, y Kp la reexpresa con presiones parciales mediante la relación Kp = Kc(RT)^Δn [@brown2012, sec. 15.2; @chang2022, sec. 14.2].

La magnitud de K señala la posición del equilibrio, y las reglas de inversión, potencias y combinación permiten manipular constantes de reacciones relacionadas [@brown2012, sec. 15.2-15.3]. El cociente de reacción Q compara el estado instantáneo con el equilibrio y dictamina la dirección del cambio [@brown2012, sec. 15.6]. El método de la tabla de equilibrio organiza los cálculos de concentraciones y constantes [@chang2022, sec. 14.4].

El principio de Le Châtelier predice el efecto de concentración, presión y temperatura: solo la temperatura modifica el valor de K, según la ecuación de van't Hoff [@brown2012, sec. 15.7]. Los catalizadores aceleran la llegada sin mover la posición [@chang2022, sec. 14.5]. El proceso Haber–Bosch integra todas estas ideas en la producción industrial de amoníaco [@brown2012, sec. 15.7].
