// Function to set the CSS variable
function setHeroHeight() {
  const vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);
}

// Subscribe on load and on resize events
document$.subscribe(() => {
  requestAnimationFrame(() => {
    setHeroHeight();
    const hero = document.getElementById('hero-container');
    if (hero) {
        hero.classList.add('ready');
    }
  })
});
