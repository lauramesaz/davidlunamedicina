# -*- coding: utf-8 -*-
# ÚNICA FUENTE DE VERDAD del sitio. Cambia aquí precios, qué incluye, preguntas y reglas,
# y luego corre:  python3 build.py
# OJO: aquí NUNCA van costos internos ni comisiones. Solo precio de venta y qué trae.

WHATSAPP = "573217591330"
TELEFONO = "+57 321 7591330"
MARCA = "Cirugía Todo Incluido"  # nombre provisional del sitio (sin marca). Cámbialo aquí.
SEDE_QX = "Q2"
VALORACION = "$200.000"
RETENCION = "20%"

# Qué significa cada cosa incluida (se usa en "Todo incluido" y en cada cirugía)
INCLUIDOS = {
    "cirujano": ("Honorarios del cirujano plástico", "Nuestros cirujanos plásticos te valoran, te operan y te acompañan en los controles."),
    "instrumentador": ("Instrumentador quirúrgico", "El profesional que asiste al cirujano durante toda la cirugía."),
    "quirofano": ("Quirófano en " + SEDE_QX, "Tu cirugía se hace en las salas de cirugía de " + SEDE_QX + ", nunca en un consultorio."),
    "implantes": ("Implantes mamarios", "El par de implantes está dentro del precio. El tamaño y el perfil los eliges con tu cirujano en la valoración."),
    "prenda": ("Brasier posquirúrgico", "La prenda especial que usarás en la recuperación. Sales de cirugía con ella puesta."),
    "faja": ("Prenda posquirúrgica", "La prenda de compresión que usarás en la recuperación. Sales de cirugía con ella puesta."),
    "poliza": ("Póliza de complicaciones", "Un seguro que te respalda si se presenta una complicación derivada de la cirugía. Operarte sin póliza es un riesgo que no te dejamos correr."),
    "bomba": ("Bomba de dolor", "Un dispositivo que administra analgesia de forma continua durante los primeros días. Es la diferencia entre una recuperación tranquila y una difícil."),
    "masajes": ("Masajes postoperatorios", "Los drenajes posquirúrgicos que ayudan a desinflamar y a que el resultado se asiente bien."),
}

NO_INCLUYE = [
    ("Cita de valoración", "Tiene un costo de " + VALORACION + " y no es abonable al tratamiento."),
    ("Exámenes prequirúrgicos", "Laboratorios y estudios que tu cirujano te ordene antes de operarte."),
    ("Medicamentos de la recuperación", "Los que te formulen para tomar en casa."),
    ("Procedimientos adicionales", "Cualquier procedimiento distinto al de la promo que se defina en la valoración."),
    ("Viaje y hospedaje", "Si vienes de otra ciudad o país."),
]

CIRUGIAS = [
    {
        "slug": "mamoplastia-de-aumento",
        "nombre": "Mamoplastia de aumento",
        "corto": "Aumento",
        "precio": "$10.900.000",
        "duracion": "2 horas aprox.",
        "frase": "Más volumen y mejor forma, con implantes incluidos.",
        "titular": "Mamoplastia de <em>aumento</em> con todo incluido",
        "intro": "Aumenta el volumen y mejora la forma de tus senos con implantes. Un solo precio, sin sumas de última hora.",
        "incluye": ["cirujano", "instrumentador", "quirofano", "implantes", "prenda", "poliza", "bomba"],
        "para_ti": [
            "Sientes que tus senos son pequeños para tu cuerpo.",
            "Perdiste volumen después de un embarazo, la lactancia o una baja de peso.",
            "Tienes una diferencia de tamaño entre un seno y otro.",
            "Tus senos están en buena posición: lo que quieres es volumen, no levantar.",
        ],
        "ojo": "Si además de volumen sientes el seno caído, probablemente tu cirugía es la mastopexia con implantes. Eso se define en la valoración.",
        "como_es": [
            "Se hace en quirófano y bajo anestesia. Tu cirujano coloca un implante en cada seno a través de una incisión pequeña, pensada para que la cicatriz quede lo más discreta posible.",
            "El tamaño, el perfil y la ubicación del implante se deciden contigo en la valoración, según tus medidas y lo que quieres lograr. No hay una talla única: hay la que le queda bien a tu cuerpo.",
        ],
        "recuperacion": [
            ("Día de la cirugía", "Sales con tu brasier posquirúrgico y la bomba de dolor funcionando. Necesitas un acompañante."),
            ("Primera semana", "Reposo relativo, sin levantar peso ni subir los brazos de más. Primer control con tu cirujano."),
            ("Semanas 2 a 4", "Vuelves poco a poco a tu rutina. Sigues usando el brasier posquirúrgico."),
            ("Mes 1 a 3", "Retomas el ejercicio cuando tu cirujano lo autorice. La inflamación baja y los implantes se van asentando."),
            ("Resultado final", "Se aprecia alrededor de los 3 a 6 meses, cuando el seno toma su forma y caída natural."),
        ],
        "hermanas": ["mastopexia-con-implantes"],
    },
    {
        "slug": "mastopexia-con-implantes",
        "nombre": "Mastopexia con implantes",
        "corto": "Mastopexia con implantes",
        "precio": "$17.900.000",
        "duracion": "5 horas aprox.",
        "frase": "Levanta, reafirma y devuelve el volumen en una sola cirugía.",
        "titular": "Mastopexia <em>con implantes</em>: levantar y dar volumen",
        "intro": "Levanta el seno caído y, en la misma cirugía, recupera el volumen con implantes. Todo dentro de un solo precio.",
        "incluye": ["cirujano", "instrumentador", "quirofano", "implantes", "prenda", "poliza", "bomba"],
        "para_ti": [
            "Tus senos cayeron después de embarazos, lactancia o cambios de peso.",
            "Sientes el seno “vacío” en la parte de arriba.",
            "La areola y el pezón apuntan hacia abajo o quedaron muy bajos.",
            "Quieres levantar y también ganar volumen.",
        ],
        "ojo": "Si estás conforme con tu volumen y solo quieres levantar, mira la mastopexia sin implantes.",
        "como_es": [
            "Se hace en quirófano y bajo anestesia. Tu cirujano retira el exceso de piel, reubica la areola y el pezón a una posición más alta y da nueva forma al seno. En el mismo tiempo quirúrgico coloca los implantes.",
            "Es una cirugía más larga que un aumento porque son dos trabajos en uno. Las cicatrices dependen de cuánto haya que levantar; tu cirujano te explica en la valoración cuál técnica aplica para ti.",
        ],
        "recuperacion": [
            ("Día de la cirugía", "Sales con tu brasier posquirúrgico y la bomba de dolor. Necesitas un acompañante."),
            ("Primera semana", "Reposo relativo y cuidado de las heridas. Primer control con tu cirujano."),
            ("Semanas 2 a 4", "Regreso gradual a tus actividades, sin esfuerzos ni peso."),
            ("Mes 1 a 3", "Ejercicio cuando tu cirujano lo autorice. Comienza el cuidado de las cicatrices."),
            ("Resultado final", "Alrededor de los 6 meses. Las cicatrices siguen aclarando hasta por un año."),
        ],
        "hermanas": ["mastopexia-sin-implantes", "mamoplastia-de-aumento"],
    },
    {
        "slug": "mastopexia-sin-implantes",
        "nombre": "Mastopexia sin implantes",
        "corto": "Mastopexia sin implantes",
        "precio": "$15.900.000",
        "duracion": "5 horas aprox.",
        "frase": "Levanta y reafirma con tu propio tejido, sin implantes.",
        "titular": "Mastopexia <em>sin implantes</em>: levantar con tu propio tejido",
        "intro": "Levanta y da nueva forma a tus senos usando tu propio tejido. Para quienes están conformes con su volumen y no quieren implantes.",
        "incluye": ["cirujano", "instrumentador", "quirofano", "prenda", "poliza", "bomba"],
        "para_ti": [
            "Tus senos cayeron, pero te gusta tu volumen actual.",
            "No quieres implantes.",
            "La areola y el pezón quedaron muy bajos.",
            "Quieres un seno más firme y en su lugar, con un resultado natural.",
        ],
        "ojo": "Si además quieres más volumen o llenar la parte de arriba del seno, mira la mastopexia con implantes.",
        "como_es": [
            "Se hace en quirófano y bajo anestesia. Tu cirujano retira el exceso de piel, reacomoda tu propio tejido mamario y reubica la areola y el pezón a una posición más alta.",
            "No se coloca ningún implante: el resultado se logra con lo que ya tienes. Las cicatrices dependen de cuánto haya que levantar; se define en la valoración.",
        ],
        "recuperacion": [
            ("Día de la cirugía", "Sales con tu brasier posquirúrgico y la bomba de dolor. Necesitas un acompañante."),
            ("Primera semana", "Reposo relativo y cuidado de las heridas. Primer control con tu cirujano."),
            ("Semanas 2 a 4", "Regreso gradual a tus actividades, sin esfuerzos ni peso."),
            ("Mes 1 a 3", "Ejercicio cuando tu cirujano lo autorice. Comienza el cuidado de las cicatrices."),
            ("Resultado final", "Alrededor de los 6 meses. Las cicatrices siguen aclarando hasta por un año."),
        ],
        "hermanas": ["mastopexia-con-implantes"],
    },
    {
        "slug": "lipo",
        "nombre": "Lipo",
        "corto": "Lipo",
        "precio": "$18.900.000",
        "duracion": "8 horas aprox.",
        "frase": "Define tu contorno. Incluye los masajes postoperatorios.",
        "titular": "<em>Lipo</em> con masajes postoperatorios incluidos",
        "intro": "Retira la grasa localizada que no se va con dieta ni ejercicio y define tu contorno. El precio ya trae los masajes de la recuperación.",
        "incluye": ["cirujano", "instrumentador", "quirofano", "faja", "poliza", "bomba", "masajes"],
        "para_ti": [
            "Tienes grasa localizada que no cede con dieta ni ejercicio.",
            "Estás en un peso estable y cercano a tu peso saludable.",
            "Quieres definir cintura, abdomen, espalda u otras zonas.",
            "Entiendes que la lipo moldea el cuerpo: no es un método para bajar de peso.",
        ],
        "ojo": "Las zonas a trabajar y si eres candidata se definen en la valoración. Si no cumples las condiciones de seguridad, no te operamos.",
        "como_es": [
            "Se hace en quirófano y bajo anestesia. A través de incisiones muy pequeñas, tu cirujano retira la grasa de las zonas acordadas y trabaja el contorno.",
            "Es la cirugía más larga de nuestras promos y por eso la seguridad manda: la cantidad de grasa que se puede retirar tiene un límite, y ese límite lo pone tu salud, no el resultado.",
        ],
        "recuperacion": [
            ("Día de la cirugía", "Sales con tu prenda posquirúrgica y la bomba de dolor. Necesitas un acompañante."),
            ("Primera semana", "Reposo relativo, caminatas cortas. Inician tus masajes postoperatorios y tienes el primer control."),
            ("Semanas 2 a 4", "Continúas con masajes y prenda. Vuelves poco a poco a tu rutina."),
            ("Mes 1 a 3", "Ejercicio cuando tu cirujano lo autorice. La inflamación va bajando semana a semana."),
            ("Resultado final", "Alrededor de los 3 a 6 meses, cuando el cuerpo desinflama por completo."),
        ],
        "hermanas": [],
    },
]

PROCESO = [
    ("Cita de valoración", "Nuestros cirujanos te examinan y te dicen qué cirugía es para ti. " + VALORACION + ", no abonable."),
    ("Exámenes prequirúrgicos", "Confirman que es seguro operarte. Sin exámenes, no hay cirugía."),
    ("Separas tu fecha", "Con un abono reservas tu quirófano en " + SEDE_QX + "."),
    ("Preparación", "Te decimos qué suspender, el ayuno y qué llevar."),
    ("Día de la cirugía", "Sales con tu prenda, tu bomba de dolor y tus indicaciones."),
    ("Primeros días", "Reposo en casa y línea directa para tus dudas."),
    ("Controles y resultado", "Te vemos hasta darte el alta."),
]

QUE_LLEVAR = [
    "Documento de identidad y resultados de tus exámenes.",
    "Ropa cómoda, de abotonar o de cierre adelante.",
    "Zapatos bajos y fáciles de poner.",
    "Un acompañante adulto que te lleve a casa y se quede contigo la primera noche.",
    "Sin joyas, esmalte, maquillaje ni lentes de contacto.",
    "El ayuno cumplido tal como te lo indicaron.",
]

# (categoría, pregunta, respuesta, [slugs de cirugías donde también aparece])
TODAS = ["mamoplastia-de-aumento", "mastopexia-con-implantes", "mastopexia-sin-implantes", "lipo"]
MAMAS = TODAS[:3]
IMPL = TODAS[:2]
FAQ = [
    ("Precio", "¿El precio de la promo es el precio final?", "Sí. El precio incluye los honorarios del cirujano, el instrumentador, el quirófano en " + SEDE_QX + ", la póliza de complicaciones, la bomba de dolor y la prenda posquirúrgica; además los implantes o los masajes cuando la cirugía los lleva. Si en la valoración se define un procedimiento adicional o distinto, te lo cotizamos antes de que tomes cualquier decisión.", TODAS),
    ("Precio", "¿Qué no está incluido?", "La cita de valoración (" + VALORACION + "), los exámenes prequirúrgicos, los medicamentos para tomar en casa y, si vienes de otra ciudad, tu viaje y hospedaje.", TODAS),
    ("Precio", "¿La cita de valoración se descuenta del valor de la cirugía?", "No. La valoración cuesta " + VALORACION + " y no es abonable al tratamiento. Es una consulta médica completa con nuestros cirujanos, y su valor no se devuelve.", []),
    ("Precio", "¿Por qué tengo que pagar la valoración?", "Porque es una consulta médica real: nuestros cirujanos te examinan, revisan tu caso y te dicen qué cirugía es para ti, o si no eres candidata. Ese tiempo profesional es el que pagas.", []),
    ("Precio", "¿Por qué el precio es más bajo que en otros lugares?", "Es una promo con un paquete cerrado: mismos estándares, mismo quirófano y mismo equipo. Lo que cambia es que te damos un solo precio con todo adentro, en lugar de sumarte cada cosa por aparte.", []),
    ("Precio", "¿Hasta cuándo está vigente la promo?", "Las promos tienen cupos y vigencia limitada. Escríbenos por WhatsApp y te confirmamos la disponibilidad de hoy.", []),
    ("Precio", "¿Me pueden dar el precio exacto sin valoración?", "El precio de cada promo es el que ves publicado. La valoración sirve para confirmar que esa cirugía sí es la tuya y que es seguro operarte.", []),

    ("Seguridad", "¿Dónde me operan?", "En las salas de cirugía de " + SEDE_QX + ". Nunca operamos en consultorios ni en lugares que no sean un quirófano.", TODAS),
    ("Seguridad", "¿Quién me opera?", "Nuestros cirujanos plásticos. Los conoces en tu cita de valoración: quien te valora es quien conoce tu caso.", []),
    ("Seguridad", "¿Qué es la póliza de complicaciones y por qué importa?", "Es un seguro que cubre la atención si se presenta una complicación derivada de tu cirugía. Toda cirugía tiene riesgos; la póliza hace que, si algo pasa, no tengas que resolverlo sola ni con tu bolsillo. Por eso va incluida y no es opcional.", TODAS),
    ("Seguridad", "¿Qué tipo de anestesia se usa?", "Depende de la cirugía y de tu caso. Te lo explican en la valoración, y antes de operarte se revisa que seas apta para la anestesia.", []),
    ("Seguridad", "¿Qué exámenes me piden?", "Los prequirúrgicos habituales: laboratorios y los estudios que tu cirujano considere según tu edad, tu salud y la cirugía. Te entregamos la orden en la valoración.", []),
    ("Seguridad", "¿Pueden decirme que no me operan?", "Sí, y es una buena señal. Si tus exámenes, tu peso o tu estado de salud hacen que la cirugía no sea segura, no te operamos. Primero tu salud.", ["lipo"]),
    ("Seguridad", "¿Qué riesgos tiene la cirugía?", "Toda cirugía tiene riesgos: sangrado, infección, problemas de cicatrización o relacionados con la anestesia, entre otros. Tu cirujano te los explica uno a uno en la valoración y firmas un consentimiento informado antes de operarte.", []),

    ("Dolor y recuperación", "¿Me va a doler?", "Vas a sentir molestia, pero para eso está la bomba de dolor: administra analgesia de forma continua los primeros días, que son los más incómodos. Va incluida en todas las promos.", TODAS),
    ("Dolor y recuperación", "¿Qué es exactamente la bomba de dolor?", "Es un dispositivo pequeño y portátil que entrega medicamento para el dolor de manera constante durante los primeros días. Te lo llevas puesto a casa y se retira en pocos días.", []),
    ("Dolor y recuperación", "¿Cuántos días de incapacidad necesito?", "Depende de la cirugía y de tu trabajo. Como guía: alrededor de una semana para trabajos de oficina tras un aumento, y entre dos y tres semanas tras una mastopexia o una lipo. Tu cirujano te da el tiempo exacto.", TODAS),
    ("Dolor y recuperación", "¿Cuándo puedo volver a hacer ejercicio?", "Caminar, desde los primeros días. El ejercicio como tal vuelve de forma gradual, normalmente después del primer mes y solo cuando tu cirujano lo autorice.", TODAS),
    ("Dolor y recuperación", "¿Cuándo veo el resultado final?", "Al principio hay inflamación, y es normal. El resultado se aprecia entre los 3 y 6 meses, según la cirugía.", []),
    ("Dolor y recuperación", "¿Cómo quedan las cicatrices?", "Toda cirugía deja cicatriz. Las ubicamos donde menos se noten y te enseñamos a cuidarlas. Su aspecto final depende también de tu piel y de qué tan juiciosa seas con los cuidados; siguen aclarando hasta por un año.", MAMAS),
    ("Dolor y recuperación", "¿Necesito que alguien me cuide?", "Sí. Necesitas un acompañante adulto el día de la cirugía y, como mínimo, la primera noche. Lo ideal son los primeros dos o tres días.", []),
    ("Dolor y recuperación", "¿Cuántos controles tengo después?", "Tienes controles con tu cirujano hasta el alta. El primero es en la primera semana.", []),
    ("Dolor y recuperación", "¿Los masajes postoperatorios son necesarios?", "En la lipo, sí: ayudan a desinflamar, a evitar acumulaciones de líquido y a que el resultado quede parejo. Por eso van incluidos en la promo de lipo.", ["lipo"]),
    ("Dolor y recuperación", "¿Cuánto tiempo uso la prenda posquirúrgica?", "Normalmente entre uno y tres meses, según la cirugía y tu evolución. Tu cirujano te indica cuándo dejarla.", ["lipo"]),

    ("Implantes", "¿Los implantes están incluidos en el precio?", "Sí, en la mamoplastia de aumento y en la mastopexia con implantes el par de implantes ya está dentro del precio.", IMPL),
    ("Implantes", "¿Cómo se escoge el tamaño?", "Lo escoges con tu cirujano en la valoración, según el ancho de tu tórax, tu piel y el resultado que quieres. El objetivo es que se vea proporcionado con tu cuerpo.", IMPL),
    ("Implantes", "¿Podré lactar después?", "En la mayoría de los casos, sí. Cuéntale a tu cirujano si planeas un embarazo para que lo tenga en cuenta al planear tu cirugía.", IMPL),
    ("Implantes", "¿Los implantes hay que cambiarlos?", "No tienen una fecha de vencimiento fija, pero tampoco son para toda la vida. Requieren control periódico y, en algún momento, pueden necesitar recambio.", IMPL),
    ("Implantes", "¿Con qué frecuencia debo revisarlos?", "Con tus controles médicos y los estudios de imagen que tu cirujano te recomiende a lo largo de los años.", []),
    ("Implantes", "¿Cuál es la diferencia entre aumento y mastopexia?", "El aumento da volumen. La mastopexia levanta el seno caído. Si necesitas las dos cosas, es mastopexia con implantes. Cuál es la tuya se define en la valoración.", MAMAS),

    ("Requisitos", "¿Desde qué edad me puedo operar?", "Desde los 18 años, con el desarrollo completo y buen estado de salud.", []),
    ("Requisitos", "¿Hay un peso máximo para operarme?", "Más que un peso, revisamos tu índice de masa corporal y tu salud general. Si está por fuera del rango seguro, no operamos hasta que lo esté.", ["lipo"]),
    ("Requisitos", "Fumo, ¿puedo operarme?", "Debes suspender el cigarrillo y el vapeador varias semanas antes y después de la cirugía, porque afectan la cicatrización y aumentan el riesgo de complicaciones. Tu cirujano te da el tiempo exacto.", []),
    ("Requisitos", "¿Y si tengo una enfermedad o tomo medicamentos?", "Cuéntalo todo en la valoración. Muchas condiciones controladas no impiden operarse, pero necesitamos saberlas para cuidarte.", []),
    ("Requisitos", "¿Puedo operarme si planeo un embarazo pronto?", "Lo ideal es operarte cuando no planees un embarazo cercano, porque el embarazo y la lactancia pueden cambiar el resultado.", MAMAS),
    ("Requisitos", "¿La lipo sirve para bajar de peso?", "No. La lipo moldea y define; no reemplaza una alimentación saludable ni el ejercicio. Los mejores resultados se ven en personas con peso estable.", ["lipo"]),

    ("Pagos", "¿Cómo separo mi fecha de cirugía?", "Después de la valoración, reservas tu fecha con un abono. El saldo se paga antes de la cirugía.", []),
    ("Pagos", "Si me arrepiento, ¿me devuelven el abono?", "Sí se devuelve, con una retención del " + RETENCION + " del valor abonado por gastos administrativos. El valor de la cita de valoración no se devuelve. El detalle está en los términos y condiciones.", []),
    ("Pagos", "¿Qué medios de pago reciben?", "Escríbenos por WhatsApp y te contamos los medios de pago disponibles hoy.", []),
    ("Pagos", "¿Puedo cambiar la fecha de mi cirugía?", "Sí, avisando con anticipación y según la disponibilidad de quirófano. Revisa las condiciones en los términos.", []),

    ("Vengo de lejos", "No vivo en la ciudad, ¿puedo operarme con ustedes?", "Sí. Atendemos pacientes de otras ciudades y del exterior. Te ayudamos a organizar tus fechas para que valoración, cirugía y controles te queden en un solo viaje.", []),
    ("Vengo de lejos", "¿Cuántos días debo quedarme después de la cirugía?", "Como guía, entre una y dos semanas para cirugías de seno y entre dos y tres para lipo. El tiempo exacto lo define tu cirujano en los controles.", []),
    ("Vengo de lejos", "¿Cuándo puedo viajar en avión?", "Solo cuando tu cirujano lo autorice en tu control. Viajar antes de tiempo aumenta los riesgos.", []),
    ("Vengo de lejos", "¿Puedo adelantar algo antes de viajar?", "Sí. Escríbenos por WhatsApp para adelantar tu información y dejar agendada la valoración para cuando llegues.", []),
]
CATS = ["Precio", "Seguridad", "Dolor y recuperación", "Implantes", "Requisitos", "Pagos", "Vengo de lejos"]

TERMINOS = [
    ("1. Sobre este sitio", [
        "Este sitio presenta nuestras promociones de cirugía plástica. La información tiene fines informativos y no reemplaza una consulta médica. Ninguna cirugía se programa sin una cita de valoración previa.",
    ]),
    ("2. Cita de valoración", [
        "Todo tratamiento inicia con una cita de valoración con nuestros cirujanos, con un costo de <strong>" + VALORACION + "</strong>.",
        "El valor de la cita de valoración <strong>no es abonable</strong> al valor de la cirugía ni de ningún tratamiento.",
        "El valor de la cita de valoración <strong>no se devuelve</strong> en ningún caso, incluso si después de la consulta decides no operarte o si nuestros cirujanos determinan que no eres candidata a la cirugía.",
    ]),
    ("3. Abonos y reserva de fecha", [
        "La fecha de cirugía se reserva con un abono. El saldo debe estar pago antes de la cirugía.",
        "Si después de abonar decides no realizarte la cirugía y solicitas la devolución, se hará una <strong>retención del " + RETENCION + " del valor abonado por concepto de gastos administrativos</strong>. El valor restante se te devuelve.",
    ]),
    ("4. Precios de las promociones", [
        "Los precios publicados corresponden al procedimiento descrito en cada promoción, con lo que se indica como incluido.",
        "No incluyen la cita de valoración, los exámenes prequirúrgicos, los medicamentos de la recuperación, procedimientos adicionales ni gastos de viaje u hospedaje.",
        "Si en la valoración se define un procedimiento distinto o adicional al de la promoción, se te entregará una cotización antes de que tomes cualquier decisión.",
        "Las promociones tienen cupos y vigencia limitada, y pueden modificarse o terminarse sin previo aviso. Se respeta el precio a quienes ya hayan abonado.",
    ]),
    ("5. Condiciones médicas", [
        "La cirugía solo se realiza si nuestros cirujanos te consideran candidata y si tus exámenes prequirúrgicos lo permiten. El equipo médico puede aplazar o no realizar una cirugía cuando no sea segura para ti.",
        "Todas las cirugías se realizan en las salas de cirugía de " + SEDE_QX + ".",
        "Toda cirugía tiene riesgos, que te serán explicados en la valoración y constarán en el consentimiento informado que firmas antes de operarte.",
        "Los resultados varían de una persona a otra. Los tiempos de recuperación publicados son una guía general, no una garantía.",
    ]),
    ("6. Reprogramación", [
        "Puedes solicitar el cambio de tu fecha de cirugía avisando con anticipación. La nueva fecha depende de la disponibilidad de quirófano y del equipo quirúrgico.",
    ]),
    ("7. Tus datos personales", [
        "Los datos que compartes con nosotros se usan únicamente para contactarte y gestionar tu atención, conforme a la Ley 1581 de 2012 de protección de datos personales. Puedes pedir que los actualicemos o eliminemos escribiéndonos por nuestros canales de contacto.",
    ]),
    ("8. Contacto", [
        "Si tienes dudas sobre estos términos, escríbenos por WhatsApp al " + TELEFONO + ".",
    ]),
]

# Selector del inicio: (lo que la paciente quiere, slug recomendado, por qué)
SELECTOR = [
    ("Más volumen", "mamoplastia-de-aumento", "Tus senos están en su lugar; lo que buscas es tamaño y forma."),
    ("Levantar y rellenar", "mastopexia-con-implantes", "El seno cayó y además lo sientes vacío: se levanta y se da volumen en una sola cirugía."),
    ("Levantar, sin implantes", "mastopexia-sin-implantes", "Te gusta tu volumen; solo quieres el seno firme y en su lugar."),
    ("Definir mi cuerpo", "lipo", "Grasa localizada que no se va con dieta ni ejercicio. Incluye los masajes."),
]

# ---------- v3: versión "para escanear" ----------
# clave: (icono, frase de 3-5 palabras)
INCLUIDOS_CORTO = {
    "cirujano": ("user", "Honorarios completos"),
    "instrumentador": ("team", "Equipo en sala"),
    "quirofano": ("cruz", "Nunca en consultorio"),
    "implantes": ("implantes", "El par, dentro del precio"),
    "prenda": ("prenda", "Sales con él puesto"),
    "faja": ("prenda", "Sales con ella puesta"),
    "poliza": ("escudo", "Tu respaldo si algo pasa"),
    "bomba": ("gota", "Menos dolor los primeros días"),
    "masajes": ("brillo", "Para desinflamar mejor"),
}
NO_INCLUYE_ICONOS = ["calendario", "frasco", "pastilla", "mas", "avion"]

RAPIDOS = {  # slug: (incapacidad aprox., resultado final)
    "mamoplastia-de-aumento": ("≈ 1 semana", "3 a 6 meses"),
    "mastopexia-con-implantes": ("2 a 3 semanas", "≈ 6 meses"),
    "mastopexia-sin-implantes": ("2 a 3 semanas", "≈ 6 meses"),
    "lipo": ("2 a 3 semanas", "3 a 6 meses"),
}
PUNTOS = {  # slug: [(icono, título, detalle)]
    "mamoplastia-de-aumento": [
        ("luna", "En quirófano y con anestesia", "Nunca en un consultorio."),
        ("regla", "Incisión pequeña", "Pensada para una cicatriz discreta."),
        ("implantes", "Tamaño a tu medida", "Lo eliges con tu cirujano en la valoración."),
        ("reloj", "2 horas aprox.", "Es la más corta de nuestras promos."),
    ],
    "mastopexia-con-implantes": [
        ("luna", "En quirófano y con anestesia", "Nunca en un consultorio."),
        ("prenda", "Se retira la piel que sobra", "Y se suben areola y pezón."),
        ("implantes", "Se colocan los implantes", "En la misma cirugía."),
        ("regla", "Cicatrices según tu caso", "Dependen de cuánto haya que levantar."),
    ],
    "mastopexia-sin-implantes": [
        ("luna", "En quirófano y con anestesia", "Nunca en un consultorio."),
        ("prenda", "Se retira la piel que sobra", "Y se suben areola y pezón."),
        ("user", "Con tu propio tejido", "No se coloca ningún implante."),
        ("regla", "Cicatrices según tu caso", "Dependen de cuánto haya que levantar."),
    ],
    "lipo": [
        ("luna", "En quirófano y con anestesia", "Nunca en un consultorio."),
        ("regla", "Incisiones muy pequeñas", "Por ahí se retira la grasa."),
        ("escudo", "Hay un límite seguro", "Cuánta grasa se retira lo define tu salud."),
        ("brillo", "Masajes incluidos", "Clave para un resultado parejo."),
    ],
}

# ---------- v6: persuasión ----------
# Si la promo tiene fecha real de cierre, escríbela aquí (ej. "31 de octubre"). Vacío = no se muestra. NUNCA inventar urgencia.
VIGENCIA = ""

# Los 4 miedos que frenan la compra y con qué se resuelven (pregunta, icono, respuesta corta, detalle)
MIEDOS = [
    ("¿Y si después me cobran más?", "check", "Precio cerrado.", "Lo que ves es lo que pagas. Lo que no incluye está escrito desde hoy."),
    ("¿Me va a doler mucho?", "gota", "Bomba de dolor incluida.", "Analgesia continua en los días más incómodos."),
    ("¿Y si algo sale mal?", "escudo", "Póliza de complicaciones incluida.", "No tienes que resolverlo sola ni con tu bolsillo."),
    ("¿Dónde me van a operar?", "cruz", "En quirófano, en " + SEDE_QX + ".", "Nunca en un consultorio. Con exámenes previos obligatorios."),
]
