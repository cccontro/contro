const observer = new IntersectionObserver(entries => {
entries.forEach(entry => {
  if (entry.isIntersecting) {
    entry.target.classList.add("shown"); // Highlight when in view
  } else {
    entry.target.classList.remove("shown"); // Remove highlight
  }
});
}, { threshold: 0.5 }); // Trigger when 50% of the element is visible

document$.subscribe(function() {
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

    window.addEventListener("resize", function() {
        getHeaderHeight();
    });

    const titles = document.querySelectorAll("h1, h2, h3, .highlight");

    // Observe each title
    titles.forEach(title => observer.observe(title));
});