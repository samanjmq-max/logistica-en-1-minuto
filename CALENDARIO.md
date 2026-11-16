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

1. **Gancho en la primera frase:** una pregunta o un dato que sorprenda. Nada de introducciones. **El gancho dice qué pierde o qué paga el espectador** (plata, carga, tiempo): "¿quién pierde?", "te cobran", "pagás el doble". Nada de ganchos de lista o descriptivos ("6 X que tenés que conocer", "¿carga el doble?"). *(Revisión 2026-11-09, datos de Instagram: el 004 "Si el barco se hunde, ¿quién pierde?" fue el mejor: 141 vistas y 52,6 % pasó los 3 s. Los descriptivos rindieron peor: 007 "¿carga el doble?" 18,3 % pasó los 3 s; 006 "6 contenedores" 3,8 s de promedio; 002 "el viaje" 3,6 s. Revisión 2026-11-16: el 010 "AVERÍA GRUESA: tu carga llegó sana y pagás igual" tuvo el mejor paso de los 3 s hasta ahora (81,8 %) y 12,2 s de promedio (33 % del video), con solo 15 vistas. Se mantiene la regla.)*
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
20. **Programado no es publicado.** Antes de producir, la tarea diaria revisa en Metricool (getScheduledPosts) el estado de todo lo programado en los días anteriores, en cada red. Si alguna dice ERROR: no se produce un video nuevo, se anota el error exacto en el registro, se avisa al propietario y la próxima publicación es el video más viejo que quedó sin salir. En el registro se escribe "programado" solo cuando Metricool lo aceptó, y "publicado" solo cuando el estado dice PUBLISHED. *(Revisión 2026-11-16: del 10/11 20:30 al 15/11 Metricool rechazó todo con "You have reached your Metricool account limit" y la tarea siguió produciendo y anotando "programado" durante 6 días sin que saliera nada.)*

## Temas (en orden de producción)

### Orden para la semana del 17 al 23/11 (resumen semanal 2026-11-16)

**Del 10/11 a la noche al 16/11 no se publicó nada:** Metricool rechazó cada publicación con "You have reached your Metricool account limit" (L03, 013, 036, 055, L02b, 011 y 031). El 052 (16/11) y el 014 (17/11) están programados con el mismo riesgo. Los videos están renderizados pero nadie los vio, así que la lista de la semana pasada no se llegó a probar.

1. **No se producen Shorts ni largos nuevos hasta que se vuelva a publicar** (lo decide el propietario: plan de Metricool, publicación a mano o esperar que se renueve el límite). Con 9 videos listos hay atraso para más de una semana.
2. **Primero sale el atraso, en el mismo orden**, uno por día a las 19:00: 013 → 036 → 055 → 011 → 031 → 052 → 014 (los que no hayan salido). Los largos L03 y L02b van a las 20:30, martes y viernes.
3. **Al reprogramar después del 18/11, sacar de la descripción los cupones LANZAMIENTO y DEPOSITO7** (vencen ese día). El resto de la descripción queda igual.
4. Terminado el atraso, siguen temas nuevos rotando series y con gancho de plata: 037 (demurrage como problema real, serie 2) → 053 (conteo cíclico, serie 3) → 016 (mercancías peligrosas, serie 1).

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
| 011 | Seguro de carga: cláusulas A, B y C | ¿Qué pasa si se pierde mi mercadería? | Renderizado, NO publicado (falló el 2026-11-14: límite de Metricool) |
| 012 | Contenedores que caen al mar | Cuántos se pierden por año | Pendiente (se pasó el 2026-11-16: solo como cifra es una curiosidad sin acción y útil < 4; retomarlo solo con un enfoque útil, por ejemplo qué hacer si tu contenedor es uno de ellos, sin repetir 010 y 011) |
| 013 | Demurrage y detention | La multa que te cobra la naviera por día | Renderizado, NO publicado (falló el 2026-11-11: límite de Metricool) |
| 014 | VGM (SOLAS): pesar el contenedor | Sin este número, tu contenedor no sube | Renderizado, programado 2026-11-17 19:00 (en riesgo: límite de Metricool; verificar el 18/11) |
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
| 031 | Recepción | Recibir sin controlar contra la orden de compra | Pagaste mercadería que nunca entró | Renderizado, NO publicado (falló el 2026-11-15: límite de Metricool) |
| 032 | Despacho | Pedidos que salen tarde | El camión se fue y el pedido quedó | Pendiente |
| 033 | Despacho | Carga mal armada en el camión | Llegó roto por cómo se cargó | Pendiente |
| 034 | Transporte | Rutas de reparto mal armadas | Tu camión recorre el doble de lo necesario | Pendiente |
| 035 | Transporte | Entregas fallidas en última milla | Fue, no había nadie, y vuelve mañana | Pendiente |
| 036 | Importación | Carga trabada en aduana por documentos | Un error en la factura y la carga no sale | Renderizado, NO publicado (falló el 2026-11-12: límite de Metricool) |
| 037 | Importación | Demurrage por retirar tarde el contenedor | La multa diaria que nadie vio venir | Pendiente |
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
| 045 | Cómo enviar un paquete al exterior desde Uruguay | Lo que nadie te dice antes de ir al correo | Pendiente |
| 046 | Compras en el exterior y franquicia (Uruguay) | Cuándo pagás impuestos y cuándo no | Pendiente |
| 047 | Cómo leer el rastreo de un envío | "En tránsito" hace una semana: qué significa | Pendiente |
| 048 | Qué no se puede enviar (mercancías prohibidas y peligrosas) | Las baterías que te frenan el paquete | Pendiente |
| 049 | Cómo ordenar un depósito chico | Encontrar cualquier cosa en 30 segundos | Pendiente |
| 050 | Cómo almacenar en altura sin riesgo | Lo pesado abajo, siempre | Pendiente |
| 051 | Pallet: medidas y cómo armarlo | El pallet mal armado que se cae en el camión | Pendiente |
| 052 | Cómo cotizar un flete | Tres datos que te pide cualquier transportista | Renderizado, programado 2026-11-16 19:00 (en riesgo: límite de Metricool; verificar el 17/11) |
| 053 | Cómo hacer un inventario sin parar la operación | El conteo cíclico | Pendiente |
| 054 | Cómo importar por primera vez | Los pasos, en orden | Pendiente |
| 055 | ¿Autoelevador o transpaleta? La pregunta que decide | Comprar el equipo equivocado te come el capital | Renderizado, NO publicado (falló el 2026-11-13: límite de Metricool) |
| 056 | Cuánto espacio necesitás para arrancar un depósito | El error de alquilar de más (o de menos) | Pendiente |


## Videos largos (horizontales, 8 a 10 minutos)

**Por qué son la prioridad:** es la plata real del canal. Desde el 1/2/2027 los nuevos canales necesitan el doble para monetizar (8.000 horas o 20 millones de vistas de Shorts), y hasta los que ya están en el programa dejan de cobrar por Shorts si no hacen 10 millones de vistas en 90 días; los videos largos siguen pagando. Objetivo: entrar al programa ANTES del 1/2/2027 (hoy: 1.000 suscriptores + 4.000 horas, o 10 M de vistas de Shorts). Ritmo: un video largo por semana.

Reglas extra para largos (guía de producción de MrBeast): el primer minuto es el más importante (cumplir la promesa del título y mostrar lo que viene); un nuevo gancho cada 2 a 3 minutos ("y lo que viene ahora es lo que más plata hace perder"); lo más explicativo va en la segunda mitad; terminar apenas llega el remate.

Para sumar horas de reproducción y cobrar más por vista. Cada uno junta y amplía los Shorts de un mismo tema, con capítulos, miniatura propia y un llamado a suscribirse a mitad del video (antes de la parte más útil). Mínimo 8 minutos (desde ahí YouTube permite anuncios a mitad del video). Formato en guion.yaml: `formato: largo`, campos `capitulo` en las escenas y `miniatura: {arriba, abajo}`. Se renderizan como release `largos` del repositorio.

| # | Tema | Estado |
| --- | --- | --- |
| L01 | Incoterms 2020: los 11 explicados y los 5 errores que te hacen perder plata | Publicado (2026-11-04 20:30, 8:04 min; falta la miniatura) |
| L02 | Contenedores: tipos, medidas, TEU y cómo elegir 20 o 40 pies | Publicado (2026-11-06 20:30, 8:32 min) |
| L03 | PRIMERA IMPORTACIÓN: los 7 pasos para importar a Uruguay sin pagar de más | Renderizado, reprogramado 2026-11-17 20:30 (falló el 10/11 por el límite de Metricool; en riesgo, verificar el 18/11). No se produjo L04 (regla 20) |
| L02b | AUTOELEVADOR O TRANSPALETA: cómo elegir el equipo de tu depósito sin gastar de más | Renderizado, NO publicado (falló el 2026-11-13 20:30: límite de Metricool) |
| L04 | Los 10 problemas más caros de un depósito y cómo resolverlos | Pendiente |
| L05 | DEMURRAGE y detention: cómo no pagar días de contenedor y cómo negociar los días libres | Pendiente |
| L06 | EXPORTAR DESDE Uruguay por primera vez: pasos, documentos y certificado de origen | Pendiente |
| L07 | INVENTARIO SIN errores: cómo hacer un conteo cíclico en tu depósito paso a paso | Pendiente |

## Producto propio y afiliados (links para las descripciones)

- **Producto propio** (guía "Sin errores en comercio exterior" + comparador de costos, USD 7, Hotmart ID 8887961, ACTIVO desde 2026-11-04): https://go.hotmart.com/M108343404O?dp=1
  - Va en la PRIMERA línea de la descripción de todo video sobre Incoterms, costos de importación, aduana, importar o seguros de carga: "📘 Guía práctica + planilla para comparar cotizaciones: https://go.hotmart.com/M108343404O?dp=1". En el resto de los videos, al final de la descripción.
  - Cupón de lanzamiento **LANZAMIENTO** (28 % de descuento: USD 7 → USD 5,04), válido hasta el 2026-11-18. Hasta esa fecha, agregar en la descripción: "Con el cupón LANZAMIENTO la pagás USD 5 (hasta el 18/11)". Después de esa fecha, sacarlo.
  - En videos largos, mencionarlo una vez en el cierre ("el link está en la descripción"), sin exagerar promesas.
- **Producto propio 2** (guía "Tu primer depósito" + planilla de arranque, USD 10, Hotmart ID 8890964, ACTIVO desde 2026-11-04): https://go.hotmart.com/U108348887Q?dp=1
  - Va en la PRIMERA línea de la descripción de todo video sobre depósitos, almacenamiento, estanterías, autoelevadores, transpaletas, layout, inventario o arrancar un negocio logístico (por ejemplo 055, 056 y L02b): "📗 Guía + planilla para armar tu primer depósito: https://go.hotmart.com/U108348887Q?dp=1". En esos videos va este producto y no el de Incoterms.
  - Cupón de lanzamiento **DEPOSITO7** (30 %: USD 10 → USD 7), válido hasta el 2026-11-18. Hasta esa fecha agregar: "Con el cupón DEPOSITO7 la pagás USD 7 (hasta el 18/11)". Link directo con el cupón ya aplicado: https://pay.hotmart.com/U108348887Q?offDiscount=DEPOSITO7. Después del 18/11, sacarlo.
- **Afiliado: Mega Logística Internacional** (CAMEX, Hotmart desde 2018; USD 49,54; comisión 60 %): https://go.hotmart.com/M108343505U
  - Usarlo solo en videos de logística internacional o transporte. Va al final de la descripción como: "Curso recomendado de logística internacional (link de afiliado): …".
  - Siempre aclarar que es un link de afiliado. Nunca prometer resultados ni usar la marca Hotmart. Nada de spam en WhatsApp ni Telegram (reglas de Hotmart).
- **Afiliado: Mega de Comercio Exterior** (CAMEX, Hotmart ID 1522260, afiliación confirmada): https://go.hotmart.com/P108344299F
  - Usarlo en videos de importar, exportar, aduana, Incoterms o costos de importación. Va al final de la descripción como: "Curso recomendado de comercio exterior (link de afiliado): https://go.hotmart.com/P108344299F".
  - No poner los dos cursos CAMEX en el mismo video: logística internacional o transporte → Mega Logística; comercio exterior o aduana → Mega de Comercio Exterior.
- **Ghost Importer** (ID 2291543): afiliación solicitada el 04/11, esperando aceptación del productor. No usar hasta que esté confirmada.
