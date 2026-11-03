# Calendario de contenido · Logística en 1 Minuto

Serie principal: **Logística en 1 minuto**. Un concepto técnico por Short, explicado como lo explicaría un profesor de comercio exterior, con un dato verificable y fuente en el guion.

## Reglas de calidad (crítica interna antes de producir)

1. **Gancho en la primera frase:** una pregunta o un dato que sorprenda. Nada de introducciones.
2. **Un concepto por video.** Si hacen falta dos, son dos videos.
3. **Un dato concreto y con fuente** en cada video: un número, una norma, un caso real.
4. **Visual que explica:** códigos resaltados, cifras grandes, comparaciones. El texto en pantalla aporta, no repite la voz.
5. **Menos de 50 segundos, medido en el MP4 final** (`ffprobe`), no en el guion. Si pasa de 50 s, se cortan escenas antes de programar. Máximo 7 escenas con narración. *(Revisión 2026-11-02: el 003 salió con 62 s y 9 escenas; en Instagram la gente lo miró 9,3 s en promedio, un 15 %.)*
6. **Nada que no esté verificado.** Ante la duda, el dato se saca.
7. **Siempre instructivo.** Cada video enseña algo que el espectador puede aplicar o entender mejor de la logística. Nada de curiosidades sueltas ni temas fuera de logística y comercio exterior.
8. **Música de fondo original** (generada por pipeline/musica.py, sin derechos de terceros), baja debajo de la voz. Se desactiva con musica: false en el guion.

## Temas (en orden de producción)

| # | Tema | Gancho | Estado |
| --- | --- | --- | --- |
| 002 | El viaje de tu celular | Muchos celulares caros vuelan, no navegan | Programado (2026-11-02 19:00) |
| 003 | Qué significan las letras de un contenedor (ISO 6346) | Si sabés leerlo, sabés de quién es | Publicado (2026-11-01) |
| 004 | Incoterms: EXW, FOB y CIF | ¿Quién paga si el barco se hunde? | Programado (2026-11-03 19:00) |
| 005 | Incoterms: DAP y DDP | El Incoterm que te puede fundir | Programado (2026-11-04 19:00) |
| 006 | Tipos de contenedor: dry, high cube, reefer, open top, flat rack, tanque | No todos los contenedores son iguales | Programado (2026-11-05 19:00) |
| 007 | TEU y FEU: cómo se mide un barco | Un barco no se mide en toneladas | Pendiente |
| 008 | El Bill of Lading | El papel que vale lo mismo que la mercadería | Pendiente |
| 009 | Factura comercial, packing list y certificado de origen | Un error en un papel y la carga queda trabada | Pendiente |
| 010 | Avería gruesa | Tu carga llegó perfecta y igual te cobran | Pendiente |
| 011 | Seguro de carga: cláusulas A, B y C | ¿Qué pasa si se pierde mi mercadería? | Pendiente |
| 012 | Contenedores que caen al mar | Cuántos se pierden por año | Pendiente (buscar cifra oficial) |
| 013 | Demurrage y detention | La multa que te cobra la naviera por día | Pendiente |
| 014 | VGM (SOLAS): pesar el contenedor | Por qué un contenedor mal pesado hunde barcos | Pendiente |
| 015 | Trincaje de contenedores | Cómo se atan miles de cajas en alta mar | Pendiente |
| 016 | Mercancías peligrosas: clases IMO | Qué significan los rombos de colores | Pendiente |
| 017 | Cadena de frío | Por qué el reefer nunca se apaga | Pendiente |
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
| 028 | Depósito | Errores de picking | Mandaste el producto equivocado al cliente | Pendiente |
| 029 | Depósito | Mercadería vencida (sin FEFO) | Tiraste mercadería que estaba en el depósito | Pendiente |
| 030 | Recepción | Camiones esperando en la puerta | Tres horas para descargar un camión | Pendiente |
| 031 | Recepción | Recibir sin controlar contra la orden de compra | Pagaste mercadería que nunca entró | Pendiente |
| 032 | Despacho | Pedidos que salen tarde | El camión se fue y el pedido quedó | Pendiente |
| 033 | Despacho | Carga mal armada en el camión | Llegó roto por cómo se cargó | Pendiente |
| 034 | Transporte | Rutas de reparto mal armadas | Tu camión recorre el doble de lo necesario | Pendiente |
| 035 | Transporte | Entregas fallidas en última milla | Fue, no había nadie, y vuelve mañana | Pendiente |
| 036 | Importación | Carga trabada en aduana por documentos | Un error en la factura y la carga no sale | Pendiente |
| 037 | Importación | Demurrage por retirar tarde el contenedor | La multa diaria que nadie vio venir | Pendiente |
| 038 | Inventario | Quiebres de stock | Tenés de todo, menos lo que se vende | Pendiente |
| 039 | Inventario | Sobrestock | Plata parada en la estantería | Pendiente |
| 040 | Gestión | Medir sin KPIs | Si no lo medís, no lo podés mejorar | Pendiente |
| 041 | Seguridad | Accidentes con autoelevadores | El riesgo número uno del depósito | Pendiente |
| 042 | Devoluciones | Logística inversa desordenada | Las devoluciones que se comen el depósito | Pendiente |

