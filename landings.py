# -*- coding: utf-8 -*-
# Landings de pauta (Meta) con test de 3 preguntas que califica el lead + página de gracias con píxel.
# Uso:  python3 landings.py      → genera l/<cirugia>.html y l/gracias.html
# Son páginas SOLO para anuncios: no salen en el menú y le dicen a Google que no las muestre (noindex).
import os, re, json, time
from html import escape
from datos import *

AQUI = os.path.dirname(os.path.abspath(__file__))
CX = {c["slug"]: c for c in CIRUGIAS}
V = int(time.time())

# ---------------------------------------------------------------- CONFIGURACIÓN
# Cirugías con landing. Se van agregando UNA POR UNA, cuando Laura aprueba la anterior.
LANDINGS = ["mamoplastia-de-aumento", "mastopexia-con-implantes", "mastopexia-sin-implantes", "lipo"]

# Titular de cada landing. Lo que va en <span class="lp-cola"> se esconde en celular para que el test quepa en la primera pantalla.
TITULARES = {
    "mamoplastia-de-aumento": 'Mamoplastia de <em>aumento</em><span class="lp-cola"> con todo incluido</span>',
    "mastopexia-con-implantes": 'Mastopexia <em>con implantes</em><span class="lp-cola">: levanta y da volumen</span>',
    "mastopexia-sin-implantes": 'Mastopexia <em>sin implantes</em><span class="lp-cola">: levanta con tu propio tejido</span>',
    "lipo": '<em>Lipo</em> con masajes<span class="lp-cola"> postoperatorios</span> incluidos',
}
# Primer paso del proceso, según la cirugía
PASO1 = {
    "mamoplastia-de-aumento": "Tu cirujano te examina y define contigo el tamaño de tus implantes.",
    "mastopexia-con-implantes": "Tu cirujano te examina, define cuánto hay que levantar y el tamaño de tus implantes.",
    "mastopexia-sin-implantes": "Tu cirujano te examina y define cuánto hay que levantar con tu propio tejido.",
    "lipo": "Tu cirujano te examina y define contigo las zonas a trabajar.",
}

# ID del píxel de Meta (solo números). Vacío = no se carga el píxel.
PIXEL_ID = "583112267661780"

# Dirección de la "aplicación web" de Google Apps Script que escribe en la hoja de leads.
# Vacío = el formulario funciona igual, pero no guarda en la hoja (solo para pruebas).
HOJA_URL = ""

# Las 3 preguntas. Cada opción: (código, texto). El código es lo que se guarda en la hoja.
P1 = ("¿Para cuándo te gustaría <em>operarte</em>?", [
    ("antes-15-ene", "Antes del 15 de enero"),
    ("proximos-meses", "En los próximos meses"),
    ("sin-fecha", "Todavía no tengo fecha"),
    ("averiguando", "Solo estoy averiguando"),
])
P2_OPC = [
    ("contado", "De contado"),
    ("financiacion", "Con financiación"),
    ("no-alcanza", "Ahora ese valor no me alcanza"),
]
P3 = ("¿Quieres agendar tu <em>valoración</em> con el cirujano?", [
    ("esta-semana", "Sí, quiero agendarla esta semana"),
    ("mas-adelante", "Sí, pero más adelante"),
    ("info", "Primero quiero más información"),
])

ICONOS = {
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>',
    "team": '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3 3-6 6-6s6 3 6 6"/><circle cx="17" cy="9" r="2"/><path d="M17 14c2 0 4 2 4 5"/>',
    "cruz": '<rect x="4" y="4" width="16" height="16" rx="4"/><path d="M12 8v8M8 12h8"/>',
    "implantes": '<circle cx="8" cy="12" r="4"/><circle cx="16" cy="12" r="4"/>',
    "prenda": '<path d="M8 4l4 3 4-3 4 4-3 3v9H7v-9L4 8z"/>',
    "escudo": '<path d="M12 3l8 3v6c0 5-3 8-8 9-5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "gota": '<path d="M12 3s6 6 6 11a6 6 0 0 1-12 0c0-5 6-11 6-11z"/>',
    "brillo": '<path d="M12 4v4M12 16v4M4 12h4M16 12h4M7 7l2 2M15 15l2 2M17 7l-2 2M9 15l-2 2"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
    "wa": '<path d="M4 20l1.3-4A8 8 0 1 1 8 18.7z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 1c-1-.5-1.5-1-2-2l1-1-1-2z"/>',
}
TITULOS = {"cirujano": "Cirujano plástico", "instrumentador": "Instrumentador", "quirofano": "Quirófano en " + SEDE_QX, "implantes": "Implantes",
           "prenda": "Brasier posquirúrgico", "faja": "Prenda posquirúrgica", "poliza": "Póliza de complicaciones", "bomba": "Bomba de dolor", "masajes": "Masajes incluidos"}


def ico(n):
    return '<span class="ico"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>' % ICONOS[n]


def pixel_base():
    if not PIXEL_ID:
        return "<script>window.fbq=window.fbq||function(){};</script>"
    return """<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','%s');fbq('track','PageView');</script>
<noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id=%s&ev=PageView&noscript=1"></noscript>""" % (PIXEL_ID, PIXEL_ID)


def envolver(titulo, descripcion, cuerpo, extra_body=""):
    return """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(t)s</title>
<meta name="description" content="%(d)s">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#fbfbf9">
<script>document.documentElement.className="js"</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css?v=%(v)s">
<link rel="stylesheet" href="/assets/landing.css?v=%(v)s">
%(px)s
</head>
<body class="lp">
<main>
%(c)s
</main>
<footer class="lp-pie"><div class="cont">
  <a class="btn tc" href="/terminos-y-condiciones">Términos y condiciones →</a>
  <p>La información de esta página es orientativa y no reemplaza una consulta médica. Toda cirugía tiene riesgos y los resultados varían de una persona a otra.</p>
</div></footer>
%(x)s
<script src="/assets/app.js?v=%(v)s"></script>
<script src="/assets/landing.js?v=%(v)s"></script>
</body>
</html>
""" % {"t": escape(titulo), "d": escape(descripcion), "v": V, "px": pixel_base(), "c": cuerpo, "x": extra_body}


def guardar(ruta, html):
    p = os.path.join(AQUI, ruta)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print("✓", ruta)


def opciones(nombre, lista):
    return "".join('<button type="button" class="opc" data-campo="%s" data-valor="%s"><span>%s</span></button>' % (nombre, v, t) for v, t in lista)


def test(c):
    p2 = ("¿Cómo <em>pagarías</em> tu cirugía?", P2_OPC)
    precio_t = '<p class="precio-t"><span>Precio total · todo incluido</span><b>%s</b></p>' % c["precio"]
    paso = lambda n, titulo, cuerpo, extra="": '<fieldset class="paso-t" data-paso="%d"%s><legend><small>Pregunta %d de 3</small>%s</legend>%s<div class="opcs">%s</div></fieldset>' % (
        n, "" if n == 1 else " hidden", n, titulo, extra, cuerpo)
    return """<form class="test" id="test" novalidate data-cx="%(slug)s" data-nombre-cx="%(nombre)s" data-hoja="%(hoja)s">
  <div class="test-cab"><span>¿Eres candidata?</span><span class="test-cuenta">30 segundos</span></div>
  <div class="test-barra" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  %(p1)s
  %(p2)s
  %(p3)s
  <fieldset class="paso-t" data-paso="4" hidden>
    <legend><small>Último paso</small>¿A dónde te <em>escribimos</em>?</legend>
    <div class="campo"><label for="lp-nombre">Tu nombre</label><input id="lp-nombre" name="nombre" autocomplete="given-name" autocapitalize="words" enterkeyhint="next" required placeholder="Ej.: Camila"></div>
    <div class="campo"><label for="lp-wa">Tu WhatsApp</label><input id="lp-wa" name="whatsapp" type="tel" inputmode="tel" autocomplete="tel" enterkeyhint="send" required placeholder="Ej.: 300 123 4567"><small class="ayuda">¿Fuera de Colombia? Agrega el indicativo (+1, +34…).</small></div>
    <p class="error-t" role="alert" hidden></p>
    <button class="btn pri" type="submit">Ver mi resultado →</button>
    <p class="legal">Al enviar autorizas que te contactemos por WhatsApp sobre tu cirugía y aceptas los <a href="/terminos-y-condiciones">términos y condiciones</a>.</p>
  </fieldset>
  <button type="button" class="atras" hidden>← Atrás</button>
</form>""" % {
        "slug": c["slug"], "nombre": escape(c["nombre"]), "hoja": escape(HOJA_URL),
        "p1": paso(1, P1[0], opciones("plazo", P1[1])),
        "p2": paso(2, p2[0], opciones("pago", p2[1]), precio_t),
        "p3": paso(3, P3[0], opciones("valoracion", P3[1]), '<p class="nota-t">El cirujano te examina y te dice si eres candidata. Cuesta <b>%s</b> y no es abonable a la cirugía.</p>' % VALORACION),
    }


def landing(c):
    faqs = [f for f in FAQ if c["slug"] in f[3]][:6]
    sellos = [TITULOS[k] for k in c["incluye"] if k in ("implantes", "masajes")] + ["Póliza", "Bomba de dolor"]
    if len(sellos) < 3:
        sellos.append("Quirófano en " + SEDE_QX)
    rap = RAPIDOS[c["slug"]]
    cuerpo = """
<section class="lp-hero"><div class="cont lp-grid">
  <div class="lp-texto">
    <p class="ceja">Promo de cirugía plástica</p>
    <h1>%(titular)s</h1>
    <div class="lp-precio"><b>%(precio)s</b><span>Precio total · todo incluido</span></div>
    <ul class="lp-sellos">%(sellos)s</ul>
    <p class="lp-vigencia">Promo para cirugías realizadas antes del %(fecha)s.</p>
  </div>
  %(test)s
</div></section>

<section class="banda clara delgada"><div class="cont"><div class="datos lp-datos"><div class="dato"><span>Duración</span><b>%(dur)s</b></div><div class="dato"><span>Incapacidad</span><b>%(inc)s</b></div><div class="dato"><span>Resultado</span><b>%(res)s</b></div></div></div></section>

<section class="sec pegada"><div class="cont dos">
  <div class="fija ver"><span class="etiqueta">Un solo precio</span><h2>Tu precio <em>lo incluye todo</em></h2><p class="bajada lp-bajada">%(precio)s y no hay sumas de última hora. Toca cada cosa para ver qué es.</p></div>
  <div class="ver"><div class="mosaico">%(incluye)s</div></div>
</div></section>

<section class="sec pegada"><div class="cont dos">
  <div class="fija ver"><h2>Es para ti <em>si…</em></h2></div>
  <div class="ver"><ul class="lista">%(para_ti)s</ul><p class="pista lp-pista">%(ojo)s</p></div>
</div></section>

<section class="banda salvia"><div class="cont angosto">
  <div class="sec-cab ver"><h2>Tus miedos, <em>resueltos</em></h2></div>
  <div class="filas">%(miedos)s</div>
</div></section>

<section class="sec pegada"><div class="cont">
  <div class="sec-cab ver"><h2>Tres pasos y <em>listo</em></h2></div>
  <div class="rejilla r3">%(pasos)s</div>
</div></section>

<section class="sec pegada"><div class="cont dos">
  <div class="fija ver"><h2>Preguntas <em>frecuentes</em></h2></div>
  <div class="ver"><div class="acordeon">%(faq)s</div></div>
</div></section>

<section class="banda champan cierre"><div class="cont"><div class="panel ver">
  <h2>¿Eres <em>candidata</em>?</h2>
  <div class="valor lp-valor-cierre">%(precio)s</div>
  <div class="fila-btn lp-centro"><a class="btn pri lp-btn-cierre" href="#test" data-ir-test>Hacer el test →</a></div>
  <p class="micro lp-centro">3 preguntas · 30 segundos · sin compromiso</p>
</div></div></section>

<section class="tc-banda"><div class="cont"><div class="tc-caja"><div><span class="tc-ceja">Importante · léelo antes de pagar</span><h2>Devoluciones: se retiene el %(ret)s</h2><p>La cita de valoración no se devuelve. Si abonas y luego decides no operarte, se te devuelve lo abonado reteniendo el %(ret)s por gastos administrativos. Tu cirugía debe realizarse antes del %(fecha)s.</p></div><a class="btn tc" href="/terminos-y-condiciones">Leer términos y condiciones →</a></div></div></section>
""" % {
        "titular": TITULARES[c["slug"]], "precio": c["precio"], "fecha": FECHA_LIMITE, "ret": RETENCION,
        "sellos": "".join("<li>%s</li>" % s for s in sellos),
        "test": test(c), "dur": c["duracion"].replace(" aprox.", ""), "inc": rap[0], "res": rap[1],
        "incluye": "".join('<details><summary>%s<span>%s<small>%s</small></span></summary><p class="mas-info">%s</p></details>' % (
            ico(INCLUIDOS_CORTO[k][0]), TITULOS[k], INCLUIDOS_CORTO[k][1], INCLUIDOS[k][1]) for k in c["incluye"]),
        "para_ti": "".join("<li><div><b>%s</b></div></li>" % x for x in c["para_ti"]),
        "ojo": c["ojo"],
        "miedos": "".join('<div class="fila ver"><span>%s</span><b>%s</b></div>' % (q, r.rstrip(".")) for q, i, r, d in MIEDOS),
        "pasos": "".join('<div class="tarjeta ver"><span class="num">%d</span><h3>%s</h3><p>%s</p></div>' % (n, t, d) for n, (t, d) in enumerate([
            ("Valoración · " + VALORACION, PASO1[c["slug"]]),
            ("Separas tu fecha", "Con un abono reservas tu cirugía. El precio de la promo se respeta desde que abonas."),
            ("Tu cirugía en " + SEDE_QX, "En quirófano, con póliza y bomba de dolor. Te acompañamos hasta el alta."),
        ], 1)),
        "faq": "".join('<details><summary>%s</summary><div class="resp"><p>%s</p></div></details>' % (q, a) for cat, q, a, _ in faqs),
    }
    barra = '<div class="accion solo-movil lp-barra"><div class="t"><b>%s</b><span>%s</span></div><a class="btn pri ch" href="#test" data-ir-test>¿Soy candidata?</a></div>' % (c["precio"], c["nombre"])
    guardar("l/%s.html" % c["slug"], envolver("%s · %s todo incluido" % (c["nombre"], c["precio"]), c["intro"], cuerpo, barra))


def gracias():
    datos_cx = {c["slug"]: {"nombre": c["nombre"], "precio": c["precio"]} for c in CIRUGIAS}
    textos = {k: dict(v) for k, v in [("plazo", P1[1]), ("pago", P2_OPC), ("valoracion", P3[1])]}
    cuerpo = """
<section class="lp-gracias"><div class="cont angosto">
  <div class="g-tarjeta" data-gracias data-wa="%(wa)s" data-cx='%(cx)s' data-textos='%(tx)s'>
    <span class="g-check">%(check)s</span>
    <p class="ceja g-ceja">Recibimos tus respuestas</p>
    <h1 class="g-titulo">¡Gracias!</h1>
    <p class="bajada g-texto">Una asesora te escribe por WhatsApp para resolver tus dudas.</p>
    <a class="btn pri g-wa" href="https://wa.me/%(wa)s" target="_blank" rel="noopener">%(ico_wa)s<span class="g-wa-txt">Escribir por WhatsApp</span></a>
    <p class="micro g-micro">Respuesta por WhatsApp · sin compromiso</p>
  </div>

  <div class="g-bloque" data-solo="A" hidden>
    <h2>Qué pasa en tu <em>valoración</em></h2>
    <ul class="lista">
      <li><div><b>Te examina nuestro cirujano</b><span>Toma tus medidas y te dice qué se puede lograr en tu cuerpo.</span></div></li>
      <li><div><b>Resuelves todas tus dudas</b><span>Riesgos, recuperación, tamaño, cicatrices. Sin afán.</span></div></li>
      <li><div><b>Sales con tu orden de exámenes</b><span>Para separar tu fecha antes del %(fecha)s.</span></div></li>
    </ul>
    <p class="pista">La valoración cuesta %(val)s y no es abonable a la cirugía.</p>
  </div>

  <div class="g-bloque" data-solo="BC" hidden>
    <h2>Mientras tanto, <em>mira esto</em></h2>
    <div class="rejilla r3 g-enlaces">
      <a class="tarjeta" data-enlace-cx href="/cirugias"><span class="num">La promo</span><h3>Todo lo que incluye</h3><span class="mas">Ver →</span></a>
      <a class="tarjeta" href="/formas-de-pago"><span class="num">Pagos</span><h3>Cómo se paga tu cirugía</h3><span class="mas">Ver →</span></a>
      <a class="tarjeta" href="/preguntas-frecuentes"><span class="num">Dudas</span><h3>Preguntas frecuentes</h3><span class="mas">Ver →</span></a>
    </div>
  </div>
</div></section>
""" % {
        "wa": WHATSAPP, "cx": escape(json.dumps(datos_cx, ensure_ascii=False), quote=True), "tx": escape(json.dumps(textos, ensure_ascii=False), quote=True),
        "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 12.5l4 4 8-9"/></svg>', "ico_wa": ico("wa"), "fecha": FECHA_LIMITE, "val": VALORACION,
    }
    guardar("l/gracias.html", envolver("Gracias · recibimos tus respuestas", "Recibimos tus respuestas.", cuerpo))


for slug in LANDINGS:
    landing(CX[slug])
gracias()
print("\nListo: %d landing(s) + gracias. Píxel: %s · Hoja: %s" % (len(LANDINGS), PIXEL_ID or "SIN CONFIGURAR", "conectada" if HOJA_URL else "SIN CONFIGURAR"))
