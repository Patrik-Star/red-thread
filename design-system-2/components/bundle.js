/* @ds-bundle: {"format":4,"namespace":"RedThread","components":[{"name":"Wordmark"},{"name":"Button"},{"name":"CaseTag"},{"name":"ThreadDivider"},{"name":"GameNote"},{"name":"Evidence"},{"name":"Receipt"},{"name":"PhoneScreenshot"},{"name":"PhoneRecords"},{"name":"BankStatement"},{"name":"Ticket"},{"name":"HandwrittenNote"},{"name":"CctvStill"},{"name":"Printout"}]} */
(function () {
  var R = window.React, h = R.createElement;
  function cx() { return Array.prototype.filter.call(arguments, Boolean).join(' '); }
  function pad(n) { return n != null ? String(n).padStart(2, '0') : ''; }
  // "[redacted]" inside any evidence string becomes a black bar.
  function txt(s) {
    if (typeof s !== 'string' || s.indexOf('[redacted]') < 0) return s;
    return s.split('[redacted]').reduce(function (acc, part, i) {
      if (i) acc.push(h('span', { key: 'r' + i, className: 'rt-redact', role: 'img', 'aria-label': 'redacted' }));
      if (part) acc.push(part);
      return acc;
    }, []);
  }

  /* ---------- Game layer ---------- */

  function Wordmark(p) {
    var size = p.size || 'md';
    return h('span', { className: cx('rt-wordmark', 'rt-wordmark-' + size, p.className), role: 'img', 'aria-label': 'Red Thread' },
      h('svg', { className: 'rt-wordmark-thread', viewBox: '0 0 100 10', preserveAspectRatio: 'none', 'aria-hidden': true },
        h('path', { d: 'M0 3 C 18 9, 40 10, 62 8 S 90 4, 100 2' })),
      h('span', { className: 'rt-wordmark-text', 'aria-hidden': true }, 'Red Thread'),
      h('span', { className: 'rt-wordmark-pin', 'aria-hidden': true }));
  }

  function Button(p) {
    var variant = p.variant || 'ghost', size = p.size || 'md';
    var rest = {};
    for (var k in p) if (k !== 'variant' && k !== 'size' && k !== 'className' && k !== 'children') rest[k] = p[k];
    rest.className = cx('rt-btn', 'rt-btn-' + variant, size === 'sm' && 'rt-btn-sm', p.className);
    if (!rest.type) rest.type = 'button';
    return h('button', rest, p.children);
  }

  function CaseTag(p) {
    return h('span', { className: cx('rt-tag', 'rt-tag-' + (p.tone || 'neutral'), p.className) }, p.children);
  }

  function ThreadDivider(p) {
    return h('div', { className: cx('rt-divider', p.className), role: 'separator' },
      p.label ? h('span', null, p.label) : h('span', { className: 'rt-divider-knot', 'aria-hidden': true }));
  }

  function CodeCells(p) {
    var n = p.length || 4;
    var refs = R.useRef([]);
    var st = R.useState(function () { return Array(n).fill(''); }), vals = st[0], setVals = st[1];
    if (vals.length !== n) { vals = Array(n).fill(''); }
    var done = p.state === 'right';
    function commit(next) {
      setVals(next);
      if (next.every(Boolean) && p.onComplete) p.onComplete(next.join(''));
    }
    function clean(v) { return (v || '').replace(p.numeric ? /[^0-9]/g : /[^0-9A-Za-z\u00C0-\u017F]/g, '').toUpperCase(); }
    function fill(i, chars) {
      var next = vals.slice(), j = i;
      for (var k = 0; k < chars.length && j < n; k++, j++) next[j] = chars[k];
      commit(next);
      var to = Math.min(j, n - 1);
      if (refs.current[to]) refs.current[to].focus();
    }
    function change(i, e) {
      var c = clean(e.target.value);
      if (c.length > 1) return fill(i, c.slice(vals[i] && c[0] === vals[i] ? 1 : 0));
      var next = vals.slice(); next[i] = c; commit(next);
      if (c && i < n - 1) refs.current[i + 1].focus();
    }
    function paste(i, e) {
      var c = clean(e.clipboardData && e.clipboardData.getData('text'));
      if (!c) return;
      e.preventDefault(); fill(i, c);
    }
    function key(i, e) {
      if (e.key === 'Backspace' && !vals[i] && i > 0) refs.current[i - 1].focus();
      else if (e.key === 'ArrowLeft' && i > 0) refs.current[i - 1].focus();
      else if (e.key === 'ArrowRight' && i < n - 1) refs.current[i + 1].focus();
    }
    var id = R.useId ? R.useId() : 'code';
    var label = p.label || 'Unlock code';
    return h('div', { className: 'rt-note-code', 'data-state': p.state || undefined },
      h('label', { className: 'rt-note-code-label', htmlFor: id + '0' }, label),
      h('div', { className: 'rt-note-code-cells', role: 'group', 'aria-label': label + ', ' + n + (p.numeric ? ' digits' : ' characters') },
        vals.map(function (v, i) {
          return h('input', { key: i, id: id + i, ref: function (el) { refs.current[i] = el; }, value: v, inputMode: p.numeric ? 'numeric' : 'text', autoComplete: 'one-time-code', autoCapitalize: 'characters', spellCheck: false, maxLength: n, disabled: p.disabled || done, 'aria-invalid': p.state === 'wrong' || undefined, 'aria-label': 'Character ' + (i + 1) + ' of ' + n, onChange: function (e) { change(i, e); }, onPaste: function (e) { paste(i, e); }, onKeyDown: function (e) { key(i, e); }, onFocus: function (e) { e.target.select(); } });
        })),
      p.message ? h('p', { className: 'rt-note-code-msg', 'data-state': p.state || undefined, role: p.state ? 'status' : undefined, 'aria-live': p.state ? 'polite' : undefined }, p.message) : null);
  }

  function GameNote(p) {
    var kind = p.kind || 'instruction';
    return h('section', { className: cx('rt-note', 'rt-note-' + kind, p.className), 'aria-label': p.ariaLabel },
      p.title ? h('h3', { className: 'rt-note-title' }, p.title) : null,
      p.children ? h('div', { className: 'rt-note-body' }, p.children) : null,
      kind === 'unlock' ? h(CodeCells, { key: 'len' + (p.codeLength || 4), length: p.codeLength, numeric: p.numeric, label: p.codeLabel, message: p.codeMessage, state: p.codeState, onComplete: p.onCode, disabled: p.disabled }) : null,
      (p.meta || p.metaEnd) ? h('div', { className: 'rt-note-meta' }, h('span', null, p.meta), p.metaEnd ? h('span', null, p.metaEnd) : null) : null);
  }

  function EvidenceTag(p) {
    var status = p.status || 'new';
    return h('div', { className: cx('rt-tagm', 'rt-tagm-' + status) },
      h('span', { className: 'rt-tagm-hole', 'aria-hidden': true }),
      h('div', { className: 'rt-tagm-meta' }, h('span', null, p.number != null ? 'Evidence ' + pad(p.number) : 'Evidence'), h('span', { className: 'rt-tagm-status' }, { 'new': 'New', found: 'Filed', locked: 'Locked' }[status])),
      p.title ? h('h3', { className: 'rt-tagm-title' }, p.title) : null,
      p.found ? h('div', { className: 'rt-tagm-found' }, h('span', null, 'Found '), p.found) : null);
  }

  function Evidence(p) {
    var status = p.status || 'new';
    var device = p.device;
    return h('figure', { className: cx('rt-ev', 'rt-ev-' + status, p.className), style: { margin: 0 } },
      (p.number != null || p.title) ? h(EvidenceTag, { number: p.number, status: status, title: p.title, found: p.found }) : null,
      h('div', { className: cx('rt-ev-object', device && 'rt-ev-object-device') },
        h('div', { 'aria-hidden': status === 'locked' ? true : undefined }, p.children),
        status === 'locked' ? h('div', { className: 'rt-ev-lock' }, h('div', { className: 'rt-note' }, h('div', { className: 'rt-note-body' }, p.lockedText || 'Reach the location to open this.'))) : null),
      p.caption ? h('figcaption', { className: 'rt-sr' }, p.caption) : null);
  }

  /* ---------- Story layer: evidence objects ---------- */

  function Receipt(p) {
    var lines = p.lines || [];
    return h('div', { className: 'rt-paper rt-receipt' },
      h('div', { className: 'rt-receipt-head' },
        p.heading ? h('div', { className: 'rt-receipt-heading' }, p.heading) : null,
        h('div', { className: 'rt-receipt-merchant' }, p.merchant),
        p.address ? h('div', null, p.address) : null,
        p.gstNumber ? h('div', { className: 'rt-receipt-muted' }, 'GST No. ' + p.gstNumber) : null),
      h('div', { className: 'rt-receipt-row' }, h('span', null, p.date), h('span', null, p.time)),
      p.serial ? h('div', { className: 'rt-receipt-row rt-receipt-muted' }, h('span', null, p.serial), h('span', null, p.server || '')) : null,
      h('hr', { className: 'rt-receipt-rule' }),
      lines.map(function (l, i) {
        return h('div', { key: i, className: 'rt-receipt-row' }, h('span', null, txt((l.qty ? l.qty + ' x ' : '') + l.item)), h('span', null, l.price));
      }),
      h('hr', { className: 'rt-receipt-rule' }),
      p.subtotal ? h('div', { className: 'rt-receipt-row' }, h('span', null, 'Subtotal'), h('span', null, p.subtotal)) : null,
      p.total ? h('div', { className: 'rt-receipt-row rt-receipt-total' }, h('span', null, 'Total'), h('span', null, p.total)) : null,
      p.gst ? h('div', { className: 'rt-receipt-row rt-receipt-muted' }, h('span', null, 'Incl. GST 15%'), h('span', null, p.gst)) : null,
      p.paid ? h('div', { className: 'rt-receipt-row' }, h('span', null, p.paid), h('span', null, p.tendered || p.total)) : null,
      p.card ? h('div', { className: 'rt-receipt-row rt-receipt-muted' }, h('span', null, txt(p.card)), h('span', null, '')) : null,
      (p.extra || []).map(function (l, i) { return h('div', { key: 'x' + i, className: 'rt-receipt-row rt-receipt-muted' }, h('span', null, txt(l[0])), h('span', null, txt(l[1] || ''))); }),
      p.footer ? h('div', { className: 'rt-receipt-foot' }, p.footer) : null,
      p.stamp ? h('div', { className: 'rt-receipt-stamp' }, h('span', { className: 'rt-stamp' }, p.stamp)) : null);
  }

  function Bars() { return h('span', { className: 'rt-phone-bars' }, [4, 6, 8, 11].map(function (v, i) { return h('i', { key: i, style: { height: v } }); })); }

  function PhoneScreenshot(p) {
    var screen;
    if (p.children) screen = p.children;
    else if (p.app === 'calls') {
      screen = [
        h('div', { key: 't', className: 'rt-phone-title' }, 'Recents'),
        h('div', { key: 'c', className: 'rt-phone-calls' }, (p.calls || []).map(function (c, i) {
          return h('div', { key: i, className: cx('rt-phone-call', c.missed && 'rt-phone-call-missed') },
            h('div', null, h('b', null, txt(c.name)), h('small', null, (c.missed ? 'Missed · ' : '') + (c.kind || 'mobile') + (c.duration ? ' · ' + c.duration : ''))),
            h('time', null, c.time));
        }))];
    } else {
      var initials = (p.contact || '').split(/\s+/).filter(function (w) { return /^[A-Za-z\u00C0-\u017F]/.test(w); }).map(function (w) { return w[0].toUpperCase(); }).join('').slice(0, 2);
      var who = p.contact || 'Them';
      screen = [
        h('div', { key: 'h', className: 'rt-phone-head' }, h('span', { className: 'rt-phone-avatar', 'aria-hidden': true }, initials || h('svg', { viewBox: '0 0 24 24', width: 22, height: 22, fill: 'currentColor' }, h('circle', { cx: 12, cy: 9, r: 4 }), h('path', { d: 'M4 20c1.5-4 4.5-6 8-6s6.5 2 8 6z' }))), h('span', { className: 'rt-phone-name' }, p.contact)),
        h('div', { key: 'm', className: 'rt-phone-thread' },
          (p.messages || []).map(function (m, i) {
            if (m.day) return h('div', { key: i, className: 'rt-phone-day' }, m.day);
            if (m.receipt) return h('div', { key: i, className: 'rt-phone-receipt' }, m.receipt);
            return h('div', { key: i, className: cx('rt-bubble', 'rt-bubble-' + (m.from === 'me' ? 'me' : 'them')) }, h('span', { className: 'rt-sr' }, (m.from === 'me' ? 'Me' : who) + ': '), txt(m.text));
          }))];
    }
    return h('div', { className: 'rt-phone', role: 'group', 'aria-label': p.label || ('Screenshot of a phone' + (p.app === 'calls' ? ': recent calls' : p.contact ? ': messages with ' + p.contact : '')) },
      h('div', { className: 'rt-phone-screen' },
        h('span', { className: 'rt-phone-island', 'aria-hidden': true }),
        h('div', { className: 'rt-phone-status', 'aria-hidden': true }, h('span', null, p.time || '23:41'),
          h('span', { className: 'rt-phone-status-r' }, h(Bars), h('span', { className: 'rt-phone-batt' }, h('b', { style: { width: (p.battery != null ? p.battery : 34) + '%' } })))),
        screen,
        h('span', { className: 'rt-phone-home', 'aria-hidden': true })));
  }

  function DocHead(p) {
    return [
      h('div', { key: 'h', className: 'rt-doc-head' }, h('div', { className: 'rt-doc-org' }, p.org), h('div', { className: 'rt-doc-title' }, p.title)),
      p.info ? h('dl', { key: 'i', className: 'rt-doc-info' }, p.info.reduce(function (a, kv, i) { a.push(h('dt', { key: 'k' + i }, kv[0]), h('dd', { key: 'v' + i }, txt(kv[1]))); return a; }, [])) : null];
  }

  function PhoneRecords(p) {
    var dirs = { out: 'Outgoing', 'in': 'Incoming', missed: 'Missed', sms: 'SMS out', 'sms-in': 'SMS in' };
    return h('div', { className: 'rt-paper rt-doc' },
      DocHead({ org: p.carrier, title: 'Itemised call record', info: [['Account holder', p.holder], ['Number', p.number], ['Period', p.period]].filter(function (r) { return r[1]; }) }),
      h('table', null,
        h('thead', null, h('tr', null, ['Date', 'Time', 'Type', 'Number', 'Duration'].map(function (c, i) { return h('th', { key: c, className: cx(i === 4 && 'rt-num', i === 0 && 'rt-col-fold') || undefined, 'aria-label': i === 4 ? c : undefined }, i === 4 ? [h('span', { key: 'f', className: 'rt-th-full' }, c), h('span', { key: 's', className: 'rt-th-short', 'aria-hidden': true }, 'Dur.')] : c); }))),
        h('tbody', null, (p.rows || []).map(function (r, i) {
          return h('tr', { key: i, className: r.marked ? 'rt-marked' : undefined },
            h('td', { className: 'rt-nowrap rt-col-fold' }, r.date), h('td', { className: 'rt-nowrap' }, h('span', { className: 'rt-fold', 'aria-hidden': true }, r.date), r.time), h('td', null, h('span', { className: 'rt-dir' }, dirs[r.dir] || r.dir)), h('td', { className: 'rt-nowrap' }, txt(r.to)), h('td', { className: 'rt-num' }, r.duration || '—'));
        }))),
      p.footer ? h('div', { className: 'rt-doc-foot' }, p.footer) : null);
  }

  function BankStatement(p) {
    return h('div', { className: 'rt-paper rt-doc rt-doc-bank' },
      DocHead({ org: p.bank, title: 'Statement', info: [['Account', p.account], ['Name', p.holder], ['Period', p.period]].filter(function (r) { return r[1]; }) }),
      h('table', null,
        h('thead', null, h('tr', null, ['Date', 'Details', 'Debit', 'Credit', 'Balance'].map(function (c, i) { return h('th', { key: c, className: cx(i > 1 && 'rt-num', i === 0 && 'rt-col-fold') || undefined }, c); }))),
        h('tbody', null, (p.rows || []).map(function (r, i) {
          return h('tr', { key: i, className: r.marked ? 'rt-marked' : undefined },
            h('td', { className: 'rt-nowrap rt-col-fold' }, r.date), h('td', { className: 'rt-wrap' }, h('span', { className: 'rt-fold', 'aria-hidden': true }, r.date), txt(r.details)), h('td', { className: 'rt-num' }, r.out || ''), h('td', { className: 'rt-num' }, r['in'] || ''), h('td', { className: 'rt-num' }, r.balance || ''));
        }))),
      p.footer ? h('div', { className: 'rt-doc-foot' }, p.footer) : null);
  }

  function Ticket(p) {
    return h('div', { className: cx('rt-paper rt-ticket', p.torn && 'rt-ticket-torn') },
      h('div', { className: 'rt-ticket-main' },
        h('div', { className: 'rt-ticket-op' }, p.operator),
        h('div', { className: 'rt-ticket-route' }, h('span', null, p.from), h('i', { 'aria-label': 'to' }, 'to'), h('span', null, p.to)),
        h('dl', { className: 'rt-ticket-grid' },
          h('dt', null, (p.labels && p.labels.date) || 'Date'), h('dt', null, (p.labels && p.labels.time) || 'Sailing'), h('dt', null, (p.labels && p.labels.fare) || 'Fare'),
          h('dd', null, p.date), h('dd', null, p.time), h('dd', null, p.fare))),
      h('div', { className: 'rt-ticket-stub', 'aria-hidden': p.torn ? true : undefined },
        h('span', null, p.passenger || 'Adult'), h('b', null, p.time), h('span', null, txt(p.serial || ''))));
  }

  function HandwrittenNote(p) {
    var lines = Array.isArray(p.lines) ? p.lines : [p.children];
    return h('div', { className: cx('rt-paper rt-hand', p.paper === 'plain' && 'rt-hand-plain') },
      lines.map(function (l, i) { return h('p', { key: i }, txt(l)); }),
      p.signed ? h('p', { className: 'rt-hand-sign' }, p.signed) : null);
  }

  function CctvStill(p) {
    return h('div', { className: 'rt-paper rt-cctv' },
      p.src ? h('img', { src: p.src, alt: p.alt || '' }) : h('div', { className: 'rt-cctv-empty', 'data-slot': p.slot ? '' : undefined }, p.slot || 'No signal'),
      h('div', { className: 'rt-cctv-burn top' }, h('span', { className: 'rt-cctv-rec' }, p.camera || 'CAM 03'), h('span', null, p.place || '')),
      h('div', { className: 'rt-cctv-burn bottom' }, h('span', null, p.date), h('span', null, p.timestamp)));
  }

  function Printout(p) {
    var cols = p.columns || [];
    return h('div', { className: 'rt-paper rt-doc' },
      DocHead({ org: p.org, title: p.title, info: p.info }),
      h('table', null,
        h('thead', null, h('tr', null, cols.map(function (c, i) { return h('th', { key: i, className: c.align === 'right' ? 'rt-num' : undefined }, c.label); }))),
        h('tbody', null, (p.rows || []).map(function (r, i) {
          var cells = Array.isArray(r) ? r : r.cells;
          return h('tr', { key: i, className: r.marked ? 'rt-marked' : undefined },
            cols.map(function (c, j) { return h('td', { key: j, className: cx(c.align === 'right' && 'rt-num', c.wrap ? 'rt-wrap' : 'rt-nowrap') }, txt(cells[j] == null ? '' : cells[j])); }));
        }))),
      p.footer ? h('div', { className: 'rt-doc-foot' }, p.footer) : null);
  }

  window.RedThread = Object.assign(window.RedThread || {}, {
    Wordmark: Wordmark, Button: Button, CaseTag: CaseTag, ThreadDivider: ThreadDivider,
    GameNote: GameNote, Evidence: Evidence, EvidenceTag: EvidenceTag,
    Receipt: Receipt, PhoneScreenshot: PhoneScreenshot, PhoneRecords: PhoneRecords, BankStatement: BankStatement,
    Ticket: Ticket, HandwrittenNote: HandwrittenNote, CctvStill: CctvStill, Printout: Printout
  });
})();
