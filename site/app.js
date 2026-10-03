(() => {
  const key = 'mlpower-clase01-read';
  let read = [];
  try { const saved = JSON.parse(localStorage.getItem(key) || '[]'); if (Array.isArray(saved)) read = saved.filter(n => Number.isInteger(n) && n >= 1 && n <= 33); } catch {}
  read = [...new Set(read)];
  const current = Number(document.body.dataset.current);
  const mark = document.getElementById('mark-read');
  const status = document.getElementById('save-status');
  const links = [...document.querySelectorAll('.lesson-link')];
  function update() {
    document.getElementById('read-count').textContent = `${read.length} / 33`;
    document.getElementById('progress').value = read.length;
    links.forEach(a => a.classList.toggle('is-read', read.includes(Number(a.dataset.slide))));
    if (mark) { const done = read.includes(current); mark.setAttribute('aria-pressed', String(done)); mark.textContent = done ? 'Leída ✓' : 'Marcar como leída'; }
  }
  update();
  if (current) { try { localStorage.setItem('mlpower-last', String(current)); } catch {} }
  const resume = document.getElementById('resume');
  if (resume) { try { const last = Number(localStorage.getItem('mlpower-last')); if (last >= 1 && last <= 33) resume.href = `/clase-01/diapositiva-${String(last).padStart(2,'0')}.html`; } catch {} }
  if (mark) mark.addEventListener('click', () => { read = read.includes(current) ? read.filter(n => n !== current) : [...read,current]; update(); try { localStorage.setItem(key,JSON.stringify(read)); status.textContent = 'Progreso guardado en este navegador.'; } catch { status.textContent = 'No se pudo guardar el progreso en este navegador.'; } });
  const norm = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  document.getElementById('search').addEventListener('input', e => { const q = norm(e.target.value.trim()); let visible = 0; links.forEach(a => { a.hidden = !norm(a.dataset.search).includes(q); if (!a.hidden) visible++; }); document.querySelectorAll('nav h3').forEach(h => { let next = h.nextElementSibling, has = false; while (next && next.tagName !== 'H3') { if (!next.hidden) has = true; next = next.nextElementSibling; } h.hidden = !has; }); document.getElementById('no-results').hidden = visible > 0; });
  document.getElementById('menu').addEventListener('click', e => { const open = document.body.classList.toggle('menu-open'); e.currentTarget.setAttribute('aria-expanded',String(open)); });
  document.addEventListener('keydown',e => { if (e.key === 'Escape') { document.body.classList.remove('menu-open'); document.getElementById('menu').setAttribute('aria-expanded','false'); } });
  const print = document.getElementById('print'); if (print) print.addEventListener('click', () => window.print());
})();
