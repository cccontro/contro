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
});