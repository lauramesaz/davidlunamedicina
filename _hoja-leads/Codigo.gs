/**
 * Hoja de leads de las landings de cirugía.
 * Cada vez que alguien llena el test en una landing, aparece una fila nueva aquí.
 *
 * CÓMO SE INSTALA (una sola vez):
 * 1. Crear una hoja de Google nueva → menú Extensiones → Apps Script.
 * 2. Borrar lo que haya y pegar TODO este código. Guardar.
 * 3. Elegir la función "preparar" arriba y darle ▶ Ejecutar (pide autorizar: aceptar con tu cuenta).
 * 4. Botón azul "Implementar" → "Nueva implementación" → tipo "Aplicación web".
 *    - Ejecutar como: Yo.   - Quién tiene acceso: Cualquier usuario.
 * 5. Copiar la "URL de la aplicación web" (termina en /exec) y pegarla en landings.py → HOJA_URL.
 */

const PESTANA = 'Leads';
const CORREO_AVISO = ''; // si se llena con un correo, llega un aviso cada vez que entra un lead A

const COLUMNAS = [
  ['fecha', 'Fecha'], ['puntaje', 'Puntaje'], ['cirugia', 'Cirugía'], ['nombre', 'Nombre'], ['whatsapp', 'WhatsApp'],
  ['plazo', '¿Para cuándo?'], ['pago', '¿Cómo pagaría?'], ['valoracion', '¿Valoración?'],
  ['utm_campaign', 'Campaña'], ['utm_content', 'Anuncio'], ['utm_term', 'Conjunto'], ['utm_source', 'Fuente'],
  ['pagina', 'Página'], ['id', 'ID'],
];
const TEXTOS = {
  plazo: { 'antes-15-ene': 'Antes del 15 de enero', 'proximos-meses': 'En los próximos meses', 'sin-fecha': 'Todavía no tiene fecha', 'averiguando': 'Solo está averiguando' },
  pago: { 'contado': 'De contado', 'financiacion': 'Con financiación', 'no-alcanza': 'No le alcanza ahora' },
  valoracion: { 'esta-semana': 'Sí, esta semana', 'mas-adelante': 'Sí, más adelante', 'info': 'Primero quiere información' },
};
const COLORES = { A: '#d9ead3', B: '#fff2cc', C: '#efefef' };
const ETIQUETAS = { A: '🟢 A · caliente', B: '🟡 B · tibio', C: '⚪ C · frío' };

function hoja_() {
  const libro = SpreadsheetApp.getActiveSpreadsheet();
  return libro.getSheetByName(PESTANA) || libro.insertSheet(PESTANA);
}

function preparar() {
  const h = hoja_();
  h.getRange(1, 1, 1, COLUMNAS.length).setValues([COLUMNAS.map((c) => c[1])])
    .setFontWeight('bold').setBackground('#111111').setFontColor('#ffffff');
  h.setFrozenRows(1);
  h.setColumnWidths(1, COLUMNAS.length, 150);
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const d = JSON.parse(e.postData.contents || '{}');
    if (!d.nombre || !d.whatsapp) return ContentService.createTextOutput('falta');
    const h = hoja_();
    if (h.getLastRow() === 0) preparar();
    // no repetir el mismo lead si llega dos veces
    if (d.id && h.getLastRow() > 1) {
      const ids = h.getRange(2, COLUMNAS.length, h.getLastRow() - 1, 1).getValues().flat();
      if (ids.includes(d.id)) return ContentService.createTextOutput('repetido');
    }
    const fila = COLUMNAS.map(([k]) => {
      let v = d[k] || '';
      if (TEXTOS[k] && TEXTOS[k][v]) v = TEXTOS[k][v];
      if (k === 'puntaje') v = ETIQUETAS[v] || v;
      if (k === 'whatsapp') v = "'+" + String(v).replace(/\D/g, '');
      return String(v).slice(0, 300);
    });
    h.appendRow(fila);
    h.getRange(h.getLastRow(), 1, 1, COLUMNAS.length).setBackground(COLORES[d.puntaje] || null);
    if (CORREO_AVISO && d.puntaje === 'A') {
      MailApp.sendEmail(CORREO_AVISO, '🟢 Lead A: ' + d.nombre + ' · ' + d.cirugia,
        d.nombre + ' quiere ' + d.cirugia + '.\nWhatsApp: https://wa.me/' + String(d.whatsapp).replace(/\D/g, '') +
        '\nPara cuándo: ' + (TEXTOS.plazo[d.plazo] || '') + '\nPago: ' + (TEXTOS.pago[d.pago] || ''));
    }
    return ContentService.createTextOutput('ok');
  } finally {
    lock.releaseLock();
  }
}
