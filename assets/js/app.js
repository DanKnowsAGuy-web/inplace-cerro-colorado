/* Cerro Colorado / In-Place BaseGrade — interactive report behaviours.
   Tab switching, count-up stats, CBR threshold, scrollytelling,
   reveal-on-scroll, scrollspy, reading progress, lightbox, blur-up,
   and a textured parallax hero. Vanilla JS, no dependencies. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('has-js');
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var IO = window.IntersectionObserver;

  function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }
  function isES(el) { var p = el.closest('.tab-panel'); return p && /^es/.test(p.id); }

  /* ---------------------------------------------------------- count-up */
  function fmt(n, dec, comma) {
    var s = dec > 0 ? n.toFixed(dec) : Math.round(n).toString();
    if (comma) {
      var parts = s.split('.');
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      s = parts.join('.');
    }
    return s;
  }
  function countUp(el) {
    if (el.dataset.counted) return;
    var groups = el.textContent.match(/\d[\d,]*(?:\.\d+)?/g);
    if (!groups || groups.length !== 1) { el.dataset.counted = '1'; return; }
    var raw = groups[0], comma = raw.indexOf(',') > -1, clean = raw.replace(/,/g, '');
    var dec = (clean.split('.')[1] || '').length, target = parseFloat(clean);
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null), node, tn = null, idx = -1;
    while ((node = walker.nextNode())) { var i = node.nodeValue.indexOf(raw); if (i > -1) { tn = node; idx = i; break; } }
    if (!tn) { el.dataset.counted = '1'; return; }
    var before = tn.nodeValue.slice(0, idx), after = tn.nodeValue.slice(idx + raw.length);
    el.dataset.counted = '1';
    if (RM) { tn.nodeValue = before + fmt(target, dec, comma) + after; return; }
    var dur = 1100, start = null;
    function frame(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      tn.nodeValue = before + fmt(target * easeOutCubic(p), dec, comma) + after;
      if (p < 1) requestAnimationFrame(frame);
      else tn.nodeValue = before + fmt(target, dec, comma) + after;
    }
    requestAnimationFrame(frame);
  }

  /* ------------------------------------------------ CBR bars + threshold */
  var THR = 0.765; // bar width fraction that corresponds to 100% CBR
  var doneTbs = [];
  function drawThreshold(tb) {
    var wraps = tb.querySelectorAll('.tr-bar-wrap');
    if (!wraps.length) return;
    var line = tb.querySelector('.tb-thr');
    if (!line) {
      line = document.createElement('div');
      line.className = 'tb-thr';
      line.innerHTML = '<span class="tb-thr-flag">100%</span>';
      tb.appendChild(line);
    }
    var tbR = tb.getBoundingClientRect();
    var first = wraps[0].getBoundingClientRect(), last = wraps[wraps.length - 1].getBoundingClientRect();
    if (!first.width) return;
    line.style.left = ((first.left - tbR.left) + first.width * THR) + 'px';
    line.style.top = ((first.top - tbR.top) - 8) + 'px';
    line.style.height = ((last.bottom - first.top) + 16) + 'px';
    requestAnimationFrame(function () { line.classList.add('show'); });
  }
  function tagRows(tb) {
    var es = isES(tb);
    tb.querySelectorAll('.tr').forEach(function (tr) {
      if (tr.querySelector('.tr-tag')) return;
      // Derive CBR from the bar's data-w (source of truth) so we don't read
      // the .tr-val text while its count-up is still animating.
      var w = parseFloat((tr.querySelector('.tr-bar') || {}).getAttribute &&
        tr.querySelector('.tr-bar').getAttribute('data-w'));
      if (isNaN(w)) return;
      var v = w / THR;
      var pass = v >= 98;
      tr.classList.add(pass ? 'tr-pass' : 'tr-below');
      var tag = document.createElement('span');
      tag.className = 'tr-tag';
      tag.textContent = pass ? (es ? 'CUMPLE' : 'PASSES') : (es ? 'DEBAJO' : 'BELOW');
      (tr.querySelector('.tr-val-wrap') || tr).appendChild(tag);
      requestAnimationFrame(function () { tag.classList.add('show'); });
    });
  }
  function triggerTb(tb) {
    if (tb.dataset.tbDone) return;
    tb.dataset.tbDone = '1';
    tb.querySelectorAll('.tr-bar').forEach(function (b) { b.style.width = (b.getAttribute('data-w') || 0) + '%'; });
    tb.querySelectorAll('.tr-val').forEach(countUp);
    drawThreshold(tb);
    doneTbs.push(tb);
    setTimeout(function () { tagRows(tb); }, RM ? 0 : 650);
  }

  /* --------------------------------------------------------- observers */
  if (IO) {
    var revealObs = new IO(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); revealObs.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

    var revealSel = '.eyebrow,h2,h3,.lead,.preface,.dc,.tb,.table-wrap,.cred,.pq,.fig,.gal figure,.cert figure,.mapwrap,.doc-title,.doc-meta';
    document.querySelectorAll(revealSel).forEach(function (el) {
      el.classList.add('reveal');
      revealObs.observe(el);
    });
    // staggered cascade inside grids/galleries
    document.querySelectorAll('.dc-grid,.gallery,.certgrid').forEach(function (grid) {
      Array.prototype.forEach.call(grid.children, function (child, i) {
        var d = (i % 4 * 0.07) + 's';
        var r = child.classList.contains('reveal') ? child : child.querySelector('.reveal');
        if (r) r.style.transitionDelay = d;
      });
    });

    var countObs = new IO(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { countUp(e.target); countObs.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.4 });
    document.querySelectorAll('.dc-num').forEach(function (el) { countObs.observe(el); });

    var tbObs = new IO(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { triggerTb(e.target); tbObs.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.25 });
    document.querySelectorAll('.tb').forEach(function (tb) { tbObs.observe(tb); });

    var spyObs = new IO(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var panel = e.target.closest('.tab-panel'); if (!panel) return;
        panel.querySelectorAll('.toc-item').forEach(function (a) {
          a.classList.toggle('toc-active', a.getAttribute('href') === '#' + e.target.id);
        });
      });
    }, { rootMargin: '-28% 0px -62% 0px', threshold: 0 });
    document.querySelectorAll('.tab-panel section[id]').forEach(function (s) { spyObs.observe(s); });
  } else {
    document.querySelectorAll('.tb').forEach(triggerTb);
    document.querySelectorAll('.dc-num,.tr-val').forEach(countUp);
  }

  /* ------------------------------------------- scrollytelling (method) */
  function buildScrolly(sec) {
    var steps = Array.prototype.slice.call(sec.querySelectorAll('.ps'));
    if (steps.length < 2) return;
    var imgs = ['pg10_1', 'pg11_1', 'pg10_1', 'pg12_1', 'pg30_1'];
    var host = steps[0].parentNode;
    var scrolly = document.createElement('div'); scrolly.className = 'scrolly';
    var visual = document.createElement('div'); visual.className = 'scrolly-visual';
    visual.innerHTML = '<figure><img class="scrolly-img" alt=""><figcaption class="scrolly-cap"></figcaption></figure>';
    var wrap = document.createElement('div'); wrap.className = 'scrolly-steps';
    host.insertBefore(scrolly, steps[0]);
    scrolly.appendChild(visual); scrolly.appendChild(wrap);
    steps.forEach(function (ps, i) {
      ps.dataset.img = 'assets/img/' + (imgs[i] || imgs[imgs.length - 1]) + '.jpg';
      var h = ps.querySelector('h3'); ps.dataset.cap = h ? h.textContent : '';
      wrap.appendChild(ps);
    });
    var gal = sec.querySelector('.gallery'); if (gal) gal.parentNode.removeChild(gal);
    var img = visual.querySelector('.scrolly-img'), cap = visual.querySelector('.scrolly-cap'), cur = -1;
    function setStep(i) {
      if (i === cur) return; cur = i;
      img.src = steps[i].dataset.img; cap.textContent = steps[i].dataset.cap;
      steps.forEach(function (s, j) { s.classList.toggle('step-active', j === i); });
    }
    setStep(0);
    if (IO) {
      var so = new IO(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { var i = steps.indexOf(e.target); if (i > -1) setStep(i); } });
      }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
      steps.forEach(function (s) { so.observe(s); });
    } else { steps.forEach(function (s) { s.classList.add('step-active'); }); }
  }
  document.querySelectorAll('.tab-panel section[id$="5"]').forEach(buildScrolly);

  /* ---------------------------------------------------------- blur-up */
  document.querySelectorAll('.gal img,.cert img,.fig img').forEach(function (img) {
    img.classList.add('imgfx');
    if (img.complete && img.naturalWidth) img.classList.add('ready');
    else img.addEventListener('load', function () { img.classList.add('ready'); });
    img.addEventListener('error', function () { img.classList.add('ready'); });
  });

  /* --------------------------------------------------------- lightbox */
  var lb = document.createElement('div');
  lb.className = 'lb'; lb.setAttribute('aria-hidden', 'true');
  lb.innerHTML = '<button class="lb-btn lb-close" aria-label="Close">×</button>' +
    '<button class="lb-btn lb-prev" aria-label="Previous">‹</button>' +
    '<button class="lb-btn lb-next" aria-label="Next">›</button>' +
    '<figure class="lb-fig"><img class="lb-img" alt=""><figcaption class="lb-cap"></figcaption></figure>';
  document.body.appendChild(lb);
  var lbImg = lb.querySelector('.lb-img'), lbCap = lb.querySelector('.lb-cap');
  var lbPrev = lb.querySelector('.lb-prev'), lbNext = lb.querySelector('.lb-next');
  var lbList = [], lbIdx = 0;
  function lbShow(i) {
    lbIdx = (i + lbList.length) % lbList.length;
    var im = lbList[lbIdx], fig = im.closest('figure'), fc = fig && fig.querySelector('figcaption');
    lbImg.src = im.currentSrc || im.src;
    lbCap.innerHTML = fc ? fc.innerHTML : (im.alt || '');
    var multi = lbList.length > 1;
    lbPrev.classList.toggle('hide', !multi); lbNext.classList.toggle('hide', !multi);
  }
  function lbOpen(img) {
    var c = img.closest('.gallery,.certgrid');
    lbList = c ? Array.prototype.slice.call(c.querySelectorAll('img')) : [img];
    lbShow(lbList.indexOf(img));
    lb.classList.add('open'); lb.setAttribute('aria-hidden', 'false');
  }
  function lbClose() { lb.classList.remove('open'); lb.setAttribute('aria-hidden', 'true'); lbImg.src = ''; }
  document.addEventListener('click', function (e) {
    var img = e.target.closest && e.target.closest('img');
    if (img && img.matches('.gal img,.cert img,.fig img')) { e.preventDefault(); lbOpen(img); }
  });
  lb.querySelector('.lb-close').addEventListener('click', lbClose);
  lbPrev.addEventListener('click', function () { lbShow(lbIdx - 1); });
  lbNext.addEventListener('click', function () { lbShow(lbIdx + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb-fig')) lbClose(); });
  document.addEventListener('keydown', function (e) {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') lbClose();
    else if (e.key === 'ArrowLeft') lbShow(lbIdx - 1);
    else if (e.key === 'ArrowRight') lbShow(lbIdx + 1);
  });

  /* --------------------------------------------- hero texture + parallax */
  var cover = document.querySelector('.cover');
  var topo = null;
  if (cover) {
    var topoSvg = "<svg xmlns='http://www.w3.org/2000/svg' width='1400' height='720' viewBox='0 0 1400 720'><g fill='none' stroke='#9a7232' stroke-width='1.1'>" +
      "<path d='M-20 70 C 240 24 470 140 700 92 S 1180 18 1420 104'/>" +
      "<path d='M-20 158 C 250 110 470 226 700 178 S 1190 104 1420 192'/>" +
      "<path d='M-20 246 C 240 198 480 314 700 266 S 1180 192 1420 280'/>" +
      "<path d='M-20 334 C 250 286 470 402 700 354 S 1190 280 1420 368'/>" +
      "<path d='M-20 422 C 240 374 480 490 700 442 S 1180 368 1420 456'/>" +
      "<path d='M-20 510 C 250 462 470 578 700 530 S 1190 456 1420 544'/>" +
      "<path d='M-20 598 C 240 550 480 666 700 618 S 1180 544 1420 632'/>" +
      "<path d='M-20 686 C 250 638 470 754 700 706 S 1190 632 1420 720'/>" +
      "</g></svg>";
    var grainSvg = "<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/></filter><rect width='160' height='160' filter='url(#n)'/></svg>";
    topo = document.createElement('div'); topo.className = 'cover-topo';
    topo.style.backgroundImage = "url(\"data:image/svg+xml," + encodeURIComponent(topoSvg) + "\")";
    var grain = document.createElement('div'); grain.className = 'cover-grain';
    grain.style.backgroundImage = "url(\"data:image/svg+xml," + encodeURIComponent(grainSvg) + "\")";
    cover.insertBefore(grain, cover.firstChild);
    cover.insertBefore(topo, cover.firstChild);
  }

  /* ------------------------------------------ progress bar + parallax */
  var bar = document.createElement('div'); bar.className = 'progress'; document.body.appendChild(bar);
  var ticking = false;
  function onScroll() {
    var max = root.scrollHeight - root.clientHeight;
    var y = window.pageYOffset || root.scrollTop || 0;
    bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(y / max, 1) : 0) + ')';
    if (topo && !RM) topo.style.transform = 'translateY(' + (y * 0.22) + 'px)';
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  /* ------------------------------------------------------ resize redraw */
  var rt;
  window.addEventListener('resize', function () {
    clearTimeout(rt);
    rt = setTimeout(function () {
      doneTbs.forEach(function (tb) { if (tb.offsetParent !== null) drawThreshold(tb); });
    }, 150);
  });

  /* -------------------------------------------------------- tab switch */
  // The sticky header stays in the reader's chosen language and only toggles
  // Full Report <-> Summary. A subtle switch flips language (keeping the same
  // report type), labelled in the *other* language so each reader recognises it.
  var LBL = {
    en: { full: 'Full Report', sum: 'Summary', other: 'Español', aria: 'Cambiar a español / Switch to Spanish' },
    es: { full: 'Informe Completo', sum: 'Resumen', other: 'English', aria: 'Switch to English / Cambiar a inglés' }
  };
  var state = { lang: 'en', type: 'full' };
  var fullBtn = document.querySelector('.type-btn[data-type="full"]');
  var sumBtn = document.querySelector('.type-btn[data-type="sum"]');
  var langSwitch = document.querySelector('.lang-switch');

  function applyTabs(scrollToBar) {
    var id = state.lang + state.type;
    document.querySelectorAll('.tab-panel').forEach(function (p) { p.classList.toggle('active', p.id === id); });
    var L = LBL[state.lang];
    if (fullBtn) { fullBtn.textContent = L.full; fullBtn.classList.toggle('active', state.type === 'full'); }
    if (sumBtn) { sumBtn.textContent = L.sum; sumBtn.classList.toggle('active', state.type === 'sum'); }
    if (langSwitch) {
      langSwitch.querySelector('.ls-txt').textContent = L.other;
      langSwitch.setAttribute('aria-label', L.aria);
    }
    var panel = document.getElementById(id);
    requestAnimationFrame(function () {
      if (panel) panel.querySelectorAll('.tb[data-tb-done]').forEach(drawThreshold);
      onScroll();
    });
    if (scrollToBar) {
      var tabsBar = document.querySelector('.tabs-bar');
      if (tabsBar) window.scrollTo({ top: tabsBar.offsetTop, behavior: 'instant' });
    }
  }

  if (fullBtn) fullBtn.addEventListener('click', function () { state.type = 'full'; applyTabs(true); });
  if (sumBtn) sumBtn.addEventListener('click', function () { state.type = 'sum'; applyTabs(true); });
  if (langSwitch) langSwitch.addEventListener('click', function () {
    state.lang = state.lang === 'en' ? 'es' : 'en'; applyTabs(true);
  });
  applyTabs(false);
})();
