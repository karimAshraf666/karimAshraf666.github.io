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
    link.addEventListener('click', closeMenu);
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
