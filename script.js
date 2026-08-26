const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-toggle');

if (header && menuButton) {
  const closeMenu = () => {
    header.classList.remove('menu-open');
    menuButton.setAttribute('aria-expanded', 'false');
  };

  menuButton.addEventListener('click', () => {
    const isOpen = header.classList.toggle('menu-open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
  });

  header.querySelectorAll('nav a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });
}

document.querySelectorAll('[data-year]').forEach((node) => {
  node.textContent = new Date().getFullYear();
});
