const observer = new IntersectionObserver(entries => {
entries.forEach(entry => {
  if (entry.isIntersecting) {
    entry.target.classList.add("shown"); // Highlight when in view
  } else {
    entry.target.classList.remove("shown"); // Remove highlight
  }
});
}, { threshold: 0.5 }); // Trigger when 50% of the element is visible

document$.subscribe(function () {
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

    // Select elements to observe
    const titles = document.querySelectorAll("h1, h2, h3, .highlight");

    titles.forEach(title => observer.observe(title));



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
            console.log(anaAna);
            document.querySelectorAll(".shown").forEach(el => el.classList.remove("shown"));

            const matchingElements = document.querySelectorAll(`[id*="${anaId}"], [ana*="${anaId}"], p:has([href*="${anaId}"]), [id*="${anaAna}"], [ana*="${anaAna}"], p:has([href*="${anaAna}"]), [id*="${anaRef}"], [ana*="${anaRef}"], p:has([href*="${anaRef}"])`);

            matchingElements.forEach(el => el.classList.add("shown"));
        }, true);
    });
});
