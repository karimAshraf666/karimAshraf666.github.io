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

  // Category routes share the original cards, IDs and browser-local Saved state.
  const cards = [...document.querySelectorAll('[data-resource]')];
  const views = {
    library: ['All resources', null, 'Browse references, tools and skills. Every resource includes a worksheet and an AI agent guide.'],
    'ai-skills': ['AI skills', ['AI skills'], 'Agent workflows for web design, design systems, writing, research and motion. Open a skill or use its worksheet with a team.'],
    'ui-kits': ['Systems & UI kits', ['Systems & UI kits'], 'Design libraries and component references for product interfaces.'],
    'ux-patterns': ['UX patterns', ['UX patterns'], 'References for recurring interaction problems, with a worksheet to adapt each pattern.'],
    'plugins-tools': ['Plugins & tools', ['Plugins','Tools'], 'Tools for research, accessibility, design delivery and content production. Provider access and plans vary.'],
    reading: ['Articles & guides', ['Articles & guidance'], 'Research, guidance and source material to support a design decision.'],
    saved: ['Saved resources', null, 'Your personal shortlist. Saved resources stay in this browser and can be exported.']
  };
  let currentView = 'library', industry = 'all', limit = 12;
  const knownResources = new Set(cards.map((card) => card.dataset.resource));
  store.saved = store.saved.filter((id) => knownResources.has(id));
  const browse = $('workbench-navigation');
  const compactBrowse = window.matchMedia('(max-width: 1000px)');
  const closeBrowse = (focus = false) => {
    if (compactBrowse.matches) {
      browse.open = false;
      if (focus) browse.querySelector('summary').focus();
    }
  };
  browse.open = !compactBrowse.matches;
  compactBrowse.addEventListener('change', () => { browse.open = !compactBrowse.matches; });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && browse.open && compactBrowse.matches) closeBrowse(true);
  });
  const markSection = (section) => {
    document.querySelectorAll('.bench-sidebar [data-library-view]').forEach((link) => {
      if (section === 'library' && link.dataset.libraryView === currentView) link.setAttribute('aria-current','page');
      else link.removeAttribute('aria-current');
    });
    document.querySelectorAll('.bench-sidebar [data-workbench-section]').forEach((link) => {
      if (link.dataset.workbenchSection === section) link.setAttribute('aria-current','location');
      else link.removeAttribute('aria-current');
    });
    const label = {tools:'Practical tools','team-kit':'Team templates','ai-workflows':'Reusable prompts',practices:'Working practices'};
    $('browse-current').textContent = label[section] || views[currentView][0];
  };
  const updateFavorites = () => {
    cards.forEach((card) => {
      const button = card.querySelector('.bench-favorite');
      const selected = store.saved.includes(card.dataset.resource);
      const name = card.querySelector('h3').textContent;
      button.setAttribute('aria-pressed', String(selected));
      button.setAttribute('aria-label', `${selected ? 'Unsave' : 'Save'} ${name}`);
      button.textContent = selected ? '★' : '☆';
    });
    document.querySelectorAll('[data-count="saved"]').forEach((node) => { node.textContent = store.saved.length; });
  };
  const filterLibrary = () => {
    const terms = $('resource-search').value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const kinds = views[currentView][1];
    const matches = cards.filter((card) => {
      const haystack = `${card.textContent} ${card.dataset.type} ${card.dataset.industries}`.toLocaleLowerCase();
      return (industry === 'all' || card.dataset.industries.split(' ').includes(industry)) &&
        (!kinds || kinds.includes(card.dataset.type)) &&
        (currentView !== 'saved' || store.saved.includes(card.dataset.resource)) &&
        terms.every((term) => haystack.includes(term));
    });
    const visible = new Set(matches.slice(0, limit));
    cards.forEach((card) => { card.hidden = !visible.has(card); });
    $('resource-count').textContent = `Showing ${Math.min(limit, matches.length)} of ${matches.length} resource${matches.length === 1 ? '' : 's'}`;
    $('resource-empty').hidden = matches.length !== 0;
    $('resource-empty').textContent = currentView === 'saved' && !store.saved.length ? 'Save a resource with its star button to keep it here.' : 'No resources match this search and industry. Clear them or search the full library.';
    $('search-all-resources').hidden = matches.length !== 0 || currentView === 'library' || (currentView === 'saved' && !store.saved.length);
    $('show-more').hidden = matches.length <= limit;
    $('show-more').textContent = `Show ${Math.min(12, Math.max(0,matches.length - limit))} more resources`;
    $('export-shortlist').hidden = currentView !== 'saved' || !store.saved.length;
    $('clear-filters').hidden = industry === 'all' && !terms.length;
  };
  const selectView = (key, { navigate = false, preserveSearch = false } = {}) => {
    if (!views[key]) return;
    currentView = key; limit = 12;
    if (!preserveSearch) { industry = 'all'; $('resource-industry').value = 'all'; $('resource-search').value = ''; }
    $('library-title').textContent = views[key][0];
    $('library-description').textContent = views[key][2];
    $('browse-current').textContent = views[key][0];
    $('resource-search').placeholder = key === 'library' ? 'Search resources' : `Search ${views[key][0].toLocaleLowerCase()}`;
    markSection('library');
    filterLibrary();
    if (navigate) {
      if (location.hash !== `#${key}`) history.pushState(null,'',`#${key}`);
      closeBrowse();
      $('library-title').focus({preventScroll:true});
      $('library').scrollIntoView({block:'start'});
    }
  };
  document.querySelectorAll('[data-library-view]').forEach((link) => {
    link.addEventListener('click', (event) => { event.preventDefault(); selectView(link.dataset.libraryView,{navigate:true}); });
  });
  document.querySelectorAll('.bench-sidebar [data-workbench-section]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      const section = $(link.dataset.workbenchSection);
      if (location.hash !== link.hash) history.pushState(null,'',link.hash);
      closeBrowse(); markSection(section.id);
      const heading = section.querySelector('h2');
      heading.tabIndex = -1; heading.focus({preventScroll:true}); section.scrollIntoView({block:'start'});
    });
  });
  const syncLibraryRoute = () => { const key = location.hash.slice(1) || 'library'; if (views[key]) selectView(key); };
  window.addEventListener('hashchange',syncLibraryRoute);
  window.addEventListener('popstate',syncLibraryRoute);
  cards.forEach((card) => {
    const button = card.querySelector('.bench-favorite'); button.hidden = false;
    button.addEventListener('click', () => {
      const id = card.dataset.resource;
      store.saved = store.saved.includes(id) ? store.saved.filter((x) => x !== id) : [...store.saved,id];
      persist(); updateFavorites(); filterLibrary();
    });
  });
  $('resource-industry').addEventListener('change', () => { industry = $('resource-industry').value; limit = 12; filterLibrary(); });
  $('resource-search').addEventListener('input', () => { limit = 12; filterLibrary(); });
  $('clear-filters').addEventListener('click', () => { industry = 'all'; $('resource-industry').value = 'all'; $('resource-search').value = ''; limit = 12; filterLibrary(); });
  $('search-all-resources').addEventListener('click', () => { industry = 'all'; $('resource-industry').value = 'all'; selectView('library',{navigate:true,preserveSearch:true}); });
  $('show-more').addEventListener('click', () => {
    const oldVisible = cards.filter((card) => !card.hidden).length;
    limit += 12; filterLibrary();
    const next = cards.filter((card) => !card.hidden)[oldVisible];
    if (next) next.querySelector('a').focus({preventScroll:true});
  });
  $('export-shortlist').addEventListener('click', () => {
    const selected = cards.filter((card) => store.saved.includes(card.dataset.resource));
    if (!selected.length) return;
    const text = '# Design Workbench resource shortlist\n\n' + selected.map((card) => {
      const name = card.querySelector('h3').textContent;
      const purpose = card.querySelector('h3 + p').textContent;
      const guidance = [...card.querySelectorAll('details p')].map((p) => p.textContent.trim()).join('\n\n');
      return `## ${name}\nReference: ${card.querySelector('[data-source-link]').href}\nHuman worksheet: ${card.querySelector('.bench-resource-files a').href}\nAI agent guide: ${card.querySelector('.bench-resource-files a[download]').href}\n\n${purpose}\n\n${guidance}\n`;
    }).join('\n');
    download('design-resource-shortlist.md',text);
  });
  $('library-controls').hidden = false;
  updateFavorites(); syncLibraryRoute(); filterLibrary();
  if ('IntersectionObserver' in window) {
    const sectionObserver = new IntersectionObserver((entries) => {
      const visible = entries.find((entry) => entry.isIntersecting);
      if (visible) markSection(visible.target.id);
    }, {rootMargin:'-180px 0px -55% 0px',threshold:0});
    ['library','tools','team-kit','ai-workflows','practices'].forEach((id) => sectionObserver.observe($(id)));
  }

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
