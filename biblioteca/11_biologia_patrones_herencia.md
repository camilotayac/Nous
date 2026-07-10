---
titulo: "11 PATRONES DE HERENCIA"
fuente: ""
fecha_conversion: 2026-07-08
tags:
  - académico
math: true
---
## 11.1 ¿CUÁL ES LA BASE FÍSICA DE LA HERENCIA?

La herencia es el proceso mediante el cual los rasgos de los organismos se transmiten a sus descendientes. 

## Los genes son secuencias de nucleótidos en ubicaciones específicas de los cromosomas

Un cromosoma consta de una doble hélice de ADN, empaquetada con varias Proteínas (histonas y no histonas). Segmentos de ADN, que varían en longitud desde algunos cientos hasta muchos miles de nucleótidos, son las unidades de la herencia, los genes, que codifican la información necesaria para producir proteínas, células y organismos completos. Por tanto, los genes son partes de cromosomas (FIG. 11-1). La ubicación física de un gen en un cromosoma se llama su locus (plural, loci). Los cromosomas son organismos diploides que se presentan en pares llamados homólogos. Ambos miembros de un par de homólogos tienen los mismos genes, ubicados en los mismos loci. Sin embargo, las secuencias de nucleótidos de un gen dado pueden diferir en diferentes miembros de una especie, o incluso en dos homólogos de un solo individuo. Estas diferentes versiones de un gen en un locus dado se llaman alelos (véase la Fig. 11-1). Para entender la relación entre genes y alelos, puede ser útil pensar en los genes como en oraciones muy largas, escritas en un alfabeto de nucleótidos en lugar de letras. Los alelos de un gen son como escrituras ligeramente diferentes de palabras individuales en distintas copias de la misma oración de nucleótidos.

![[fb5d1c94a30e992c7a1b5e470468648049cccf0983ba30d8f9b89db6dd0bdca4.jpg]]
FIGURA 11-1 Las relaciones entre genes, alelos y cromosomas Cada cromosoma homólogo porta el mismo conjunto de genes. Cada gen se ubica en la misma posición, o locus, en su cromosoma. Las diferencias en secuencias de nucleótidos en el mismo locus de gen producen diferentes alelos del gen. Los organismos diploides tienen dos alelos de cada gen, uno en cada homólogo. Los alelos en los dos homólogos pueden ser iguales o diferentes.
## Las mutaciones son fuente de alelos

Casi todos los alelos en tus cromosomas fueron heredados de tus padres. Pero, ¿de dónde provinieron estos alelos en primer lugar? Todos los alelos al inicio surgieron como mutaciones: cambios en la secuencia de nucleótidos en el ADN de un gen. Si una mutación ocurre en una célula que se convierte en espermatozoide u óvulo, puede transmitirse del progenitor al descendiente. La mayoría de los alelos en el ADN de un organismo aparecieron primero como mutaciones en las células reproductivas de los ancestros del organismo, acaso hace cientos o incluso millones de años, y se han heredado, desde entonces, de generación en generación. Algunos alelos, que se llamarán “mutaciones nuevas”, quizás ocurrieron en las células reproductivas de los propios progenitores del organismo, pero esto es raro.

## Los dos alelos de un organismo pueden ser iguales o diferentes

Puesto que un organismo diploide tiene pares de cromosomas homólogos, y ambos miembros de un par contienen los mismos loci de genes, el organismo tiene dos copias de cada gen. Si ambos homólogos tienen el mismo alelo en un locus de gen dado, se dice que el organismo es homocigoto en dicho locus. (Homocigoto proviene de palabras griegas que significan “mismo par”.) Los cromosomas mostrados en la Figura 11-1 son homocigotos en dos loci. Si dos cromosomas homólogos tienen diferentes alelos en un locus, el organismo es heterocigoto (“diferente par”) en dicho locus. Los cromosomas en la Figura 11-1 son heterocigotos en un locus.

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• describir las relaciones entre cromosomas, ADN, genes, mutaciones y alelos?

• explicar qué significa para un organismo ser heterocigoto u homocigoto para un gen?

## 11.2 ¿CÓMO SE DESCUBRIERON LOS PRINCIPIOS DE LA HERENCIA?

A mediados del siglo XIX, los experimentos de un monje austriaco, Gregor Mendel (FIG. 11-2), revelaron múltiples principios importantes de la herencia. Aunque Mendel trabajó mucho antes de que se descubrieran el ADN, los cromosomas o la meiosis, su investigación reveló hechos esenciales acerca de genes y alelos y cómo se heredan durante la reproducción sexual. Puesto que sus experimentos son ejemplos elegantes de ciencia en acción, sigue las rutas de descubrimiento de Mendel.

## Hacerlo bien: los secretos del éxito de Mendel

Para cualquier experimento exitoso en biología hay tres pasos clave: elegir un “sistema” adecuado sobre el cual trabajar (el sistema podría ser tan diverso como una enzima, una ruta metabólica, un organismo o un ecosistema), diseñar y realizar el experimento de manera correcta, y analizar los datos en forma

adecuada. Mendel fue el primer genetista en completar los tres pasos.

![[4ec4b17c8e81f25dc62877d2ee7ed1fbaf4b50cad011771c340931d314e9fdc0.jpg]]

Mendel eligió el gui  
sante comestible para sus   
experimentos (FIG. 11-3). Las estructuras reproductivas masculinas de una flor, llamados estambres, producen polen. Cada grano de

![[ec4d729332f8284ad3018e33b84f5faeb8c2e7f362345360801d898ec20cb062.jpg]]  
FIGURA 11-3 Flores del guisante comestible En la flor intacta de guisante (izquierda), los pétalos inferiores encierran las estructuras reproductivas: los estambres (masculina) y carpelo (femenina). Usualmente, el polen no puede entrar a la flor desde el exterior, de modo que los guisantes por lo general se autopolinizan y, en consecuencia, autofecundan. Si la flor está abierta (derecha), puede polinizarse a mano.

polen contiene espermatozoides. La polinización permite a un espermatozoide fecundar un óvulo, que se ubica dentro del ovario de la estructura reproductiva femenina de la flor, llamada carpelo. En las flores de guisantes, los pétalos encierran todas las estructuras reproductivas, lo que evita la entrada de polen de otra flor. En consecuencia, los óvulos en una flor de guisante deben fertilizarse por espermatozoides del polen de la misma flor. Cuando el espermatozoide de un organismo fecunda sus propios óvulos, el proceso se llama autofecundación.

Sin embargo, Mendel con frecuencia quiso aparear dos plantas de guisante diferentes para ver qué características heredarían sus descendientes. Para hacer esto, abrió una flor de guisante y removió sus estambres, lo que evitó la autofecundación. Después espolvoreó la punta pegajosa del carpelo con polen de la flor de otra planta. Cuando el espermatozoide de un organismo fecunda los óvulos de un organismo diferente, el proceso se llama fecundación cruzada.

El diseño experimental de Mendel era simple, pero brillante. Estudió rasgos con formas inequívocamente diferentes, como flores blancas frente a moradas. También comenzó por estudiar sólo un rasgo a la vez. Los primeros investigadores por lo general intentaron estudiar la herencia al considerar de manera simultánea todas las características de organismos completos, incluidos rasgos que difieren sólo un poco entre organismos. No es de sorprender que los investigadores por lo general estuvieran más confundidos que iluminados.

Para ayudar a interpretar sus resultados, Mendel siguió la herencia de rasgos durante varias generaciones y contó el número de descendientes con cada tipo de rasgo. Cuando analizó estos números, los patrones básicos de la herencia se volvieron claros. En la actualidad, cuantificar los resultados experimentales y aplicar análisis estadístico son herramientas esenciales casi en todo campo de la biología. En la época de Mendel, el análisis numé- rico era una innovación.

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• distinguir entre autofecundación y fecundación cruzada?

• explicar las características importantes del diseño experimental de Mendel?

## 11.3 ¿CÓMO SE HEREDAN RASGOS INDIVIDUALES?

Los organismos de línea pura tienen un rasgo, como las flores moradas, que heredan sin cambios todos los descendientes producidos por autofecundación. En su primer conjunto de experimentos, Mendel realizó fecundación cruzada con plantas de guisante que eran línea pura para diferentes formas de un solo rasgo. La descendencia de los progenitores que difieren en al menos un rasgo genéticamente determinado se llaman hí- bridos. Para determinar los rasgos de la descendencia, Mendel guardó las semillas híbridas y las cultivó el año siguiente.

En uno de estos experimentos, Mendel fecundó cruzando plantas de línea pura para flores blancas con plantas de línea pura para flores moradas. Ésta fue la generación parental, denominada con la letra P. Cuando cultivó las semillas híbridas, descubrió que toda la descendencia de la primera generación (la generación “filial primera”, o F ) produjo flores moradas (FIG. 11-4). ¿Qué ocurrió con el color blanco? Las flores de los híbridos $\mathrm { F } _ { 1 }$ fueron tan moradas como sus progenitores morados de línea pura. El color blanco de su progenitor blanco de línea pura pareció desaparecer.

Entonces Mendel permitió la autofecundación de las flores $\mathrm { F } _ { 1 } ,$recolectó las semillas y las plantó la siguiente primavera. En la segunda generación (F ), Mendel contó 705 plantas con flores moradas y 224 plantas con flores blancas. Estos números son aproximadamente tres cuartos flores moradas y un cuarto flores blancas, o una razón de alrededor de tres moradas a una blanca (FIG. 11-5). Este resultado mostró que la capacidad para producir flores blancas no desapareció en los híbridos$\mathrm { F } _ { 1 } ,$ sólo se ocultó.

Mendel permitió la autofecundación de las plantas $\mathrm { F } _ { 2 }$y produjo una tercera generación (F ). Descubrió que todas las plantas$\mathrm { F } _ { 2 }$con flores blancas produjeron descendencia con flores blancas; esto es, eran línea pura. En contraste, cuando las plantas$\mathrm { F } _ { 2 }$con flores moradas se autofecundaban, sus descendientes eran de dos tipos. Aproximadamente un tercio eran línea pura para moradas, pero los otros dos tercios fueron híbridos que produjeron descendencia tanto con flores moradas como con flores blancas, de nuevo en la razón de tres moradas a una blanca. Por tanto, la generación$\mathrm { F } _ { 2 }$ incluyó un cuarto de plantas blancas de línea pura, un cuarto de moradas de línea pura y un medio de moradas híbridas.

![[9dde5b4cccbd298026f46d546d69165d83dd5dec9ef899d976a89ad33283102e.jpg]]  
FIGURA 11-4 Cruce de plantas de guisante de línea pura para flores blancas o moradas Toda la descendencia tiene flores moradas.

![[2f650ea6e00cd52cb367fbf0d7e1d5e9c0b741fc1c189d70ba6a3c7d1db6349c.jpg]]  
FIGURA 11-5 Autofecundación de plantas de guisante $\boldsymbol { \mathsf { F } } _ { \mathbf { 1 } }$ con flores moradas Tres cuartos de la descendencia tiene flores moradas y un cuarto, flores blancas.

## La herencia de alelos dominantes y recesivos en cromosomas homólogos explica los resultados de las cruzas de Mendel

Los resultados de Mendel, complementados por el conocimiento moderno de los genes y cromosomas, permiten desarrollar una hipótesis de cinco partes para explicar la herencia de rasgos individuales:

Cada rasgo está determinado por pares de unidades físicas discretas llamadas genes. Cada organismo tiene dos alelos por cada gen, uno en cada cromosoma homólogo. Los guisantes con flores blancas de línea pura tienen diferentes alelos del gen de color de flor que poseen los guisantes de línea pura con flor morada.

• Los organismos de línea pura tienen dos copias del mismo alelo para un gen dado y por tanto son homocigotos para dicho gen. Todos los gametos de un homocigoto individual reciben el mismo alelo para dicho gen (FIG. 11-6a). Los organismos

![[e0c779abf832ba67e1b9771a2f9d5daef2e0d45d1d910d6d26c5bda650454291.jpg]]  
(a) Gametos producidos por un progenitor homocigoto

![[034a33ece6a16bd4d9e95940b5ef597c013295820f909c3f720daa47ec41e415.jpg]]  
(b) Gametos producidos por un progenitor heterocigoto

FIGURA 11-6 Distribución de alelos en los gametos (a) Todos los gametos producidos por los organismos homocigotos contienen el mismo alelo. (b) La mitad de los gametos producidos por los organismos heteroci gotos contienen un alelo, y la mitad de los gametos contienen el otro alelo.

híbridos tienen dos alelos diferentes para un gen dado y de este modo son heterocigotos para dicho gen. La mitad de los gametos de un heterocigoto contendrán un alelo para dicho gen y la mitad contendrá el otro alelo (FIG. 11-6b).

Cuando dos alelos diferentes están presentes en un organismo, uno, el alelo dominante, puede enmascarar la expresión del otro, el alelo recesivo. Sin embargo, el alelo recesivo todavía está presente. En el guisante comestible, el alelo para flores moradas es dominante, y el alelo para flores blancas es recesivo.

• Los cromosomas homólogos se separan, o segregan, entre ellos durante la meiosis, lo que en consecuencia separa los alelos que portan. Esto se conoce como ley de segregación de Mendel: cada gameto recibe sólo un alelo de cada par de genes. Cuando un espermatozoide fecunda un óvulo, la descendencia resultante recibe un alelo del padre (en su espermatozoide) y uno de la madre (en su óvulo).

• Puesto que los cromosomas homólogos se separan al azar durante la meiosis, la distribución de alelos en los gametos también es aleatoria.

Observa cómo esta hipótesis explica los resultados de los experimentos de Mendel con el color de la flor (FIG. 11-7). Se usarán letras para representar los diferentes alelos, asignando la letra P mayúscula al alelo dominante para color de flor morada, y la letra p minúscula al alelo recesivo para color de flor blanca. Una planta homocigota de flor morada tiene dos alelos para color de flor morada $( P P ) ;$una planta homocigota de flor blanca tiene dos alelos para color de flor blanca (pp). Por tanto, todos los espermatozoides y óvulos producidos por una planta$P P$portan el alelo$P ,$ y todos los espermatozoides y óvulos de una planta pp portan el alelo p (FIG. 11-7a).

La descendencia $\mathrm { F } _ { 1 }$de fecundación cruzada se produce cuando el espermatozoide P fecunda los óvulos p o cuando el espermatozoide$p$fecunda los óvulos P. En ambos casos, la descendencia$\mathrm { F } _ { 1 }$fue$P { p \mathrm { . } }$Puesto que P es dominante sobre${ \boldsymbol { p } } ,$ todos los descendientes fueron morados (FIG. 11-7b).

Para la generación $\mathrm { F } _ { 2 } ,$Mendel permitió que las plantas$\mathrm { F } _ { 1 }$heterocigotas se autofecundaran. Una planta heterocigota produce igual número de espermatozoides P y p, e igual número de óvulos P y p. Cuando una planta$P p$se autofecunda, cada tipo de espermatozoide tiene igual posibilidad de fecundar cada tipo de óvulo (FIG. 11-7c). Por tanto, la generación$\mathrm { F } _ { 2 }$tuvo tres tipos de descendientes: PP, Pp y pp. Los tres tipos ocurrieron en las proporciones aproximadas de un cuarto$P P$ (homocigoto morado), un medio Pp (heterocigoto morado) y un cuarto pp (homocigoto blanco).

Dos organismos que se ven parecidos en realidad pueden tener diferentes combinaciones de alelos. La combinación de alelos que porta un organismo (por ejemplo, PP o Pp) es su genotipo. Los rasgos del organismo, incluidos su apariencia externa, comportamiento, enzimas digestivas, tipo de sangre o cualquier otra característica observable o mensurable, constituyen su fenotipo. Como has visto, las plantas con genotipo o PP o Pp tienen

FIGURA 11-7 La segregación de alelos y la fusión de gametos predicen la distribución de alelos y rasgos en la herencia del color de flor en los guisantes (a) La generación parental: todos los gametos de los progenitores homocigotos PP contienen el alelo P; todos los gametos de los progenitores homocigotos pp contienen el alelo p. (b) La generación F : fusión de gametos que contienen el alelo P con gametos que contienen el alelo p produce sólo descendencia Pp. (Observa que Pp es el mismo genotipo que pP.) (c) La generación $\mathsf { F } _ { 2 } \colon$la mitad de los gametos de los progenitores heterocigotos Pp contiene el alelo$P y$la mitad contiene el alelo$p .$ La fusión de estos gametos produce descendencia PP, Pp y pp.

![[0159ca2ed40cb14ea4658575a2dd186aea1b407d03af17266cf40d2ead0e9d5a.jpg]]  
(a) Gametos producidos por progenitores homocigotos

$$\mathsf { F } _ { 1 }$$

![[5f78d9a208b7924d539a0b0a4a4f7b4a72f41294f02e13eb2836f9fd835468a9.jpg]]  
(b) Fusión de gametos produce descendencia $\boldsymbol { \mathsf { F } } _ { 1 }$

![[2ea5b9e764a65ae82984149f3c5ead0616963e7c5d4040c77669f55e62317f01.jpg]]  
(c) Fusión de gametos de la generación $\mathsf { F } _ { 1 }$produce descendencia$\mathsf { F } _ { 2 }$el fenotipo de flores moradas. Por tanto, la generación$\mathrm { F } _ { 2 }$ de los guisantes de Mendel consistió de tres genotipos (un cuarto PP, un medio Pp y un cuarto pp), pero sólo dos fenotipos (tres cuartos morado y un cuarto blanco).

## La “contabilidad genética” puede predecir los genotipos y fenotipos de la descendencia

El método del cuadrado de Punnett, llamado así en honor de R. C. Punnett, un famoso genetista de comienzos del siglo XX, es una forma conveniente para predecir los genotipos y fenotipos de la descendencia. La FIGURA 11-8a muestra cómo usar un cuadrado de Punnett para determinar las proporciones esperadas de la descendencia que surgen a partir de la cruza de dos organismos que son heterocigotos para un solo rasgo. La FIGURA 11-8b muestra cómo calcular las proporciones de la descendencia usando las probabilidades de que cada tipo de espermatozoide fecundará cada tipo de óvulo.

FIGURA 11-8 Determinación del resultado de la cruza de un solo rasgo (a) El cuadrado de Punnett te permite predecir tanto los genotipos como los fenotipos de cruzas específicas; aquí se le utilizará para una cruza entre plantas de guisante que son heterocigotas para un solo rasgo: el color de la flor.

1. Asigna letras a los diferentes alelos; usa mayúsculas para alelos dominantes y minúsculas para alelos recesivos.

2. Determina todos los tipos de gametos genéticamente diferentes que pueden producirse por los progenitores masculino y femenino.

3. Dibuja el cuadrado de Punnett, con las columnas etiquetadas con todos los posibles genotipos de los óvulos y las filas etiquetadas con todos los posibles genotipos de los espermatozoides. (También se muestran las fracciones de cada genotipo.)

4. Escribe el genotipo del descendiente en cada recuadro al combinar el genotipo del espermatozoide en su fila con el genotipo del óvulo en su columna. (Multiplica la fracción de espermatozoide de cada tipo en los encabezados de fila por la fracción de óvulos de cada tipo en los encabezados de columna.)

5. Cuenta el número de descendientes con cada genotipo. Observa que Pp es el mismo genotipo que $p P _ { \ l }$6. Convierte el número de descendientes de cada genotipo a una fracción del número total de descendientes. En este ejemplo, de cuatro fecundaciones, se predice que sólo una produce el genotipo pp, de modo que se predice que un cuarto del número total de descendientes producidos por esta cruza es blanco. Para determinar las fracciones fenotípicas, suma las fracciones de genotipos que producirían un fenotipo dado. Por ejemplo, las flores moradas se producen por${ \begin{array} { l } { { \frac { 1 } { 4 } } \ : P P + { \frac { 1 } { 4 } } \ : P p + { \frac { 1 } { 4 } } \ : p P , } \end{array} }$ para un total de tres cuartos de la descendencia.

(b) También se pueden usar probabilidades para predecir el resultado de la cruza de un solo rasgo. Determina las fracciones de óvulos y espermatozoides de cada genotipo y multiplica estas fracciones para calcular la fracción de descendientes de cada genotipo. Cuando dos genotipos producen el mismo genotipo (por ejemplo, Pp y pP), suma las fracciones de cada genotipo para determinar la fracción fenotípica.

PENSAMIENTO CRÍTICO Si cruzaras una planta heterocigota Pp con una planta homocigota recesiva pp, ¿cuál sería la razón esperada de descendientes? ¿Cómo difiere esto de la descendencia de una cruza PP × pp? Intenta resolver esto antes de seguir leyendo el texto.

![[00bb9d6c7e40a8d2310a9358e8122e209be352104fce18f6eab82f4c80075b97.jpg]]  
(a) Cuadrado de Punnett de la cruza de un solo rasgo

![[bc9afaaa7b678bd2f855e910a27e8ce8cc9f86fc7dd88b01143e1829051eed50.jpg]]  
(b) Uso de probabilidades para determinar la descendencia de la cruza de un solo rasgo

Mientras uses estas técnicas de contabilidad genética, ten en mente que, en un experimento real, la descendencia real no ocurrirá exactamente en las proporciones predichas. ¿Por qué? Considera un ejemplo familiar. Cada vez que se concibe un bebé, tiene igual posibilidad de ser un niño o una niña. Sin embargo, muchas familias con dos hijos no tienen una niña y un niño. La razón 1:1 de niñas a niños ocurre sólo si promedias los sexos de los hijos en muchas familias.

## La hipótesis de Mendel puede usarse para predecir el resultado de nuevos tipos de cruzas de un solo rasgo

Probablemente has reconocido que Mendel usó el método científico: hizo una observación y la usó para formular una hipótesis. Pero, ¿la hipótesis de Mendel predice con precisión los resultados de más experimentos? Con base en la hipótesis de que las plantas heterocigotas $\mathrm { F } _ { 1 }$tienen un alelo para flores moradas y uno para blancas (esto es, tienen el genotipo$P { p \llap / } _ { { P } }$ , Mendel predijo el resultado de la fertilización cruzada de plantas Pp con plantas homocigotas recesivas blancas (pp): debería haber igual número de descendientes PP (morada) y pp (blanca). De hecho esto es lo que descubrió.

![[59e7edd852ff6fa620cce005c82a2ae3d1aae67f5d52e4264ef9fab5066b4181.jpg]]  
FIGURA 11-9 Cuadrado de Punnett de una cruza de prueba Un organismo con un fenotipo dominante puede ser u homocigoto o heterocigoto. La cruza de tal organismo con un organismo homocigoto recesivo puede determinar si el organismo dominante es homocigoto (izquierda) o heterocigoto (derecha).

Este tipo de experimento tiene usos prácticos para los criadores de plantas y animales domésticos, quienes quieren saber si un organismo con un rasgo deseable dominante transmitirá dicho rasgo a todos sus descendientes o sólo a algunos de ellos. La fertilización cruzada de un organismo con un fenotipo domi nante (en este caso, una flor morada) pero genotipo desconocido, con un organismo homocigoto recesivo (una flor blanca) se conoce como cruza de prueba, porque pone a prueba si el organismo con el fenotipo dominante es homocigoto o heterocigoto (FIG. 11-9). Cuando se cruza con un homocigoto recesivo (pp), un homocigoto dominante (PP) produce descendencia total fenotípicamente dominante, mientras que un heterocigoto dominante (Pp) produce descendencia con fenotipos tanto dominantes como recesivos en una razón 1:1.

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• describir el patrón de herencia de un rasgo controlado por un solo gen con dos alelos, uno dominante y uno recesivo? • distinguir entre genotipo y fenotipo?

• calcular las proporciones de la descendencia con cada genotipo y fenotipo que se produciría al aparear progenitores con varias combinaciones de los dos alelos?

## EST UDIO DE C ASO CONTINUACIÓN Muerte súbita en la cancha

Muchos rasgos, en seres humanos y otros organismos, se heredan en una forma mendeliana simple. El síndrome de Marfan, por ejemplo, se hereda como un rasgo dominante, lo que significa que un solo alelo de fibrilina defectuosa es suficiente para causar el trastorno. Flo Hyman heredó su alelo defectuoso de su padre. ¿Todos los rasgos genéticamente determinados se heredan de acuerdo con los patrones directos estudiados por Gregor Mendel? En la Sección 11.5 regresarás a esta pregunta.

## 11.4 ¿CÓMO SE HEREDAN LOS RASGOS MÚLTIPLES?

Mendel se dirigió a continuación a la herencia de rasgos múltiples (FIG. 11-10). Realizó fertilización cruzada con plantas que diferían en dos rasgos, por ejemplo, color de semilla (amarillo o verde) y forma de semilla (lisa o rugosa). A partir de cruzas tempranas de plantas con estos rasgos, Mendel ya sabía que el alelo liso del gen de forma de semilla (S) es dominante al alelo rugoso (s) y que el alelo amarillo del gen de color de semilla (Y) es dominante al alelo verde (y). Cruzó una planta de línea pura que producía semillas amarillas lisas (SSYY) con una planta de línea pura que producía semillas verdes rugosas (ssyy). La planta SSYY sólo puede producir gametos SY, y la planta ssyy produce solamente gametos sy. Por tanto, toda la descendencia $\mathrm { F } _ { 1 }$ era heterocigota: genotípicamente SsYy con el fenotipo de semillas lisas amarillas.

![[e644dfe72831e7294aee4fe9f195ba3a816f8c32c3b5aa185341009969936010.jpg]]  
FIGURA 11-10 Rasgos de plantas de guisante estudiadas por Gregor Mendel

Mendel permitió que estas plantas heterocigotas $\mathrm { F } _ { 1 }$se autofecundaran. La generación$\mathrm { F } _ { 2 }$ constó de 315 plantas con semillas lisas amarillas; 101 con semillas rugosas amarillas; 108 con semillas lisas verdes, y 32 con semillas rugosas verdes: una razón de aproximadamente 9:3:3:1. La descendencia que se produjo a partir de otras cruzas de plantas que eran heterocigotas para dos rasgos también tuvo razones fenotípicas de alrededor de 9:3:3:1.

## Mendel hipotetizó que los rasgos se heredan de manera independiente

Mendel se dio cuenta de que estos resultados podrían explicarse si los genes para el color y la forma de las semillas se heredaran de manera independiente uno de otro y no influyeran mutuamente durante la formación de gametos. Si esta hipótesis es correcta, entonces, para cada rasgo, tres cuartos de la descendencia deberían mostrar el fenotipo dominante y un cuarto, el fenotipo recesivo. Este resultado es justo lo que Mendel observó. Descubrió 423 plantas con semillas lisas (de cualquier color) y 133 con semillas rugosas (de cualquier color), una razón de más o menos 3:1; 416 plantas produjeron semillas amarillas (de cualquier forma) y 140 produjeron semillas verdes (de cualquier forma), también una razón de alrededor de 3:1. La FIGURA 11-11 muestra cómo puede usarse un cuadrado de Punnet o cálculo de probabilidades para estimar las proporciones de genotipos y fenotipos de la

![[97ffb164aa6297d737a36cd5b011ffd2c91ad630864976ee57ef51d782f3d88f.jpg]]

![[b797e15c3931dc97fdaa6b0b67a7a5b4392f7845324b30bac24843b113b877c0.jpg]]  
(b) Uso de probabilidades para determinar la descendencia de una cruza de dos rasgos

FIGURA 11-11 Predicción de genotipos y fenotipos para una cruza entre progenitores que son heterocigotos para dos rasgos En semillas de guisantes, el color amarillo (Y) es dominante sobre el verde (y), y la forma lisa (S) es dominante sobre rugosa (s). (a) En esta cruza, un individuo heterocigoto para ambos rasgos (SsYy) se autofecunda. En una cruza que involucre dos genes independientes, habrá igual número de gametos con todas las posibles combinaciones de alelos de los dos genes: SY, Sy, sY y sy. Coloca estas combinaciones de gametos como las etiquetas para las filas y columnas en el cuadrado de Punnett y luego calcula la descendencia como se explicó en la Figura 11-8. Observa cómo el cuadrado de Punnett predice tanto las frecuencias de las combinaciones de rasgos $( \frac { 9 } { 1 6 }$lisa, amarilla;$\frac { 3 } { 1 6 }$lisa, verde;$\frac { 3 } { 1 6 }$rugosa, amarilla, y$\textstyle { \frac { 1 } { 1 6 } }$rugosa, verde) como las frecuencias de rasgos individuales$\textstyle { \binom { 3 } { 4 } }$amarillo,$, { \frac { 1 } { 4 } }$verde,$\textstyle { \frac { 3 } { 4 } }$lisa$y \frac { 1 } { 4 }$rugosa). (b) La probabilidad de dos eventos independientes es el producto (multiplicación) de sus probabilidades individuales. Por ejemplo, para encontrar la probabilidad de lanzar dos monedas y obtener dos caras, multiplica las probabilidades de que en cada moneda aparezca cara$\begin{array} { r } { ( \frac { 1 } { 2 } \times \frac { 1 } { 2 } = \frac { 1 } { 4 } ) } \end{array}$ . La forma de la semilla es independiente de su color. Por tanto, multiplicar las probabilidades individuales de los genotipos o fenotipos para cada rasgo produce las frecuencias predichas para los genotipos o fenotipos combinados de la descendencia. Estas frecuencias son idénticas a las generadas por el cuadrado de Punnett.

PENSAMIENTO CRÍTICO ¿El genotipo de una planta que porta semillas lisas amarillas puede revelarse mediante una cruza de prueba con una planta que porte semillas rugosas verdes?

FIGURA 11-12 Distribución independiente de alelos El movimiento de cromosomas durante la meiosis produce distribución independiente de alelos, que aquí se muestra para dos genes. Cada combinación de alelos tiene igual probabilidad de ocurrencia, lo que produce gametos en las proporciones predichas <sup>1</sup><sub>4</sub> SY, <sup>1</sup><sub>4</sub> sy, <sup>1</sup><sub>4</sub> Sy y <sup>1</sup><sub>4</sub> sY.

PENSAMIENTO CRÍTICO Si los genes para color de semilla y forma de semilla estuvieran en el mismo cromosoma en lugar de sobre diferentes cromosomas, ¿sus alelos se distribuirían de manera independiente? ¿Por qué sí o por qué no?

descendencia de una cruza entre organismos que son heterocigotos para dos rasgos.

La herencia independiente de dos o más rasgos se llama ley de distribución independiente. Rasgos múltiples se heredan de manera independiente si los alelos del gen que controla algún rasgo dado se distribuyen hacia gametos independientemente de los alelos para los genes que controlan todos los demás rasgos. La distribución independiente ocurrirá cuando los rasgos a estudiar están controlados por genes en diferentes pares de cromosomas homólogos. ¿Por qué? Durante la meiosis, cromosomas homólogos pareados se alinean en la metafase I. Cuál homólogo da frente a cuál polo de la célula es aleatorio, y la orientación de un par homólogo no influye en los otros pares (véase el Capítulo 10). En consecuencia, cuando los homólogos se separan durante la anafase I, cuál homólogo del par 1 se mueve al “norte” no afecta cuál homólogo del par 2 se mueve al “norte”, y así por el estilo. El resultado es que los alelos de genes en diferentes cromosomas se distribuyen independientemente de los demás (FIG. 11-12).

![[31b8d3efa508e0f4e70e7e74387851a48f95648f3639acae67ae2980f171cff6.jpg]]  
la distribución independiente produce cuatro combinaciones alélicas igualmente probables durante la meiosis

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• describir el patrón de herencia simultánea de dos rasgos, si cada uno de los rasgos está controlado por un gen separado sólo con dos alelos, uno dominante y uno recesivo?

• explicar la ley de distribución independiente?

• calcular las frecuencias de los genotipos y fenotipos de la descendencia que se produciría mediante el apareamiento de organismos con varias combinaciones de los dos alelos de cada gen, si supones distribución independiente de los dos genes?

## 11.5 ¿LAS REGLAS MENDELIANAS DE LA HERENCIA SE APLICAN A TODOS LOS RASGOS?

En la discusión hasta el momento, se ha supuesto que cada rasgo está completamente controlado por un solo gen, que sólo existen dos posibles alelos de cada gen y que un alelo es del todo dominante sobre el otro. Sin embargo, la mayoría de los rasgos están influidos en formas más variadas y sutiles.

## En la dominancia incompleta, el fenotipo de los heterocigotos es intermedio entre los fenotipos de los homocigotos

Cuando un alelo es completamente dominante sobre un segundo alelo, los heterocigotos con un alelo dominante tienen el mismo fenotipo que los homocigotos con dos alelos dominantes (véanse las Figuras 11-8 y 11-9). Sin embargo, en algunos casos el fenotipo heterocigoto es intermedio entre los dos fenotipos homocigotos, un patrón de herencia llamado dominancia incompleta. Por ejemplo, el palomino dorado se considera como uno de

![[555106d3b9d0ccae72d9353f18524eb037ad8d0febf57c38eef2b9bc824ff2b3.jpg]]  
los caballos más hermosamente coloreado. Los palominos son heterocigotos para dos alelos con dominancia incompleta que en este texto se llamarán zaino $( C _ { 1 } )$y perlino$( C _ { 2 } )$. Los caballos con pelajes castaño rojizo-marrón son homocigotos para el alelo$C _ { 1 } ,$y los perlinos, con pelajes cremoso pálido, son homocigotos para el alelo$C _ { 2 } .$Puesto que los palominos son heterocigotos$( C _ { 1 } C _ { 2 } ) .$no son raza pura; una cruza entre palominos puede producir potrillos zainos, palominos o perlinos, con probabilidades de un cuarto zaino$( C _ { 1 } C _ { 1 } )$, un medio palomino$( C _ { 1 } C _ { 2 } )$y un cuarto perlino$( C _ { 2 } C _ { 2 } ;$ FIG. 11-13).

## Un solo gen puede tener alelos múltiples

Recuerda que los alelos se originan como mutaciones, que entonces pueden heredarse de generación en generación. A lo largo de miles de generaciones y millones de organismos de una especie dada, muchas mutaciones diferentes pueden ocurrir en el mismo gen, lo que resulta en múltiples alelos del gen. Aunque un organismo individual puede tener cuando mucho dos alelos diferentes de un gen (uno en cada uno de dos cromosomas homólogos), si se examinan los genes de todos los miembros de una especie, se pueden encontrar docenas, incluso cientos, de diferentes alelos para algunos genes. Desde luego, cuál de estos alelos hereda un descendiente depende de cuáles alelos estén presentes en sus progenitores.

Los tipos de sangre humana son un ejemplo familiar de alelos múltiples de un solo gen. Los tipos sanguíneos A, B, AB y O surgen como resultado de tres alelos diferentes de un gen (que se designarán A, B y o). Este gen codifica una enzima que agrega molé- culas de azúcar a los extremos de glicoproteínas que se extienden desde las superficies de los eritrocitos. Los alelos $A \mathrm { ~ y ~ } B$ codifican enzimas que agregan diferentes azúcares a las glicoproteínas (las moléculas resultantes se llamarán glicoproteínas tipo A y tipo B, respectivamente). El alelo o codifica una enzima no funcional que no agrega moléculas de azúcar.

Una persona puede tener uno de seis genotipos: AA, BB, AB, Ao, Bo u oo. Los alelos A y B son dominantes sobre o. Por tanto, las personas con genotipos AA o Ao elaboran sólo glicoproteínas tipo A y tienen sangre tipo A. Quienes tienen genotipos BB o Bo sintetizan sólo glicoproteínas

tipo B y tienen tipo de sangre B. Los individuos oo homocigotos recesivos carecen de ambos tipos de glicoproteínas y tienen sangre tipo O. En las personas con sangre tipo AB están presentes ambas enzimas, de modo que sus eritrocitos tienen glicoproteínas $\textsc { A y B }$Cuando un heterocigoto expresa los fenotipos de dos de los homocigotos (en este caso, glicoproteínas$\boldsymbol { \mathrm { ~ A ~ y ~ B ~ } }$ , el patrón de herencia se llama codominancia, y se dice que los alelos son mutuamente codominantes.

El hecho de que las personas tengan diferentes tipos de sangre afecta la seguridad de las transfusiones sanguíneas. El sistema inmunitario humano produce proteínas llamadas anticuerpos, que se enlazan a moléculas complejas que no se producen en el propio cuerpo de una persona (si se enlazaran a moléculas “propias”, tu sistema inmunitario destruiría las células de tu cuerpo). En su papel usual de defensa contra las enfermedades, los anticuerpos se enlazan a moléculas sobre la superficie de bacterias o virus invasores y ayudan a destruirlos. Sin embargo, ciertos anticuerpos complican las transfusiones sanguíneas. Estos anticuerpos se enlazarán a glicoproteínas “extranjeras” sobre los eritrocitos; esto es: glicoproteínas que portan azúcares que son diferentes de los azúcares en los eritrocitos propios de una persona. Si a las personas se les dan transfusiones del tipo de sangre equivocado, sus anticuerpos se enlazan a las glicoproteínas extranjeras, lo que hace que los eritrocitos en la sangre transfundida se agrupen y rompan. Los cúmulos y fragmentos resultantes pueden taponar pequeños vasos sanguíneos y dañar órganos vitales como cerebro, corazón, pulmones o riñones. Por tanto, el tipo de sangre debe coincidir cuidadosamente antes de una transfusión sanguínea.

<table><tr><td colspan="2">TABLA 11-1</td><td colspan="6">Características de grupos sanguíneos humanos</td></tr><tr><td>Tipo de sangre</td><td>Genotipo</td><td>Eritrocitos</td><td>Tiene anticuerpos plasmáticos para:</td><td>Puede recibir sangre de:</td><td></td><td>Puede donar sangre a:</td><td>Frecuencia en EUA</td></tr><tr><td>A</td><td>AA o Ao</td><td></td><td></td><td>Glicoproteína B</td><td>A u O (no sangre con glicoproteína B)</td><td>A o AB</td><td>42%</td></tr><tr><td>B</td><td>BB o Bo</td><td>Glicoproteína A</td><td>Glicoproteína A</td><td>B u O (no sangre con glicoproteína A)</td><td></td><td>B o AB</td><td>10%</td></tr><tr><td>AB</td><td>AB</td><td>Glicoproteína B</td><td>Ninguna glicoproteína</td><td>AB, A, B, O (receptor universal)</td><td></td><td>AB</td><td>4%</td></tr><tr><td>0</td><td>00</td><td>Glicoproteínas A y B Ninguna glicoproteína A o B</td><td>Ambas glicoproteínas</td><td>O (no sangre con glicoproteínas A o B)</td><td></td><td>O, AB, A, B (donador universal)</td><td>44%</td></tr></table>

La TABLA 11-1 resume los tipos de sangre humanos y las transfusiones seguras. Obviamente, una persona puede donar sangre a cualquiera con el mismo tipo de sangre. Además, la sangre tipo O, con eritrocitos que carecen de azúcares, puede transfundirse con seguridad a todos los otros tipos sanguíneos, porque los eritrocitos tipo O no son atacados por los anticuerpos que se encuentran en la sangre A, B o AB. (Los anticuerpos en la sangre del donador se diluyen demasiado por el volumen mucho mayor de la sangre del receptor como para causar problemas.) Las personas con sangre tipo O se llaman “donadores universales”. Pero la sangre tipo O contiene anticuerpos para las glicoproteínas A y B, de modo que los individuos tipo O pueden recibir transfusiones sólo de sangre tipo O. La sangre tipo AB no contiene anticuerpos contra algún tipo de eritrocito, de modo que una persona con sangre tipo AB puede recibir sangre de personas con cualquier otro tipo de sangre; por ende, se les llama “receptores universales”.

## Los genes individuales por lo general tienen efectos múltiples sobre el fenotipo

Los genes individuales con frecuencia tienen efectos fenotípicos múltiples, un fenómeno llamado pleiotropía. Por ejemplo, una mutación en un solo gen en un ratón de laboratorio produjo un ratón desnudo (FIG. 11-14). Los investigadores rápidamente descubrieron que los ratones desnudos no sólo no tienen pelo, sino que también carecen de timo y virtualmente no tienen respuesta inmunitaria, y las hembras no desarrollan glándulas mamarias funcionales, de modo que no pueden nutrir a sus crías.

![[f452e919f3640ba7fd9fd0677783250560d6363a7a136deda1e3738a2e13b6b2.jpg]]

FIGURA 11-14 Ratones desnudos

## EST UDIO DE C ASO CONTINUACIÓN Muerte súbita en la cancha

En el síndrome de Marfan, un solo alelo de fibrina defectuoso produce el aumento de estatura, extremidades largas, manos y pies grandes, paredes débiles en la aorta, y con frecuencia cristalino dislocado en uno o ambos ojos, un sorprendente ejemplo de peliotropía en seres humanos. Sin embargo, los tipos y severidad de los síntomas varían, incluso entre miembros de la familia que portan el mismo alelo defectuoso de fibrilina. Esta variabilidad sugiere que factores ambientales o las acciones de otros genes pueden afectar el fenotipo de Marfan. ¿La mayoría de los rasgos son influidos por el ambiente y por los alelos de otros genes que hereda un individuo?

pelaje claro en todo su cuerpo. En un siamés adulto, el alelo para pelaje oscuro sólo se expresa en las áreas más frías (nariz, orejas, garras y cola).

![[0e31f017956881de2b1c4f6a5073a33f8e6c3af82d6c7726d882fad73b03cd45.jpg]]  
FIGURA 11-15 Color de piel en los seres humanos La herencia poligénica y cantidades variables de bronceado producen una gradación continua de colores de piel.

## Muchos rasgos están influenciados por varios genes

Probablemente en tu clase haya personas de varias estaturas, colores de piel y constituciones corporales, variaciones que no pueden dividirse en fenotipos definidos conveniente y fácilmente. Los rasgos como éstos están influenciados por interacciones entre dos o más genes, un proceso llamado herencia poligé- nica. Como podrás imaginar, mientras más genes contribuyan a un solo rasgo, mayor será el número de posibles fenotipos y más finas las gradaciones entre ellos.

Por ejemplo, el color de piel humana es afectado por al menos diez genes diferentes (FIG. 11-15). Algunos genes tienen efectos extremadamente grandes: las personas que son homocigotas para un alelo recesivo de un gen particular carecen de pigmentación en piel, ojos y cabello (véase la Sección 11.8). Otros genes tienen efectos pequeños, con varios alelos que producen piel ligeramente más oscura o más clara. Al menos 400 genes contribuyen a la estatura humana; no es de sorprender que la variación en estatura sea continua, sin incrementos discretos.

## El ambiente influye la expresión de los genes

Un organismo no sólo es la suma de sus genes. Además de su genotipo, el ambiente donde vive un organismo también influye profundamente su fenotipo. El color de piel de los gatos siameses ilustra con claridad los efectos ambientales sobre la acción gé- nica. Todos los gatos siameses nacen con pelaje claro, pero en las primeras semanas, orejas, nariz, garras y cola se vuelven oscuros (FIG. 11-16). Uno de los genes de los gatos siameses codifica una

FIGURA 11-16 Influencia ambiental  
![[d0ac5396453e2b48cbbe7fc8e68f4a7056cf2fd966ba885f1bdc79f9897df64d.jpg]]

## ¿TE HAS PREGUNTADO...

Los perros evolucionaron de los lobos. Aunque todos los lobos tienen aproximadamente el

mismo tamaño, los perros varían en tamaño más que cualquier otro mamífero, desde el enorme gran danés y el lobero irlandés, hasta las minúsculas razas toy, como el chihuahua minúsculas razas toy, como el chihuahua

y los pomerania. Los investigadores han identificado seis genes que explican la mayoría de la diferencia en tamaño entre las razas. Las razas pequeñas por lo general son homocigotas para alelos “pequeños”

por qué los perros varían tanto en tamaño?

de la mayoría de estos genes. Todos los lobos conocidos, junto con la mayoría de los perros grandes como el danés y los loberos, son homocigotos para los alelos “grandes” de los seis. Los perros de talla media tienden a ser heterocigotos para más o menos la mitad de los genes. Estos patrones sugieren que la herencia poligénica con dominancia incompleta entre dos o más alelos de cada gen controla el tamaño en los perros. ¿Por qué sólo los perros, y no los lobos, tienen alelos pequeños? Los alelos pequeños pudieron surgir como mutaciones en perros o lobos. Sin embargo, una vez ocurridas las mutaciones, las personas quienes prefirieron perros pequeños cruzaron selectivamente perros pequeños entre sí, con frecuencia conservando los más pequeños de cada camada, y por tanto sin darse cuenta seleccionaron los alelos pequeños para estos genes. La protección humana evitó que la selección natural descartara los alelos pequeños. En contraste, los alelos pequeños que pudieron surgir en los lobos se eliminaron rápidamente mediante selección natural, ¡sólo imagina el destino de un lobo del tamaño de un chihuahua en la vida silvestre!

![[1a5ee19479ec3ec1897d5af3d2c5562eaa788a68741b64032931fe210ceddcc7.jpg]]

enzima que produce pelaje oscuro. Esta enzima se sintetiza en células de pigmento en todo el cuerpo del gato. Siendo así, ¿por qué los gatos siameses no son completamente negros? Porque la enzima que produce pigmento oscuro es inactiva a temperaturas por arriba de más o menos 34 °C. Mientras están dentro del útero de su madre, los gatitos nonatos están calientes, de modo que los gatitos siameses recién nacidos tienen pelaje claro en todo su cuerpo. Después de nacer, las orejas, nariz, garras y cola se vuelven más frías que el resto del cuerpo, de modo que en dichas áreas se produce pigmento oscuro.

La mayoría de las influencias ambientales son más complicadas y sutiles que ésta. Por ejemplo, la exposición a la luz solar afecta de manera significativa el color de piel. Cuando se combina con compleja herencia poligénica, el resultado es una variación casi continua en el fenotipo (véase la Fig. 11-15). La estatura de los seres humanos está muy influida por la nutrición, que no sólo contribuye a un fenotipo continuamente variable, sino también ha hecho que las estaturas promedio cambien de manera importante con el tiempo: en muchos países, la estatura promedio aumentó en alrededor de 10 cm durante los últimos 150 años, ya que el mejoramiento en la nutrición permitió que más personas alcanzaran su potencial genético pleno.

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• describir los patrones de herencia de rasgos que muestren dominancia incompleta, codominancia y alelos múltiples?

• explicar cómo la herencia poligénica y las influencias ambientales se combinan para producir variación casi continua en muchos fenotipos?

## 11.6 ¿CÓMO SE HEREDAN LOS GENES UBICADOS EN EL MISMO CROMOSOMA?

Todo cromosoma contiene muchos genes, hasta varios miles en un cromosoma en realidad grande. Este hecho tiene importantes implicaciones para la herencia.

## Los genes en el mismo cromosoma tienden a heredarse juntos

Los cromosomas, no los genes individuales, se distribuyen de manera independiente durante la meiosis I. Por tanto, los genes ubicados en diferentes cromosomas se distribuyen independientemente en gametos. En contraste, los genes en el mismo cromosoma tienden a heredarse juntos, un fenómeno llamado ligamiento genético. Uno de los primeros pares de genes ligados en ser descubierto se encontró en el guisante dulce, una especie diferente del guisante comestible de Mendel. En los guisantes dulces, el gen para color de flor (morada frente a roja) y el gen para forma de grano de polen (redondo frente a largo) se portan en el mismo cromosoma (FIG. 11-17). Por ende, los alelos para dichos genes por lo general se distribuyen juntos en los gametos durante la meiosis y se heredan juntos.

Considera una planta heterocigota de guisante dulce con flores moradas y polen largo. Supón que el alelo dominante morado del gen de color de flor y el alelo dominante largo del gen forma de polen se ubican en un cromosoma homólogo (Fig. 11-17, arriba) y que el alelo rojo recesivo del gen de color de flor y el alelo redondo recesivo del gen de forma de polen se ubican en el otro homólogo (Fig. 11-17, abajo). Por tanto, es probable que los gametos producidos por esta planta tengan o alelos morados y largos o rojos y redondos. Este patrón de herencia no se conforma a la ley de distribución independiente porque los alelos para color de flor y forma de polen no se segregan de manera mutuamente independiente, sino que tienden a permanecer unidos durante la meiosis.

![[233934e14a84a0176c90f48bb9710c30e1f9a2863b0c95ae415d2dd15a888d76.jpg]]  
FIGURA 11-17 Genes unidos en cromosomas homólogos en el guisante dulce Los genes para el color de la flor y la forma del polen están en el mismo cromosoma, por lo que tienden a heredarse juntos.

## El cruzamiento crea nuevas combinaciones de alelos ligados

Sin embargo, genes en el mismo cromosoma no siempre permanecen juntos. Si realizas fertilización cruzada de dos guisantes dulces con los cromosomas mostrados en la Figura 11-17, podrías esperar que toda la descendencia tuviera o flores moradas con granos de polen largos o flores rojas con granos de polen redondos. (Intenta resolver esto con un cuadrado de Punnett.) En realidad, por lo general encontrarías algunos descendientes con flores moradas y polen redondo y algunos con flores rojas y polen largo, como si, en ocasiones, los genes para color de flor y forma de polen no estuvieran ligados. ¿Cómo puede ocurrir esto?

Durante la profase I de la meiosis, en ocasiones cromosomas homólogos intercambian partes, un proceso llamado cru zamiento (véase el Capítulo 10, Fig. 10-8). En la mayoría de los cromosomas, durante la división celular meiótica ocurre al menos un intercambio entre cada par homólogo. El intercambio de segmentos correspondientes de ADN durante el cruzamiento produce recombinación genética: nuevas combinaciones de alelos de los genes que se ubican en cromosomas homólogos. Entonces, cuando los homólogos se separan en la anafase I, las células hijas haploides recibirán cromosomas con diferentes conjuntos de alelos que los que tienen los cromosomas de la célula progenitora.

Observa los cromosomas del guisante dulce durante la meiosis. En la profase I, los cromosomas homólogos duplicados se aparean (FIG. 11-18a). Cada homólogo tendrá una o más regiones donde ocurre el cruzamiento. Imagina que el cruzamiento intercambia los alelos para color de flor entre cromátidas no hermanas de los dos homólogos (FIG. 11-18b). En la anafase I, los homólogos separados ahora tendrán cada uno una cromátida que porta un trozo de ADN de una cromátida del otro homólogo (FIG. 11-18c). Durante la meiosis II se distribuirán cuatro tipos de cromosomas, uno hacia cada una de las cuatro células hijas: dos cromosomas sin cambios y dos cromosomas recombinados (FIG. 11-18d).

![[d27bc8e2dfa57d737dc0cffb74f21970a973db642df0c53ce9091092e0b1a108.jpg]]  
(a) Cromosomas duplicados en profase de meiosis I

![[657c887de773f01ead06fdae9d08e18deff5578fafb33d6b39161adf4a09ad1c.jpg]]  
(b) Entrecruzamiento (cromátidas no hermanas) durante la profase I

![[534d9b188266da1955137fb480725d863f5a82186ab72cbe1e96bac32bf8ce84.jpg]]  
(c) Cromosomas homólogos se separan en anafase I

![[c5fbf2220789f2d3a647aa34db4812eb2eb00c1be3cc1014bf6b51d8682d80d5.jpg]]  
(d) Cromosomas sin cambios y recombinados después de meiosis II

FIGURA 11-18 El entrecruzamiento recombina alelos en cromosomas homólogos (a) Durante la profase de la meiosis I, se aparen cromosomas homólogos duplicados. (b) Cromátidas no hermanas de los dos homólogos intercambian partes mediante cruzamiento. (c) Cuando los cromosomas homólogos se separan durante la anafase de la meiosis I, una cromátida de cada uno de los homólogos ahora contiene un fragmento de ADN de una cromátida del otro homólogo. (d) Después de la meiosis II, dos de las células hijas haploides reciben cromosomas sin cambios, y dos reciben cromosomas recombinados. Los cromosomas recombinados contienen distribuciones alélicas que no ocurren en los cromosomas parentales originales.

Por tanto, se producirán algunos gametos con cada una de las cuatro configuraciones: PL y pl (las mismas configuraciones que los cromosomas parentales originales) y Pl y pL (nuevas configuraciones en los cromosomas recombinados). Si un espermatozoide con un cromosoma Pl fecunda un óvulo con un cromosoma pl, la planta descendiente tendrá flores moradas (Pp) y polen redondo (ll). Si un espermatozoide con un cromosoma pL fecunda un óvulo con un cromosoma pl, entonces la descendencia tendrá flores rojas (pp) y polen largo (Ll).

Mientras más alejados estén los genes en un cromosoma, más probable es que ocurrirá cruzamiento entre ellos. Piensa en un par de cromosomas homólogos como dos cuerdas largas, cada una con una tira roja en un extremo, una tira azul muy cerca de la roja y una tira amarilla en el extremo opuesto. Si lanzas la cuerda sobre el piso de modo que una aterrice encima de la otra, las cuerdas casi siempre se cruzarán entre las tiras azul y amarilla, pero muy rara vez se cruzarán entre las tiras roja y azul. De igual modo, dos genes juntos en un cromosoma están fuertemente ligados y rara vez se separarán mediante un cruzamiento. Sin embargo, si dos genes están muy separados, el cruzamiento entre los genes ocurrirá con tanta frecuencia que parecerán estar distribuidos de manera independiente, como si estuviesen en diferentes cromosomas. Cuando Gregor Mendel descubrió la distribución independiente, no sólo fue astuto y cuidadoso, también fue afortunado. Los siete rasgos que estudió eran controlados por genes que estaban sólo en cuatro cromosomas diferentes. Él observó distribución independiente porque los genes que estaban en los mismos cromosomas estaban separados.

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• describir cómo difieren los patrones de herencia entre rasgos controlados por genes en un solo cromosoma y rasgos controlados por genes en diferentes cromosomas?

## 11.7 ¿CÓMO SE HEREDAN EL SEXO Y LOS RASGOS LIGADOS AL SEXO?

En muchos animales, el sexo de un individuo está determinado por sus cromosomas sexuales. En los mamíferos, las hembras tienen dos cromosomas sexuales idénticos, llamados cromosomas X, mientras que los machos tienen un cromosoma X y un cromosoma Y (FIG. 11-19). A pesar de sus enormes diferencias en tamaño y composición genética, los cromosomas X y Y actúan como homólogos: se aparean durante la profase de la meiosis I y se separan durante la anafase I. Los otros cromosomas, que ocurren en pares homólogos con apariencia idéntica en machos y hembras, se llaman autosomas.

## En los mamíferos, el sexo de un descendiente está determinado por el cromosoma sexual en el espermatozoide

Durante la formación de espermatozoides, los cromosomas sexuales se segregan, y cada espermatozoide recibe o un cromosoma X o uno Y (más un miembro de cada par de autosomas). Los cromosomas sexuales también se segregan durante la formación de óvulos, pero, dado que las hembras tienen dos cromosomas X, todo óvulo recibe un cromosoma X (y un miembro de cada par de autosomas). Por tanto, un descendiente macho se produce si un óvulo es fecundado por un espermatozoide que lleva Y, y un

![[e3232d27b277d0b45317b0a1cdb5651b84e6a4c7d5a2e60017cf067617818c6e.jpg]]  
FIGURA 11-19 Cromosomas sexuales humanos El cromosoma Y (derecha), que porta relativamente pocos genes, es mucho más pequeño que el cromosoma Y (izquierda). Imagen cortesía de Indigo® Instruments: http://www.indigo.com.

FIGURA 11-20 Determinación del sexo en mamíferos El descendiente macho recibe su cromosoma Y de su padre; el descendiente hembra recibe el cromosoma X del padre (etiquetado X ). Tanto machos como hembras reciben un cromosoma X (o X o X ) de su madre.

![[10df186573e1093007d8f35f0865bb39da86a9a911bac113e54447b500b52e41.jpg]]

![[e4f442767feaa8901d5784c7c74523db36d3b152376331ad675db2545b847110.jpg]]

descendiente hembra se produce si un óvulo es fecundado por un espermatozoide que lleva X (FIG. 11-20).

## Los genes ligados al sexo se encuentran sólo en el cromosoma X o en el Y

Los genes que se ubican sólo en los cromosomas sexuales se conocen como ligados al sexo. En los mamíferos, el cromosoma Y tiene relativamente pocos genes. El cromosoma Y humano contiene varias docenas de genes, muchos de los cuales tienen un papel en la reproducción masculina. El gen ligado a Y mejor conocido es el que determina el sexo, llamado SRY. Durante la vida embrionaria, la acción de SRY pone en movimiento toda la ruta de desarrollo del macho. Bajo condiciones normales, SRY hace que el sexo masculino esté 100% ligado al cromosoma Y.

En contraste con el pequeño cromosoma Y, el cromosoma X humano contiene más de mil genes, cuya mayoría no tiene contraparte en el cromosoma Y. La mayoría de los genes en el cromosoma X determina rasgos que son importantes en ambos sexos, como la visión de color, capacidades para coagulación sanguínea y la presencia de proteínas estructurales específicas en los músculos. Puesto que tienen dos cromosomas X, las hembras pueden ser u homocigotas o heterocigotas para genes en el cromosoma X, y en los alelos se expresarán relaciones dominantes frente a recesivas. Los machos, en contraste, expresan por completo todos los alelos que tienen en su único cromosoma X, sin importar si dichos alelos serían dominantes o recesivos en las hembras.

Observa un ejemplo familiar: la deficiencia al color rojoverde, más comúnmente conocida como ceguera de color, lo que por lo general es una denominación incorrecta (FIG. 11-21). La deficiencia de color es causada por alelos recesivos de alguno de dos genes ubicados en el cromosoma X. Los alelos dominantes normales de estos genes (se les llamará C) codifican proteínas que permiten que un conjunto de células de visión a color en el ojo, llamadas conos, sean más sensibles a la luz roja y otro conjunto sea más sensible a la luz verde. Existen varios alelos recesivos defectuosos de estos genes (se les llamará c). Ciertos alelos en extremo defectuosos codifican proteínas que hacen que ambos conjuntos de conos sean igualmente sensibles a las luces roja y verde. En consecuencia, la persona afectada no puede distinguir el rojo del verde y en verdad es ciega al color rojo-verde. Sin embargo, los alelos más comunes, moderadamente defectuosos, producen conos que responden de manera diferente a las luces roja y verde, de modo no tan diferente como hacen los conos normales rojo y verde. Los hombres con estos alelos moderadamente defectuosos son deficientes de color: los camiones de bomberos todavía se ven rojos y el césped todavía parece verde, pero muchos colores “rojizos” y “verdosos” no pueden distinguirse unos de otros (FIG. 11-21a).

¿Cómo se hereda la deficiencia al color? Un hombre puede tener el genotipo CY o cY, lo que significa que tiene un alelo de visión de color C o c en su cromosoma X y ningún gen de visión de color en su cromosoma Y. Tendrá visión a color normal si su cromosoma X porta el alelo C o será deficiente al color si porta el alelo c. Una mujer puede ser CC, Cc o cc. Las mujeres con genotipos CC o Cc tendrán visión a color normal; sólo las mujeres con genotipos cc serán deficientes al color. Aproximadamente 7% de los hombres tienen visión a color defectuosa. Entre las mujeres, alrededor de 93% son homocigotas normales CC, 7% son heterocigotas normales Cc y menos de 0.5% son homocigotas deficientes a color cc.

![[e879d89c0360c536dfd4ae53ac51a5c005e567b1bbd8e11822ad33144bce6e4f.jpg]]  
(a) Visión a color normal (izquierda); simulación de deficiencia al color rojo-verde (derecha)

![[28a4ba0b7ab3c32a52a1cfc6ad0f740c08b52708fe6fd7722d5fed2bfde29e40.jpg]]  
(b) Hijos esperados de un hombre con visión a color normal (CY) y una mujer heterocigota (Cc)

FIGURA 11-21 Herencia ligada al sexo de deficiencia al color rojoverde (a) Estas fotografías muestran a las personas con visión a color normal cómo se ve el mundo a través de los ojos de una persona con deficiencia al color rojo-verde. Para uno de los autores de este libro (GA), las fotografías izquierda y derecha de cada par parecen casi iguales. (b) Un cuadrado de Punnett muestra la herencia de deficiencia de color desde una mujer heterocigota (Cc) hacia sus hijos.

Un hombre con deficiencia al color (cY) puede transmitir su alelo defectuoso c sólo a sus hijas, porque sólo sus hijas heredan su cromosoma X. Sin embargo, por lo general, sus hijas tendrán visión a color normal, porque también heredan un alelo normal C de su madre, quien muy probablemente es homocigota normal CC. Los hijos de una mujer heterocigota (Cc) tienen 50% de posibilidad de heredar su alelo defectuoso (FIG. 11-21b). Los hijos que reciben el alelo defectuoso padecen deficiencia al color (cY), mientras que los hijos que heredan el alelo funcional tienen visión a color normal (CY).

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• explicar por qué el espermatozoide determina el sexo de los descendientes en los mamíferos?

• explicar por qué la mayoría de los rasgos ligados al sexo están controlados por genes en el cromosoma X?

• describir el patrón de herencia de los rasgos ligados al sexo?

## 11.8 ¿CÓMO SE HEREDAN LOS TRASTORNOS GENÉTICOS HUMANOS?

Muchas enfermedades humanas están influidas en mayor o menor grado por la genética. Puesto que las cruzas experimentales entre seres humanos están fuera de discusión, los especialistas en genética humana buscan registros médicos, históricos y familiares para estudiar cruzas pasadas. Los registros que se extienden a través de varias generaciones pueden ordenarse en forma de linajes familiares, diagramas que muestran las relaciones gené- ticas entre un conjunto de individuos relacionados (FIG. 11-22).

El análisis cuidadoso de los linajes de los seres humanos, combinado con tecnología de genética molecular, ha producido grandes avances en la comprensión de las enfermedades genéticas humanas. Por ejemplo, los genetistas ahora conocen los genes responsables para docenas de enfermedades hereditarias, incluidas anemia falciforme, hemofilia, distrofia muscular, síndrome de Marfan y fibrosis quística. La investigación en genética molecular ha aumentado la capacidad para predecir enfermedades genéticas y, en algunos casos, incluso curarlas (véase el Capítulo 14).

En el Capítulo 10 se estudiaron los trastornos que surgen a partir de un número anormal de cromosomas, que son causados por errores en la meiosis. En este capítulo el enfoque estará sobre los trastornos causados por alelos defectuosos de un solo gen. Sin embargo, así como rasgos comunes como la estatura y el color de piel con frecuencia están influidos por varios genes (véase la Sección 11.5), genes múltiples, que interactúan con factores ambientales complejos, pueden predisponer a las personas a desarrollar problemas de salud como enfermedades de Parkinson y Alzheimer, cáncer y esquizofrenia.

![[e4b5602e6b19879a5d3711f241cd75a3d331b96b0a458b49884a0a08a5158466.jpg]]

![[748535bdf119df52be818c9f291136e5a9128c110c03e63ba8f1773f774bdee4.jpg]]

![[7bbb1737538ec560da4bbfa5a16a55aabf2d10deb782c70048993206b20b169a.jpg]]  
FIGURA 11-22 Linajes familiares (a) Un linaje para un rasgo dominante. Observa que cualquier descendiente que muestra un rasgo dominante debe tener al menos un progenitor con el rasgo. (b) Un linaje para un rasgo recesivo. Cualquier individuo que muestre un rasgo recesivo debe ser homocigoto recesivo. Si los progenitores de dicha persona no muestran el rasgo, entonces ambos progenitores deben ser heterocigotos (portadores). Observa que el genotipo no puede determinarse para algunos descendientes, que pueden ser o portadores u homocigotos dominantes.

## Algunos trastornos genéticos humanos son causados por alelos recesivos

El cuerpo humano depende de las acciones de miles de enzimas y otras proteínas. Una mutación en un alelo del gen que codifica una de estas proteínas puede deteriorar o destruir su función. Sin embargo, la presencia de un alelo normal puede generar sufi ciente proteína funcional como para permitir que el heterocigoto tenga el mismo fenotipo que los homocigotos con dos alelos normales. En estos casos, un alelo mutante que codifica una proteína no funcional es recesivo a un alelo normal que codifica una proteína funcional, y un fenotipo anormal ocurre sólo en las personas que heredan dos copias del alelo mutante.

Un portador de un trastorno genético es una persona que es heterocigota, con un alelo normal dominante y un alelo defectuoso recesivo. Los portadores son fenotípicamente sanos, pero pueden transmitir alelos defectuosos a sus descendientes. De manera muy probable, todas las personas portan algunos alelos recesivos que producirían serios trastornos genéticos en homocigotos. Cada vez que nace un niño, existe una posibilidad de 50:50 de que se le transmita el alelo defectuoso. Por lo general esto es inocuo, porque un hombre y una mujer no relacionados en general tienen alelos defectuosos de genes diferentes, y sus hijos desarrollarán un trastorno genético sólo si son homocigotos para un alelo defectuoso del mismo gen. Sin embargo, las parejas relacionadas (en especial los primos hermanos o cercanos) heredaron algunos de sus genes de ancestros comunes recientes y por tanto tienen más probabilidad de portar un alelo defectuoso del mismo gen. Si un hombre y una mujer son ambos heterocigotos para un alelo recesivo defectuoso del mismo gen, tienen una posibilidad de uno a cuatro de tener un hijo con el trastorno gené- tico (véase la Fig. 11-22).

## El albinismo resulta de un defecto en la producción de melanina

Para producir melanina, el pigmento oscuro de la piel, el cabello y el iris del ojo, se necesita una enzima llamada tirosinasa. La producción normal de melanina ocurrirá si una persona tiene o uno o dos alelos funcionales de tirosinasa. Sin embargo, si una persona es homocigota para un alelo que codifica tirosinasa defectuosa, ocurre albinismo (FIG. 11-23). El albinismo en seres humanos y otros mamíferos resulta en piel y cabello muy pálidos.

## La anemia falciforme es causada por un alelo defectuoso para síntesis de hemoglobina

Los eritrocitos están empaquetados con proteínas hemoglobina, que transportan oxígeno y dan a las células su color rojo. Anemia

![[61ecec1383a0d512528517b650d83f2b61fcf9e2e42b21cb3d8fa0dacf3f1362.jpg]]

![[edf7ddd7b7cdb6b2770a284dfcf9028f8a7ac48717fed91d88eeafd0e4558f31.jpg]]  
(a) Seres humanos  
(b) Wallaby

FIGURA 11-23 Albinismo (a) El albinismo ocurre en la mayoría de los vertebrados, incluidos los seres humanos. Los iris de este niño son extremadamente pálidos, de modo que sus ojos son muy sensibles a la luz brillante. (b) El wallaby albino en primer plano está seguro en un zoológico, pero en un ambiente silvestre, su pelaje blanco brillante lo volvería muy notorio para los depredadores.

![[a68799d99ab69e778a9a041d2a29e97317a84fc7dc99161b605379be7ac044de.jpg]]  
(a) Eritrocitos normales

![[4d6aeced101fad470d7081436a6285a6a55a67ed1004b0a901a65546667a9946.jpg]]  
(b) Eritrocitos falciformes  
FIGURA 11-24 Anemia falciforme (a) Los eritrocitos normales tienen forma de disco con centros “abollados”. (b) Cuando el oxígeno sanguíneo es bajo, los eritrocitos en una persona con anemia falciforme se alargan, adelgazan y curvan, y parecen una hoz.

es un término genérico dado a algunas enfermedades, todas caracterizadas por un conteo bajo de eritrocitos o hemoglobina en sangre por abajo de lo normal. La anemia falciforme es una forma hereditaria de anemia que resulta de una mutación en el gen de hemoglobina. Un cambio en un solo nucleótido coloca un aminoácido incorrecto en una posición crucial en la proteína hemoglobina (véase la Sección 13.4 del Capítulo 13). Cuando las personas con anemia falciforme se ejercitan o mueven hacia grandes alturas, las concentraciones de oxígeno en su sangre caen, y las proteínas de hemoglobina falciforme dentro de sus eritrocitos se pegan. Los cúmulos resultantes de hemoglobina sacan a los eritrocitos de sus usuales formas flexibles de disco (FIG. 11-24a) y les dan formas largas de hoz rígida (FIG. 11-24b). Las células falciformes son frágiles y se dañan con facilidad. La anemia ocurre porque los eritrocitos falciformes se destruyen antes de completar su ciclo de vida usual.

La forma de hoz también produce otras complicaciones. Las células falciformes se atascan en los capilares, lo que causa coá- gulos sanguíneos. Los tejidos abajo del coágulo no reciben suficiente oxígeno. Si los bloqueos ocurren en vasos sanguíneos en el cerebro pueden producir ictus paralizantes.

Las personas homocigotas para el alelo de célula falciforme sólo sintetizan hemoglobina defectuosa. En consecuencia, muchos de sus eritrocitos adquieren forma de hoz y sufren de anemia falciforme. Aunque los heterocigotos producen más o menos la mitad de hemoglobina normal y la mitad de hemoglobina anormal, tienen mucho menos eritrocitos falciformes y rara vez muestran síntoma alguno. Dado que sólo las personas que son homocigotas para el alelo de célula falciforme muestran síntomas, la anemia falciforme por lo general es considerada un trastorno recesivo. Sin embargo, durante ejercicio en especial extenuante, algunos heterocigotos pueden experimentar complicaciones que amenacen su vida, como se explora en el “Guardián de la salud: Alelos falciformes y atletismo”.

Entre 5 y 25% de los africanos subsaharianos y 8% de los afroamericanos son heterocigotos para anemia falciforme, pero el alelo es muy raro en los caucásicos. ¿Por qué? ¿La selección natural no debía operar para eliminar el alelo de célula falciforme tanto en poblaciones de africanos como de caucásicos? La diferencia surge porque los heterocigotos tienen cierta resistencia al parásito que causa malaria, que es común en África y otros lugares con climas cálidos y húmedos, mas no en regiones más frías como la mayor parte de Europa. Esta “ventaja heterocigota”

explica la mayor prevalencia del alelo de célula falciforme en personas con origen africano.

## Algunos trastornos genéticos humanos son causados por alelos incompletamente dominantes

En algunos casos, la cantidad de proteína funcional producida por un alelo normal no es suficiente para compensar un alelo defectuoso, de modo que el alelo defectuoso es incompletamente dominante sobre el alelo normal. Por ejemplo, la dominancia incompleta explica la severidad variable de la hipercolesteremia familiar, una enfermedad en la que una persona afectada no puede limpiar lipoproteína de baja densidad (LDL, el colesterol “malo”) del torrente sanguíneo. Los resultantes altos niveles de colesterol producen endurecimiento de las arterias. Las personas que son homocigotas para el alelo defectuoso tienen niveles de colesterol extremadamente elevados y desarrollan cardiopatías a edades muy jóvenes, y con frecuencia sufren serios ataques cardiacos en la niñez. Los hombres heterocigotos por lo general tienen ataques cardiacos en sus 40 o 50 años de edad, y las mujeres heterocigotas aproximadamente una década más tarde.

## Algunos trastornos genéticos humanos son causados por alelos dominantes

Algunos trastornos genéticos serios, como la enfermedad de Huntington, son causados por alelos dominantes. Así como una planta de guisante sólo necesita un alelo dominante de color morado para tener flores moradas (véanse las figuras 11-7 y 11-8), una persona sólo necesita tener un alelo dominante defectuoso para sufrir de estos trastornos. Por tanto, quienes heredan un trastorno genético dominante deben tener al menos un progenitor con la enfermedad (véase la Fig. 11-22a). En raros casos, un alelo dominante que causa un trastorno genético puede resultar no a partir de un alelo transmitido de generación en generación, sino de una mutación en el óvulo o espermatozoide de un progenitor que de otro modo no es afectado. En este caso, ningún progenitor tendrá la enfermedad.

¿Cómo un alelo defectuoso puede ser dominante al alelo funcional normal? Algunos alelos dominantes defectuosos codifican una proteína anormal que interfiere con la función del

![[e229dcabb637b7d13e6576b2a0206b88117fb0d4ae606b3772209e0ac2fa0939.jpg]]

# Alelos falciformes y atletismo

GUARDIÁN DE LA SALUD

La anemia falciforme es considerada un rasgo recesivo porque, por lo general, sólo las personas homocigotas recesivas muestran síntomas. Sin embargo, a nivel molecular, la mitad de las proteínas hemoglobina en un heterocigoto son defectuosas. ¿Esto realmente no afecta en absoluto?

Para la gran mayoría de los heterocigotos (con frecuencia descritos como poseedores de “rasgo falciforme”) de hecho no hay efectos para la salud. No obstante, un número muy pequeño de heterocigotos puede experimentar serios problemas médicos durante ejercicio extremo. Considera a Devard y Devaughn Darling, gemelos idénticos, que comparten todos sus genes, incluida una copia del alelo falciforme.

Los hermanos Darling destacaron en múltiples deportes durante el bachillerato. Ambos eran probables iniciadores del equipo de fútbol de Florida State University cuando lo impensable ocurrió un día durante la práctica: Devaughn colapsó y murió. Nadie podía probar que la muerte de Devaughn fue causada por la combinación de entrenamiento extenuante y el rasgo falciforme, pero las sospechas eran grandes. La universidad decidió que no quería arriesgar a Devard a sufrir el mismo destino y le prohibió jugar fútbol. Sin embargo, Devard fue transferido a la Washington State University y jugó fútbol para los Cougars durante dos años. Después jugó cinco temporadas en la Liga Nacional de Fútbol (NFL; FIG. E11-1).

Los hermanos Darling ejemplifican el raro, pero real, dilema que enfrentan los atletas con rasgo falciforme. La carrera futbolística de Devard y los logros de muchos otros heterocigotos muestran que tener el rasgo falciforme no descarta el deporte extenuante. Aunque la National Collegiate Athletic Association (NCAA: Asociación Nacional de Deporte Universitario) requiere el tamizado de células falciformes de todos los atletas de las divisiones I y II, la Asociación está de acuerdo en que “los estudiantes atletas no deben ser excluidos de la participación atlética”. Sin embargo, la trágica muerte de Devaughn subraya la necesidad de tomar precauciones adecuadas. La deshidratación durante el ejercicio extremo, en especial en climas calurosos, tal vez es el riesgo más importante para los heterocigotos, de modo que la NCAA recomienda que los atletas “estén bien hidratados en todo momento”. Esta y otras precauciones sencillas han ayudado al ejército estadounidense a eliminar las muertes en exceso causadas por el rasgo falciforme durante

normal. Otros alelos dominantes pueden codificar proteínas que realizan nuevas reacciones tóxicas. Incluso otros alelos dominantes pueden codificar una proteína que es hiperactiva y realiza su función en momentos y lugares inadecuados en el cuerpo.

## La enfermedad de Huntington es causada por una proteína defectuosa que mata células en regiones específicas del cerebro

La enfermedad de Huntington es un trastorno dominante que causa un deterioro lento y progresivo de partes del cerebro, lo que resulta en pérdida de coordinación, movimientos agitados, perturbación de la personalidad y, con el tiempo, la muerte. Los síntomas de la enfermedad de Huntington por lo general no aparecen sino hasta los 30 a 50 años de edad. Por tanto, antes de experimentar sus primeros síntomas, muchas víctimas de Huntington transmiten el alelo a sus hijos. Los genetistas aislaron el el entrenamiento básico. De hecho, el ejército incluso ya no realiza tamizados para rasgo falciforme. Procedimientos médicamente adecuados y entrenamientos en seres humanos (por ejemplo, darse cuenta de que fracasar para “hacerse el fuerte” ante seria tensión física no es un signo de debilidad mental) ayudan a todos los atletas, no sólo a quienes tienen rasgo falciforme.

![[7ab5c0e9ea4d762822bb377233b0641aed0c98d9a9411e1055b2b49bab63267a.jpg]]  
FIGURA E11-1 Devard Darling corre hacia la luz para los Jefes de Kansas City El gemelo idéntico de Devard, Devaughn, murió durante la práctica de fútbol en la universidad, probablemente a partir de complicaciones de rasgo falciforme.

EVALÚA LO SIGUIENTE En enero de 2012, el equipo de fútbol de los Acereros de Pittsburgh jugó contra los Broncos de Denver en el “Mile-High City” (la altitud de Denver está a una milla sobre el nivel del mar). El entrenador en jefe de los Acereros, Mike Tomlin, no permitió que jugara el profundo Ryan Clark, porque Clark tenía rasgo falciforme. ¿Qué podría pasar cuando alguien con rasgo falciforme se ejercita a grandes alturas? ¿Crees que Tomlin hizo lo correcto al poner en la banca a Clark? Explica tu razonamiento.

gen de Huntington en 1993 y, pocos años después, identificaron el producto del gen, una proteína que llamaron “huntingtina”. La huntingtina normal afecta la transcripción génica, la función del citoesqueleto y el movimiento de organelos dentro de las cé- lulas cerebrales. La huntingtina mutante está troceada en fragmentos tóxicos dentro de las células, lo que al final las mata.

## Algunos trastornos genéticos humanos están ligados al sexo

Como se describió antes, el cromosoma X contiene muchos genes que no tienen contraparte en el cromosoma Y. Puesto que los hombres tienen un solo cromosoma X, sólo tienen un alelo para cada uno de estos genes. Por tanto, los hombres muestran los fenotipos producidos por estos alelos solos, incluso si los alelos son recesivos y estuvieran enmascarados por alelos dominantes en las mujeres.

![[3e09ba7100207bc66419cf8a365e0ea38f7991987339488ba211048fe7f6fad5.jpg]]  
FIGURA 11-25 Hemofilia entre las familias reales de Europa Un famoso linaje genético muestra la transmisión de la hemofilia ligada al sexo desde la reina Victoria de Inglaterra (sentada al frente, en el centro, con bastón, en 1885) a sus descendientes y a final de cuentas casi a toda la casa real europea, debido a los extensos matrimonios de sus hijos con la realeza de otras naciones europeas. Puesto que los ancestros de Victoria estaban libres de hemofilia, el alelo de la hemofilia debió surgir como una mutación o en la misma Victoria o en uno de sus progenitores (o como resultado de infidelidad matrimonial).

PENSAMIENTO CRÍTICO ¿Por qué no es posible que una mutación en el esposo de Victoria, Albert, fuera la fuente original de hemofilia en este linaje familiar?

Un hijo recibe su cromosoma X de su madre y lo transmite sólo a sus hijas. Por ende, los trastornos ligados a X causados por alelos recesivos tienen un patrón único de herencia. Dichos trastornos aparecen con mucha más frecuencia en hombres y por lo general saltan generaciones: un hombre afectado transmite el rasgo a una hija portadora con fenotipo normal, quien a su vez tiene algunos hijos afectados. Los defectos genéticos más familiares debidos a alelos recesivos de los genes del cromosoma X son la deficiencia en la visión a color rojo-verde (véase la Fig. 11-21), la hemofilia y la distrofia muscular.

La hemofilia es causada por un alelo recesivo en el cromosoma X que resulta en una deficiencia en una de las proteínas necesarias para la coagulación sanguínea. Las personas con hemofilia tienen moretones con facilidad y pueden sangrar mucho en lesiones menores. Con frecuencia tienen anemia debido a pérdida de sangre. No obstante, incluso antes del tratamiento moderno con factores de coagulación, algunos hombres hemofí- licos sobrevivieron para transmitir su alelo defectuoso a sus hijas, quienes a su vez podrían transmitirlo a sus hijos (FIG. 11-25). En el “Guardián de la salud: Distrofia muscular” se describe esta enfermedad, una degeneración mortal de los músculos en los niños jóvenes.

## COMPRUEBA TU APRENDIZAJE

¿Puedes…

• usar linajes para determinar el patrón de herencia de un rasgo?

• describir por qué algunos trastornos genéticos pueden ser dominantes, incompletamente dominantes o recesivos, y dar ejemplos de cada uno?

![[033ecea449e459bf22c4e85c54b4e0f47de3785d6db580fb181995132a5b937e.jpg]]

GUARDIÁN DE LA SALUD

# Distrofia muscular

Cuando la halterófila Tatiana Kashirina, de Rusia, estableció un nuevo récord mundial en el “envión” en la Olimpiada de Londres 2012, levantó 151 kilogramos, aproximadamente 50% más que su propio peso corporal (FIG. E11-2). ¿Cómo sus músculos podrían soportar el estrés? Las células musculares están firmemente enlazadas mediante una proteína muy larga llamada distrofina. Los casi 3700 aminoácidos de la distrofina forman una barra flexible aunque fuerte que conecta el citoesqueleto dentro de una célula muscular con proteínas en su membrana plasmática, que a su vez se une a proteínas de soporte en la matriz extracelular que rodea cada célula muscular. Cuando un músculo se contrae, sus células permanecen intactas porque las fuerzas se distribuyen equitativamente a lo largo de cada célula y a la matriz extracelular.

Por desgracia, alrededor de 1 en 3500 niños tienen proteí- nas distrofina defectuosas y sufren de distrofia muscular, que literalmente significa “degeneración de los músculos”. La distrofia muscular de Duchenne es la forma más devastadora de la enfermedad; la distrofia muscular de Becker es una forma menos severa. La distrofia muscular puede ser causada por más de mil alelos defectuosos diferentes del gen distrofina. La falta de distrofina funcional significa que la contracción muscular ordinaria rasga las células musculares, que mueren y son sustituidas por grasa y tejido conectivo (FIG. E11-3). Hacia los siete u ocho años de edad, los niños con distrofia muscular de Duchenne ya no pueden caminar. La muerte por lo general se presenta a comienzos de sus 20, por problemas cardiacos y respiratorios.

Las niñas casi nunca tienen distrofia muscular de Duchenne porque el gen distrofina está en el cromosoma X, y los alelos de la distrofia muscular son recesivos. Por tanto, un niño sufrirá distrofia muscular si tiene un alelo distrofina defectuoso en su único cromosoma X, pero una niña, con dos cromosomas X, necesitaría dos copias defectuosas para padecer el trastorno. Esto casi nunca ocurre, porque una niña tendría que heredar un alelo distrofina defectuoso de su madre, en uno de sus cromosomas X, y uno de su padre, en su cromosoma X. Puesto que ellos sufren discapacidad temprana y mueren, los niños con distrofia muscular de Duchenne casi nunca tienen hijos.

![[7025f10e6f585ef137e90b4e1147523779a003464dd5dd9fc72f9f83f7a62847.jpg]]

FIGURA E11-3 Los efectos de la distrofia muscular La micrografía de la izquierda muestra un músculo normal, con poco espacio entre las células. Un músculo distrófico (derecha) tiene menos células musculares y más irregulares, con espacios entre las células que se llena con grasa y tejido conectivo.

![[32fc3be392c83bb7b01b8d41cd983c7408ec5433acc7695f2509943b43115e00.jpg]]  
FIGURA E11-2 Tatiana Kashirina establece un récord mundial en el envión.

Si los niños afectados casi nunca se reproducen, ¿la selección natural no debería erradicar por completo los alelos de distrofina defectuosos? En realidad, la selección natural sí elimina rápidamente estos alelos. Sin embargo, el gen distrofina es enorme: aproximadamente 2.4 millones de nucleótidos de largo, comparado con alrededor de 28 mil nucleótidos para el gen humano promedio. ¿Por qué importa esto? Recuerda: los alelos surgen como mutaciones en el ADN. Mientras más largo sea el gen, mayores son las posibilidades de que ocurra una mutación: dado que el gen distrofina es casi cien veces más largo que el gen promedio, su tasa de mutación es más o menos cien veces mayor. Como resultado, casi un tercio de los niños con distrofia muscular reciben una nueva mutación que ocurrió en una célula reproductiva de su madre, y dos tercios heredan una mutación preexistente. Las nuevas mutaciones contrarrestan la selección natural, lo que resulta en la incidencia estable de aproximadamente 1 en 3500 niños.

En la actualidad no existe cura, aunque hay tratamientos disponibles que lentifican la degeneración muscular, prolongan la vida y hacen sentir más cómodos a los niños afectados. Sin embargo, ensayos clínicos han mostrado que una novedosa técnica molecular puede engañar a los músculos de alrededor de 13% de los niños con distrofia muscular para elaborar distrofina parcialmente funcional a partir de un alelo de distrofina defectuoso. Todavía más prometedores son los estudios en ratones que han descubierto que la utrofina, una proteína muscular diferente, que se presenta de manera natural, puede ser capaz de sustituir parcialmente la distrofina. En 2014, un pequeño ensayo clínico mostró que los niños tratados con un medicamento experimental que aumenta la síntesis de utrofina tuvieron menos daño muscular que los niños no tratados. Si más ensayos confirman estos resultados, este nuevo medicamento puede mejorar enormemente la salud y la esperanza de vida de todos los niños con distrofia muscular.

EVALÚA LO SIGUIENTE La madre de un niño pequeño está devastada por descubrir que su hijo tiene distrofia muscular de Duchenne. Ella se realiza una prueba de ADN y descubre que es portadora de un alelo de distrofina defectuoso. Si ella decide tener otro hijo, ¿cuál es la probabilidad de que el segundo hijo tendrá el trastorno? La mujer tiene dos hermanas. ¿Cuál es la probabilidad de que ellas también sean portadoras?

# ESTUD IO DE CASO OTRO VISTAZO

# Muerte súbita en la cancha

El síndrome de Marfan provocó la muerte de Flo Hyman, pero no necesariamente es mortal si se detecta a tiempo. En 2014, la estrella de baloncesto de la universidad de Baylor, Isaiah Austin (FIG. 11-26) decidió jugar de manera profesional después de su primer año en la universidad. Por fortuna para Austin, la Asociación Nacional de Baloncesto (NBA) tamiza de manera extensiva a todos los jugadores en busca de problemas de salud antes de que sean elegibles para la selección. Los médicos de la NBA diagnosticaron a Austin con síndrome de Marfan, y descubrieron que tenía una aorta agrandada, tal vez con paredes débiles. Si Austin hubiese continuado en el baloncesto universitario en lugar de probar suerte como profesional, acaso hubiera tenido el destino que sufrió Flo Hyman. Austin no puede practicar deportes competitivos; de hecho, no debe ejercitarse en absoluto de forma extenuante, ya que el ejercicio aumenta la presión arterial, que puede impo ner demasiado estrés sobre su aorta y causarle una ruptura. Sin embargo, con monitorización cuidadosa, y acaso medicamentos que mantengan baja su presión arterial, tendría que ser capaz de vivir una vida normal.

CONSIDERA ESTO En algunos trastornos genéticos, incluidos distrofia muscular de Duchenne, fibrosis quística, anemia falciforme y la mayoría de los casos de síndrome de Marfan, pueden detectarse los alelos defectuosos tanto en adultos como en embriones. Si tú y tu cónyuge supieran que portan alelos para un grave trastorno genético, ¿buscarían el diagnóstico prenatal de un embrión? ¿Qué harían si su embrión estuviese destinado a nacer con síndrome de Marfan? ¿Con distrofia muscular de Duchenne?

![[b07e7d8283e2f7ef9d54f28e2536d36dd1880145875270f9a8574d4f71fd7302.jpg]]  
FIGURA 11-26 Isaiah Austin Debido a que tiene síndrome de Marfan, el esfuerzo y el aumento en presión arterial de un salto podrían romper la aorta de Austin.

## REPASO DEL CAPÍTULO

En la sección de Respuestas al final del libro encontrarás las respuestas a las preguntas de Pensamiento crítico, Evalúa lo siguiente, Opción múltiple y Llena los espacios.

## Resumen de conceptos clave

## 11.1 ¿Cuál es la base física de la herencia?

Las unidades de la herencia son los genes, que son segmentos de ADN que se encuentran en ubicaciones específicas (loci) en los cromosomas. Los genes pueden existir en dos o más formas alternativas, llamadas alelos. Cuando ambos cromosomas homólogos portan el mismo alelo en un locus dado, el organismo es homocigoto para dicho gen. Cuando los dos cromosomas homólogos tienen alelos diferentes en un locus dado, el organismo es heterocigoto para dicho gen.

## 11.2 ¿Cómo se descubrieron los principios de la herencia?

Gregor Mendel dedujo muchos principios de la herencia a mediados del siglo XIX, antes del descubrimiento del ADN, los genes, los cromosomas o la meiosis. Él hizo esto al elegir un sujeto experimental adecuado, diseñar sus experimentos cuidadosamente, seguir la progenie durante varias generaciones y analizar de manera estadística sus datos.

## 11.3 ¿Cómo se heredan rasgos individuales?

Un rasgo es una característica observable o mensurable del fenotipo de un organismo, como el color de una flor o el tipo de sangre. Cada progenitor proporciona a sus descendientes un alelo de cada gen, de modo que los descendientes heredan un par de alelos por cada gen. La combinación de alelos en la descendencia determina su fenotipo. Los alelos dominantes enmascaran la expresión de los alelos recesivos, lo cual puede resultar en organismos con el mismo fenotipo pero diferentes genotipos. Los organismos con dos alelos dominantes (homocigoto dominante) tienen el mismo fenotipo que los organismos con un alelo dominante y uno recesivo (heterocigoto). Puesto que cada alelo se segrega al azar durante la meiosis, es posible predecir las proporciones relativas de la descendencia con un rasgo particular, usando cuadrados de Punnett o probabilidad.

## 11.4 ¿Cómo se heredan los rasgos múltiples?

Si los genes para dos rasgos se ubican en cromosomas separados, sus alelos se distribuyen de manera independiente entre sí dentro del óvulo o el espermatozoide; esto es: la distribución de alelos de un gen en los gametos no afecta la distribución de los alelos del otro gen. Por ende, la cruza de dos organismos que son heterocigotos en dos loci de cromosomas separados produce descendencia con nueve genotipos diferentes. Para alelos dominantes y recesivos típicos, la descendencia mostrará sólo cuatro fenotipos diferentes.

## 11.5 ¿Las reglas mendelianas de la herencia se aplican a todos los rasgos?

No toda la herencia sigue el patrón simple dominante-recesivo. En la dominancia incompleta, los heterocigotos tienen un fenotipo que es intermedio entre los dos fenotipos homocigotos. Si se examinan los genes de muchos miembros de una especie dada, se puede encontrar que muchos genes tienen más de dos alelos. La codominancia resulta cuando dos alelos de un solo gen contribuyen de manera independiente al fenotipo observado. La pleiotropia ocurre cuando un solo gen tiene efectos sobre varios aspectos, en apariencia no relacionados, del fenotipo de un organismo. En la herencia poligénica, varios genes diferentes contribuyen al fenotipo. El ambiente influye sobre la expresión fenotípica de casi todos los rasgos.

## 11.6 ¿Cómo se heredan los genes ubicados en el mismo cromosoma?

Los genes en el mismo cromosoma tienden a heredarse juntos. Sin embargo, el cruzamiento resultará en cierta recombinación de alelos en cada cromosoma. El cruzamiento ocurrirá con más frecuencia mientras más separados estén los genes dentro del cromosoma.

## 11.7 ¿Cómo se heredan el sexo y los rasgos ligados al sexo?

En muchos animales, el sexo está determinado por cromosomas sexuales, con frecuencia designados X y Y. En los mamíferos, las hembras tienen dos cromosomas X; los machos tienen un cromosoma X y uno Y. Los espermatozoides del macho contienen o un cromosoma X o uno Y, mientras que los óvulos de las hembras siempre tienen un cromosoma X. Por tanto, el sexo está determinado por el cromosoma sexual en el espermatozoide que fecunda un óvulo.

Los genes ligados al sexo se encuentran en el cromosoma X o Y. En los mamíferos, el cromosoma Y tiene menos genes que el cromosoma X, de modo que la mayoría de los genes ligados al sexo se encuentran en el cromosoma X. Puesto que los machos tienen sólo una copia de los genes del cromosoma X, los rasgos recesivos en el cromosoma X tienen más probabilidad de expresarse fenotípicamente en los machos.

## 11.8 ¿Cómo se heredan los trastornos genéticos humanos?

Para determinar el modo de herencia de los rasgos en seres humanos se usan técnicas de genética molecular y el análisis de linajes familiares. Algunos trastornos genéticos se heredan como rasgos recesivos; en consecuencia, sólo las personas homocigotas recesivas muestran síntomas de la enfermedad. Los heterocigotos se llaman portadores; ellos portan el alelo recesivo pero no expresan el rasgo. Algunos trastornos se heredan como rasgos incompletamente dominantes. Los heterocigotos, con sólo un alelo defectuoso, muestran algunos síntomas del trastorno, mientras que las personas que son homocigotas para el alelo defectuoso tienen un trastorno más severo. Otros trastornos se heredan como simples rasgos dominantes. En tales casos, sólo se necesita una copia del alelo dominante para producir todos los síntomas de la enfermedad. Algunos trastornos genéticos en los seres humanos están ligados al sexo.

## Términos clave

albinismo 190   
alelo 175   
anemia falciforme 191   
autofecundación 176   
autosoma 187   
codominancia 183   
cromosoma sexual 187   
cromosoma X 187   
cromosoma Y 187   
cruza de prueba 180   
distrofia muscular 194   
dominancia   
incompleta 182   
dominante 178

enfermedad de

Huntington 192   
fenotipo 179   
fertilización cruzada 176   
gen 175   
genotipo 179   
hemofilia 193   
herencia 175   
herencia poligénica 185   
heterocigoto 176   
híbrido 177   
homocigoto 176   
ley de distribución

independiente 182

ley de segregación 178   
ligado al sexo 188   
ligamiento genético 186   
linaje 189   
línea pura 177   
locus (plural, loci) 175   
método del cuadrado de   
Punnett 179   
mutación 175   
peliotropía 184   
portador 190   
recesivo 178   
recombinación genética 186

## Razonamiento de conceptos

## Opción múltiple

1. La posición física de un gen en un cromosoma es su

; formas ligeramente diferentes de un gen se

llaman

a. locus; alelos

b. locus; poligénica

c. quiasma; alelos

d. rasgo; híbridos

2. Si un organismo tiene dos alelos diferentes (llama a los alelos a y b) de un gen,

a. su fenotipo será el mismo que el de un organismo con dos alelos idénticos de este gen.

b. todos sus gametos contendrán tanto el alelo a como el alelo b.

c. es homocogito para dicho gen.

d. es heterocigoto para dicho gen.

3. Distribución independiente significa que

a. dos genes tienden a heredarse juntos.

b. cuál alelo de un gen se incluye en un gameto no tiene efecto sobre cuál alelo de un segundo gen se incluye en el mismo gameto.

c. cuál alelo de un gen se incluye en un gameto determina cuál alelo de un segundo gen se incluye en el mismo gameto.

d. cromosomas homólogos no se separan durante la meiosis.

4. Si un gen se ubica en el cromosoma X de un mamífero,

a. sólo se expresa en las hembras.

b. sólo se expresa en los machos.

c. está ligado al sexo, y las hembras tienen más probabilidad de mostrar rasgos recesivos.

d. está ligado al sexo, y los machos tienen más probabilidad de mostrar rasgos recesivos.

5. Una cruza de prueba se usa para determinar

a. el genotipo de un organismo con un rasgo fenotípicamente dominante.

b. el genotipo de un organismo con un rasgo fenotípicamente recesivo.

c. el genotipo de un organismo que muestra efectos pleiotrópicos de un gen.

d. si un rasgo se hereda poligénicamente.

## Llena los espacios

1. Un organismo se describe como Rr, con coloración roja. Rr es del organismo, mientras que el color rojo es su . Este organismo sería (homocigoto/ heterocigoto) para este gen de color.

2. La herencia de múltiples rasgos depende de las ubicaciones de los genes que controlan los rasgos. Si los genes están en diferentes cromosomas, entonces los rasgos se heredan (como grupo/de manera independiente) . Si los genes se ubican unos cerca de otros en un solo cromosoma, entonces los rasgos tienden a heredarse (como grupo/de manera independiente) . Se dice que los genes en el mismo cromosoma son

3. En los mamíferos, los machos tienen cromosomas sexuales (XX/XY/YY) y las hembras tienen cromosomas sexuales (XX/XY/YY) . El sexo de la descendencia depende de cuál cromosoma está presente en el (espermatozoide/óvulo)

4. Los genes que están presentes en un cromosoma sexual pero no en el otro se llaman

5. Cuando el fenotipo de los heterocigotos es intermedio entre los fenotipos de los dos homocigotos, este patrón de herencia se llama . Cuando los heterocigotos expresan fenotipos de ambos homocigotos (no intermedio, pero que muestra ambos rasgos), esto se llama . En , muchos genes, por lo general con similares efectos sobre el fenotipo, controlan la herencia de un rasgo.

## Preguntas de repaso

1. Define los siguientes términos: gen, alelo, dominante, recesivo, línea pura, homocigoto, heterocigoto, fertilización cruzada y autofecundación.

2. Explica por qué se dice que los genes ubicados en el mismo cromosoma están ligados. ¿Por qué los alelos de los genes ligados en ocasiones se separan durante la meiosis?

3. Define herencia poligénica. ¿Por qué la herencia poligénica en ocasiones permite que los progenitores produzcan descendencia que es notablemente diferente en color de piel que cualquiera de los progenitores?

4. ¿Qué es ligado al sexo? En los mamíferos, ¿cuál sexo tendría más probabilidad de mostrar rasgos recesivos ligados al sexo?

5. ¿Cuál es la diferencia entre un fenotipo y un genotipo? ¿Conocer el fenotipo de un organismo siempre te permite determinar el genotipo? ¿Qué tipo de experimento realizarías para determinar el genotipo de un individuo fenotípicamente dominante?

6. En el linaje de la parte (a) de la Figura 11-22, ¿crees que los individuos que muestran el rasgo son homocigotos o heterocigotos? ¿Cómo puedes decirlo a partir del linaje?

## Aplicación de conceptos

1. En ocasiones, se usa el término gen en lugar de casualidad. Compara los términos alelo y gen.

2. En un universo alternativo, todos los genes en todas las especies sólo tienen dos alelos, uno dominante y uno recesivo. ¿Todo rasgo tiene sólo dos fenotipos? ¿Todos los miembros de una especie que son dominantes para un gen dado tienen exactamente el mismo fenotipo? Explica tu razonamiento.

## Problemas genéticos

1. En cierto ganado, el color de pelaje puede ser rojo (homocigoto $R _ { 1 } R _ { 1 } )$, blanco (homocigoto$R _ { 2 } R _ { 2 } )$o roano (una mezcla de pelajes rojo y blanco, heterocigoto$R _ { 1 } R _ { 2 } )$

a. Cuando un toro rojo se aparea con una vaca blanca, ¿qué genotipos y fenotipos de descendencia podrían obtenerse?   
b. Si uno de los toros descendientes en la parte (a) se apareara con una vaca blanca, ¿qué genotipos y fenotipos de descendencia podrían producirse? ¿En qué proporción?

2. En el guisante comestible, alto (T) es dominante sobre bajo (t), y las vainas verdes (G) son dominantes sobre las vainas amarillas (g). Elabora una lista con los tipos de gametos y descendientes que se producirían en las siguientes cruzas:

a. TtGg × TtGg

b. TtGg × TTGG

c. TtGg × Ttgg

3. En los tomates, el fruto redondo (R) es dominante sobre el fruto largo (r), y la piel lisa (S) es dominante sobre la piel crespa (s). Un tomate liso redondo de línea pura (RRSS) se cruza con un tomate crespo largo de línea pura (rrss). Todos los descendientes F fueron redondos y lisos (RrSs). Cuando estas plantas F se cruzan, se obtiene la siguiente generación F : Redondo, liso: 43

Largo, crespo: 13

¿Es probable que los genes para textura de piel y forma de fruto estén en el mismo cromosoma, o en diferentes cromosomas? Explica tu respuesta.

4. En los tomates del problema 3, un descendiente F (RrSs) se cruza con un homocigoto recesivo (rrss). Se obtiene la siguiente descendencia:

Redondo, liso: 583 Largo, crespo: 602

Redondo, crespo: 21 Largo, liso: 16

¿Cuál es la explicación más probable para esta distribución de fenotipos?

5. En los seres humanos, el color de cabello está controlado por dos genes que interactúan. El mismo pigmento, melanina, está presente tanto en personas con cabello castaño como en personas con cabello rubio, pero el cabello castaño tiene mucho más pigmento. El cabello castaño (B) es dominante sobre el rubio (b). Si la melanina se puede sintetizar depende de otro gen. La forma dominante de este segundo gen (M) permite la síntesis de melanina; la forma recesiva (m) evita la síntesis de melanina. Los homocigotos recesivos (mm) son albinos. ¿Cuáles serán las proporciones esperadas de los fenotipos en los hijos de los siguientes padres?

a. BBMM × BbMm

b. BbMm × BbMm

c. BbMm × bbmm

6. En los seres humanos, uno de los genes que determinan la visión a color se ubica en el cromosoma X. La forma dominante (C) produce visión a color normal; la deficiencia al color rojo-verde (c) es recesiva. Si un hombre con visión a color normal se casa con una mujer deficiente al color, ¿cuál es la probabilidad de que tengan un hijo deficiente al color? ¿Una hija deficiente al color?

7. En la pareja descrita en el problema 6, la mujer da a luz a una hija con deficiencia al color, pero normal en otros aspectos. Su cónyuge presenta una demanda de divorcio alegando adulterio. ¿Este caso se sostendrá en la corte? Explica tu respuesta.