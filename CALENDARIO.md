# Calendario de contenido · Logística en 1 Minuto

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

1. **Gancho en la primera frase:** una pregunta o un dato que sorprenda. Nada de introducciones.
2. **Un concepto por video.** Si hacen falta dos, son dos videos.
3. **Un dato concreto y con fuente** en cada video: un número, una norma, un caso real.
4. **Visual que explica:** códigos resaltados, cifras grandes, comparaciones. El texto en pantalla aporta, no repite la voz.
5. **Menos de 50 segundos, medido en el MP4 final** (`ffprobe`), no en el guion. Si pasa de 50 s, se cortan escenas antes de programar. Máximo 7 escenas con narración. *(Revisión 2026-11-02: el 003 salió con 62 s y 9 escenas; en Instagram la gente lo miró 9,3 s en promedio, un 15 %.)*
6. **Nada que no esté verificado.** Ante la duda, el dato se saca.
7. **Siempre instructivo y útil.** Cada video responde una duda o resuelve un problema real que alguien tuvo (desde enviar un paquete hasta almacenarlo o importar). Tiene que dejar una acción concreta: un paso, una regla o una cuenta que el espectador puede aplicar hoy. Nada de curiosidades sueltas ni temas fuera de logística y comercio exterior.
8. **Música de fondo original** (generada por pipeline/musica.py, sin derechos de terceros), baja debajo de la voz. Se desactiva con musica: false en el guion.
9. **Título:** las dos primeras palabras son las que se ven al deslizar: van en MAYÚSCULAS y son la palabra clave fuerte del tema (ej.: "INCOTERM PELIGROSO: DDP te puede fundir 💸"). Corto, un emoji, y deja curiosidad: no explica todo.
10. **Hashtags: 4 como máximo**, #Shorts primero y 3 del tema exacto. Nada de hashtags genéricos ni de relleno (#viral, #fyp): YouTube los toma como spam.
11. **Horario:** 19:00 por defecto. Cuando haya 3 semanas de datos, el resumen semanal prueba otro horario y decide con números (no con consejos de terceros).
12. **Primeros 3 segundos:** imagen que se mueve + la frase gancho en pantalla desde el primer cuadro. Nada de logo, saludo ni pausa al inicio. Es lo que decide si deslizan.
13. **Llamado a seguir atado al contenido:** además del cierre, cuando el video tiene una lista o un remate, pedir que sigan ANTES del remate y conectado al tema ("Seguí la cuenta: el tercer error es el que más plata cuesta"). Nunca al principio.
14. **Primero el empaque:** título y gancho se escriben ANTES que el guion. Si el título no entusiasma, se cambia la idea, no se fuerza el guion.
15. **Nunca borrar un video con advertencia o strike:** se apela desde YouTube Studio. Borrarlo elimina la posibilidad de apelar.
16. **Cumplir la promesa del título en los primeros segundos** (MrBeast: la gente se va cuando el video no es lo que prometía el título). Nada de "hoy te voy a contar": se empieza mostrando.
17. **Remate y corte.** Cuando llega la respuesta, el video termina enseguida: el cierre es una sola frase. Un final largo hace que deslicen antes de que el video cuente como visto completo.
18. **Rotar formatos:** no repetir la misma serie más de 3 días seguidos (conceptos, problemas reales, guías rápidas).
19. **Links en la descripción:** aplicar la sección "Producto propio y afiliados" de este archivo en cada video (YouTube, TikTok, Instagram y Pinterest).

## Temas (en orden de producción)

| # | Tema | Gancho | Estado |
| --- | --- | --- | --- |
| 002 | El viaje de tu celular | Muchos celulares caros vuelan, no navegan | Programado (2026-11-02 19:00) |
| 003 | Qué significan las letras de un contenedor (ISO 6346) | Si sabés leerlo, sabés de quién es | Publicado (2026-11-01) |
| 004 | Incoterms: EXW, FOB y CIF | ¿Quién paga si el barco se hunde? | Programado (2026-11-03 19:00) |
| 005 | Incoterms: DAP y DDP | El Incoterm que te puede fundir | Programado (2026-11-04 19:00) |
| 006 | Tipos de contenedor: dry, high cube, reefer, open top, flat rack, tanque | No todos los contenedores son iguales | Programado (2026-11-05 19:00) |
| 007 | TEU y FEU: ¿20 o 40 pies? (peso ÷ volumen) | Un 40 pies carga menos peso que uno de 20 | Publicado (2026-11-06) |
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

## Serie 3: Cómo hacerlo (guías rápidas para cualquiera)

Formato: **la duda → los pasos → el error a evitar**. Para personas y pequeños negocios, no solo profesionales. Cuando el tema depende del país, se arranca por Uruguay con datos oficiales verificados al producir (Correo Uruguayo, DNA, etc.) y se aclara en pantalla. Se intercala con las otras series (por ejemplo, uno de cada tres videos) cuando el resumen semanal lo justifique.

| # | Duda | Gancho | Estado |
| --- | --- | --- | --- |
| 043 | Cómo embalar un paquete para que llegue sano | El 80 % de lo que se rompe, se rompe por cómo se embaló | Pendiente (verificar cifra o sacar) |
| 044 | Peso volumétrico: cómo se calcula | Te cobraron más de lo que pesa tu caja | Pendiente |
| 045 | Cómo enviar un paquete al exterior desde Uruguay | Lo que nadie te dice antes de ir al correo | Pendiente |
| 046 | Compras en el exterior y franquicia (Uruguay) | Cuándo pagás impuestos y cuándo no | Pendiente |
| 047 | Cómo leer el rastreo de un envío | "En tránsito" hace una semana: qué significa | Pendiente |
| 048 | Qué no se puede enviar (mercancías prohibidas y peligrosas) | Las baterías que te frenan el paquete | Pendiente |
| 049 | Cómo ordenar un depósito chico | Encontrar cualquier cosa en 30 segundos | Pendiente |
| 050 | Cómo almacenar en altura sin riesgo | Lo pesado abajo, siempre | Pendiente |
| 051 | Pallet: medidas y cómo armarlo | El pallet mal armado que se cae en el camión | Pendiente |
| 052 | Cómo cotizar un flete | Tres datos que te pide cualquier transportista | Pendiente |
| 053 | Cómo hacer un inventario sin parar la operación | El conteo cíclico | Pendiente |
| 054 | Cómo importar por primera vez | Los pasos, en orden | Pendiente |


## Videos largos (horizontales, 8 a 10 minutos)

**Por qué son la prioridad:** es la plata real del canal. Desde el 1/2/2027 los nuevos canales necesitan el doble para monetizar (8.000 horas o 20 millones de vistas de Shorts), y hasta los que ya están en el programa dejan de cobrar por Shorts si no hacen 10 millones de vistas en 90 días; los videos largos siguen pagando. Objetivo: entrar al programa ANTES del 1/2/2027 (hoy: 1.000 suscriptores + 4.000 horas, o 10 M de vistas de Shorts). Ritmo: un video largo por semana.

Reglas extra para largos (guía de producción de MrBeast): el primer minuto es el más importante (cumplir la promesa del título y mostrar lo que viene); un nuevo gancho cada 2 a 3 minutos ("y lo que viene ahora es lo que más plata hace perder"); lo más explicativo va en la segunda mitad; terminar apenas llega el remate.

Para sumar horas de reproducción y cobrar más por vista. Cada uno junta y amplía los Shorts de un mismo tema, con capítulos, miniatura propia y un llamado a suscribirse a mitad del video (antes de la parte más útil). Mínimo 8 minutos (desde ahí YouTube permite anuncios a mitad del video). Formato en guion.yaml: `formato: largo`, campos `capitulo` en las escenas y `miniatura: {arriba, abajo}`. Se renderizan como release `largos` del repositorio.

| # | Tema | Estado |
| --- | --- | --- |
| L01 | Incoterms 2020: los 11 explicados y los 5 errores que te hacen perder plata | Programado (2026-11-05 20:30, 8:04 min) |
| L02 | Contenedores: tipos, medidas, TEU y cómo elegir 20 o 40 pies | Pendiente |
| L03 | Cómo importar por primera vez desde Uruguay, paso a paso | Pendiente |
| L04 | Los 10 problemas más caros de un depósito y cómo resolverlos | Pendiente |

## Producto propio y afiliados (links para las descripciones)

- **Producto propio** (guía "Sin errores en comercio exterior" + comparador de costos, USD 7, Hotmart ID 8887961, ACTIVO desde 2026-11-04): https://go.hotmart.com/M108343404O?dp=1
  - Va en la PRIMERA línea de la descripción de todo video sobre Incoterms, costos de importación, aduana, importar o seguros de carga: "📘 Guía práctica + planilla para comparar cotizaciones: https://go.hotmart.com/M108343404O?dp=1". En el resto de los videos, al final de la descripción.
  - En videos largos, mencionarlo una vez en el cierre ("el link está en la descripción"), sin exagerar promesas.
- **Afiliado: Mega Logística Internacional** (CAMEX, Hotmart desde 2018; USD 49,54; comisión 60 %): https://go.hotmart.com/M108343505U
  - Usarlo solo en videos de logística internacional o transporte. Va al final de la descripción como: "Curso recomendado de logística internacional (link de afiliado): …".
  - Siempre aclarar que es un link de afiliado. Nunca prometer resultados ni usar la marca Hotmart. Nada de spam en WhatsApp ni Telegram (reglas de Hotmart).
