(() => {
  'use strict';
  const KEY = 'karim-design-workbench-v1';
  const $ = (id) => document.getElementById(id);
  const status = $('bench-status');
  const notify = (message) => { status.textContent = message; };
  let store = { drafts: {}, saved: [] };
  let persistent = true;
  try {
    const previous = JSON.parse(localStorage.getItem(KEY) || 'null');
    if (previous && typeof previous === 'object') {
      if (previous.drafts && typeof previous.drafts === 'object') store.drafts = previous.drafts;
      if (Array.isArray(previous.saved)) store.saved = previous.saved.filter((x) => typeof x === 'string');
    }
  } catch (_) { persistent = false; }
  const persist = () => {
    try { localStorage.setItem(KEY, JSON.stringify(store)); }
    catch (_) { persistent = false; }
    if (!persistent) $('draft-storage-note').textContent = 'Browser storage is unavailable. Download drafts and saved resources before leaving this page.';
  };
  const download = (name, text, type = 'text/markdown;charset=utf-8') => {
    const url = URL.createObjectURL(new Blob([text], { type }));
    const link = document.createElement('a');
    link.href = url; link.download = name; document.body.append(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    notify('Download started.');
  };
  const copy = async (id) => {
    const element = $(id);
    const value = 'value' in element ? element.value : element.textContent;
    if (!value.trim()) { notify('Create or complete the draft first.'); element.focus(); return; }
    try { await navigator.clipboard.writeText(value); notify('Copied.'); }
    catch (_) {
      if ('select' in element) { element.focus(); element.select(); }
      else {
        const range = document.createRange(); range.selectNodeContents(element);
        const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      }
      notify('Clipboard access is unavailable. The text is selected for manual copying.');
    }
  };

  // Library controls enhance the static cards; all resources work without JS.
  const cards = [...document.querySelectorAll('[data-resource]')];
  let industry = 'all', savedOnly = false, limit = 9;
  const knownResources = new Set(cards.map((card) => card.dataset.resource));
  store.saved = store.saved.filter((id) => knownResources.has(id));
  const updateFavorites = () => cards.forEach((card) => {
    const button = card.querySelector('.bench-favorite');
    const selected = store.saved.includes(card.dataset.resource);
    const name = card.querySelector('h3').textContent;
    button.setAttribute('aria-pressed', String(selected));
    button.setAttribute('aria-label', `${selected ? 'Unsave' : 'Save'} ${name}`);
    button.textContent = selected ? '★' : '☆';
  });
  const filterLibrary = () => {
    const terms = $('resource-search').value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const kind = $('resource-type').value;
    const matches = cards.filter((card) => {
      const haystack = `${card.textContent} ${card.dataset.industries}`.toLocaleLowerCase();
      return (industry === 'all' || card.dataset.industries.split(' ').includes(industry)) &&
        (kind === 'all' || card.dataset.type === kind) &&
        (!savedOnly || store.saved.includes(card.dataset.resource)) &&
        terms.every((term) => haystack.includes(term));
    });
    const visible = new Set(matches.slice(0, limit));
    cards.forEach((card) => { card.hidden = !visible.has(card); });
    $('resource-count').textContent = `${Math.min(limit, matches.length)} of ${matches.length} matching resources`;
    $('resource-empty').hidden = matches.length !== 0;
    $('resource-empty').textContent = savedOnly && !store.saved.length ? 'Your saved resources will appear here. Use the star on a resource to keep it.' : 'No matching resources. Try another term or reset the search.';
    $('show-more').hidden = matches.length <= limit;
    $('show-more').textContent = `Show ${Math.min(9, matches.length - limit)} more resources`;
    $('export-shortlist').hidden = !savedOnly || !store.saved.length;
    $('clear-filters').hidden = industry === 'all' && kind === 'all' && !terms.length;
    const refine = $('library-options').querySelector('summary');
    refine.textContent = kind === 'all' ? 'Refine' : 'Refine · 1';
    refine.title = kind === 'all' ? 'Filter by resource type' : `Resource type: ${kind}`;
  };
  cards.forEach((card) => {
    const button = card.querySelector('.bench-favorite'); button.hidden = false;
    button.addEventListener('click', () => {
      const id = card.dataset.resource;
      const selected = store.saved.includes(id);
      store.saved = selected ? store.saved.filter((x) => x !== id) : [...store.saved, id];
      persist(); updateFavorites(); filterLibrary();
    });
  });
  $('resource-industry').addEventListener('change', () => {
    industry = $('resource-industry').value; limit = 9; filterLibrary();
  });
  $('saved-only').addEventListener('click', () => {
    savedOnly = true; limit = 9;
    $('saved-only').setAttribute('aria-pressed', 'true'); $('all-resources').setAttribute('aria-pressed', 'false'); filterLibrary();
  });
  $('all-resources').addEventListener('click', () => {
    savedOnly = false; limit = 9;
    $('saved-only').setAttribute('aria-pressed', 'false'); $('all-resources').setAttribute('aria-pressed', 'true'); filterLibrary();
  });
  ['resource-search','resource-type'].forEach((id) => $(id).addEventListener(id === 'resource-search' ? 'input' : 'change', () => { limit = 9; filterLibrary(); }));
  $('clear-filters').addEventListener('click', () => {
    industry = 'all'; limit = 9;
    $('resource-search').value = ''; $('resource-type').value = 'all';
    $('resource-industry').value = 'all';
    filterLibrary();
  });
  $('show-more').addEventListener('click', () => {
    const oldVisible = cards.filter((card) => !card.hidden).length;
    limit += 9; filterLibrary();
    const newlyShown = cards.filter((card) => !card.hidden)[oldVisible];
    if (newlyShown) newlyShown.querySelector('a').focus({ preventScroll: true });
  });
  $('export-shortlist').addEventListener('click', () => {
    const selected = cards.filter((card) => store.saved.includes(card.dataset.resource));
    if (!selected.length) { $('resource-count').textContent = 'Save a resource with the star button before exporting a list.'; return; }
    const text = '# Design Workbench resource shortlist\n\n' + selected.map((card) => {
      const name = card.querySelector('h3').textContent;
      const purpose = card.querySelector('h3 + p').textContent;
      const guidance = [...card.querySelectorAll('details p')].map((paragraph) => paragraph.textContent.trim()).join('\n\n');
      return `## ${name}\nReference: ${card.querySelector('[data-source-link]').href}\nHuman worksheet: ${card.querySelector('.bench-resource-files a').href}\nAI agent guide: ${card.querySelector('.bench-resource-files a[download]').href}\n\n${purpose}\n\n${guidance}\n`;
    }).join('\n');
    download('design-resource-shortlist.md', text);
    $('resource-count').textContent = `Exported ${selected.length} saved resource${selected.length === 1 ? '' : 's'}.`;
  });
  $('library-controls').hidden = false;
  updateFavorites(); filterLibrary();
  const options = $('library-options');
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && options.open) { options.open = false; options.querySelector('summary').focus(); }
  });
  document.addEventListener('click', (event) => {
    if (options.open && !options.contains(event.target)) options.open = false;
  });

  // Native tab semantics and keyboard navigation.
  const tabs = [...document.querySelectorAll('.bench-tab')];
  const activateTab = (tab, focus = false) => {
    tabs.forEach((other) => {
      const selected = other === tab;
      other.setAttribute('aria-selected', String(selected)); other.tabIndex = selected ? 0 : -1;
      $(other.getAttribute('aria-controls')).hidden = !selected;
    });
    if (focus) tab.focus();
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => activateTab(tab));
    tab.addEventListener('keydown', (event) => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); activateTab(tabs[next], true); }
    });
  });

  const states = [
    ['default','Default / ready','What must be true before the user can act?'],
    ['focus','Focused / selected','Which element is active and how is that communicated?'],
    ['loading','Loading','What is pending, and which actions remain available?'],
    ['empty','Empty','Is this first use, a zero result or unavailable data?'],
    ['error','Error','What is confirmed to have failed, and how can the user recover?'],
    ['success','Success','What confirms completion, and what is the next useful action?'],
    ['disabled','Disabled','Why is the action unavailable, and is the reason understandable?'],
    ['partial','Partial / interrupted','What has completed, and what must be preserved?'],
    ['unknown','Pending / unknown outcome','How can the system establish status before a retry?'],
    ['permission','Permission restricted','What can this role access, and what path is available?'],
  ];
  const defaultStates = ['default','loading','error','success'];
  states.forEach(([id,label]) => {
    const wrapper = document.createElement('label');
    const input = document.createElement('input'); input.type = 'checkbox'; input.value = id; input.id = `state-${id}`;
    input.checked = defaultStates.includes(id); input.dataset.draft = 'true';
    wrapper.append(input, document.createTextNode(label)); $('state-choices').append(wrapper);
  });
  const stateSpec = () => {
    const name = $('state-name').value.trim() || '[Pattern name]';
    const selected = states.filter(([id]) => $(`state-${id}`).checked);
    if (!selected.length) { notify('Select at least one relevant state.'); $('state-default').focus(); return; }
    const parts = [
      `# ${name}: interaction-state specification`,
      `Owner: ${$('state-owner').value.trim() || '[Assign owner]'}`,
      `Platform: ${$('state-platform').value}\nLanguage: ${$('state-language').value}`,
      `## Task and constraints\n${$('state-context').value.trim() || '[Define task and confirmed constraints]'}`,
      'Status: Draft for team review. Complete the fields and validate backend behavior.'
    ];
    selected.forEach(([,label,question]) => parts.push(`## ${label}\nQuestion: ${question}\nTrigger: [Define]\nVisible feedback: [Define]\nAvailable action: [Define]\nPreserved data: [Define]\nRecovery / next step: [Define]\nAccessibility and RTL check: [Define]\nAcceptance test: [Define]`));
    parts.push('## Review\nDesign owner: [Assign]\nEngineering / QA reviewers: [Assign]\nOpen questions: [List]\nEvidence and verification: [Link]');
    $('state-output').value = parts.join('\n\n'); saveDrafts(); notify('Specification created. Complete the editable fields before sharing.');
  };
  $('state-form').addEventListener('submit', (event) => { event.preventDefault(); stateSpec(); });
  $('state-example').addEventListener('click', () => {
    $('state-name').value = 'Transfer confirmation (practice example)';
    $('state-context').value = 'The connection drops after confirmation. Distinguish confirmed failure from a pending or unknown outcome. Ask engineering how status can be checked and when retry is safe.';
    states.forEach(([id]) => { $(`state-${id}`).checked = ['default','loading','error','success','unknown'].includes(id); });
    saveDrafts(); stateSpec();
  });

  const checks = [
    'The user task and expected outcome are explicit.',
    'Labels, hierarchy and primary actions are understandable.',
    'Required states and backend signals are specified.',
    'Error, interruption and recovery behavior are checked.',
    'Permissions and role-specific actions are checked.',
    'Repeated actions and uncertain outcomes are handled.',
    'Data is preserved appropriately during recovery.',
    'Realistic content, long text and empty data are checked.',
    'Arabic, English and mixed-direction content are checked.',
    'Target devices, resizing and text scaling are checked.',
    'Contrast, focus, labels and input behavior are checked.',
    'Relevant assistive-technology checks are recorded.',
    'Design and implementation use the agreed patterns.',
    'Acceptance checks have supporting evidence.',
    'Findings have impact, severity and an owner.',
    'Unresolved issues and verification steps are explicit.'
  ];
  checks.forEach((text,index) => {
    const label = document.createElement('label'); const input = document.createElement('input');
    input.type = 'checkbox'; input.id = `qa-check-${index}`; input.dataset.draft = 'true';
    label.append(input, document.createTextNode(text)); $('qa-checklist').append(label);
  });
  const updateQA = () => {
    const count = checks.filter((_,index) => $(`qa-check-${index}`).checked).length;
    $('qa-count').textContent = `${count} / ${checks.length} reviewed`;
    $('qa-progress').value = count; $('qa-progress').max = checks.length;
  };
  const qaText = () => [
    `# Design quality review: ${$('qa-journey').value.trim() || '[Journey]'}`,
    `Owner: ${$('qa-owner').value.trim() || '[Assign]'}\nBuild/design: ${$('qa-build').value.trim() || '[Reference]'}\nDevice/language: ${$('qa-scope').value.trim() || '[Define]'}`,
    `Review coverage: ${$('qa-count').textContent}. Checked means reviewed, not passed.`,
    '## Checks\n' + checks.map((text,index) => `- [${$(`qa-check-${index}`).checked ? 'x' : ' '}] ${text}`).join('\n'),
    `## Findings and evidence\n${$('qa-findings').value.trim() || '[Record findings; do not infer a pass from coverage]'}`,
    `## Unresolved issues and next action\n${$('qa-blockers').value.trim() || '[Confirm remaining issues, owner and verification]'}`
  ].join('\n\n');
  $('qa-export').addEventListener('click', () => download('design-quality-review.md', qaText()));
  $('qa-reset').addEventListener('click', () => {
    checks.forEach((_,index) => { $(`qa-check-${index}`).checked = false; });
    updateQA(); saveDrafts(); notify('Review checks reset. Your context and findings are preserved.');
  });

  const decisionFields = [ ['problem','Problem and user impact'], ['evidence','Evidence, constraints and unknowns'], ['options','Options and tradeoffs'], ['choice','Proposed decision and rationale'], ['checks','Acceptance and follow-up checks'], ['rollout','Rollout, dependencies and review date'] ];
  $('decision-form').addEventListener('submit', (event) => {
    event.preventDefault();
    const parts = [`# ${$('decision-title').value.trim() || '[Decision title]'}`, `Status: Proposed\nOwner and reviewers: ${$('decision-owner').value.trim() || '[Assign]'}`];
    decisionFields.forEach(([id,label]) => parts.push(`## ${label}\n${$(`decision-${id}`).value.trim() || '[Complete]'}`));
    parts.push('## What would change this decision?\n[Record evidence or conditions that would trigger a review]');
    $('decision-output').value = parts.join('\n\n'); saveDrafts(); notify('Decision brief created. Review the editable draft before sharing.');
  });

  // Persist only workbench drafts and favorites; never clear unrelated browser data.
  const draftControls = [...document.querySelectorAll('#interactive-tools input, #interactive-tools select, #interactive-tools textarea')];
  const saveDrafts = () => {
    draftControls.forEach((control) => { store.drafts[control.id] = control.type === 'checkbox' ? control.checked : control.value; });
    persist();
  };
  draftControls.forEach((control) => {
    const value = store.drafts[control.id];
    if (control.type === 'checkbox' && typeof value === 'boolean') control.checked = value;
    else if (control.tagName === 'SELECT' && typeof value === 'string' && [...control.options].some((option) => option.value === value)) control.value = value;
    else if (control.tagName !== 'SELECT' && control.type !== 'checkbox' && typeof value === 'string') control.value = value;
    control.addEventListener('input', () => { updateQA(); saveDrafts(); });
    control.addEventListener('change', () => { updateQA(); saveDrafts(); });
  });
  document.querySelectorAll('[data-copy]').forEach((button) => {
    button.hidden = false; button.addEventListener('click', () => copy(button.dataset.copy));
  });
  [['state-export','state-output','interaction-state-spec.md'], ['decision-export','decision-output','design-decision-brief.md']].forEach(([button,output,name]) => $(button).addEventListener('click', () => {
    if (!$(output).value.trim()) { notify('Create the draft first.'); $(output).focus(); return; }
    download(name,$(output).value);
  }));
  updateQA(); persist(); $('interactive-tools').hidden = false;
})();
