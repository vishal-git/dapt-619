/* Minimal presentation engine: slides + click-fragments + progress bar + overview. No dependencies. */
(() => {
  const deck = document.getElementById('deck');
  const slides = [...deck.querySelectorAll('.slide')];
  const bar = document.querySelector('#progress > i');
  const hudL = document.getElementById('hud-l');
  const hudR = document.getElementById('hud-r');
  const overview = document.getElementById('overview');
  const helpbox = document.getElementById('helpbox');
  let cur = 0, frag = 0, lastDir = 1;
  const W = 1280, H = 720;

  // Pre-compute fragment steps per slide (sorted unique data-f values)
  const steps = slides.map(s => {
    const vals = [...s.querySelectorAll('[data-f],[data-fa]')].map(e => +(e.dataset.f ?? e.dataset.fa));
    return [...new Set(vals)].sort((a, b) => a - b);
  });
  const totalSteps = steps.reduce((n, s) => n + s.length + 1, 0);
  const stepsBefore = slides.map((_, i) => steps.slice(0, i).reduce((n, s) => n + s.length + 1, 0));

  function fit() {
    const sc = Math.min(innerWidth / W, (innerHeight - 6) / H);
    deck.style.transform = `scale(${sc})`;
  }
  addEventListener('resize', fit); fit();

  function applyFrags() {
    const s = slides[cur];
    const shown = new Set(steps[cur].slice(0, frag));
    s.querySelectorAll('[data-f],[data-fa]').forEach(e => e.classList.toggle('on', shown.has(+(e.dataset.f ?? e.dataset.fa))));
  }

  // Section badge: icon + name of the current section, shown on every slide after its divider
  const secinfo = []; let curSec = null;
  slides.forEach((s, i) => {
    if (s.classList.contains('section') && !s.classList.contains('quiz')) {
      const use = s.querySelector('.big-ico use');
      curSec = { icon: use ? use.getAttribute('href') : null, name: s.dataset.section || '', num: (s.querySelector('.kicker') || {}).textContent || '' };
      secinfo[i] = null; // the divider itself shows no badge
    } else secinfo[i] = s.dataset.section ? curSec : null;
  });
  const badgeEl = document.getElementById('secbadge');
  function badge(i) {
    const s = secinfo[i];
    if (!s || !s.icon) { badgeEl.classList.remove('show'); return; }
    badgeEl.innerHTML = `<svg class="ico"><use href="${s.icon}"/></svg><span>${s.num.replace(/section\s*/i, '')} · <b>${s.name}</b></span>`;
    badgeEl.classList.add('show');
  }
  // Roadmap breadcrumb: where this slide sits in today's session (Part 2 only)
  const ROADMAP = [
    { key: 'Warm-up', label: 'Warm-up', icon: '#i-quiz', s: 1 },
    { key: 'Testing', label: 'Testing', icon: '#i-flask', s: 1 },
    { key: 'Structure', label: 'Structure', icon: '#i-tree', s: 1 },
    { key: 'Gradio', label: 'Gradio', icon: '#i-app', s: 2 },
    { key: 'Polars', label: 'Polars', icon: '#i-bolt', s: 2 },
    { key: 'Tabular FMs', label: 'Foundation models', icon: '#i-brain', s: 2 },
  ];
  const APPENDIX = { 'Cookiecutter': 'A', 'Beyond your laptop': 'B', 'More tabular FMs': 'C' };
  const roadEl = document.getElementById('roadmap');
  function roadmap(i) {
    if (!roadEl) return;
    const key = (slides[i].dataset.section || '').split(' · ')[0];
    if (APPENDIX[key]) { roadEl.innerHTML = `<span class="stop now">Appendix ${APPENDIX[key]} · ${key}</span>`; roadEl.classList.add('show'); return; }
    const at = ROADMAP.findIndex(r => r.key === key);
    if (at < 0) { roadEl.classList.remove('show'); return; }
    const sess = ROADMAP[at].s;
    roadEl.innerHTML = `<span class="sess">Session ${sess}</span>` + ROADMAP.filter(r => r.s === sess).map(r => {
      const k = ROADMAP.indexOf(r);
      return `<span class="stop ${k < at ? 'done' : k === at ? 'now' : ''}"><svg class="ico"><use href="${r.icon}"/></svg>${r.label}</span>`;
    }).join('<span class="sep">›</span>');
    roadEl.classList.add('show');
  }
  // Quiz progress: "Quick check ▬▬▭" on each question slide of a run
  (() => {
    let run = [];
    const flush = () => { run.forEach((s, k) => {
      const d = document.createElement('div'); d.className = 'qprog';
      d.innerHTML = `Q${k + 1} of ${run.length} ` + run.map((_, m) => `<i class="${m <= k ? 'on' : ''}"></i>`).join('');
      s.appendChild(d);
    }); run = []; };
    slides.forEach(s => { if (s.classList.contains('q')) run.push(s); else flush(); });
    flush();
  })();

  let prevCur = -1;
  function render(dir) {
    if (prevCur !== cur && prevCur >= 0) slides[prevCur].querySelectorAll('iframe').forEach(f => { f.src = f.src; }); // stop embedded video when leaving a slide
    prevCur = cur;
    slides.forEach((s, i) => { s.classList.toggle('active', i === cur); s.classList.toggle('back', i === cur && dir < 0); });
    applyFrags();
    bar.style.width = (100 * (cur + 1) / slides.length) + '%';
    badge(cur);
    roadmap(cur);
    const sec = slides[cur].dataset.section || '';
    hudL.innerHTML = `<b>DAPT 619</b> · Analytics Computing${sec ? ' · ' + sec : ''}`;
    hudR.innerHTML = `<b>${cur + 1}</b> / ${slides.length}${steps[cur].length ? ` · <span style="color:var(--dim)">${frag}/${steps[cur].length}</span>` : ''}`;
    history.replaceState(null, '', `#${cur + 1}${frag ? '.' + frag : ''}`);
  }

  function next() {
    if (frag < steps[cur].length) { frag++; applyFrags(); render(1); return; }
    if (cur < slides.length - 1) { cur++; frag = 0; render(1); }
  }
  function prev() {
    if (frag > 0) { frag--; applyFrags(); render(-1); return; }
    if (cur > 0) { cur--; frag = steps[cur].length; render(-1); }
  }
  function goto(i, f = 0, dir = 1) {
    cur = Math.max(0, Math.min(slides.length - 1, i));
    frag = Math.max(0, Math.min(steps[cur].length, f));
    render(dir);
  }
  function nextSlide() { if (cur < slides.length - 1) goto(cur + 1, 0, 1); }
  function prevSlide() { if (cur > 0) goto(cur - 1, 0, -1); }

  // Overview grid
  const grid = overview.querySelector('.grid');
  slides.forEach((s, i) => {
    const d = document.createElement('div');
    d.className = 'thumb' + (s.classList.contains('section') ? (s.classList.contains('quiz') ? ' quiz' : ' sec') : '');
    const t = s.dataset.title || (s.querySelector('h1,h2') || {}).textContent || '';
    d.innerHTML = `<b>${t.trim().slice(0, 48)}</b>${s.dataset.section || ''}<i>${i + 1}</i>`;
    d.onclick = () => { closeOverview(); goto(i); };
    grid.appendChild(d);
  });
  function openOverview() { overview.classList.add('open'); grid.children[cur].classList.add('current'); grid.children[cur].scrollIntoView({ block: 'center' }); }
  function closeOverview() { overview.classList.remove('open'); [...grid.children].forEach(c => c.classList.remove('current')); }

  // Keyboard
  addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (helpbox.classList.contains('open')) { helpbox.classList.remove('open'); return; }
    if (overview.classList.contains('open')) { if (e.key === 'Escape' || e.key === 'o') closeOverview(); return; }
    switch (e.key) {
      case 'ArrowRight': case 'ArrowDown': case ' ': case 'PageDown': case 'Enter': e.preventDefault(); next(); break;
      case 'ArrowLeft': case 'ArrowUp': case 'Backspace': case 'PageUp': e.preventDefault(); prev(); break;
      case 'n': nextSlide(); break;
      case 'p': prevSlide(); break;
      case 'Home': goto(0); break;
      case 'End': goto(slides.length - 1, steps[slides.length - 1].length); break;
      case 'o': case 'Escape': openOverview(); break;
      case 'f': document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen(); break;
      case 'a': document.body.classList.toggle('no-anim'); break;
      case '?': case 'h': helpbox.classList.toggle('open'); break;
      case 'b': document.body.classList.toggle('blackout'); break;
    }
  });
  // Mouse: click advances, shift/right-click goes back. Presentation clickers send PageDown/PageUp.
  // In-deck jump links: <a class="jump" href="#slide-id"> goes to the <section id="slide-id">; <a class="jump back"> returns
  // to the slide the last jump came from (or to its own href if the deck was opened directly on the appendix).
  const backStack = [];
  const slideById = id => slides.findIndex(s => s.id === id);
  deck.addEventListener('click', e => {
    const a = e.target.closest('a');
    if (a) {
      const href = a.getAttribute('href') || '';
      if (a.classList.contains('jump') && href.startsWith('#')) {
        e.preventDefault();
        if (a.classList.contains('back') && backStack.length) { const i = backStack.pop(); goto(i, steps[i].length, -1); return; }
        const i = slideById(href.slice(1));
        if (i >= 0) { if (!a.classList.contains('back') && !a.classList.contains('skip')) backStack.push(cur); goto(i, 0, 1); }
      }
      return;
    }
    e.shiftKey ? prev() : next();
  });
  deck.addEventListener('contextmenu', e => { e.preventDefault(); prev(); });
  // Mouse wheel: one step per notch, throttled
  let wheelAt = 0;
  addEventListener('wheel', e => {
    if (overview.classList.contains('open') || helpbox.classList.contains('open')) return;
    const now = Date.now(); if (now - wheelAt < 350 || Math.abs(e.deltaY) < 4) return; wheelAt = now;
    e.deltaY > 0 ? next() : prev();
  }, { passive: true });
  // Touch swipe
  let tx = null;
  addEventListener('touchstart', e => { tx = e.touches[0].clientX; }, { passive: true });
  addEventListener('touchend', e => { if (tx === null) return; const dx = e.changedTouches[0].clientX - tx; if (Math.abs(dx) > 40) dx < 0 ? next() : prev(); else next(); tx = null; });
  document.getElementById('help').onclick = () => helpbox.classList.toggle('open');
  helpbox.onclick = () => helpbox.classList.remove('open');
  overview.onclick = e => { if (e.target === overview) closeOverview(); };

  // Start from hash (#12 or #12.3)
  const m = location.hash.match(/#(\d+)(?:\.(\d+))?/);
  goto(m ? +m[1] - 1 : 0, m ? +(m[2] || 0) : 0);
  addEventListener('hashchange', () => { const m = location.hash.match(/#(\d+)(?:\.(\d+))?/); if (m && (+m[1] - 1 !== cur)) goto(+m[1] - 1, +(m[2] || 0)); });
  addEventListener('hashchange', () => { const i = slideById(decodeURIComponent(location.hash.slice(1))); if (i >= 0 && i !== cur) goto(i); });

  // Embedded video: YouTube rejects embeds from file:// pages (error 153), so only embed when served over http(s).
  document.querySelectorAll('.yt-slot').forEach(slot => {
    if (location.protocol.startsWith('http')) {
      slot.innerHTML = `<iframe class="shot" width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/${slot.dataset.video}" title="YouTube video" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen style="background:#000;display:block"></iframe>`;
    }
  });
  // Title-slide punch card: hover a column to decode it
  document.querySelectorAll('.title-slide .hero .card').forEach(card => {
    const clear = () => card.querySelectorAll('.lit').forEach(e => e.classList.remove('lit'));
    card.querySelectorAll('.colhit').forEach(hit => hit.addEventListener('mouseenter', () => {
      const { col } = hit.dataset;
      card.classList.add('decoding'); clear();
      card.querySelectorAll(`[data-col="${col}"]`).forEach(e => e.classList.add('lit'));
    }));
    card.addEventListener('mouseleave', () => { card.classList.remove('decoding'); clear(); });
  });
  // expose for testing
  window.Deck = { next, prev, goto, backStack, get cur() { return cur; }, get frag() { return frag; }, steps, count: slides.length };
})();
