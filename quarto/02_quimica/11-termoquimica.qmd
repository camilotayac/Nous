# Termoquímica

## Introducción

El capítulo anterior mostró que la temperatura de un gas mide la energía cinética media de sus moléculas, pero no explicó cómo fluye esa energía de un cuerpo a otro ni cómo la aprovechan las reacciones químicas. Este capítulo estudia esos intercambios, que gobiernan desde la combustión del metano en un hornillo hasta el metabolismo de una barra de cereales.

La **termodinámica** (del griego *thérme*, "calor", y *dýnamis*, "potencia") nació durante la Revolución Industrial, cuando físicos e ingenieros quisieron conocer la eficiencia de las máquinas de vapor y de los motores eléctricos que dominaban el mundo industrializado [@brown2012, sec. 5.1; @brock2015, cap. 5]. La rama que examina los cambios de energía que acompañan a las reacciones químicas se llama **termoquímica** [@brown2012, sec. 5.1].

La termoquímica empezó antes que la termodinámica formal: en el siglo XVIII el escocés Joseph Black estudió los calores específicos y latentes y mostró que cada sustancia absorbe calor de manera distinta, y que fundir un sólido o hervir un líquido exige calor sin que el termómetro registre cambio [@brock2015, cap. 5].

De esas observaciones nace la pregunta central del capítulo: ¿cuánto calor libera o consume una reacción química y cómo se mide? La respuesta exige precisar primero qué son la energía, el trabajo y el calor, y definir luego las magnitudes que permiten predecir balances energéticos a presión constante [@brown2012, sec. 5.1].

## La naturaleza de la energía

La [**energía**]{#sec-energia-calor} se define comúnmente como la capacidad de realizar trabajo o transferir calor, lo que obliga a precisar ambos conceptos [@brown2012, sec. 5.1]. El **trabajo** es la energía empleada para mover un objeto contra una fuerza, y el **calor** es la energía transferida de un objeto más caliente a otro más frío [@brown2012, sec. 5.1]. Con la excepción de la luz solar, casi toda la energía de la vida diaria proviene de reacciones químicas, desde la combustión de la gasolina hasta las baterías [@brown2012, sec. 5.1].

Tanto las pelotas de béisbol como las moléculas poseen **energía cinética**, la energía del movimiento, cuya magnitud depende de la masa y de la rapidez del objeto [@brown2012, sec. 5.1]. Un camión grande avanza a 55 millas por hora con más energía que un sedán a la misma velocidad, y en química interesan los átomos y moléculas invisibles que nunca dejan de moverse [@brown2012, sec. 5.1].

$$E_k = \tfrac{1}{2} m v^2$$ {#eq-energia-cinetica}

En la ecuación @eq-energia-cinetica, $E_k$ es la energía cinética en joules, $m$ la masa en kilogramos y $v$ la rapidez en metros por segundo, de modo que un objeto de dos kilogramos a un metro por segundo posee exactamente un joule [@brown2012, sec. 5.1]. Como la rapidez aparece al cuadrado, duplicar la velocidad cuadruplica la energía, mientras que duplicar la masa solo la duplica [@brown2012, sec. 5.1].

Todas las demás formas de energía, como la almacenada en un resorte estirado, en un peso suspendido o en un enlace químico, son **energía potencial**, la energía que un objeto posee por su posición relativa a otros objetos [@brown2012, sec. 5.1]. En química domina la energía potencial electrostática, que crece con el producto de las cargas y decrece con la distancia, como se estudió en el capítulo 8 [@brown2012, sec. 5.1].

Una ciclista en la cima de una colina convierte su energía potencial en cinética al descender: la primera disminuye mientras la segunda crece [@brown2012, sec. 5.1]. También las sustancias almacenan energía química en la disposición de sus átomos, y esa energía se libera al reaccionar, mientras que la energía térmica de un cuerpo se asocia al movimiento molecular [@brown2012, sec. 5.1].

La unidad SI de energía es el **joule** (J), en honor de James Joule, el científico británico que investigó el trabajo y el calor en Manchester entre 1840 y 1878 [@brown2012, sec. 5.1; @pauling1988, sec. 10-1]. Un joule equivale a un kilogramo por metro cuadrado por segundo al cuadrado, y como resulta pequeño para la química se emplean kilojoules en las reacciones [@brown2012, sec. 5.1].

La unidad tradicional sigue viva: la **caloría** (cal) se definió originalmente como la energía para elevar de 14,5 a 15,5 grados la temperatura de un gramo de agua, y hoy se define exactamente como 4,184 J [@brown2012, sec. 5.1]. En nutrición se usa la Caloría con mayúscula, que equivale a mil calorías pequeñas, es decir, a una kilocaloría [@brown2012, sec. 5.1].

Que un gramo de agua exija justamente esa energía fue establecido por Joule tras los experimentos del conde Rumford, quien en 1798 calentó un cañón por fricción con un taladro romo [@pauling1988, sec. 10-1]. La fricción convierte el movimiento ordenado en movimiento molecular aleatorio, y ese aumento de temperatura es el calor [@pauling1988, sec. 10-1].

## Sistema, entorno y transferencia de energía

Para estudiar los cambios de energía hay que aislar una porción limitada del universo, llamada **sistema**, mientras que todo lo demás constituye el **entorno** [@brown2012, sec. 5.1; @pauling1988, sec. 10-1]. En una reacción de laboratorio los reactivos y productos forman el sistema, y el recipiente con cuanto lo rodea conforma el entorno [@brown2012, sec. 5.1].

Los sistemas se clasifican por lo que intercambian con su entorno: un **sistema abierto** intercambia materia y energía, como una olla destapada que hierve; un **sistema cerrado** intercambia energía pero no materia, como la mezcla de hidrógeno y oxígeno en un cilindro con pistón; y un **sistema aislado** no intercambia ni una ni otra, como un termo que intenta conservar el café caliente [@brown2012, sec. 5.1].

La energía se transfiere entre sistema y entorno de dos maneras generales: como trabajo o como calor [@brown2012, sec. 5.1]. El trabajo realizado al mover un objeto es el producto de la fuerza por la distancia recorrida, como al levantar una bola de boliche, y el calor fluye del sistema caliente al entorno frío tras una combustión [@brown2012, sec. 5.1].

En física se distingue además el trabajo útil del rozamiento, que disipa el movimiento dirigido en movimiento molecular aleatorio y produce el aumento de temperatura que asociamos con el calor [@pauling1988, sec. 10-1]. Esa distinción será clave para entender por qué la entalpía, y no la energía interna, se mide con facilidad a presión constante [@brown2012, sec. 5.3].

## La primera ley de la termodinámica

El estudio cuantitativo de estos intercambios se apoya en una observación central: la energía no se crea ni se destruye, sino que se transforma o se transfiere, y cualquier energía que pierde el sistema la gana el entorno [@brown2012, sec. 5.2]. Esa conservación es la **primera ley de la termodinámica**, una de las observaciones más importantes de la ciencia [@brown2012, sec. 5.2].

Para aplicarla cuantitativamente se define la **energía interna**, E, como la suma de todas las energías cinéticas y potenciales de los componentes del sistema, incluidas las interacciones de núcleos y electrones [@brown2012, sec. 5.2]. No conocemos el valor absoluto de E, pero la termodinámica solo necesita el cambio ΔE entre el estado inicial y el final [@brown2012, sec. 5.2].

$$\Delta E = q + w$$ {#eq-primera-ley}

En la ecuación @eq-primera-ley, $q$ es el calor transferido al sistema o desde él y $w$ el trabajo realizado sobre el sistema o por él, ambos en joules y con signo que indica la dirección [@brown2012, sec. 5.2]. Cuando el sistema gana calor y recibe trabajo, q y w son positivos, como depósitos en una cuenta bancaria de energía; cuando pierde calor y realiza trabajo, ambos son negativos, como retiros [@brown2012, sec. 5.2].

Un proceso en el que el sistema absorbe calor se llama **proceso endotérmico**, como la fusión del hielo que enfría el recipiente, y un proceso en el que el sistema cede calor se llama **proceso exotérmico**, como la combustión de la gasolina [@brown2012, sec. 5.2]. En la reacción 2 H₂(g) + O₂(g) → 2 H₂O(l) el sistema pierde energía, ΔE es negativo y los productos poseen menos energía interna que los reactivos [@brown2012, sec. 5.2].

La energía interna es una **función de estado**: una propiedad determinada por el estado presente del sistema, no por el camino para alcanzarlo [@brown2012, sec. 5.2]. Cincuenta gramos de agua a 25 °C tienen la misma energía interna vengan de enfriar agua a 100 °C o de fundir hielo y calentarlo [@brown2012, sec. 5.2]. Subir de Chicago, a 596 pies, hasta Denver, a 5280 pies, cambia la altitud en 4684 pies sea cual sea la ruta, pero la distancia recorrida depende del camino [@brown2012, sec. 5.2].

Por eso q y w no son funciones de estado, aunque su suma ΔE sí lo sea [@brown2012, sec. 5.2]. Una pila descargada por un cable corto pierde toda su energía como calor, pero la misma pila moviendo un motor la pierde como trabajo y solo parte como calor; las magnitudes de q y w difieren entre caminos, aunque su suma es idéntica porque ΔE depende solo de los estados inicial y final [@brown2012, sec. 5.2].

El tricloruro de nitrógeno lo cuantifica: al descomponerse dos moles de NCl₃ líquido, ΔE vale exactamente −451,9 kJ tanto si la reacción ocurre en una ampolla sin trabajo como si mueve un motor del 43 por ciento de eficiencia, que entrega 194,3 kJ de trabajo y 257,6 kJ de calor [@pauling1988, sec. 10-2]. La energía interna cambia igual, aunque el reparto entre calor y trabajo sea distinto [@pauling1988, sec. 10-2].

## Entalpía y trabajo presión-volumen

Casi todas las reacciones transcurren a presión atmosférica constante, en recipientes abiertos donde el único trabajo relevante es el de expansión o compresión de gases, llamado **trabajo presión-volumen** [@brown2012, sec. 5.3]. Cuando el cinc reacciona con ácido clorhídrico en un aparato con pistón, el hidrógeno que se forma levanta el pistón contra la atmósfera y el sistema realiza trabajo sobre el entorno [@brown2012, sec. 5.3].

$$w = -P \Delta V$$ {#eq-trabajo-pv}

En la ecuación @eq-trabajo-pv, $w$ es el trabajo presión-volumen en joules, $P$ la presión externa constante en pascales y $\Delta V$ el cambio de volumen en metros cúbicos, positivo si los gases se expanden y negativo si se comprimen [@brown2012, sec. 5.3]. Un gas que se expande realiza trabajo sobre el entorno, así que w resulta negativo, mientras que comprimirlo exige trabajo del entorno y w resulta positivo [@brown2012, sec. 5.3].

La descomposición lenta de dos moles de NCl₃ en un cilindro con pistón, a una atmósfera y 25 °C, produce un volumen adicional de 97,852 litros, lo que equivale a un trabajo de 9,91 kJ contra la atmósfera [@pauling1988, sec. 10-2]. Esa corrección presión-volumen separa el calor medido en una bomba del calor medido a presión constante [@pauling1988, sec. 10-2].

Trabajar a presión constante invita a combinar las tres funciones de estado E, P y V en una nueva llamada [**entalpía**]{#sec-entalpia} (del griego *enthalpein*, "calentar"), definida como la energía interna más el producto de la presión por el volumen [@brown2012, sec. 5.3]. El vocablo fue acuñado en 1909 por Kamerlingh Onnes, aunque no se generalizó en la literatura química hasta los años cincuenta, y la tradición histórica liga el símbolo H a la ley de Hess, cuya vigencia se comprueba más adelante [@brock2015, cap. 5].

$$H = E + PV$$ {#eq-entalpia}

En la ecuación @eq-entalpia, $H$ es la entalpía en joules o kilojoules, $E$ la energía interna, $P$ la presión y $V$ el volumen del sistema [@brown2012, sec. 5.3]. Como E, P y V son funciones de estado, la entalpía también lo es, y su utilidad aparece en procesos a presión constante donde solo se realiza trabajo presión-volumen [@brown2012, sec. 5.3].

Sustituyendo la primera ley y el trabajo presión-volumen se obtiene el resultado central de esta sección: a presión constante y con solo trabajo presión-volumen, el cambio de entalpía vale ΔE más el término PΔV, lo que coincide exactamente con el calor qP ganado o perdido por el sistema [@brown2012, sec. 5.3].

$$\Delta H = \Delta E + P\Delta V = q_P$$ {#eq-deltaH-qp}

En la ecuación @eq-deltaH-qp, $\Delta H$ es el cambio de entalpía a presión constante, $\Delta E$ el cambio de energía interna, $P$ la presión constante y $\Delta V$ el cambio de volumen, de modo que el producto $P\Delta V$ es el trabajo presión-volumen [@brown2012, sec. 5.3]. Cuando ΔH es positivo el sistema ha ganado calor y el proceso es endotérmico; cuando es negativo lo ha cedido y el proceso es exotérmico [@brown2012, sec. 5.3].

## Entalpías de reacción

El acierto de usar la entalpía en lugar de la energía fue reconocido por el científico estadounidense J. Willard Gibbs en sus estudios teóricos de 1876 y 1878, que fundaron la termodinámica química [@pauling1988, sec. 10-2]. En la reacción H₂(g) + ½O₂(g) → H₂O(l) a 25 °C y 1 atm, el ΔH vale −285,840 kJ por mol, mientras que el ΔE vale −282,123 kJ, y la diferencia de 3,7 kJ corresponde a la disminución de volumen de los gases [@pauling1988, sec. 10-2].

La **entalpía de reacción**, también llamada calor de reacción y abreviada ΔH_rxn, es la entalpía de los productos menos la entalpía de los reactivos [@brown2012, sec. 5.4]. Al quemar 2 moles de H₂(g) para formar 2 moles de H₂O(g) a presión constante, el sistema libera 483,6 kJ, y esa información se resume en una **ecuación termoquímica** que muestra el valor de ΔH al final de la ecuación balanceada [@brown2012, sec. 5.4].

Los coeficientes de una ecuación termoquímica representan los moles que producen el cambio de entalpía asociado, y el signo negativo indica el carácter exotérmico, visible en un diagrama en el que los reactivos quedan por encima de los productos [@brown2012, sec. 5.4]. Las ecuaciones obedecen además tres reglas sencillas que se usarán durante todo el capítulo [@brown2012, sec. 5.4].

La primera regla dice que la entalpía es una propiedad extensiva: la magnitud de ΔH es proporcional a la cantidad de reactivo consumido, de modo que quemar un mol de CH₄ libera 890 kJ y quemar dos moles libera 1780 kJ [@brown2012, sec. 5.4]. La segunda, que el cambio de entalpía tiene igual magnitud pero signo opuesto al de la reacción inversa: formar CH₄ a partir de CO₂ y H₂O absorbe 890 kJ [@brown2012, sec. 5.4].

La tercera regla dice que el cambio de entalpía depende de los estados físicos de reactivos y productos: si el producto fuera H₂O(g) en lugar de H₂O(l), el ΔH de la combustión del metano pasaría de −890 a −802 kJ, y la conversión de dos moles de agua líquida en vapor absorbe 88 kJ a 25 °C [@brown2012, sec. 5.4]. Las ecuaciones termoquímicas deben, pues, especificar los estados de agregación [@brown2012, sec. 5.4].

Esa cifra de 88 kJ merece un contraste con las fuentes: Pauling reporta que el calor necesario para vaporizar un mol de agua en su punto de ebullición vale 40,6 kJ, lo que daría unos 81 kJ para dos moles [@pauling1988, sec. 10-3]. La diferencia entre 88 y 81 kJ se explica porque el calor requerido depende de la temperatura y es mayor a 25 °C que a 100 °C, de modo que ambas fuentes son correctas en sus condiciones [@brown2012, sec. 5.4].

La reacción del hidrógeno con el oxígeno es tan exotérmica y rápida que puede estallar, como demostraron el incendio del dirigible Hindenburg en Lakehurst en 1937 y el transbordador Challenger en 1986 [@brown2012, sec. 5.4]. Su violencia recuerda que la termoquímica no predice la rapidez de una reacción, solo su balance energético [@brown2012, sec. 5.4].

Atkins advierte además de los límites de una regla práctica: la energía liberada al formarse enlaces nuevos debe superar a la invertida en romper los antiguos, y el balance, no una simple caída de energía, decide si una combustión produce calor [@atkins2015, cap. 3]. La misma cautela vale para la espontaneidad: el hielo se funde a temperatura ambiente aunque el proceso sea endotérmico, y solo la entropía lo explicará en el capítulo 18 [@brown2012, sec. 5.4; @atkins2015, cap. 3].

## Calorimetría: capacidad calorífica y calor específico

La **calorimetría** mide el flujo de calor que acompaña a una reacción observando el cambio de temperatura que produce, y el aparato usado para ello es el **calorímetro** [@brown2012, sec. 5.5]. Todos los objetos se calientan al ganar calor, pero la magnitud del cambio varía de una sustancia a otra, y esa variación se cuantifica con la capacidad calorífica [@brown2012, sec. 5.5].

La **capacidad calorífica**, C, es el calor requerido para elevar la temperatura de un objeto en 1 K, y cuanto mayor es, más calor hace falta para producir un aumento dado [@brown2012, sec. 5.5]. Para sustancias puras se reporta por cantidad fija de materia, lo que permite comparar materiales distintos con una métrica común [@brown2012, sec. 5.5].

La cantidad de calor por mol se llama **capacidad calorífica molar** y la cantidad por gramo se llama **calor específico** [@brown2012, sec. 5.5]. El agua destaca por su altísimo valor de 4,18 J por gramo y kelvin, que estabiliza la temperatura de los océanos y que sirvió para definir la caloría [@brown2012, sec. 5.5]. Se requieren por ejemplo 209 J para elevar un kelvin la temperatura de 50,0 g de agua [@brown2012, sec. 5.5].

$$q = C_s \cdot m \cdot \Delta T$$ {#eq-q-calor}

En la ecuación @eq-q-calor, $q$ es el calor ganado o perdido por la muestra en joules, $C_s$ su calor específico en joules por gramo y kelvin, $m$ su masa en gramos y $\Delta T$ el cambio de temperatura, cuya magnitud coincide en kelvin y grados Celsius [@brown2012, sec. 5.5]. Se necesitan 79 kJ para calentar 250 g de agua de 22 a 98 °C, y la capacidad calorífica molar del agua vale 75,3 J por mol y kelvin [@brown2012, sec. 5.5].

Sobre estas medidas se construyeron regularidades históricas: la **regla de Dulong y Petit** (1819) afirma que para los elementos sólidos pesados el producto del calor específico por el peso atómico ronda 26 J por mol y grado, unos 6,4 cal, y Berzelius la usó para determinar pesos atómicos [@pauling1988, sec. 10-3; @brock2015, cap. 5].

La **regla de Kopp** extiende el espíritu regular al punto de ebullición: en las series homólogas orgánicas, una diferencia de n grupos CH₂ corresponde a unos n·19 °C, n carbonos a n·29 °C, y la adición de hidrógenos baja el punto de ebullición cerca de 5 °C por átomo [@brock2015, cap. 5].

## Calorimetría a presión constante y a volumen constante

Cuando la reacción ocurre en disolución a presión atmosférica esencialmente constante, el calorímetro de vaso de café mide directamente ΔH [@brown2012, sec. 5.5]. Los reactivos y productos forman el sistema, el agua de la disolución forma parte del entorno, y al suponer el calorímetro aislado, el calor que gana o pierde la disolución es igual en magnitud y opuesto en signo al de la reacción [@brown2012, sec. 5.5].

Una reacción exotérmica eleva la temperatura de la disolución y una endotérmica la disminuye [@brown2012, sec. 5.5]. Al mezclar 50 mL de HCl 1,0 M con 50 mL de NaOH 1,0 M, la temperatura sube de 21,0 a 27,5 °C, y el balance, con 100 g de disolución y 0,050 mol de HCl, conduce a una entalpía de neutralización cercana a −54 kJ por mol de HCl [@brown2012, Sample Exercise 5.6].

Para las reacciones de combustión se usa el **calorímetro de bomba**, un recipiente sellado que soporta altas presiones, se llena de oxígeno y se sumerge en agua medida con precisión [@brown2012, sec. 5.5]. La muestra se enciende con una corriente eléctrica y el calor liberado lo absorben el agua y el resto del calorímetro, cuyo calor total se determina con una sustancia patrón: un gramo de ácido benzoico libera 26,38 kJ, y si eleva la temperatura 4,857 °C, la capacidad calorífica del aparato vale 5,431 kJ/°C [@brown2012, sec. 5.5].

$$q_{rxn} = -C_{cal}\,\Delta T$$ {#eq-bomba}

En la ecuación @eq-bomba, $q_{rxn}$ es el calor que libera la reacción en kilojoules, $C_{cal}$ la capacidad calorífica total del calorímetro en kilojoules por grado y $\Delta T$ el aumento de temperatura en grados, positivo para una combustión exotérmica [@brown2012, sec. 5.5]. El signo negativo expresa que el calor liberado por la reacción es absorbido por el calorímetro, que se calienta [@brown2012, sec. 5.5].

Como la bomba mantiene el volumen constante, el calor transferido corresponde a ΔE, no a ΔH, aunque la diferencia suele ser pequeña: para la metilhidracina ronda 1 kJ por mol, menos del 0,1 por ciento [@brown2012, sec. 5.5]. Al quemar 4,00 g en una bomba de capacidad 7,794 kJ/°C, la temperatura sube de 25,00 a 39,50 °C y el cálculo revela cerca de −1,30 × 10³ kJ por mol [@brown2012, Sample Exercise 5.7].

El contraste entre ΔE y ΔH se hace visible cuando cambia mucho el número de moles gaseosos, como en la descomposición del NCl₃, donde la corrección presión-volumen alcanza 9,91 kJ [@pauling1988, sec. 10-2]. Por eso los valores tabulados de entalpía se corrigen a partir de medidas de bomba [@brown2012, sec. 5.5].

## La ley de Hess

No siempre hace falta medir cada reacción, porque la entalpía es una función de estado y el cambio de entalpía de un proceso es el mismo se realice en un solo paso o en una serie de ellos [@brown2012, sec. 5.6]. El químico Germain Hess mostró entre 1838 y 1840 que el calor desprendido es constante ocurra la reacción en uno o en varios pasos, y esa regularidad se conoce como **ley de Hess**, una de las muchas reglas epónimas de la química [@brock2015, cap. 5].

Cuando los físicos enunciaron la primera ley de la termodinámica quedó claro que la ley de Hess no era sino una consecuencia de que la energía no puede crearse ni destruirse [@brock2015, cap. 5]. La ley convierte un pequeño número de mediciones experimentales en la puerta de entrada a un número enorme de reacciones [@brown2012, sec. 5.6].

La combustión del metano ilustra el principio: un solo paso de CH₄(g) a CO₂(g) y H₂O(l) libera 890 kJ, y el mismo proceso en dos pasos, la combustión a H₂O(g) con −802 kJ seguida de la condensación del vapor con −88 kJ, suma exactamente −890 kJ [@brown2012, sec. 5.6]. Un diagrama de entalpía muestra que el cambio del camino directo iguala siempre la suma de los pasos [@brown2012, sec. 5.6].

Un caso célebre de utilidad es la combustión del carbono a monóxido de carbono, imposible de medir directamente porque el carbono reacciona de forma incompleta con medio mol de O₂ [@brown2012, sec. 5.6]. Quemando el carbono a CO₂ se liberan 393,5 kJ por mol, y quemando el CO a CO₂, 283,0 kJ por mol; restando ambas, la formación de CO libera 110,5 kJ por mol [@brown2012, Sample Exercise 5.8].

El mismo método explica por qué el grafito es más estable que el diamante: sus combustiones liberan 393,5 y 395,4 kJ por mol respectivamente, de modo que la conversión de grafito en diamante absorbe 1,9 kJ por mol [@brown2012, Practice Exercise 5.8]. La forma de menor entalpía, el grafito, es la estable a presión ambiente [@brown2012, Practice Exercise 5.8].

## Entalpías de formación

Las tablas termoquímicas se organizan en torno a un proceso particular: la formación de un compuesto a partir de sus elementos constituyentes, cuyo cambio de entalpía se llama [**entalpía de formación**]{#sec-entalpias-formacion-reaccion} [@brown2012, sec. 5.7]. Para comparar valores hace falta fijar un **estado estándar**, la forma pura de la sustancia a presión de una atmósfera y a la temperatura de interés, habitualmente 298 K [@brown2012, sec. 5.7].

La **entalpía estándar de formación**, ΔH°f, es el cambio de entalpía de la reacción que forma un mol de compuesto a partir de sus elementos, todos en sus estados estándar [@brown2012, sec. 5.7]. La fuente de oxígeno es O₂ y no O ni O₃, la de carbono es el grafito y no el diamante, y la de hidrógeno es H₂ gaseoso, porque esas son las formas más estables a 298 K y 1 atm [@brown2012, sec. 5.7].

Por definición, la entalpía estándar de formación de la forma más estable de cualquier elemento es cero, ya que no se necesita ninguna reacción de formación [@brown2012, sec. 5.7]. Con esos ceros como referencia, las tablas asignan a cada compuesto un valor que resume su estabilidad relativa [@brown2012, sec. 5.7].

$$\Delta H^\circ_{rxn} = \sum n\,\Delta H^\circ_f(\text{productos}) - \sum m\,\Delta H^\circ_f(\text{reactivos})$$ {#eq-deltaH-rxn}

En la ecuación @eq-deltaH-rxn, la sigma mayúscula indica la suma sobre todos los productos y reactivos, $n$ y $m$ son los coeficientes estequiométricos de cada sustancia en la ecuación balanceada, y cada término multiplica la entalpía estándar de formación correspondiente, cuyo resultado es la **entalpía estándar de reacción** [@brown2012, sec. 5.7]. Los productos aparecen en el sentido directo de sus reacciones de formación y suman, mientras que los reactivos son la inversa de las suyas y restan [@brown2012, sec. 5.7].

La combustión de un mol de propano, C₃H₈(g) con cinco moles de O₂ para dar tres de CO₂ y cuatro de H₂O(l), se descompone en la descomposición del propano, la formación de tres moles de CO₂ y la de cuatro moles de H₂O líquida [@brown2012, sec. 5.7]. Sumando los valores tabulados con sus coeficientes, el ΔH° de la reacción vale −2220 kJ, y dividiendo entre la masa molar, el propano rinde −50,3 kJ por gramo [@brown2012, sec. 5.7; @brown2012, Sample Exercise 5.11].

La misma fórmula aplicada al benceno líquido, C₆H₆, conduce a un ΔH° de −3267 kJ por mol, lo que supone −41,8 kJ por gramo [@brown2012, Sample Exercise 5.11]. Entre los dos hidrocarburos se encierra una regla general: quemar un gramo de hidrocarburo rinde entre 40 y 50 kJ [@brown2012, Sample Exercise 5.11].

## Alimentos y combustibles

El **valor combustible** de una sustancia es la energía liberada al quemar un gramo de ella, medible por calorimetría [@brown2012, sec. 5.8]. El cuerpo obtiene su energía de los carbohidratos y las grasas, y el balance de la combustión es el mismo en la bomba y en el organismo: los carbohidratos rinden 17 kJ por gramo y las grasas 38 kJ por gramo, más energéticas por unidad de masa e insolubles en agua, lo que facilita su almacenamiento [@brown2012, sec. 5.8].

Las proteínas producen el mismo valor de 17 kJ por gramo que los carbohidratos cuando se metabolizan, aunque en la bomba liberan más porque su nitrógeno acaba en el cuerpo como urea y no como N₂ [@brown2012, sec. 5.8]. El cuerpo humano requiere cerca de 100 kJ por kilogramo de masa al día para funcionar al mínimo, y una persona de 70 kg gasta unos 800 kJ por hora en trabajo ligero [@brown2012, sec. 5.8].

Los combustibles más usados del mundo son los [**combustibles fósiles**]{#sec-combustibles}, limitados y consumidos mucho más deprisa de lo que se regeneran [@brown2012, sec. 5.8]. El **gas natural** es una mezcla de hidrocarburos gaseosos con predominio del metano, el **petróleo** es un líquido con cientos de compuestos, en su mayoría hidrocarburos, y el **carbón** un sólido de hidrocarburos de alto peso molecular, el más abundante, con reservas para más de cien años al ritmo actual [@brown2012, sec. 5.8].

El azufre del carbón se convierte en dióxido de azufre al quemarse, un contaminante problemático, y su extracción y transporte encarecen su uso [@brown2012, sec. 5.8]. Frente a ellos, las **energías renovables**, como la solar, la eólica, la geotérmica, la hidroeléctrica y la biomasa, son prácticamente inagotables y aportaban cerca del 7,4 por ciento del consumo anual estadounidense [@brown2012, sec. 5.8].

En un día despejado llega a cada metro cuadrado de la superficie terrestre cerca de 1 kJ de energía solar por segundo, y la energía que cae sobre el 0,1 por ciento del territorio de Estados Unidos bastaría para el consumo nacional [@brown2012, sec. 5.8]. Una vía prometedora para almacenarla es una reacción endotérmica que puede invertirse después para liberar calor [@brown2012, sec. 5.8].

El **biocombustible** más común es el bioetanol, fermentado de los carbohidratos vegetales, con un valor combustible de unas dos terceras partes del de la gasolina, comparable al del carbón [@brown2012, sec. 5.8]. Estados Unidos y Brasil dominan su producción y juntos suministran el 85 por ciento mundial [@brown2012, sec. 5.8].

El retorno energético del maíz es modesto: por cada joule invertido en cultivarlo se obtienen 1,34 J de etanol, un rendimiento del 34 por ciento, mientras que la caña de azúcar brasileña devuelve 8,0 J por cada joule invertido [@brown2012, sec. 5.8]. El debate entre alimento y combustible explica por qué la investigación se orienta hacia el etanol celulósico de pastos de crecimiento rápido [@brown2012, sec. 5.8].

## Ejemplo resuelto: el campamento y el hornillo de metano

Una persona acampa y desea calentar 500 g de agua desde 20,0 hasta 100,0 °C con un hornillo que quema metano, cuya combustión libera 890 kJ por mol a presión constante [@brown2012, sec. 5.4]. El problema integra las dos herramientas del capítulo, el calor específico y la estequiometría energética, y muestra por qué el metano es tan eficiente como combustible doméstico [@brown2012, Sample Exercise 5.4].

Primero se calcula la energía necesaria con la ecuación @eq-q-calor, donde q vale el producto de 500 g por 4,18 J/g·K por 80,0 K, lo que da 167 200 J, es decir, 167 kJ [@brown2012, sec. 5.5]. El agua exige esa cantidad aunque el recipiente sea solo una olla, porque la ecuación del calor específico no distingue aparatos [@brown2012, sec. 5.5].

Como cada mol de metano libera 890 kJ, hacen falta 167 dividido entre 890, es decir, 0,188 mol de CH₄, y con una masa molar de 16,0 g/mol eso equivale a 3,01 g de combustible [@brown2012, sec. 5.4]. Algo más de tres gramos de gas bastan para llevar medio litro de agua a la ebullición [@brown2012, Sample Exercise 5.4].

La moraleja es doble: la pequeña masa de combustible basta para un cambio térmico grande, y el balance se resuelve siempre encadenando gramos a moles y moles a kilojoules [@brown2012, Sample Exercise 5.4]. El mismo encadenamiento, con las ecuaciones de los ejercicios siguientes, sirve para alimentos, propano y cualquier reacción cuya entalpía se conozca [@brown2012, sec. 5.8].

## Preguntas y ejercicios

Los siguientes ejercicios, inspirados en la tipología de @brown2012 (2012), cap. 5 y @pauling1988 (1988), cap. 10, se resuelven aplicando únicamente los conceptos y datos desarrollados en este capítulo, y su solucionario aparece en la sección siguiente con cada respuesta desarrollada paso a paso en prosa.

Convierta a kilojoules la energía aportada por una barra energética cuyo envase declara 620 Cal (unidad nutricional que equivale a kilocalorías), y calcule luego qué masa de agua a 25,0 °C podría llevarse hasta 100,0 °C con esa energía, aplicando el calor específico del agua y suponiendo que no hay pérdidas hacia el entorno [@brown2012, sec. 5.1; @brown2012, sec. 5.5].

Calcule el calor necesario para elevar la temperatura de 750 g de agua desde 15,0 hasta 90,0 °C empleando el calor específico de 4,18 J por gramo y kelvin, expréselo en kilojoules y en kilocalorías, e interprete el resultado comparándolo con la energía que aporta una comida típica [@brown2012, sec. 5.5; @brown2012, sec. 5.8].

Determine la temperatura final de equilibrio cuando se mezclan en un vaso aislado 400 g de agua a 85,0 °C con 150 g de agua a 18,0 °C, planteando la igualdad entre el calor cedido por la porción caliente y el absorbido por la fría, y suponiendo que el calorímetro no intercambia calor con el exterior [@brown2012, sec. 5.5].

En un calorímetro de vaso de café, la mezcla de 50 mL de HCl 0,80 M con 50 mL de NaOH 0,80 M eleva la temperatura de 21,5 a 26,1 °C; calcule la entalpía de neutralización por mol de HCl, suponiendo una disolución de 100 g y el calor específico del agua [@brown2012, Sample Exercise 5.6].

Una muestra de 1,20 g de un compuesto de masa molar 60,0 g/mol se quema en un calorímetro de bomba cuya capacidad calorífica total es 5,43 kJ/°C, y la temperatura del conjunto sube 2,90 °C; calcule el calor de combustión por gramo y por mol de muestra [@brown2012, sec. 5.5].

Usando la ley de Hess con las combustiones conocidas del carbono, que libera 393,5 kJ por mol al formar CO₂, y del monóxido de carbono, que libera 283,0 kJ al oxidarse a CO₂, calcule el cambio de entalpía de la reacción C(grafito) + ½O₂(g) → CO(g) [@brown2012, Sample Exercise 5.8].

Las combustiones del grafito y del diamante liberan 393,5 y 395,4 kJ por mol respectivamente; determine con ellas el cambio de entalpía de la conversión C(grafito) → C(diamante), indique cuál de las dos formas es la estable y justifique su respuesta con el signo obtenido [@brown2012, Practice Exercise 5.8].

Calcule los gramos de propano necesarios para liberar exactamente 1,00 × 10³ kJ de calor al quemarse, sabiendo que su combustión rinde −50,3 kJ por gramo de combustible, y exprese el resultado con tres cifras significativas, comentando brevemente con una frase la cantidad obtenida [@brown2012, Sample Exercise 5.11].

Una barra de granola contiene 4 g de proteína, 22 g de carbohidratos y 6 g de grasa; estime su valor combustible total en kilojoules y en kilocalorías usando los valores promedio de 17, 17 y 38 kJ por gramo para cada componente, respectivamente, en el orden enumerado [@brown2012, sec. 5.8].

## Solucionario

La primera pregunta convierte la unidad nutricional en energía mecánica: 620 Cal equivalen a 620 000 cal, y multiplicando por 4,184 J/cal se obtienen 2,59 × 10⁶ J, es decir, 2,59 × 10³ kJ [@brown2012, sec. 5.1]. Con @eq-q-calor y un salto de 75,0 K para el agua, la masa resulta 2 593 000 J dividido entre 313,5 J/g, lo que da 8270 g, cerca de 8,3 kg de agua hervida con una sola barra [@brown2012, sec. 5.5].

La segunda pregunta aplica la misma ecuación a 750 g con un salto de 75,0 K: q = 750 × 4,18 × 75,0 = 235 125 J, es decir, 235 kJ [@brown2012, sec. 5.5]. Dividiendo entre 4,184 se obtienen 56,2 kcal, y el resultado muestra la equivalencia entre las escalas de energía [@brown2012, sec. 5.1].

Para la mezcla de aguas, el calor cedido por la porción caliente iguala al absorbido por la fría, y la temperatura final es el promedio ponderado por las masas: (400 × 85,0 + 150 × 18,0) dividido entre 550, lo que da 66,7 °C [@brown2012, sec. 5.5]. El calor específico, idéntico en ambas porciones, se cancela, y la solución no depende de él [@brown2012, sec. 5.5].

En la neutralización, la disolución de 100 g sube 4,6 K, de modo que q = 100 × 4,18 × 4,6 = 1923 J = 1,92 kJ, y la reacción lo libera con signo opuesto [@brown2012, Sample Exercise 5.6]. Como reaccionan 0,040 mol de HCl, la entalpía por mol vale −1,92 dividido entre 0,040, es decir, −48 kJ, del mismo orden que la neutralización del ácido fuerte con la base fuerte [@brown2012, Sample Exercise 5.6].

En la bomba, el calor de reacción es el producto de la capacidad calorífica por el salto térmico, −5,43 × 2,90 = −15,7 kJ [@brown2012, sec. 5.5]. Eso corresponde a −13,1 kJ por gramo de muestra, y con 0,0200 mol quemados, a −787 kJ por mol [@brown2012, sec. 5.5].

En la ley de Hess del monóxido se invierte la segunda ecuación para que el CO aparezca como producto: la combustión del carbono libera 393,5 kJ y la oxidación del CO libera 283,0 kJ, de modo que restar la segunda de la primera da −110,5 kJ por mol de CO formado [@brown2012, Sample Exercise 5.8].

Para el diamante, la conversión se obtiene restando la combustión del grafito menos la del diamante: −393,5 kJ/mol menos −395,4 kJ/mol, lo que da +1,9 kJ por mol [@brown2012, Practice Exercise 5.8]. El signo positivo del resultado indica que el grafito, con menor entalpía, es la forma estable, tal como confirma la experiencia [@brown2012, Practice Exercise 5.8].

El propano libera 50,3 kJ por gramo, así que liberar 1,00 × 10³ kJ exige dividir 1000 entre 50,3, lo que da 19,9 g de combustible, una masa que cabe en la palma de la mano [@brown2012, Sample Exercise 5.11]. La cifra muestra cuán compacta resulta la energía almacenada en los hidrocarburos [@brown2012, Sample Exercise 5.11].

La granola suma 4 × 17 kJ de proteína, 22 × 17 kJ de carbohidratos y 6 × 38 kJ de grasa, lo que da 670 kJ, y dividiendo entre 4,184 se obtienen 160 kcal [@brown2012, sec. 5.8]. Todo el solucionario confirma el patrón del capítulo: convertir unidades con factores exactos, aplicar la ecuación del calor específico y encadenar moles, gramos y kilojoules sin perder el signo del calor [@brown2012, sec. 5.4].

## Resumen

La termoquímica mide los cambios de energía que acompañan a las reacciones químicas, y su lenguaje se construye sobre la energía cinética y potencial, el trabajo y el calor [@brown2012, sec. 5.1]. La primera ley de la termodinámica establece que la energía se conserva, y el cambio de energía interna ΔE vale la suma del calor q y el trabajo w intercambiados con el entorno [@brown2012, sec. 5.2].

Como la mayoría de los procesos ocurren a presión constante, la entalpía H = E + PV se convierte en la función más útil, pues su cambio ΔH es exactamente el calor ganado o perdido a presión constante [@brown2012, sec. 5.3]. La entalpía de reacción sigue tres reglas: es proporcional a la cantidad de sustancia, cambia de signo al invertir la reacción y depende de los estados físicos [@brown2012, sec. 5.4].

La calorimetría mide esos cambios con el vaso de café y la bomba, la ley de Hess los calcula por suma de pasos y las entalpías estándar de formación permiten obtener el ΔH° de cualquier reacción restando reactivos de productos [@brown2012, sec. 5.5; @brown2012, sec. 5.6; @brown2012, sec. 5.7]. Los alimentos y los combustibles se comparan por su valor combustible, que ronda 17 kJ por gramo en carbohidratos y proteínas y 38 kJ por gramo en las grasas [@brown2012, sec. 5.8].

La termoquímica precedió a la termodinámica formal: Hess midió calores constantes antes de que Clausius enunciara la conservación de la energía, y Lewis y Randall no impusieron una notación consistente hasta 1923 [@brock2015, cap. 5]. La historia recuerda que las leyes de la energía se descubrieron midiendo, no deduciendo [@brock2015, cap. 5].
