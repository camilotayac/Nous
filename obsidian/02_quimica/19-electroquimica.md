# Electroquímica

## Introducción

Las reacciones de oxidación-reducción ya aparecieron en el capítulo 5 (@sec-oxido-reduccion-intro) como la tercera gran clase de reacciones en disolución acuosa, y el capítulo 18 entregó el criterio termodinámico para decidir su espontaneidad [@brown2012, sec. 4.4; @chang2022, sec. 17.4]. Este capítulo cierra el círculo mostrando que la energía libre de esas reacciones puede transformarse en energía eléctrica, trabajo útil que se mide en voltios y viaja por cables [@brown2012, cap. 20]. La **electroquímica** estudia, así, el puente entre los electrones que se intercambian y la electricidad que se aprovecha [@atkins2015, cap. 4].

El puente tiene historia: el electrón lo descubrió Joseph John Thomson en 1897, y Michael Faraday (1791–1867) lo domeñó antes de que existiera su nombre, al punto de que Atkins lo llama el arquero cambiador de electrones [@atkins2015, cap. 4]. Faraday cuantificó las leyes de la electrólisis, y su apellido bautiza la constante que liga la carga eléctrica con los moles de electrones [@pauling1988, sec. 15-4]. La fabricación del acero, la corrosión de los metales y la fotosíntesis comparten este mismo lenguaje de transferencia electrónica [@atkins2015, cap. 4].

La oxidación y la reducción son inseparables, como advierte Oriakhi: una no puede ocurrir sin la otra, del mismo modo que una mano no aplaude sola [@oriakhi2021, sec. 22.1]. Los electrones cedidos por la especie que se oxida son ganados exactamente por la que se reduce, y esa contabilidad permite explotar la reacción en dispositivos que van de la batería del automóvil al marcapasos [@oriakhi2021, sec. 23.1]. El recorrido del capítulo abarcará el balanceo por semirreacciones, las celdas voltaicas, la ecuación de Nernst, las baterías, la corrosión y la electrólisis [@brown2012, cap. 20].

## De la combinación con oxígeno a la transferencia de electrones

El nombre «oxidación» nació para designar la combinación de una sustancia con el oxígeno, como en la combustión del magnesio, 2Mg + O₂ → 2MgO [@atkins2015, cap. 4; @oriakhi2021, sec. 22.2]. Pronto se advirtió que la misma cesión de electrones ocurría sin oxígeno: el magnesio también arde en cloro formando MgCl₂, y en ambos casos cede dos electrones [@atkins2015, cap. 4]. La oxidación se generalizó entonces como la pérdida de electrones, y la reducción, ya definida en el capítulo 5, como su ganancia en el sentido inverso [@atkins2015, cap. 4; @brown2012, sec. 20.1].

Oriakhi clasifica las oxidaciones según el mecanismo aparente: adición de oxígeno, combinación con un elemento más electronegativo, pérdida de hidrógeno o pérdida directa de electrones [@oriakhi2021, sec. 22.2]. La reacción H₂S + Cl₂ → 2HCl + S ilustra la tercera vía, pues el azufre pierde sus hidrógenos, y la transformación 2FeCl₂ + Cl₂ → 2FeCl₃ la cuarta, con cada ion hierro cediendo un electrón [@oriakhi2021, sec. 22.2]. En todos los casos, la especie que pierde electrones actúa como **agente reductor** y la que los gana como **agente oxidante** [@brown2012, sec. 20.1].

La transferencia de electrones arrastra consigo átomos, y esa tracción explica procesos a gran escala: la siderurgia reduce el hierro de sus óxidos, la fotosíntesis encadena reacciones redox para construir carbohidratos y la respiración degrada los alimentos como una corrosión orgánica [@atkins2015, cap. 4]. La misma química permite extraer aluminio, purificar cobre y cromar piezas, aplicaciones que se retomarán en la electrólisis [@atkins2015, cap. 4]. El número de oxidación, aprendido en el capítulo 5, será la herramienta contable para seguirles la pista a los electrones [@brown2012, sec. 20.1].

## Balanceo redox por el método de las semirreacciones

El capítulo 5 balanceó ecuaciones redox sencillas por tanteo, pero las reacciones complejas exigen un método sistemático: descomponer la ecuación en dos [**semirreacciones**]{#sec-reacciones-redox}, una de oxidación y otra de reducción, que se balancean por separado y luego se combinan [@brown2012, sec. 20.2]. El balance de masa y de carga de cada semirreacción es la clave del procedimiento, y en medio ácido se ajusta con iones H⁺ y moléculas de agua [@brown2012, sec. 20.2]. Primero se igualan los electrones de ambas y después se suman cancelando lo común [@brown2012, sec. 20.2].

En medio ácido, el permanganato oxida al ion oxalato: el MnO₄⁻ se reduce a Mn²⁺ ganando cinco electrones mientras el C₂O₄²⁻ se oxida a CO₂ perdiendo dos por cada ion [@brown2012, sec. 20.2]. Multiplicando cada semirreacción para igualar diez electrones y sumando se obtiene la ecuación neta:

$$2\mathrm{MnO}_4^- + 5\mathrm{C}_2\mathrm{O}_4^{2-} + 16\mathrm{H}^+ \rightarrow 2\mathrm{Mn}^{2+} + 10\mathrm{CO}_2 + 8\mathrm{H}_2\mathrm{O}$$ {#eq-mno4-oxalato}

En la ecuación balanceada (@eq-mno4-oxalato), el permanganato aporta los cinco electrones que necesita cada ion manganeso y el oxalato los diez que cede entre los cinco iones [@brown2012, sec. 20.2]. Los dieciséis protones y las ocho moléculas de agua ajustan la carga y el oxígeno del medio ácido [@brown2012, sec. 20.2]. En medio básico el método se adapta ajustando primero con agua y desplazando protones con iones hidróxido [@brown2012, sec. 20.2].

El método exige reconocer el cambio de número de oxidación para identificar qué se oxida y qué se reduce [@oriakhi2021, sec. 22.3]. En la ecuación (@eq-mno4-oxalato), el manganeso pasa de +7 a +2 y el carbono de +3 a +4, y esos cambios fijan la estequiometría de los electrones transferidos [@brown2012, sec. 20.2]. Cuando la misma sustancia se oxida y se reduce a la vez, la reacción se llama de desproporción y el método se aplica igualmente [@brown2012, cap. 20, ej. 20.97]. Dominar este balanceo prepara la construcción de celdas, donde cada semirreacción ocurre en un electrodo distinto [@brown2012, sec. 20.2].

## Celdas voltaicas: separar la oxidación de la reducción

Una reacción redox espontánea libera energía que, si la oxidación y la reducción ocurren en el mismo recipiente, se disipa como calor [@brown2012, sec. 20.3]. Separando ambas semirreacciones en **semiceldas** conectadas por un conductor externo, los electrones deben recorrer ese circuito y su flujo constituye corriente eléctrica [@brown2012, sec. 20.3]. El dispositivo que logra esta separación se llama **celda voltaica** o [**celda galvánica**]{#sec-celdas-voltaicas}, y en él la reacción espontánea genera electricidad [@brown2012, sec. 20.3; @oriakhi2021, sec. 23.1].

En la celda clásica de zinc y cobre, una lámina de Zn se sumerge en disolución de ZnSO₄ y otra de Cu en CuSO₄, unidas por un **puente salino** que contiene un electrolito inerte [@brown2012, sec. 20.3]. El zinc se oxida cediendo electrones a su lámina, que los conduce por el alambre externo hasta el cobre, donde el Cu²⁺ los acepta y se deposita como metal [@brown2012, sec. 20.3]. La reacción neta,

$$\mathrm{Zn}(s) + \mathrm{Cu}^{2+}(aq) \rightarrow \mathrm{Zn}^{2+}(aq) + \mathrm{Cu}(s)$$ {#eq-celda-zinc-cobre}

La ecuación (@eq-celda-zinc-cobre) es la misma reacción redox espontánea del capítulo 5, ahora domesticada para producir trabajo eléctrico en lugar de calor [@oriakhi2021, sec. 23.1]. Toda la estequiometría del capítulo 5 se conserva: un átomo de zinc reacciona con un ion cúprico para dar un ion zinc disuelto y un átomo de cobre metálico [@brown2012, sec. 20.3].

El **electrodo** donde ocurre la oxidación se llama **ánodo** y el donde ocurre la reducción, **cátodo**; en la celda de la ecuación (@eq-celda-zinc-cobre) el zinc es el ánodo y el cobre el cátodo [@brown2012, sec. 20.3]. El puente salino cierra el circuito iónico: los cationes migran hacia el cátodo y los aniones hacia el ánodo, manteniendo la neutralidad de ambas disoluciones [@brown2012, sec. 20.3]. Por el circuito externo los electrones fluyen siempre del ánodo al cátodo, y el voltímetro registra unos 1.10 V para esta celda [@brown2012, sec. 20.3; @oriakhi2021, sec. 23.1].

La serie de actividad del capítulo 5 anticipa estas transferencias: un metal más activo desplaza al menos activo de su disolución [@brown2012, sec. 20.4]. El zinc, por encima del cobre en la serie, se oxida espontáneamente ante el Cu²⁺, mientras el cobre sumergido en disolución de Zn²⁺ no deposita zinc sino que alcanza un equilibrio con una proporción diminuta de concentraciones [@pauling1988, sec. 15-5]. Pauling enfatiza que esa misma relación de equilibrio se alcanza desde cualquiera de los dos sentidos, evidencia de que la tendencia termodinámica se mide con la celda y no se decide por inspección [@pauling1988, sec. 15-5].

## Potencial de celda y la escala de los potenciales estándar

El **potencial de celda**, también llamado **fuerza electromotriz (fem)**, mide la diferencia de potencial eléctrico entre los electrodos y cuantifica la tendencia de los electrones a fluir [@brown2012, sec. 20.4; @oriakhi2021, sec. 23.2]. Un voltio equivale a un julio por coulomb, 1 V = 1 J/C, de modo que el voltaje expresa la energía eléctrica por unidad de carga [@oriakhi2021, sec. 23.2]. El potencial depende de la concentración, la presión y la temperatura, y por eso se define un estado estándar convencional [@brown2012, sec. 20.4].

El **electrodo estándar de hidrógeno (EEH)** fija el cero de la escala: platino en contacto con H₂ gaseoso a 1 atm e iones H⁺ a 1 M [@brown2012, sec. 20.4]. Todo electrodo se mide frente a este patrón, y el valor obtenido es su [**potencial estándar de reducción, E°**]{#sec-potenciales-reduccion} [@brown2012, sec. 20.4]. Mediciones de esta clase dan E°(Zn²⁺/Zn) = −0.76 V y E°(Cu²⁺/Cu) = +0.34 V, y la diferencia entre ambos, 1.10 V, reproduce el voltaje medido en la celda [@brown2012, sec. 20.4]. El potencial estándar de una celda también se calcula, según Brown, restando el potencial del ánodo al del cátodo:

$$E^\circ_{\text{celda}} = E^\circ_{\text{red}}(\text{cátodo}) - E^\circ_{\text{red}}(\text{ánodo})$$ {#eq-e0-celda}

En la ecuación (@eq-e0-celda), E°celda es el potencial estándar de la celda completa y E°red los potenciales estándar de reducción de cátodo y ánodo, ambos medidos frente al EEH [@brown2012, sec. 20.4]. Para la celda de zinc y cobre, la resta da +0.34 − (−0.76) = +1.10 V, y el signo positivo anuncia una reacción espontánea [@brown2012, sec. 20.4]. Cuanto mayor sea E°celda, mayor será la fuerza impulsora de la reacción [@brown2012, sec. 20.5].

Conviene anticipar una discrepancia de notación entre las fuentes: Pauling define el potencial de la celda como la resta del potencial del electrodo escrito a la izquierda menos el de la derecha, con semirreacciones tabuladas para producir un solo electrón, mientras Oriakhi suma el potencial de oxidación al de reducción, siendo el primero el negativo del segundo [@pauling1988, sec. 15-5-15-6; @oriakhi2021, sec. 23.2]. Las tres formulaciones son equivalentes, y su diferencia es solo de convención de signos, una fuente clásica de errores que conviene reconocer [@brown2012, sec. 20.4]. El resultado físico, el voltaje medido, no depende de la notación elegida [@brown2012, sec. 20.4].

La tabla 20.1 de Brown, de la que se reproducen valores representativos, ordena las semirreacciones de reducción por su E° [@brown2012, sec. 20.4]. La lectura se hace de arriba hacia abajo: las especies de las filas superiores se reducen con facilidad, mientras las inferiores tienden a oxidarse [@brown2012, sec. 20.4].

| Semirreacción de reducción | E° (V) |
| :--- | :---: |
| F₂ + 2e⁻ → 2F⁻ | +2.87 |
| Cl₂ + 2e⁻ → 2Cl⁻ | +1.36 |
| Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O | +1.33 |
| O₂ + 4H⁺ + 4e⁻ → 2H₂O | +1.23 |
| Ag⁺ + e⁻ → Ag | +0.80 |
| I₂ + 2e⁻ → 2I⁻ | +0.54 |
| Cu²⁺ + 2e⁻ → Cu | +0.34 |
| 2H⁺ + 2e⁻ → H₂ | 0.00 |
| Pb²⁺ + 2e⁻ → Pb | −0.13 |
| Ni²⁺ + 2e⁻ → Ni | −0.28 |
| Zn²⁺ + 2e⁻ → Zn | −0.76 |
| Al³⁺ + 3e⁻ → Al | −1.66 |
| Mg²⁺ + 2e⁻ → Mg | −2.37 |
| Li⁺ + e⁻ → Li | −3.05 |

La tabla coloca arriba a los mejores agentes oxidantes, como el flúor y el cloro, y abajo a los mejores reductores, como el litio y el magnesio [@brown2012, sec. 20.4]. Una semirreacción con E° grande y positivo procede como reducción y obliga a la otra, situada más abajo, a invertirse y oxidarse [@brown2012, sec. 20.4].

Así, el dicromato (E° = +1.33 V) oxida al yoduro (E° = +0.54 V) con un potencial de celda de 0.79 V, mientras el fluoruro, que exige +2.87 V, no puede ser oxidado por el cloro [@brown2012, sec. 20.6]. La escala de potenciales generaliza, con números, la serie de actividad cualitativa del capítulo 5 [@brown2012, sec. 20.4].

## Energía libre, trabajo eléctrico y constante de equilibrio

Un voltaje positivo significa que la reacción de celda es espontánea, y su magnitud mide la fuerza impulsora termodinámica [@brown2012, sec. 20.5]. La conexión cuantitativa con el capítulo 18 es directa, pues la energía libre de Gibbs y el potencial de celda se relacionan mediante la carga total transferida [@brown2012, sec. 20.5]. La **constante de Faraday, F**, definida como la carga de un mol de electrones, vale 96 485 C/mol y convierte los moles de electrones n en culombios [@brown2012, sec. 20.5].

$$\Delta G^\circ = -n F E^\circ$$ {#eq-dg-e}

En la ecuación (@eq-dg-e), n es el número de moles de electrones transferidos según la reacción como está escrita, F la constante de Faraday y E° el potencial estándar de la celda [@brown2012, sec. 20.5]. El signo negativo hace que un voltaje positivo produzca una energía libre negativa, la condición de espontaneidad del capítulo 18 [@brown2012, sec. 20.5].

Como E° es una propiedad intensiva, multiplicar la ecuación por un factor no altera el potencial, aunque sí cambian n, ΔG° y la constante de equilibrio [@brown2012, sec. 20.5]. Y como ΔG° = −RT ln K, la ecuación (@eq-dg-e) se transforma también en el puente electroquímico hacia las constantes del capítulo 15, que a 25 °C toma la forma [@brown2012, sec. 20.5]:

$$\log K = \frac{nE^\circ}{0.0592}$$ {#eq-logk}

La ecuación (@eq-logk) permite obtener constantes de equilibrio extremas sin medir concentraciones [@brown2012, sec. 20.5]. Para la oxidación de la plata por el oxígeno en medio ácido, 4Ag + O₂ + 4H⁺ → 4Ag⁺ + 2H₂O, con E° = 1.23 − 0.80 = +0.43 V y n = 4, la constante resulta del orden de 10²⁹ y la energía libre, −170 kJ por mol de reacción [@brown2012, sec. 20.5]. El mismo cálculo, invertido, predice la constante de equilibrio de cualquier reacción redox a partir de los datos de tabla [@brown2012, sec. 20.5].

La máxima cantidad de trabajo útil que la celda puede entregar vale w_max = −nFE, y su potencia se obtiene multiplicando el voltaje por la corriente en amperios [@brown2012, sec. 20.5]. Un vatio es un julio por segundo, y el kilovatio-hora de las facturas eléctricas equivale a 3.6 × 10⁶ J [@brown2012, sec. 20.5]. Para forzar la reacción inversa en una electrólisis, el voltaje aplicado debe superar el de la celda: si la celda se descarga con un potencial interno de 0.90 V en contra, se requiere un voltaje externo mayor que +0.90 V [@brown2012, sec. 20.9].

## La ecuación de Nernst y las celdas de concentración

Fuera del estado estándar, el potencial depende de las concentraciones según la [**ecuación de Nernst**]{#sec-ecuacion-nernst} [@brown2012, sec. 20.6]. Esta relación, que deriva del cociente de reacción Q del capítulo 15, corrige E° con el logaritmo de Q [@brown2012, sec. 20.6]. A medida que la celda se descarga, Q se acerca a la constante K y el potencial tiende a cero [@brown2012, sec. 20.6].

$$E = E^\circ - \frac{RT}{nF} \ln Q$$ {#eq-nernst}

En la ecuación de Nernst (@eq-nernst), E es el potencial bajo las condiciones dadas, R la constante de los gases, T la temperatura absoluta, F la constante de Faraday y Q el cociente de reacción, evaluado con las concentraciones reales y sin incluir sólidos puros [@brown2012, sec. 20.6]. A 25 °C, sustituyendo las constantes y expresando el logaritmo en base diez, la relación se simplifica:

$$E = E^\circ - \frac{0.0592}{n} \log Q$$ {#eq-nernst-298}

Con la forma simplificada (@eq-nernst-298), la celda de zinc y cobre con [Cu²⁺] = 5.0 M y [Zn²⁺] = 0.050 M eleva su potencial de 1.10 V a 1.16 V, pues el exceso de ion cúprico desplaza la reacción hacia los productos [@brown2012, sec. 20.6]. El cociente vale Q = 0.010 y el término 0.0296 log Q aporta +0.06 V [@brown2012, sec. 20.6]. La misma ecuación predice qué ocurre al descargar la celda: las concentraciones se igualan y el voltaje decae [@brown2012, sec. 20.6].

La célula nerviosa y el músculo cardíaco funcionan como [**celdas de concentración**]{#sec-celdas-concentracion} de iones potasio: el interior celular contiene unos 135 mM de K⁺ y el exterior unos 4 mM [@brown2012, sec. 20.6]. La ecuación de Nernst aplicada a esta diferencia predice un potencial de reposo cercano a −90 mV [@brown2012, sec. 20.6]. El electrocardiograma registra precisamente estas fluctuaciones de potencial durante el latido [@brown2012, sec. 20.6].

Cuando ambas semiceldas usan el mismo par redox en concentraciones distintas, E° se cancela y el potencial proviene solo de la diferencia de concentración [@brown2012, sec. 20.6]. La **celda de concentración** de níquel con 1.00 × 10⁻³ M frente a 1.00 M genera unos 0.09 V, y la de zinc con 3.75 × 10⁻⁴ M frente a 1.35 M, unos 0.105 V [@brown2012, sec. 20.6]. En el electrodo sumergido en la disolución diluida, el metal se disuelve buscando igualar concentraciones, y ese electrodo diluido actúa como ánodo [@brown2012, sec. 20.6].

El caso más útil de celda de concentración es el del hidrógeno, porque su potencial depende del pH [@pauling1988, sec. 15-7]. Una celda con dos electrodos de hidrógeno, uno en disolución de pH conocido y otro en la muestra, produce 0.0592 V por unidad de pH, fundamento del medidor de pH o potenciómetro [@pauling1988, sec. 15-7]. Brown resuelve el caso inverso: si el voltaje mide 0.211 V frente al electrodo estándar de hidrógeno, la disolución desconocida posee [H⁺] = 2.7 × 10⁻⁴ M, es decir, pH 3.56 [@brown2012, sec. 20.6].

## Baterías y celdas de combustible

Una **batería** es una fuente portátil y autónoma de energía formada por una o varias celdas voltaicas [@brown2012, sec. 20.7]. Las pilas domésticas de 1.5 V son una sola celda, mientras la batería de 12 V del automóvil conecta en serie seis celdas de 2 V [@brown2012, sec. 20.7; @pauling1988, sec. 15-8]. En una conexión en serie los voltajes se suman, y el electrodo positivo de cada celda es su cátodo [@brown2012, sec. 20.7].

La batería de plomo-ácido descarga el plomo esponjoso del ánodo y el PbO₂ del cátodo, ambos sumergidos en ácido sulfúrico al 38% en masa, con densidad 1.290 g/cm³ cuando está cargada [@pauling1988, sec. 15-8]. Las semirreacciones forman sulfato de plomo adherido a las placas, y la reacción global:

$$\mathrm{Pb}(s) + \mathrm{PbO}_2(s) + 2\mathrm{H}_2\mathrm{SO}_4(aq) \rightarrow 2\mathrm{PbSO}_4(s) + 2\mathrm{H}_2\mathrm{O}(l)$$ {#eq-plomo-acido}

En la ecuación (@eq-plomo-acido) el mismo elemento cambia de estado de oxidación en ambas direcciones: el plomo metálico pasa de 0 a +2 oxidándose, y el del PbO₂ pasa de +4 a +2 reduciéndose [@pauling1988, sec. 15-8]. Al descargarse, el ácido se consume y la densidad del electrolito cae, lo que permite medir la carga restante con un hidrómetro [@pauling1988, sec. 15-8]. La recarga con el alternador invierte ambas semirreacciones y repone el ácido sulfúrico [@brown2012, sec. 20.7].

Las baterías recargables modernas varían los materiales: la de níquel-cadmio entrega 1.30 V por celda con ánodo de cadmio, pero el cadmio es tóxico y denso, y se producen anualmente unos 1 500 millones de estas baterías [@brown2012, sec. 20.7]. La de níquel-hidruro metálico (NiMH) conserva el cátodo y cambia el ánodo por una aleación como ZrNi₂ capaz de absorber hidrógeno atómico, que se oxida al descargarse [@brown2012, sec. 20.7]. La de ion-litio alcanza unos 3.7 V con la inserción reversible de Li⁺ entre capas de óxido de cobalto y grafito, ofreciendo la mayor densidad de energía [@brown2012, sec. 20.7].

Una **celda de combustible** recibe continuamente el combustible y el oxidante desde el exterior, en lugar de almacenarlos dentro [@brown2012, sec. 20.7]. La celda de hidrógeno y oxígeno con membrana de intercambio protónico opera a unos 80 °C con platino como catalizador y produce cerca de un voltio por celda, de modo que varias apiladas alcanzan potencias útiles [@brown2012, sec. 20.7].

La eficiencia máxima de convertir calor en electricidad ronda el 40%, y las celdas de combustible generan electricidad aproximadamente al doble de eficiencia que los mejores motores de combustión [@brown2012, sec. 20.7]. Una celda de metanol directo, cuyos productos son CO₂ y agua, promete transportar energía con menor huella de carbono [@brown2012, sec. 20.7].

## Corrosión: la descarga espontánea de los metales

La [**corrosión**]{#sec-corrosion} es la oxidación espontánea de un metal en su entorno, y la herrumbre del hierro es su manifestación más costosa [@brown2012, sec. 20.8]. El hierro metálico, con E°(Fe²⁺/Fe) = −0.440 V, se oxida mientras el oxígeno se reduce, porque el potencial del par O₂/H₂O es más positivo que el del hierro [@brown2012, sec. 20.8]. La formación de herrumbre exige simultáneamente oxígeno y agua, y el Fe²⁺ inicial se oxida después a Fe³⁺, que precipita como óxido hidratado [@brown2012, sec. 20.8].

La velocidad de corrosión depende del entorno: la aceleran las sales, cuyos iones cierran el circuito eléctrico como un puente salino, y el contacto con metales más difíciles de oxidar que el hierro [@brown2012, sec. 20.8]. La reducción del oxígeno requiere H⁺, de modo que un pH superior a 9 la bloquea y el hierro no se corroe [@brown2012, sec. 20.8].

Las regiones deformadas o abolladas actúan como ánodos locales donde el metal se disuelve, mientras la herrumbre se deposita en el cátodo, la zona con mayor suministro de oxígeno [@brown2012, sec. 20.8]. Se estima que hasta el 20% de la producción anual de hierro en Estados Unidos reemplaza objetos descartados por daño de la herrumbre [@brown2012, sec. 20.8].

El zinc protege al hierro mejor que una pintura porque se corroe en su lugar: al ser E°(Zn²⁺/Zn) = −0.763 V más negativo que el −0.440 V del hierro, el zinc se oxida preferentemente y actúa como **ánodo de sacrificio**, mientras el hierro queda como cátodo donde el oxígeno se reduce [@brown2012, sec. 20.8].

Esta **protección catódica** se extiende a tuberías y tanques subterráneos, a los que se conecta un bloque de magnesio, con E° = −2.37 V, enterrado rodeado de yeso, sulfato de sodio y arcilla [@brown2012, sec. 20.8]. El aluminio, por su parte, se protege solo con una capa impermeable de Al₂O₃, y el acero inoxidable resiste gracias a sus elementos de aleación [@brown2012, sec. 20.8].

## Electrólisis y electrometalurgia

La [**electrólisis**]{#sec-electrolisis} invierte el proceso de la celda voltaica: aplicando un voltaje externo mayor que el de la celda en sentido contrario, se fuerza una reacción redox no espontánea [@brown2012, sec. 20.9]. El dispositivo, llamado **celda electrolítica**, conecta el electrodo positivo de la fuente al ánodo y el negativo al cátodo [@brown2012, sec. 20.9]. La electrólisis del cloruro de sodio fundido, que se funde a 801 °C, produce sodio metálico en el cátodo y cloro gaseoso en el ánodo [@brown2012, sec. 20.9]:

$$2\mathrm{NaCl}(l) \rightarrow 2\mathrm{Na}(l) + \mathrm{Cl}_2(g)$$ {#eq-nacl}

En la ecuación (@eq-nacl), cada ion sodio gana un electrón en el cátodo y cada ion cloruro pierde uno en el ánodo, y la corriente sostiene el balance de cargas [@brown2012, sec. 20.9]. La industria abarata el proceso añadiendo carbonato de sodio para bajar el punto de fusión, y separa los productos con una pantalla de hierro que deja flotar el sodio líquido, más ligero que la sal fundida [@pauling1988, sec. 15-9]. Solo una pequeña fracción del cloro estadounidense proviene de esta vía fundida, pues la mayor parte se obtiene de la salmuera [@pauling1988, sec. 15-9].

La razón para fundir la sal es la competencia del agua: en disolución acuosa, el agua admite reducción con potenciales de 0.00 V en medio ácido y −0.83 V en medio básico, mucho menos negativos que el −2.71 V del sodio, de modo que el agua se reduciría primero [@brown2012, sec. 20.9].

Por eso los metales activos como sodio, magnesio y aluminio se obtienen por **electrometalurgia**, la producción de metales por electrólisis, desde sales fundidas [@brown2012, sec. 20.9]. En la electrólisis de disoluciones solo se reducen u oxidan las especies más favorables, y la elección de electrodos inertes o activos decide el curso de la reacción [@brown2012, sec. 20.9; @oriakhi2021, sec. 23.10].

El cromado y el niquelado explotan un electrodo activo: en una disolución de NiSO₄, el cátodo de acero reduce el Ni²⁺, cuyo potencial estándar −0.28 V es menos negativo que el −0.83 V del agua, y el ánodo de níquel metálico se disuelve oxidándose [@brown2012, sec. 20.9]. Como ánodo y cátodo usan el mismo par, el potencial estándar de la celda es cero y basta un voltaje pequeño para depositar níquel [@brown2012, sec. 20.9]. La masa depositada se controla con la carga: un coulomb equivale a un amperio por segundo, y la contabilidad de electrones cierra la ecuación:

$$\text{mol } e^- = \frac{I\,t}{F}$$ {#eq-faraday}

En la ecuación (@eq-faraday), I es la corriente en amperios, t el tiempo en segundos y F la constante de Faraday, de modo que el producto It entrega directamente los moles de electrones [@brown2012, sec. 20.9]. Conviene advertir una discrepancia numérica entre las fuentes sobre F: Brown emplea 96 485 C/mol, Pauling 96 490 C y Oriakhi redondea a 96 500 C/mol [@brown2012, sec. 20.5; @pauling1988, sec. 15-4; @oriakhi2021, sec. 23.10]. La diferencia refleja la precisión de las mediciones de cada época, y para los cálculos del capítulo se toma la cifra de Brown [@brown2012, sec. 20.5].

Faraday condensó sus observaciones en dos leyes que gobiernan toda electrólisis: la masa de sustancia transformada es proporcional a la carga circulante y, para una carga dada, proporcional al peso equivalente [@pauling1988, sec. 15-4]. La ley resume el contenido de la ecuación (@eq-faraday) y de la estequiometría de cada semirreacción, como en el depósito de un mol de aluminio por cada tres moles de electrones [@brown2012, sec. 20.9]. Las dos tradiciones, la del peso equivalente de Pauling y la de los moles de electrones de Brown, describen el mismo hecho con unidades distintas [@pauling1988, sec. 15-4; @brown2012, sec. 20.9].

El aluminio resume la economía de la electrometalurgia: su óxido funde por encima de 2000 °C, pero disuelto en criolita, Na₃AlF₆, funde a unos 1012 °C, temperatura accesible en celdas de unos 5 V [@brown2012, sec. 20.9; @pauling1988, sec. 15-9]. Los ánodos de grafito se consumen en la reacción global del proceso Hall-Héroult:

$$2\mathrm{Al}_2\mathrm{O}_3 + 3\mathrm{C} \rightarrow 4\mathrm{Al} + 3\mathrm{CO}_2$$ {#eq-hall}

La ecuación (@eq-hall) muestra el doble papel del carbono, conductor eléctrico y reactivo que se oxida a dióxido [@brown2012, sec. 20.9]. Charles Hall en Estados Unidos y Paul Héroult en Francia descubrieron el proceso independientemente, con solo veintidós años, hacia 1886 [@brown2012, sec. 20.9]. Hasta entonces el aluminio se obtenía reduciendo sus sales con sodio o potasio, y en 1852 costaba 545 dólares por libra, más que el oro [@brown2012, sec. 20.9]. Hoy la industria del aluminio consume alrededor del 2% de la electricidad de Estados Unidos, y reciclar aluminio exige solo el 5% de la energía de producirlo [@brown2012, sec. 20.9].

La refinación electrolítica purifica el cobre de sus minerales: ánodos gruesos de cobre bruto se disuelven y el metal puro se deposita sobre cátodos delgados en un baño de sulfato de cobre [@pauling1988, sec. 15-9]. Las impurezas nobles, oro, plata y platino, caen al fondo como lodo anódico, mientras las activas como el hierro permanecen en disolución [@pauling1988, sec. 15-9]. La electrólisis de la salmuera produce además el cloro y la sosa cáustica de la industria química, con un cátodo de mercurio que forma una amalgama de sodio [@pauling1988, sec. 15-9].

## Ejemplo resuelto: la celda de zinc y cobre bajo condiciones reales

El ejemplo integra la escala de potenciales, la energía libre y la ecuación de Nernst para responder qué ocurre cuando la celda clásica opera fuera del estado estándar [@brown2012, sec. 20.5-20.6]. Con E°(Zn²⁺/Zn) = −0.76 V y E°(Cu²⁺/Cu) = +0.34 V, se pide calcular el potencial estándar de la celda, la energía libre estándar, la constante de equilibrio y el potencial cuando [Cu²⁺] = 2.5 M y [Zn²⁺] = 0.040 M [@brown2012, sec. 20.4-20.6].

El potencial estándar se obtiene de la ecuación (@eq-e0-celda): E° = +0.34 − (−0.76) = +1.10 V, y la energía libre, con la ecuación (@eq-dg-e) y n = 2, vale ΔG° = −2 × 96 485 × 1.10 = −212 kJ [@brown2012, sec. 20.5]. El signo negativo confirma la espontaneidad en condiciones estándar, y su magnitud, unos 212 kJ por mol de reacción, es la máxima cantidad de trabajo eléctrico recuperable si la celda operara reversiblemente [@brown2012, sec. 20.5].

La constante de equilibrio sale de la ecuación (@eq-logk): log K = 2 × 1.10/0.0592 = 37.2, de modo que K ≈ 1.4 × 10³⁷, un valor que desplaza la reacción abrumadoramente hacia el cobre metálico [@brown2012, sec. 20.5]. En el equilibrio, el ion cúprico queda prácticamente agotado y la disolución contiene casi solo Zn²⁺ [@brown2012, sec. 20.5]. Una constante tan extrema se obtiene sin esfuerzo por electroquímica, mientras medirla por análisis químico sería inviable [@brown2012, sec. 20.5].

Fuera del estado estándar, el cociente vale Q = [Zn²⁺]/[Cu²⁺] = 0.040/2.5 = 0.016, y la ecuación de Nernst (@eq-nernst-298) da E = 1.10 − 0.0296 × log(0.016) = 1.10 + 0.053 = 1.15 V [@brown2012, sec. 20.6]. El potencial supera al estándar porque el exceso de Cu²⁺ y la escasez de Zn²⁺ empujan la reacción hacia los productos [@brown2012, sec. 20.6]. Al descargarse la celda, la diferencia de concentraciones se erosiona, Q crece hasta K y el voltaje cae hacia cero [@brown2012, sec. 20.6].

El mismo formalismo explica las celdas de concentración: si ambas semiceldas fueran de cobre con [Cu²⁺] = 2.5 M y 0.040 M, el potencial sería E = 0.0296 log(2.5/0.040) = 0.053 V, con el electrodo diluido como ánodo [@brown2012, sec. 20.6]. El resultado generaliza la lección del capítulo 18: la dirección del cambio depende de las condiciones, y la termodinámica cuantifica exactamente cuánta energía se libera o se exige [@brown2012, sec. 20.6].

## Preguntas y ejercicios

Los ejercicios de este capítulo, inspirados en @brown2012 (2012), cap. 20; @pauling1988 (1988), cap. 15; @atkins2015 (2015), cap. 4; @oriakhi2021 (2021), caps. 22-23, combinan la asignación de números de oxidación, el balanceo por semirreacciones, la predicción de espontaneidad, el cálculo de potenciales, energías libres y constantes, y la cuantificación de la electrólisis.

Primer ejercicio: determina el número de oxidación del cloro en el KClO₃, del nitrógeno en el ion amonio y del manganeso en el ion permanganato, aplicando las reglas del capítulo 5 y haciendo explícitas las cargas hipotéticas de cada átomo [@brown2012, sec. 20.1]. Señala además cuál de las tres especies es el oxidante más fuerte [@brown2012, sec. 20.4].

Segundo ejercicio: balancea por el método de las semirreacciones la oxidación del ion bromuro por el dicromato en medio ácido, Br⁻ + Cr₂O₇²⁻ → BrO₃⁻ + Cr³⁺, indicando cuántos electrones se transfieren, qué especie se oxida y cuál actúa como agente oxidante [@brown2012, sec. 20.2].

Tercer ejercicio: el yodo molecular se desproporciona en medio básico dando yoduro y yodato, I₂ + OH⁻ → I⁻ + IO₃⁻, en una reacción donde la misma sustancia se oxida y se reduce a la vez [@brown2012, cap. 20, ej. 20.97]. Balancea la ecuación ajustando el medio con agua e iones hidróxido y comprueba que la suma de cargas se conserva [@brown2012, sec. 20.2].

Cuarto ejercicio: con zinc y níquel se construye una celda voltaica cuyas semiceldas son Zn²⁺/Zn y Ni²⁺/Ni [@brown2012, sec. 20.4]. Identifica ánodo y cátodo, el signo de cada electrodo, la dirección del flujo de electrones y de los iones del puente salino, y calcula el potencial estándar con la ecuación (@eq-e0-celda) [@brown2012, sec. 20.4].

Quinto ejercicio: decide si el ion Fe³⁺ oxida al cadmio metálico, sabiendo que el par Fe³⁺/Fe²⁺ tiene potencial estándar +0.771 V y que E°(Cd²⁺/Cd) = −0.403 V [@pauling1988, sec. 15-6]. Escribe la reacción global, calcula su potencial estándar y predice si avanza hacia los productos [@brown2012, sec. 20.4].

Sexto ejercicio: para la celda de zinc y níquel del cuarto ejercicio, calcula la energía libre estándar, la constante de equilibrio y el trabajo eléctrico máximo que entrega al consumirse un mol de zinc, usando las ecuaciones (@eq-dg-e) y (@eq-logk) y expresando los resultados en kilojulios por mol de reacción [@brown2012, sec. 20.5].

Séptimo ejercicio: la misma celda de zinc y níquel opera con [Ni²⁺] = 0.10 M y [Zn²⁺] = 2.0 M [@brown2012, sec. 20.6]. Calcula el cociente de reacción y el potencial con la ecuación de Nernst (@eq-nernst-298), y decide si el voltaje supera o queda por debajo del estándar [@brown2012, sec. 20.6].

Octavo ejercicio: dos semiceldas de zinc, una con [Zn²⁺] = 2.5 M y otra con 5.0 × 10⁻³ M, forman una celda de concentración [@brown2012, sec. 20.6]. Indica qué semicelda actúa como ánodo, calcula el potencial con la ecuación (@eq-nernst-298) y explica qué ocurre con las concentraciones al descargarse [@brown2012, sec. 20.6].

Noveno ejercicio: una corriente de 10.0 A circula durante 2.00 h por una celda electrolítica con iones Cr³⁺ [@brown2012, sec. 20.9]. Calcula con la ecuación (@eq-faraday) la masa de cromo depositada en el cátodo, tomando la masa molar del cromo como 52.0 g/mol [@brown2012, sec. 20.9].

Décimo ejercicio: dos celdas electrolíticas conectadas en serie depositan, la primera, plata desde Ag⁺ y la segunda, cobre desde Cu²⁺ [@pauling1988, sec. 15-4]. Si se depositan 2.16 g de plata, calcula la masa de cobre depositada y el tiempo necesario con una corriente de 1.00 A [@pauling1988, sec. 15-4].

## Solucionario

Primer ejercicio: el potasio aporta +1 y cada oxígeno −2, de modo que el cloro del KClO₃ debe ser +5 para que la suma de números de oxidación dé cero [@brown2012, sec. 20.1]. En el ion amonio cada hidrógeno vale +1 y, con carga total +1, el nitrógeno resulta −3 [@brown2012, sec. 20.1]. El permanganato, con cuatro oxígenos a −2 y carga −1, exige manganeso +7, el estado de oxidación máximo del elemento [@brown2012, sec. 20.1].

Segundo ejercicio: el bromuro se oxida a bromato cediendo seis electrones, Br⁻ + 3H₂O → BrO₃⁻ + 6H⁺ + 6e⁻, y el dicromato se reduce ganándolos, Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O [@brown2012, sec. 20.2]. Sumando y cancelando el agua y los protones comunes queda Cr₂O₇²⁻ + Br⁻ + 8H⁺ → 2Cr³⁺ + BrO₃⁻ + 4H₂O, con seis electrones transferidos: el bromo pasa de −1 a +5 y el cromo de +6 a +3 [@brown2012, sec. 20.2].

Tercer ejercicio: la oxidación I₂ + 12OH⁻ → 2IO₃⁻ + 6H₂O + 10e⁻ y la reducción I₂ + 2e⁻ → 2I⁻ se combinan multiplicando la segunda por cinco: 6I₂ + 12OH⁻ → 10I⁻ + 2IO₃⁻ + 6H₂O, que simplificada da 3I₂ + 6OH⁻ → 5I⁻ + IO₃⁻ + 3H₂O [@brown2012, sec. 20.2]. La suma de cargas se conserva: −6 a la izquierda y −5 − 1 = −6 a la derecha [@brown2012, sec. 20.2].

Cuarto ejercicio: el zinc, con E° = −0.76 V frente a −0.28 V del níquel, se oxida y es el ánodo negativo, mientras el níquel se reduce en el cátodo positivo [@brown2012, sec. 20.4]. Los electrones fluyen por el circuito externo del zinc al níquel, los cationes migran hacia el cátodo y los aniones hacia el ánodo, y el potencial estándar vale E° = −0.28 − (−0.76) = +0.48 V [@brown2012, sec. 20.4].

Quinto ejercicio: el cadmio se oxida cediendo dos electrones y el Fe³⁺ se reduce a Fe²⁺, de modo que la reacción global es 2Fe³⁺ + Cd → 2Fe²⁺ + Cd²⁺ con potencial E° = +0.771 − (−0.403) = +1.174 V [@pauling1988, sec. 15-6; @brown2012, sec. 20.4]. El voltaje positivo revela que el hierro(III) oxida al cadmio espontáneamente [@brown2012, sec. 20.4].

Sexto ejercicio: con n = 2 y E° = +0.48 V, la energía libre vale ΔG° = −2 × 96 485 × 0.48 = −92.6 kJ, y la constante, con log K = 2 × 0.48/0.0592 = 16.2, resulta K ≈ 1.7 × 10¹⁶ [@brown2012, sec. 20.5]. El trabajo eléctrico máximo coincide con ΔG° en valor absoluto, 92.6 kJ por mol de zinc, porque la celda descargada reversiblemente convierte toda la energía libre en trabajo [@brown2012, sec. 20.5].

Séptimo ejercicio: el cociente vale Q = 2.0/0.10 = 20, y el potencial, E = 0.48 − 0.0296 × log 20 = 0.48 − 0.0385 = 0.44 V [@brown2012, sec. 20.6]. El voltaje cae por debajo del estándar porque el producto Zn²⁺ abunda y el reactivo Ni²⁺ escasea, empujando la reacción hacia la izquierda [@brown2012, sec. 20.6].

Octavo ejercicio: el electrodo sumergido en la disolución diluida es el ánodo, pues el zinc metálico se disuelve buscando igualar concentraciones [@brown2012, sec. 20.6]. El potencial vale E = 0.0296 × log(2.5/0.005) = 0.0296 × 2.699 = 0.080 V, y al descargarse las dos concentraciones convergen mientras el voltaje cae a cero [@brown2012, sec. 20.6].

Noveno ejercicio: la carga total vale Q = It = 10.0 × 7200 = 7.20 × 10⁴ C, que con la ecuación (@eq-faraday) corresponde a 0.746 mol de electrones [@brown2012, sec. 20.9]. Cada ion Cr³⁺ exige tres electrones, de modo que se depositan 0.2487 mol de cromo, equivalentes a 0.2487 × 52.0 = 12.9 g [@brown2012, sec. 20.9].

Décimo ejercicio: la plata monovalente consume un electrón por átomo, de modo que 0.0200 mol de plata equivalen a 0.0200 mol de electrones [@pauling1988, sec. 15-4]. El cobre divalente deposita un átomo por cada dos electrones, 0.0100 mol, es decir 0.635 g, y el tiempo resulta t = 0.0200 × 96 485/1.00 = 1930 s, unos 32 minutos [@pauling1988, sec. 15-4].

## Resumen

La electroquímica convierte la energía de las reacciones redox en trabajo eléctrico, midiendo en voltios la fuerza impulsora que antes se expresaba como energía libre de Gibbs [@brown2012, cap. 20]. La oxidación, generalizada como pérdida de electrones, se balancea por semirreacciones que luego se combinan en la ecuación global [@brown2012, sec. 20.1-20.2]. En la celda voltaica, la oxidación ocurre en el ánodo y la reducción en el cátodo, conectados por un puente salino [@brown2012, sec. 20.3].

La escala de potenciales estándar nace del electrodo de hidrógeno y ordena oxidantes y reductores, mientras la ecuación de Nernst extiende las predicciones a cualquier concentración [@brown2012, sec. 20.4-20.6]. La energía libre, la constante de equilibrio y el trabajo máximo se entrelazan con el potencial mediante la constante de Faraday [@brown2012, sec. 20.5]. Baterías y celdas de combustible explotan estos principios, y la corrosión muestra su coste cuando el metal se disuelve sin permiso [@brown2012, sec. 20.7-20.8].

La electrólisis invierte el flujo con un voltaje externo, obteniendo metales activos desde fundentes y refinando los pasivos, y las leyes de Faraday cuantifican la masa transformada [@brown2012, sec. 20.9; @pauling1988, sec. 15-4]. El aluminio de Hall-Héroult y el cobre refinado ilustran la escala industrial del principio [@brown2012, sec. 20.9]. En suma, un solo marco, el de la transferencia de electrones, gobierna desde la batería del automóvil hasta la fotosíntesis [@atkins2015, cap. 4].
