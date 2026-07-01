 // ---------- NAVBAR SCROLL EFFECT ----------
        const navbar = document.getElementById('mainNavbar');
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 80) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }, { passive: true });

        // ---------- CONTACT FORM SUBMISSION ----------
        const contactForm = document.getElementById('contactForm');
        const contactSuccess = document.getElementById('contactSuccess');

        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Simple validation
            const inputs = this.querySelectorAll('input[required], select[required], textarea[required]');
            let valid = true;
            inputs.forEach(inp => {
                if (!inp.value.trim()) {
                    inp.classList.add('is-invalid');
                    valid = false;
                } else {
                    inp.classList.remove('is-invalid');
                }
            });
            if (!valid) return;

            // Show success message
            contactSuccess.classList.remove('d-none');
            this.reset();
            setTimeout(() => {
                contactSuccess.classList.add('d-none');
            }, 6000);
        });

        // ---------- SMOOTH SCROLL FOR NAV LINKS ----------
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    const navCollapse = document.getElementById('mainNav');
                    if (navCollapse.classList.contains('show')) {
                        const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
                        if (bsCollapse) bsCollapse.hide();
                    }
                }
            });
        });

        // ---------- ACTIVE NAV LINK HIGHLIGHT ----------
        document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
            if (link.href === window.location.href || link.href === window.location.href + '#') {
                link.classList.add('active');
                if (link.closest('.dropdown')) {
                    link.closest('.dropdown').querySelector('.dropdown-toggle')?.classList.add('active');
                }
            }
        });
        document.querySelectorAll('.navbar-nav .dropdown-toggle').forEach(function(element) {
        element.addEventListener('click', function(e) {
            let parentLi = this.parentElement;
            if (window.innerWidth <= 992) {
                if (parentLi.classList.contains('show')) {
                    parentLi.classList.remove('show');
                } else {
                    document.querySelectorAll('.navbar-nav .dropdown').forEach(function(drop) {
                        drop.classList.remove('show');
                    });
                    parentLi.classList.add('show');
                }
            }
        });
    });