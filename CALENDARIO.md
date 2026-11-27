# Calendario de contenido · Logística en 1 Minuto

**Público:** todo el mundo de habla hispana (no solo Uruguay). Montos siempre en dólares (USD); si un dato es de un país, se dice de cuál.

Serie principal: **Logística en 1 minuto**. Un concepto técnico por Short, explicado como lo explicaría un profesor de comercio exterior, con un dato verificable y fuente en el guion.

## Las 4 preguntas antes de cada video (obligatorio)

Antes de escribir el guion se responden en el propio guion.yaml, en el campo `chequeo`:

1. **¿Qué se lleva el espectador?** Una sola frase con lo que sabe o puede hacer después de verlo. Si no entra en una frase, el tema es demasiado grande: se divide.
2. **¿Qué tan útil es? (1 a 5)** 5 = le resuelve un problema o una duda real hoy. Por debajo de 4 se reescribe o se cambia el tema.
3. **¿Qué tan llamativo es? (1 a 5)** El gancho de los primeros 2 segundos: ¿alguien deja de deslizar? Por debajo de 4 se reescribe el gancho.
4. **¿Aprendí algo yo con este video?** Autocrítica del que lo escribe: si el guion solo dice lo que cualquiera ya sabe o lo que sale en el primer resultado de Google, no alcanza. Tiene que tener al menos un dato, una regla o un error típico que sorprenda incluso a alguien que ya sabe del tema. Se anota cuál es; si no hay, se investiga más o se cambia el tema.

Ejemplo:
```yaml
chequeo:
  se_lleva: "Calcular el peso volumétrico de su caja antes de pagar un envío."
  util: 5
  llamativo: 4
  gancho: "Te cobraron más de lo que pesa tu caja."
  aprendi: "Cada empresa usa su propio divisor (5000 o 6000), y eso cambia el precio."
```

Autocrítica de los primeros videos (2026-11-03), con esta regla: 003 (dígito de control) y 004 (en CIF el riesgo pasa en origen aunque el vendedor pague el seguro) la pasan. 002 (viaje del celular) es el más flojo: solo deja el dato del avión y no deja ninguna acción; no se repite ese formato de recorrido general.

## Reglas de calidad (crítica interna antes de producir)

1. **Gancho en la primera frase:** una pregunta o un dato que sorprenda. Nada de introducciones. **El gancho dice qué pierde o qué paga el espectador** (plata, carga, tiempo): "¿quién pierde?", "te cobran", "pagás el doble". Nada de ganchos de lista o descriptivos ("6 X que tenés que conocer", "¿carga el doble?"). **El texto grande del primer cuadro nombra el tema** (la cosa: contenedor, autoelevador, seguro, flete) además de la consecuencia; nada de preguntas sueltas que no dicen de qué se habla ("¿QUIÉN TE LA PAGA?"), ni de "el dato que…" sin el dato. *(Revisión 2026-11-09, datos de Instagram: el 004 "Si el barco se hunde, ¿quién pierde?" fue el mejor: 141 vistas y 52,6 % pasó los 3 s. Los descriptivos rindieron peor: 007 "¿carga el doble?" 18,3 % pasó los 3 s; 006 "6 contenedores" 3,8 s de promedio; 002 "el viaje" 3,6 s. Revisión 2026-11-16: el 010 "AVERÍA GRUESA: tu carga llegó sana y pagás igual" tuvo el mejor paso de los 3 s hasta ahora (81,8 %) y 12,2 s de promedio (33 % del video), con solo 15 vistas. Revisión 2026-11-23, Instagram del 16 al 22/11: los dos reels que Instagram repartió abrían nombrando el objeto: 014 "SIN VGM, NO EMBARCA" (91 vistas, 66,2 % deslizó, 7,9 s de promedio) y 055 "¿AUTOELEVADOR O TRANSPALETA?" (114 vistas, 77,7 % deslizó). Los que abrían con algo vago casi no se mostraron: 011 "¿QUIÉN TE LA PAGA?" 7 vistas y 85,7 % deslizó; 052 "LA FACTURA VINO MÁS CARA" 2 vistas y 100 %. Son muestras chicas: es una tendencia, no una prueba.)*
2. **Un concepto por video.** Si hacen falta dos, son dos videos.
3. **Un dato concreto y con fuente** en cada video: un número, una norma, un caso real.
4. **Visual que explica:** códigos resaltados, cifras grandes, comparaciones. El texto en pantalla aporta, no repite la voz.
5. **Menos de 50 segundos, medido en el MP4 final** (`ffprobe`), no en el guion. Si pasa de 50 s, se cortan escenas antes de programar. Máximo 7 escenas con narración. *(Revisión 2026-11-02: el 003 salió con 62 s y 9 escenas; en Instagram la gente lo miró 9,3 s en promedio, un 15 %.)*
6. **Nada que no esté verificado.** Ante la duda, el dato se saca.
7. **Siempre instructivo y útil.** Cada video responde una duda o resuelve un problema real que alguien tuvo (desde enviar un paquete hasta almacenarlo o importar). Tiene que dejar una acción concreta: un paso, una regla o una cuenta que el espectador puede aplicar hoy. Nada de curiosidades sueltas ni temas fuera de logística y comercio exterior.
8. **Música de fondo original** (generada por pipeline/musica.py, sin derechos de terceros), baja debajo de la voz. Se desactiva con musica: false en el guion.
9. **Título:** las dos primeras palabras son las que se ven al deslizar: van en MAYÚSCULAS y son la palabra clave fuerte del tema (ej.: "INCOTERM PELIGROSO: DDP te puede fundir 💸"). Corto, un emoji, y deja curiosidad: no explica todo.
10. **Hashtags: 4 como máximo**, #Shorts primero y 3 del tema exacto. Nada de hashtags genéricos ni de relleno (#viral, #fyp): YouTube los toma como spam.
11. **Horario:** 19:00 por defecto. Cuando haya 3 semanas de datos, el resumen semanal prueba otro horario y decide con números (no con consejos de terceros). *(2026-11-23: todavía no se prueba. De las 3 semanas, una (9–15/11) casi no tuvo publicaciones por el límite de Metricool, y sin datos por video de YouTube no se puede comparar un horario contra otro. Se revisa cuando haya 2 semanas seguidas publicando todos los días y vidIQ con créditos.)*
12. **Primeros 3 segundos:** imagen que se mueve + la frase gancho en pantalla desde el primer cuadro. Nada de logo, saludo ni pausa al inicio. Es lo que decide si deslizan. **El clip de la primera escena es nuevo en cada video y muestra el objeto del tema** (el contenedor, el autoelevador, la caja, el camión): nunca el mismo clip de apertura que ya usó otro video publicado, y nunca un clip genérico (billetes, firma de papeles, calculadora) como apertura. Los clips reutilizados pueden ir en las escenas del medio. Antes de programar se compara el `clip` de la primera escena con los guiones de `contenido/`. *(Revisión 2026-11-23, Instagram del 16 al 22/11: los dos reels que se repartieron abrían con un clip que nunca había abierto otro video: 055 (transpaleta, 7019231) 114 vistas y 014 (barco cargándose, 10451891) 91. Los cuatro que abrían con un clip repetido casi no se mostraron: 011, 013 y 036 abrían los tres con el mismo barco (11336230) y tuvieron 7, 7 y 3 vistas; 052 abría con billetes (6700011) y tuvo 2. Ojo: ya programados con apertura repetida, 046 (6700011, igual que el 052), 057 (10622135, igual que 004, 005 y 010), 016 (10451891, igual que el 014) y 015 (6342195, igual que el 044): sirven para confirmar o descartar esta regla.)*
13. **Llamado a seguir atado al contenido:** además del cierre, cuando el video tiene una lista o un remate, pedir que sigan ANTES del remate y conectado al tema ("Seguí la cuenta: el tercer error es el que más plata cuesta"). Nunca al principio.
14. **Primero el empaque:** título y gancho se escriben ANTES que el guion. Si el título no entusiasma, se cambia la idea, no se fuerza el guion.
15. **Nunca borrar un video con advertencia o strike:** se apela desde YouTube Studio. Borrarlo elimina la posibilidad de apelar.
16. **Cumplir la promesa del título en los primeros segundos** (MrBeast: la gente se va cuando el video no es lo que prometía el título). Nada de "hoy te voy a contar": se empieza mostrando.
17. **Remate y corte.** Cuando llega la respuesta, el video termina enseguida: el cierre es una sola frase. Un final largo hace que deslicen antes de que el video cuente como visto completo.
18. **Rotar formatos:** no repetir la misma serie más de 3 días seguidos (conceptos, problemas reales, guías rápidas).
19. **Links en la descripción:** aplicar la sección "Producto propio y afiliados" de este archivo en cada video (YouTube, TikTok, Instagram y Pinterest).
20. **Programado no es publicado.** Antes de producir, la tarea diaria revisa en Metricool (getScheduledPosts) el estado de todo lo programado en los días anteriores, en cada red. Si alguna dice ERROR: no se produce un video nuevo, se anota el error exacto en el registro, se avisa al propietario y la próxima publicación es el video más viejo que quedó sin salir. En el registro se escribe "programado" solo cuando Metricool lo aceptó, y "publicado" solo cuando el estado dice PUBLISHED. *(Revisión 2026-11-16: del 10/11 20:30 al 15/11 Metricool rechazó todo con "You have reached your Metricool account limit" y la tarea siguió produciendo y anotando "programado" durante 6 días sin que saliera nada.)*

21. **Publicar con vidIQ mientras Metricool esté bloqueado** (decisión del propietario, 2026-11-16; reemplaza el paso "Programá en Metricool" de las tareas diaria y de largos para YouTube, Instagram y TikTok; el pin de Pinterest sigue en Metricool). Si hay videos del atraso sin publicar, se programa primero el más viejo por vidIQ en lugar de producir uno nuevo (regla 20). vidIQ publica y programa gratis (0 créditos) en YouTube, Instagram y TikTok. Pasos: `vidiq_video_upload` con la URL pública del MP4 (máx. 299 MB) → miniatura con `vidiq_upload_image` (URL pública que responda 200 directo; las del release redirigen y fallan: para los largos, copiar el .jpg del release a miniaturas/LNN-tema-corto.jpg en main y usar la URL de raw.githubusercontent.com) → `vidiq_social_post_draft_create` (YouTube: título, `privacyStatus: public`, `categoryId: 27` = Educación, tags, `publishAt` con zona -03:00) → `vidiq_social_post_publish` → `vidiq_social_post_status` hasta que diga programado. Cuentas conectadas en vidIQ (2026-11-16, canPublish true): YouTube `UCYGlvUEFxyuPxuEhiAX9bbA`, Instagram `29759225183685543` (@logisticaen1minuto) y TikTok `_000ImZ-S5jGvapBHzJjWlRKWIAEgr_cTDNb`. Pinterest no está en vidIQ: queda en Metricool. Un post programado en vidIQ no se puede cancelar desde la tarea: revisar todo antes de publicar. **Por qué:** el plan gratis de Metricool permite 20 publicaciones por mes y el canal hace unas 40 (Short en 3 redes + pin + largos). Plan elegido sin pagar: vidIQ para YouTube, Instagram y TikTok; Metricool solo para el pin de Pinterest (cuando se renueve el cupo mensual). TikTok (confirmado por el propietario el 2026-11-16, regla fija): privacyLevel PUBLIC_TO_EVERYONE, allowComment true, musicUsageConfirmed true, isAiGenerated false. Instagram: el Reel va con el mismo texto (máx. 2.200 caracteres) y hashtags sin #Shorts. YouTube va en un post y Instagram + TikTok en otro, a la misma hora.

22. **Mirar qué funciona antes de escribir** (pedido del propietario, 2026-11-17). Cada tarea, antes de elegir el gancho: buscar 3 a 5 videos del nicho que estén rindiendo esa semana (vidIQ `vidiq_outliers`/`vidiq_trending_videos` si hay créditos; si no, WebSearch). Anotar en el guion, en `chequeo.referencia`, el MECANISMO que se toma (tipo de gancho, estructura, fórmula de título), nunca el texto. Prohibido copiar guiones, frases, imágenes o videos de otros canales: además de los derechos de autor, YouTube no monetiza el contenido reutilizado. Mecanismos que hoy tienen evidencia (análisis 2026-11-17, claude/analisis-competencia-2026-11-17.md en el proyecto):
    - **Plata que perdés + contraste** en los primeros 3 s (nuestro 010: 81,8 % pasó los 3 s; el 009 sin plata en el gancho: 0 %).
    - **Desmentir lo que te dijeron** ("te cotizan hasta el puerto… y después aparecen los costos").
    - **Pregunta con número concreto** en el título ("¿Cuánto pagás hoy…?", "¿Por qué subió…?").
    - **Noticia del nicho explicada en días** (Ormuz y Bab el-Mandeb, recargos de guerra, régimen de franquicias de Uruguay y Argentina): el que la explica primero se lleva las vistas. Siempre con fuente oficial y fecha.
    - **Serie reconocible** con el mismo prefijo en el título (ej.: "LO QUE PAGÁS:").
    - **TubeAlfred conectado (2026-11-17):** 50 créditos gratis por mes (se renuevan en la fecha de registro, no se acumulan). 1 crédito por búsqueda, video o transcripción; los comentarios cuestan 20 o más, solo con OK del propietario. Uso: el resumen semanal hace UNA búsqueda por tema (`youtube_search_query`, sort popularity, upload_date week o month) y anota los mecanismos; las tareas diarias no gastan créditos de TubeAlfred.
    - Lo que NO se puede ver de otros canales: su retención por segundo (es privada). La retención se mide en los nuestros, en el resumen semanal.

## Temas (en orden de producción)

### Orden para la semana del 30/11 al 6/12 (resumen semanal 2026-11-23)

Datos de la semana 16–22/11: los reels que Instagram repartió fueron los de un objeto que se ve (014 VGM, contenedor y balanza: 91 vistas; 055 autoelevador o transpaleta: 114). Los de papeles y cargos (052 flete, 036 documentos, 013 demurrage, 011 seguro) tuvieron entre 2 y 7 vistas. Esta semana se prueba si se repite: se intercalan temas con un objeto físico en el primer cuadro (serie 3 y serie 1) con la serie 2, siempre con gancho de plata (regla 1) y clip de apertura nuevo (regla 12).

1. 30/11: 028 PICKING EQUIVOCADO (serie 2) **[programado]**.
2. 1/12: 051 PALLET (serie 3): el pallet mal armado que se cae en el camión; medidas, cómo apilar y el error a evitar. Apertura: un pallet o un camión cargándose. **[programado: PALLET TRABADO, apertura 4292301]**
3. 2/12: 029 MERCADERÍA VENCIDA (serie 2): FEFO, con un número de plata perdida. Apertura: estantería con producto, no billetes. **[programado: MERCADERÍA VENCIDA, apertura 5738746]**
4. 3/12: 017 REEFER (serie 1, cadena de frío): qué pasa si se corta el frío y quién paga. Apertura: contenedor refrigerado. **[programado: CONTENEDOR REFRIGERADO, apertura 6618335 (autoelevador con contenedor), nunca usada para abrir; sin créditos de vidIQ para un clip de reefer]**
5. 4/12: 050 ALMACENAR EN ALTURA (serie 3): lo pesado abajo y la capacidad de la estantería por nivel. Apertura: estanterías. **[programado: ESTANTERÍA INDUSTRIAL, apertura 6194507 (autoelevador frente a estantería alta), nunca usada para abrir]**
6. 5/12: 033 CARGA MAL ARMADA (serie 2): llegó roto por cómo se cargó el camión. Sin repetir el 015 (aquel era el contenedor y el seguro; este es el camión y el reparto).
7. 6/12: libre para una noticia del nicho (regla 22) o 045 ENVIAR AL EXTERIOR (serie 3).

**Clips:** vidIQ vuelve a tener 150 créditos el 30/11 a la noche (hora de Uruguay). Usarlos primero en clips de apertura nuevos (regla 12), no en investigación. El resumen del 30/11 corre antes de que se renueven: tampoco va a tener datos por video de YouTube.

### Orden para la semana del 17 al 23/11 (resumen semanal 2026-11-16; actualizado 2026-11-18)

**Del 10/11 a la noche al 16/11 no se publicó nada** porque Metricool rechazó todo con "You have reached your Metricool account limit". **Resuelto el 16–17/11:** se publica por vidIQ (regla 21) y Metricool queda solo para el pin de Pinterest.

1. **[Resuelto 2026-11-17]** Se vuelve a publicar por vidIQ; se producen Shorts y largos nuevos con normalidad.
2. **[Hecho 2026-11-17]** Atraso programado por vidIQ, uno por día a las 19:00: 014 (17/11), 052 (18/11), 013 (19/11), 036 (20/11), 055 (21/11), 011 (22/11) y 031 (23/11); largos L03 (17/11) y L02b (20/11) a las 20:30.
3. **[Hecho]** Los cupones LANZAMIENTO y DEPOSITO7 vencieron el 18/11 y ya no van en ninguna descripción.
4. **Prioridad de noticias (2026-11-17, regla 22):** Short 046 IMPUESTO TEMU **[hecho, programado 24/11]**; Short 057 RECARGO ORMUZ (recargo de guerra vs. recargo de emergencia por combustible) **[hecho, programado 25/11]**. Largo L03c **[hecho, publicado 21/11 20:30]**.
5. **Próximos Shorts**, rotando series y con gancho de plata: 037 (demurrage por tramos, serie 2) **[hecho, programado 26/11]** → 053 (conteo cíclico, serie 3) **[hecho, programado 27/11]** → 016 (mercancías peligrosas, serie 1) **[hecho, programado 28/11]** → 015 (trincaje, serie 1; segundo día seguido de la serie, dentro de la regla 18) **[hecho, programado 29/11]**. El próximo día libre después es el 30/11: 028 (errores de picking, serie 2; el 027 se saltea esta semana para no repetir tema con el 053) **[hecho]**.

El 037 queda después del 013 para no repetir tema la misma semana.

| # | Tema | Gancho | Estado |
| --- | --- | --- | --- |
| 002 | El viaje de tu celular | Muchos celulares caros vuelan, no navegan | Publicado (2026-11-02) |
| 003 | Qué significan las letras de un contenedor (ISO 6346) | Si sabés leerlo, sabés de quién es | Publicado (2026-11-01) |
| 004 | Incoterms: EXW, FOB y CIF | ¿Quién paga si el barco se hunde? | Publicado (2026-11-03) |
| 005 | Incoterms: DAP y DDP | El Incoterm que te puede fundir | Publicado (2026-11-04) |
| 006 | Tipos de contenedor: dry, high cube, reefer, open top, flat rack, tanque | No todos los contenedores son iguales | Publicado (2026-11-05) |
| 007 | TEU y FEU: ¿20 o 40 pies? (peso ÷ volumen) | Un 40 pies carga menos peso que uno de 20 | Publicado (2026-11-06) |
| 008 | El Bill of Lading | El papel que vale lo mismo que la mercadería | Publicado (2026-11-08 19:00) |
| 009 | Certificado de origen (se enfocó en uno: factura comercial y packing list quedan para el 036) | Sin el certificado, pagás arancel completo | Publicado (2026-11-09 19:00) |
| 010 | Avería gruesa | Tu carga llegó perfecta y igual te cobran | Publicado (2026-11-10 19:00) |
| 011 | Seguro de carga: cláusulas A, B y C | ¿Qué pasa si se pierde mi mercadería? | Publicado (2026-11-22 19:00 por vidIQ en YouTube, Instagram y TikTok) |
| 012 | Contenedores que caen al mar | Cuántos se pierden por año | Pendiente (se pasó el 2026-11-16: solo como cifra es una curiosidad sin acción y útil < 4; retomarlo solo con un enfoque útil, por ejemplo qué hacer si tu contenedor es uno de ellos, sin repetir 010 y 011) |
| 013 | Demurrage y detention | La multa que te cobra la naviera por día | Publicado (2026-11-19 19:00 por vidIQ en YouTube, Instagram y TikTok) |
| 014 | VGM (SOLAS): pesar el contenedor | Sin este número, tu contenedor no sube | Publicado (2026-11-17 19:00 por vidIQ en YouTube, Instagram y TikTok) |
| 015 | Trincaje de contenedores (enfoque: si cargás vos, el seguro no cubre la mala estiba; cuentas del CTU Code) | TRINCAJE CASERO: llegó roto y el seguro no paga | Programado 2026-11-29 19:00 por vidIQ en YouTube, Instagram y TikTok (32 s; pin de Pinterest 19:05 en Metricool) |
| 016 | Mercancías peligrosas: clases IMO (enfoque: carga mal declarada y la sección 14 de la SDS) | CARGA PELIGROSA: era perfume y pagás 5.000 | Programado 2026-11-28 19:00 por vidIQ en YouTube, Instagram y TikTok (35 s; pin de Pinterest 19:05 en Metricool) |
| 017 | Cadena de frío (enfoque: el reefer mantiene, no enfría; preenfriar y °C vs °F) | CONTENEDOR REFRIGERADO: no enfría tu carga | Programado 2026-12-03 19:00 por vidIQ en YouTube, Instagram y TikTok (34 s; https://www.youtube.com/watch?v=t8LxW63aMio; pin de Pinterest 19:05 en Metricool) |
| 018 | Despachante de aduana y forwarder | Quién hace qué en una importación | Pendiente |
| 019 | Zona franca (caso Uruguay) | Comprar, guardar y no pagar impuestos todavía | Pendiente |
| 020 | Canal de Panamá y la sequía | Cuando falta agua, el comercio frena | Pendiente |
| 021 | El Ever Given en el canal de Suez | Un barco trabado frenó al mundo | Pendiente |
| 022 | Mar Rojo y el desvío por el Cabo de Buena Esperanza | Por qué tus compras tardan más | Pendiente |
| 023 | Cross docking | La mercadería que nunca se guarda | Pendiente |
| 024 | FIFO y FEFO en un depósito | El orden que evita tirar mercadería | Pendiente |
| 025 | El costo del picking | La parte más cara del depósito | Pendiente |
| 026 | Última milla | El tramo más caro del viaje | Pendiente |

Los temas de costos de aduana van por país (Uruguay, Argentina, México), con tasas verificadas en la fuente oficial de cada aduana al momento de producir.

## Serie 2: Problemas reales y cómo se resuelven

Formato: **problema → causa → solución**. Un problema típico de un área logística, por qué pasa y los pasos concretos para resolverlo, con el tono de un jefe de logística que ya lo vivió. Gancho: el síntoma que el espectador reconoce ("¿Te pasa que…?"). La solución tiene que ser aplicable y, cuando haya cifras, con fuente. Se produce después de terminar la serie 1 (o se intercala si el resumen semanal muestra que rinde mejor).

| # | Área | Problema | Gancho | Estado |
| --- | --- | --- | --- | --- |
| 027 | Depósito | Diferencias de inventario | El sistema dice 100 y en la estantería hay 87 | Pendiente |
| 028 | Depósito | Errores de picking (enfoque: separar los parecidos y dígito de control en la ubicación, que hay que cambiar) | PICKING EQUIVOCADO: pagás 3 envíos por un pedido | Programado 2026-11-30 19:00 por vidIQ en YouTube, Instagram y TikTok (34 s; pin de Pinterest 19:05 en Metricool) |
| 029 | Depósito | Mercadería vencida (enfoque: FIFO por entrada falla, FEFO y la regla del tercio de Japón) | MERCADERÍA VENCIDA: entró última y vence primero | Programado 2026-12-02 19:00 por vidIQ en YouTube, Instagram y TikTok (33 s; https://www.youtube.com/watch?v=ObsZeINg3k4; pin de Pinterest 19:05 en Metricool) |
| 030 | Recepción | Camiones esperando en la puerta | Tres horas para descargar un camión | Pendiente |
| 031 | Recepción | Recibir sin controlar contra la orden de compra | Pagaste mercadería que nunca entró | Programado 2026-11-23 19:00 por vidIQ en YouTube, Instagram y TikTok (falló antes en Metricool; sin cupones) |
| 032 | Despacho | Pedidos que salen tarde | El camión se fue y el pedido quedó | Pendiente |
| 033 | Despacho | Carga mal armada en el camión | Llegó roto por cómo se cargó | Pendiente (orden 30/11–6/12: 5/12) |
| 034 | Transporte | Rutas de reparto mal armadas | Tu camión recorre el doble de lo necesario | Pendiente |
| 035 | Transporte | Entregas fallidas en última milla | Fue, no había nadie, y vuelve mañana | Pendiente |
| 036 | Importación | Carga trabada en aduana por documentos | Un error en la factura y la carga no sale | Publicado (2026-11-20 19:00 por vidIQ en YouTube, Instagram y TikTok) |
| 037 | Importación | Demurrage por retirar tarde el contenedor (enfoque: la tarifa sube por tramos) | DEMURRAGE POR TRAMOS: calculaste 3.900 y pagás 4.700 | Programado 2026-11-26 19:00 por vidIQ en YouTube, Instagram y TikTok (36 s; pin de Pinterest 19:05 en Metricool) |
| 038 | Inventario | Quiebres de stock | Tenés de todo, menos lo que se vende | Pendiente |
| 039 | Inventario | Sobrestock | Plata parada en la estantería | Pendiente |
| 040 | Gestión | Medir sin KPIs | Si no lo medís, no lo podés mejorar | Pendiente |
| 041 | Seguridad | Accidentes con autoelevadores | El riesgo número uno del depósito | Pendiente |
| 042 | Devoluciones | Logística inversa desordenada | Las devoluciones que se comen el depósito | Pendiente |

## Serie 3: Cómo hacerlo (guías rápidas para cualquiera)

Formato: **la duda → los pasos → el error a evitar**. Para personas y pequeños negocios, no solo profesionales. El público es TODO el mundo de habla hispana, no solo Uruguay: los videos explican primero la regla general (que sirve en cualquier país) y, cuando algo depende del país, se aclara en pantalla y se da un ejemplo de uno o varios países (Uruguay, Argentina, México, Colombia, Chile, España) con datos oficiales verificados al producir. Se intercala con las otras series (por ejemplo, uno de cada tres videos) cuando el resumen semanal lo justifique.

| # | Duda | Gancho | Estado |
| --- | --- | --- | --- |
| 043 | Cómo embalar un paquete para que llegue sano | El 80 % de lo que se rompe, se rompe por cómo se embaló | Pendiente (verificar cifra o sacar) |
| 044 | Peso volumétrico: cómo se calcula | Te cobraron más de lo que pesa tu caja | Publicado (2026-11-07 19:00; se intercaló por la regla 18: 004 a 007 fueron 4 días seguidos de la serie 1) |
| 045 | Cómo enviar un paquete al exterior desde Uruguay | Lo que nadie te dice antes de ir al correo | Pendiente (orden 30/11–6/12: 6/12 si no hay noticia) |
| 046 | Compras en el exterior y franquicia (Uruguay) | IMPUESTO TEMU: comprás 15 y pagás 20 | Programado 2026-11-24 19:00 por vidIQ en YouTube, Instagram y TikTok (39 s; pin de Pinterest 19:05 en Metricool) |
| 047 | Cómo leer el rastreo de un envío | "En tránsito" hace una semana: qué significa | Pendiente |
| 048 | Qué no se puede enviar (mercancías prohibidas y peligrosas) | Las baterías que te frenan el paquete | Pendiente |
| 049 | Cómo ordenar un depósito chico | Encontrar cualquier cosa en 30 segundos | Pendiente |
| 050 | Cómo almacenar en altura sin riesgo (enfoque: la capacidad del bastidor depende del hueco más grande entre niveles; cartel de carga; lo pesado abajo) | ESTANTERÍA INDUSTRIAL: subís un nivel y aguanta 38 % menos | Programado 2026-12-04 19:00 por vidIQ en YouTube, Instagram y TikTok (30 s; https://www.youtube.com/watch?v=mcJWBsMqb0Y; pin de Pinterest 19:05 en Metricool) |
| 051 | Pallet: cómo armarlo (enfoque: apilado en columna vs. cruzado y cajas que sobresalen) | PALLET TRABADO: más firme y se aplasta | Programado 2026-12-01 19:00 por vidIQ en YouTube, Instagram y TikTok (36 s; pin de Pinterest 19:05 en Metricool) |
| 052 | Cómo cotizar un flete | Tres datos que te pide cualquier transportista | Publicado (2026-11-18 19:00 por vidIQ en YouTube, Instagram y TikTok) |
| 053 | Cómo hacer un inventario sin parar la operación | CONTEO CÍCLICO: cerrás un día y el stock igual falla | Programado 2026-11-27 19:00 por vidIQ en YouTube, Instagram y TikTok (33 s; pin de Pinterest 19:05 en Metricool) |
| 054 | Cómo importar por primera vez | Los pasos, en orden | Pendiente |
| 055 | ¿Autoelevador o transpaleta? La pregunta que decide | Comprar el equipo equivocado te come el capital | Publicado (2026-11-21 19:00 por vidIQ en YouTube, Instagram y TikTok) |
| 056 | Cuánto espacio necesitás para arrancar un depósito | El error de alquilar de más (o de menos) | Pendiente |
| 057 | Recargo de guerra vs. recargo de emergencia por combustible (prioridad 4 del 17/11) | RECARGO ORMUZ: tu barco no pasa y pagás igual | Programado 2026-11-25 19:00 por vidIQ en YouTube, Instagram y TikTok (35 s; pin de Pinterest 19:05 en Metricool) |


## Videos largos (horizontales, 8 a 10 minutos)

**Por qué son la prioridad:** es la plata real del canal. Desde el 1/2/2027 los nuevos canales necesitan el doble para monetizar (8.000 horas o 20 millones de vistas de Shorts), y hasta los que ya están en el programa dejan de cobrar por Shorts si no hacen 10 millones de vistas en 90 días; los videos largos siguen pagando. Objetivo: entrar al programa ANTES del 1/2/2027 (hoy: 1.000 suscriptores + 4.000 horas, o 10 M de vistas de Shorts). Ritmo: un video largo por semana.

Reglas extra para largos (guía de producción de MrBeast): el primer minuto es el más importante (cumplir la promesa del título y mostrar lo que viene); un nuevo gancho cada 2 a 3 minutos ("y lo que viene ahora es lo que más plata hace perder"); lo más explicativo va en la segunda mitad; terminar apenas llega el remate.

Para sumar horas de reproducción y cobrar más por vista. Cada uno junta y amplía los Shorts de un mismo tema, con capítulos, miniatura propia y un llamado a suscribirse a mitad del video (antes de la parte más útil). Mínimo 8 minutos (desde ahí YouTube permite anuncios a mitad del video). Formato en guion.yaml: `formato: largo`, campos `capitulo` en las escenas y `miniatura: {arriba, abajo}`. Se renderizan como release `largos` del repositorio.

| # | Tema | Estado |
| --- | --- | --- |
| L01 | Incoterms 2020: los 11 explicados y los 5 errores que te hacen perder plata | Publicado (2026-11-04 20:30, 8:04 min; falta la miniatura) |
| L02 | Contenedores: tipos, medidas, TEU y cómo elegir 20 o 40 pies | Publicado (2026-11-06 20:30, 8:32 min) |
| L03 | PRIMERA IMPORTACIÓN: los 7 pasos para importar a Uruguay sin pagar de más | Publicado (2026-11-17 20:30 por vidIQ, post a3caace6; la copia de Metricool quedó como borrador). No se produjo L04 (regla 20) |
| L02b | AUTOELEVADOR O TRANSPALETA: cómo elegir el equipo de tu depósito sin gastar de más | Publicado (2026-11-20 20:30 por vidIQ en YouTube) |
| L03c | IMPUESTO TEMU: ¿cuánto pagás hoy por comprar afuera desde Uruguay? (franquicias, IVA, 60 %, la cuenta y 6 errores) | Publicado (2026-11-21 20:30 por vidIQ, 8:46 min; https://www.youtube.com/watch?v=TKUV6IrfTv0, post 9cd99759) |
| L04 | DEPÓSITO CARO: los 10 problemas que te hacen perder plata y cómo resolver cada uno | Programado 2026-11-24 20:30 por vidIQ (8:49 min; https://www.youtube.com/watch?v=GMcGkiCtT5w, post 9d4a6ef0) |
| L05 | DEMURRAGE Y DETENTION: cuánto pagás por cada día de contenedor y cómo no pagarlo | Programado 2026-11-27 20:30 por vidIQ (8:44 min; https://www.youtube.com/watch?v=f6MToZG0U0U, post ed3bce7d) |
| L06 | EXPORTAR DESDE Uruguay por primera vez: pasos, documentos y certificado de origen | Pendiente |
| L07 | INVENTARIO SIN errores: cómo hacer un conteo cíclico en tu depósito paso a paso | Pendiente |
| L08 | FLETE INTERNACIONAL: cómo leer una cotización línea por línea (BAF, THC, recargos) y comparar dos ofertas | Pendiente |
| L09 | CERTIFICADO DE ORIGEN Mercosur: cuándo te ahorra el arancel, cómo se pide en Uruguay y los errores que lo invalidan | Pendiente |
| L10 | SEGURO DE CARGA: cuánto cuesta, qué cubre cada cláusula (A, B, C) y cómo reclamar un daño paso a paso | Pendiente |

## Producto propio y afiliados (links para las descripciones)

- **Producto propio** (guía "Sin errores en comercio exterior" + comparador de costos, USD 7, Hotmart ID 8887961, ACTIVO desde 2026-11-04): https://go.hotmart.com/M108343404O?dp=1
  - Va en la PRIMERA línea de la descripción de todo video sobre Incoterms, costos de importación, aduana, importar o seguros de carga: "📘 Guía práctica + planilla para comparar cotizaciones: https://go.hotmart.com/M108343404O?dp=1". En el resto de los videos, al final de la descripción.
  - Cupón LANZAMIENTO: vencido el 2026-11-18. No mencionarlo más.
  - En videos largos, mencionarlo una vez en el cierre ("el link está en la descripción"), sin exagerar promesas.
- **Producto propio 2** (guía "Tu primer depósito" + planilla de arranque, USD 10, Hotmart ID 8890964, ACTIVO desde 2026-11-04): https://go.hotmart.com/U108348887Q?dp=1
  - Va en la PRIMERA línea de la descripción de todo video sobre depósitos, almacenamiento, estanterías, autoelevadores, transpaletas, layout, inventario o arrancar un negocio logístico (por ejemplo 055, 056 y L02b): "📗 Guía + planilla para armar tu primer depósito: https://go.hotmart.com/U108348887Q?dp=1". En esos videos va este producto y no el de Incoterms.
  - Cupón DEPOSITO7: vencido el 2026-11-18. No mencionarlo más.
- **Afiliado: Mega Logística Internacional** (CAMEX, Hotmart desde 2018; USD 49,54; comisión 60 %): https://go.hotmart.com/M108343505U
  - Usarlo solo en videos de logística internacional o transporte. Va al final de la descripción como: "Curso recomendado de logística internacional (link de afiliado): …".
  - Siempre aclarar que es un link de afiliado. Nunca prometer resultados ni usar la marca Hotmart. Nada de spam en WhatsApp ni Telegram (reglas de Hotmart).
- **Afiliado: Mega de Comercio Exterior** (CAMEX, Hotmart ID 1522260, afiliación confirmada): https://go.hotmart.com/P108344299F
  - Usarlo en videos de importar, exportar, aduana, Incoterms o costos de importación. Va al final de la descripción como: "Curso recomendado de comercio exterior (link de afiliado): https://go.hotmart.com/P108344299F".
  - No poner los dos cursos CAMEX en el mismo video: logística internacional o transporte → Mega Logística; comercio exterior o aduana → Mega de Comercio Exterior.
- **Ghost Importer** (ID 2291543): afiliación solicitada el 04/11, esperando aceptación del productor. No usar hasta que esté confirmada.
