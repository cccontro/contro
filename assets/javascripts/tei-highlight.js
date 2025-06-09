// On page load
document$.subscribe(function () {
    // Highlight selected analysis spans
    document.querySelectorAll("[id^='s'], [ana^='#s'], p:has([href*='#s'])").forEach(element => {
        element.addEventListener("click", function () {
            const targets = new Set();

            if (this.id) {
                targets.add(this.id);
            }

            // Extract any referenced ID
            const link = this.querySelector('a');
            if (link && link.href.includes('#')) {
                const href = link.href.split('#')[1];
                if (href) targets.add(href);
            }

            // Extract IDs from multi-valued analysis attribute
            const analysis = this.getAttribute('ana');
            if (analysis) {
                analysis.trim().split(/\s+/).forEach(ref => {
                    if (ref.startsWith('#')) ref = ref.slice(1);
                    if (/^(s|r)\d+$/.test(ref)) {
                        targets.add(ref);
                    }
                });
            }

            // Clear current highlights
            document.querySelectorAll(".shown").forEach(el => el.classList.remove("shown"));

            // Highlight matching elements
            targets.forEach(id => {
                document.querySelectorAll(
                    `[id="${id}"], [ana~="#${id}"], p:has([href$="#${id}"])`
                ).forEach(el => el.classList.add("shown"));
            });
        }, true);
    });

    // Mark spans with no in-text referent
    document.querySelectorAll("[id^='s']").forEach(element => {
        const id = element.id;
        const hasText = document.querySelector(`[ana~="#${id}"]`);
        if (!hasText) {
            element.classList.add("absent");
        }
    });
});
