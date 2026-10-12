const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-toggle');

if (header && menuButton) {
  const closeMenu = (returnFocus = false) => {
    header.classList.remove('menu-open');
    menuButton.setAttribute('aria-expanded', 'false');
    if (returnFocus) menuButton.focus();
  };

  menuButton.addEventListener('click', () => {
    const isOpen = header.classList.toggle('menu-open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
  });

  header.querySelectorAll('nav a').forEach((link) => {
    link.addEventListener('click', () => closeMenu());
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && header.classList.contains('menu-open')) closeMenu(true);
  });

  const desktop = window.matchMedia('(min-width: 901px)');
  desktop.addEventListener('change', (event) => { if (event.matches) closeMenu(); });
}

document.querySelectorAll('.media-card img').forEach((image) => {
  const link = document.createElement('a');
  link.href = image.getAttribute('src');
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  link.setAttribute('aria-label', `Open full-size image: ${image.alt}`);
  image.before(link);
  link.append(image);
});

document.querySelectorAll('[data-year]').forEach((node) => {
  node.textContent = new Date().getFullYear();
});

// Motion follows the reading order and is entirely optional.
(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const targets = [...document.querySelectorAll('[data-reveal], .case-content > h2, .case-content > .media-grid, .writing-hero-inner, .bench-intro')];
  let observer;
  const revealAll = () => {
    document.body.classList.remove('motion-ready');
    targets.forEach((target) => target.classList.add('is-visible'));
    if (observer) observer.disconnect();
  };
  const startReveals = () => {
    if (preference.matches || !('IntersectionObserver' in window)) { revealAll(); return; }
    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -24px 0px', threshold: .07 });
    targets.forEach((target, index) => {
      target.dataset.reveal = '';
      if (target.classList.contains('project-card')) target.style.setProperty('--reveal-delay', `${index % 2 * 75}ms`);
      observer.observe(target);
    });
    document.body.classList.add('motion-ready');
  };
  startReveals();
  preference.addEventListener('change', () => {
    if (preference.matches) revealAll();
  });
  // Focusing an item must never leave an invisible keyboard target.
  document.addEventListener('focusin', (event) => {
    const target = event.target.closest('[data-reveal]');
    if (target) target.classList.add('is-visible');
  });

  const composition = document.querySelector('[data-tilt]');
  if (composition && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    composition.addEventListener('pointermove', (event) => {
      if (preference.matches) return;
      const box = composition.getBoundingClientRect();
      composition.style.setProperty('--tilt-x', `${((event.clientX - box.left) / box.width - .5) * 5}deg`);
      composition.style.setProperty('--tilt-y', `${-((event.clientY - box.top) / box.height - .5) * 5}deg`);
    });
    composition.addEventListener('pointerleave', () => {
      composition.style.setProperty('--tilt-x', '0deg');
      composition.style.setProperty('--tilt-y', '0deg');
    });
  }

  const isCase = document.body.classList.contains('case-page');
  const progress = isCase ? document.createElement('div') : null;
  if (progress) { progress.className = 'reading-progress'; progress.setAttribute('aria-hidden', 'true'); document.body.append(progress); }
  let scheduled = false;
  const updateScroll = () => {
    scheduled = false;
    if (progress) {
      const total = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = `scaleX(${total > 0 ? Math.min(1, Math.max(0, window.scrollY / total)) : 0})`;
    }
    if (composition && !preference.matches && window.innerWidth > 900) {
      composition.style.setProperty('--scroll-shift', `${-Math.min(18,window.scrollY * .035)}px`);
    }
  };
  window.addEventListener('scroll', () => {
    if (!scheduled) { scheduled = true; window.requestAnimationFrame(updateScroll); }
  }, { passive: true });
  window.addEventListener('resize', updateScroll);
  updateScroll();

  // Keep the floating menu's section state understandable without adding extra controls.
  if (document.body.classList.contains('home-page') && 'IntersectionObserver' in window) {
    const navigation = document.querySelector('#site-nav');
    const activeObserver = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a,b) => b.intersectionRatio-a.intersectionRatio);
      if (!visible.length) return;
      const href = `#${visible[0].target.id}`;
      navigation.querySelectorAll('a[href^="#"]').forEach((link) => {
        if (link.getAttribute('href') === href) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-100px 0px -50% 0px', threshold: [0,.1,.4] });
    ['work','about','contact'].forEach((id) => { const section = document.getElementById(id); if (section) activeObserver.observe(section); });
  }
  const sectionNav = document.querySelector('.bench-jump nav');
  if (sectionNav && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      const entry = entries.find((item) => item.isIntersecting);
      if (!entry) return;
      sectionNav.querySelectorAll('a').forEach((link) => {
        if (link.getAttribute('href') === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-150px 0px -55% 0px', threshold: 0 });
    sectionNav.querySelectorAll('a').forEach((link) => {
      const section = document.querySelector(link.getAttribute('href')); if (section) observer.observe(section);
    });
  }
})();
