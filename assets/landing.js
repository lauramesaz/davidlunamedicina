// Landings de pauta: test de 3 preguntas → puntaje A/B/C → hoja de Google → página de gracias con píxel.
(() => {
  const S = {
    get: (k) => { try { return JSON.parse(sessionStorage.getItem(k)); } catch (e) { return null; } },
    set: (k, v) => { try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) {} },
  };
  const fbq = (...a) => { try { window.fbq && window.fbq(...a); } catch (e) {} };

  // ---------- 1. Guardar de qué anuncio viene (utm / fbclid) ----------
  const q = new URLSearchParams(location.search);
  const origen = S.get('lp_origen') || {};
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid'].forEach((k) => { if (q.get(k)) origen[k] = q.get(k); });
  S.set('lp_origen', origen);

  // ---------- 2. El test ----------
  const form = document.querySelector('#test');
  if (form) {
    const pasos = [...form.querySelectorAll('.paso-t')];
    const barras = [...form.querySelectorAll('.test-barra i')];
    const atras = form.querySelector('.atras');
    const cuenta = form.querySelector('.test-cuenta');
    const resp = {};
    let actual = 1;
    let empezo = false;
    barras[0].classList.add('on');

    fbq('track', 'ViewContent', { content_name: form.dataset.nombreCx });

    const ir = (n) => {
      actual = n;
      pasos.forEach((p) => { p.hidden = Number(p.dataset.paso) !== n; });
      barras.forEach((b, i) => b.classList.toggle('on', i < n));
      atras.hidden = n === 1;
      cuenta.textContent = n === 4 ? 'Último paso' : '30 segundos';
      const p = pasos[n - 1];
      p.classList.remove('entra'); void p.offsetWidth; p.classList.add('entra');
      if (n === 4 && window.matchMedia('(hover: hover)').matches) setTimeout(() => form.querySelector('#lp-nombre').focus({ preventScroll: true }), 250);
      // que la pregunta nueva quede completa a la vista (en celular: el test sube hasta arriba)
      // solo se mueve la página si la pregunta no cabe completa en la pantalla
      setTimeout(() => {
        const top = form.getBoundingClientRect().top;
        const fin = (n === 4 ? form.querySelector('button[type=submit]') : atras).getBoundingClientRect().bottom;
        if (top < 0 || fin + 12 > window.innerHeight) window.scrollTo({ top: window.scrollY + top - 10, behavior: 'smooth' });
      }, 30);
    };

    form.addEventListener('click', (e) => {
      const b = e.target.closest('.opc');
      if (!b) return;
      if (!empezo) { empezo = true; fbq('trackCustom', 'EmpezoTest', { content_name: form.dataset.nombreCx }); }
      resp[b.dataset.campo] = b.dataset.valor;
      b.parentElement.querySelectorAll('.opc').forEach((x) => x.classList.toggle('on', x === b));
      setTimeout(() => ir(actual + 1), 260);
    });
    atras.addEventListener('click', () => ir(actual - 1));
    // en el teclado del celular, "siguiente" en el nombre pasa al WhatsApp en vez de enviar
    form.nombre.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); form.whatsapp.focus(); } });

    // Puntaje: A caliente · B tibio · C frío
    const puntaje = (r) => {
      if (r.plazo === 'averiguando' || r.pago === 'no-alcanza' || r.valoracion === 'info') return 'C';
      if (['antes-15-ene', 'proximos-meses'].includes(r.plazo) && r.valoracion === 'esta-semana') return 'A';
      return 'B';
    };
    const limpiarWa = (t) => {
      let d = t.replace(/[^\d+]/g, '');
      const mas = d.startsWith('+');
      d = d.replace(/\D/g, '');
      if (!mas && d.length === 10 && d.startsWith('3')) d = '57' + d; // celular colombiano sin indicativo
      return d;
    };

    const error = form.querySelector('.error-t');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const nombre = form.nombre.value.trim();
      const wa = limpiarWa(form.whatsapp.value);
      error.hidden = true;
      if (nombre.length < 2) { error.textContent = 'Escribe tu nombre.'; error.hidden = false; form.nombre.focus(); return; }
      if (wa.length < 10 || wa.length > 15) { error.textContent = 'Revisa tu número de WhatsApp.'; error.hidden = false; form.whatsapp.focus(); return; }

      const lead = {
        id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
        fecha: new Date().toLocaleString('es-CO', { timeZone: 'America/Bogota' }),
        cirugia: form.dataset.nombreCx, slug: form.dataset.cx,
        nombre, whatsapp: wa,
        plazo: resp.plazo, pago: resp.pago, valoracion: resp.valoracion,
        puntaje: puntaje(resp),
        pagina: location.origin + location.pathname,
        ...S.get('lp_origen'),
      };
      S.set('lp_lead', lead);
      S.set('lp_px', null);

      const boton = form.querySelector('button[type=submit]');
      boton.disabled = true; boton.textContent = 'Enviando…';
      const ir_gracias = () => { location.href = '/l/gracias'; };
      if (form.dataset.hoja) {
        // Apps Script no responde a CORS: se envía "a ciegas" y keepalive asegura que llegue aunque cambie la página
        fetch(form.dataset.hoja, { method: 'POST', mode: 'no-cors', keepalive: true, headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(lead) })
          .catch(() => {}).finally(ir_gracias);
        setTimeout(ir_gracias, 2500);
      } else {
        ir_gracias();
      }
    });

    // Barra fija del celular: se esconde mientras el test está en pantalla
    const barra = document.querySelector('.lp-barra');
    if (barra && 'IntersectionObserver' in window) {
      new IntersectionObserver(([en]) => barra.classList.toggle('oculta', en.isIntersecting), { threshold: 0.15 }).observe(form);
    }
    document.querySelectorAll('[data-ir-test]').forEach((a) => a.addEventListener('click', (e) => {
      e.preventDefault();
      form.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }));
  }

  // ---------- 3. Página de gracias ----------
  const g = document.querySelector('[data-gracias]');
  if (g) {
    const lead = S.get('lp_lead');
    const cx = JSON.parse(g.dataset.cx);
    const tx = JSON.parse(g.dataset.textos);
    const p = lead ? lead.puntaje : 'B';
    const nombre = lead && lead.nombre ? lead.nombre.split(' ')[0] : '';
    const $ = (s) => g.querySelector(s);

    if (p === 'A') {
      $('.g-ceja').textContent = 'Tu siguiente paso';
      $('.g-titulo').textContent = nombre ? `¡Listo, ${nombre}! Agendemos tu valoración` : '¡Listo! Agendemos tu valoración';
      $('.g-texto').textContent = 'Escríbenos ahora y te damos los horarios de esta semana. Tu mensaje ya va escrito.';
      $('.g-wa-txt').textContent = 'Agendar mi valoración';
    } else if (p === 'C') {
      $('.g-titulo').textContent = nombre ? `¡Gracias, ${nombre}!` : '¡Gracias!';
      $('.g-texto').textContent = 'Te dejamos todo lo que necesitas para decidir con calma. Si te queda una pregunta, escríbenos.';
      $('.g-wa-txt').textContent = 'Tengo una pregunta';
      $('.g-wa').classList.remove('pri');
    } else {
      $('.g-titulo').textContent = nombre ? `¡Gracias, ${nombre}!` : '¡Gracias!';
      $('.g-texto').textContent = 'Una asesora te escribe por WhatsApp para resolver tus dudas. Si prefieres, escríbenos tú ahora.';
    }
    document.querySelectorAll('[data-solo]').forEach((b) => { b.hidden = !b.dataset.solo.includes(p); });

    if (lead) {
      const c = cx[lead.slug] || { nombre: lead.cirugia };
      const msj = `Hola, soy ${lead.nombre}. Hice el test de ${c.nombre} en la web.\n` +
        `• Para cuándo: ${tx.plazo[lead.plazo] || '-'}\n• Cómo pagaría: ${tx.pago[lead.pago] || '-'}\n• Valoración: ${tx.valoracion[lead.valoracion] || '-'}`;
      $('.g-wa').href = `https://wa.me/${g.dataset.wa}?text=${encodeURIComponent(msj)}`;
      const enlace = document.querySelector('[data-enlace-cx]');
      if (enlace && cx[lead.slug]) { enlace.href = '/' + lead.slug; enlace.querySelector('h3').textContent = `Todo lo que incluye tu ${c.nombre.toLowerCase()}`; }

      // Píxel: una sola vez por lead (si recarga la página, no se cuenta doble)
      if (!S.get('lp_px')) {
        const d = { content_name: c.nombre, content_category: 'Cirugía', lead_score: p };
        fbq('track', 'Lead', d, { eventID: 'lead-' + lead.id });
        if (p === 'A') fbq('trackCustom', 'LeadCalificado', d, { eventID: 'lc-' + lead.id });
        S.set('lp_px', true);
      }
    }
  }
})();
