// In view observer (make headerlinks appear on scroll)
const intersectionObserver = new IntersectionObserver(entries => {
entries.forEach(entry => {
  if (entry.isIntersecting) {
    entry.target.classList.add("shown"); // Show when in view
  } else {
    entry.target.classList.remove("shown"); // Hide
  }
});
}, { threshold: 0.5 }); // Trigger when 50% of the element is visible

// First-seen observer (homepage animation)
const intersectionObserver2 = new IntersectionObserver((entries, obs) => {
entries.forEach(entry => {
  if (entry.isIntersecting) {
    const el = entry.target;
    el.removeAttribute('hidden');

    obs.unobserve(el);
  }
});
}, { threshold: 0.3 });

// Active tab observer (hide inactive tabs in nav)
const resizeObserver = new ResizeObserver(visibilityChange);

function visibilityChange() {
    // Restore visibility of all navigation items
    document.querySelectorAll(".md-nav__list .md-nav__item").forEach(item => {
        item.style.display = ""; // Reset to default
    });
    
    document.querySelectorAll(".tabbed-block").forEach(block => {
        const visibility = window.getComputedStyle(block);

        if (visibility.display === "none") {
            // Extract all headings (h2, h3, h4, h5, h6) from the hidden tabbed-block
            const headings = new Set(
                Array.from(block.querySelectorAll("h2, h3, h4, h5, h6"))
                    .map(h => h.getAttribute("id"))
                    .filter(id => id !== null)
            );

            // Find matching navigation items
            document.querySelectorAll(".md-nav__list .md-nav__item a.md-nav__link").forEach(a => {
                const url = new URL(a.href);
                const frag = url.hash.slice(1); // Remove the #

                // Hide the ancestor .md-nav__item
                if (headings.has(frag)) {
                    const navItem = a.closest(".md-nav__item");
                    if (navItem) {
                        navItem.style.display = "none";
                    }
                }
            });
        }
    });
};

// Function to set the vh variable
function setHeroHeight() {
  const vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);
}


// Custom highlight handler
const HighlightRegistry = {
    className: "marked",
    selector: ".marked",

    clear() {
        document.querySelectorAll(this.selector).forEach(el =>
            el.classList.remove(this.className)
        );
    },

    highlight(ids) {
        this.clear();
        ids.forEach(id => {
            document.querySelectorAll(
                `[id="${id}"], [ana~="#${id}"], p:has([href$="#${id}"])`
            ).forEach(el => el.classList.add(this.className));
        });
    },

    getTargets(el) {
        const targets = new Set();

        if (el.id) {
            targets.add(el.id);
        }

        const link = el.querySelector('a');
        if (link && link.href.includes('#')) {
            const href = link.href.split('#')[1];
            if (href) targets.add(href);
        }

        const analysis = el.getAttribute('ana');
        if (analysis) {
            analysis.trim().split(/\s+/).forEach(ref => {
                if (ref.startsWith('#')) ref = ref.slice(1);
                if (/^(s|r)\d+$/.test(ref)) {
                    targets.add(ref);
                }
            });
        }

        return [...targets];
    }
};

// On page load
document$.subscribe(function () {

    // Hero height adjustment
    if (location.pathname === "/contro/") {

        requestAnimationFrame(() => {
            setHeroHeight();
            const hero = document.getElementById('hero-container');
            if (hero) {
                hero.classList.add('ready');
            }
        });

    // Dynamic higlight analysis spans
    } else if (location.pathname === "/contro/examples/") {

        // Global listener to clear highlights
        document.addEventListener("click", () => HighlightRegistry.clear());

        // Highlight matching elements
        document.querySelectorAll("[id^='s'], [ana^='#s'], p:has([href*='#s'])").forEach(element => {
            element.addEventListener("click", function (event) {
                event.stopPropagation(); // prevent global listener
                const targets = HighlightRegistry.getTargets(this);
                HighlightRegistry.highlight(targets);
            }, true);
        });

        // Disable spans with no in-text referent
        document.querySelectorAll("[id^='s']").forEach(element => {
            const id = element.id;
            const hasText = document.querySelector(`span[ana~="#${id}"]`);
            if (!hasText) {
                element.classList.add("absent");
                document.querySelectorAll(`p:has([href$='#${id}'])`).forEach(cited => {
                    cited.classList.add("absent");
                });
            }
        });
    }

    // Header transition from background to theme color on scroll
    const header = document.querySelector(".md-header");

    function getHeaderHeight() {
        return header ? header.offsetHeight : 0;
    }

    window.addEventListener("scroll", function () {
        if (window.scrollY > getHeaderHeight()) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    });

    window.addEventListener("resize", function () {
        getHeaderHeight();
    });

    // Observe titles to show headerlinks when viewed on scroll
    const titles = document.querySelectorAll("h1, h2, h3");
    titles.forEach(el => intersectionObserver.observe(el));

    // Homepage animation
    const animated = document.querySelectorAll('[hidden]');
    animated.forEach(el => intersectionObserver2.observe(el));

    // Observe all .tabbed-block elements for changes in display style
    document.querySelectorAll(".tabbed-block").forEach(block => {
        resizeObserver.observe(block);
    });
});