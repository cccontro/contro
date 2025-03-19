const intersectionObserver = new IntersectionObserver(entries => {
entries.forEach(entry => {
  if (entry.isIntersecting) {
    entry.target.classList.add("shown"); // Highlight when in view
  } else {
    entry.target.classList.remove("shown"); // Remove highlight
  }
});
}, { threshold: 0.5 }); // Trigger when 50% of the element is visible

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
            const headings = Array.from(block.querySelectorAll("h2, h3, h4, h5, h6"))
                .map(h => h.firstChild.textContent.trim());
            console.log(headings)
            // Find matching navigation items
            document.querySelectorAll(".md-nav__list .md-nav__item span").forEach(span => {
                if (headings.includes(span.textContent.trim())) {
                    // Hide the ancestor .md-nav__item
                    let navItem = span.closest(".md-nav__item");
                    if (navItem) {
                        navItem.style.display = "none";
                    }
                }
            });
        }
    });
};

// On page load
document$.subscribe(function () {
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

    // Observe titles and other elements to highlight when viewed on scroll
    const titles = document.querySelectorAll("h1, h2, h3, .highlight");

    titles.forEach(title => intersectionObserver.observe(title));


    // Highlight selected analysis spans
    document.querySelectorAll("[id*='cv-s'], [id*='cr-s'], [ana*='#cv'], [ana*='#cr'], p:has([href*='cv-s']), p:has([href*='cr-s'])").forEach(element => {

        element.addEventListener("click", function () {
            const anaId = this.id;
            let anaRef = "";
            if (this.querySelector('a')) {
                anaRef = this.querySelector('a').href.split('#')[1];
            }
            let anaAna = "";
            if (/cv|cr/.test(this.getAttribute('ana'))) {
                anaAna = this.getAttribute('ana').slice(1);
            }            
            document.querySelectorAll(".shown").forEach(el => el.classList.remove("shown"));

            const matchingElements = document.querySelectorAll(`[id*="${anaId}"], [ana*="${anaId}"], p:has([href*="${anaId}"]), [id*="${anaAna}"], [ana*="${anaAna}"], p:has([href*="${anaAna}"]), [id*="${anaRef}"], [ana*="${anaRef}"], p:has([href*="${anaRef}"])`);

            matchingElements.forEach(el => el.classList.add("shown"));
        }, true);
    });

    // Observe all .tabbed-block elements for changes in display style
    document.querySelectorAll(".tabbed-block").forEach(block => {
        resizeObserver.observe(block);
    });
});