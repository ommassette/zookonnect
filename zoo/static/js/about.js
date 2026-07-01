    // ---------- MOBILE DROPDOWN TOGGLE (from your original HTML) ----------
    document.querySelectorAll('.navbar-nav .dropdown-toggle').forEach(function(element) {
        element.addEventListener('click', function(e) {
            let parentLi = this.parentElement;
            if (window.innerWidth <= 992) {
                e.preventDefault(); // prevent default for mobile
                if (parentLi.classList.contains('show')) {
                    parentLi.classList.remove('show');
                } else {
                    // Close all other dropdowns
                    document.querySelectorAll('.navbar-nav .dropdown').forEach(function(drop) {
                        drop.classList.remove('show');
                    });
                    parentLi.classList.add('show');
                }
            }
        });
    });

    // ---------- ACTIVE NAV LINK HIGHLIGHT (already in base, but ensure it works) ----------
    // (Optional) if you want to re-run it on page load:
    document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
        if (link.href === window.location.href || link.href === window.location.href + '#') {
            link.classList.add('active');
            if (link.closest('.dropdown')) {
                link.closest('.dropdown').querySelector('.dropdown-toggle')?.classList.add('active');
            }
        }
    });