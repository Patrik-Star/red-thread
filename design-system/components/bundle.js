/* @ds-bundle: {"format":4,"namespace":"RedThread","components":[{"name":"Wordmark"},{"name":"Button"},{"name":"CaseTag"},{"name":"EvidenceCard"},{"name":"ThreadDivider"}]} */
(function () {
  var R = window.React, h = R.createElement;
  function cx() { return Array.prototype.filter.call(arguments, Boolean).join(' '); }

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

  function EvidenceCard(p) {
    var status = p.status || 'new';
    var label = { 'new': 'New', found: 'Found', locked: 'Locked' }[status];
    return h('article', { className: cx('rt-evidence', 'rt-evidence-' + status, p.className) },
      h('span', { className: 'rt-evidence-pin', 'aria-hidden': true }),
      h('div', { className: 'rt-evidence-meta' },
        h('span', null, 'Evidence ' + (p.number != null ? String(p.number).padStart(2, '0') : '')),
        h('span', null, label)),
      h('h3', { className: 'rt-evidence-title' }, p.title),
      h('p', { className: 'rt-evidence-body', 'aria-hidden': status === 'locked' ? true : undefined }, p.children),
      p.location ? h('div', { className: 'rt-evidence-loc' }, h('span', { 'aria-hidden': true }, '→'), h('span', null, p.location)) : null);
  }

  function ThreadDivider(p) {
    return h('div', { className: cx('rt-divider', p.className), role: 'separator' },
      p.label ? h('span', null, p.label) : h('span', { className: 'rt-divider-knot', 'aria-hidden': true }));
  }

  window.RedThread = Object.assign(window.RedThread || {}, {
    Wordmark: Wordmark, Button: Button, CaseTag: CaseTag, EvidenceCard: EvidenceCard, ThreadDivider: ThreadDivider
  });
})();
