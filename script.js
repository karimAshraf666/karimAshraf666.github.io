/* Shared behaviour for every page. Every lookup is guarded so a page that omits
   an element (a project page without a footer, for example) never throws. */

const yearSlot = document.getElementById('year');
if (yearSlot) {
  yearSlot.textContent = new Date().getFullYear();
}

const header = document.querySelector('.site-header');
const toggle = document.querySelector('.menu-toggle');
const nav = header ? header.querySelector('nav') : null;

if (header && toggle && nav) {
  const setOpen = (open) => {
    header.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? 'Close' : 'Menu';
  };

  toggle.addEventListener('click', () => {
    setOpen(!header.classList.contains('menu-open'));
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setOpen(false));
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && header.classList.contains('menu-open')) {
      setOpen(false);
      toggle.focus();
    }
  });
}
