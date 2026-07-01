 // ---------- NAVBAR SCROLL EFFECT ----------
        const navbar = document.getElementById('mainNavbar');
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 80) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }, { passive: true });

        // ---------- LEAFLET MAP ----------
        (function() {
            const map = L.map('coverageMap').setView([-0.2, 36.0], 7);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; OpenStreetMap contributors',
                maxZoom: 18,
            }).addTo(map);

            function createCountyPolygon(center, radius, color, label) {
                const points = [];
                const numPoints = 30;
                for (let i = 0; i < numPoints; i++) {
                    const angle = (i / numPoints) * 2 * Math.PI;
                    const dx = radius * 0.35 * Math.cos(angle);
                    const dy = radius * 0.35 * Math.sin(angle);
                    points.push([center[0] + dy, center[1] + dx]);
                }
                return L.polygon(points, {
                    color: color,
                    weight: 3,
                    opacity: 0.8,
                    fillColor: color,
                    fillOpacity: 0.2
                }).bindPopup(`<strong>${label}</strong><br>Coverage: Fiber, 4G, 5G`);
            }

            createCountyPolygon([-1.2921, 36.8219], 1.0, '#F57C00', 'Nairobi County').addTo(map);
            createCountyPolygon([0.5143, 35.2698], 0.7, '#FFB74D', 'Eldoret / Uasin Gishu').addTo(map);
            createCountyPolygon([-0.6818, 34.7661], 0.6, '#E65100', 'Kisii County').addTo(map);

            L.marker([-1.2921, 36.8219]).addTo(map).bindPopup('Nairobi');
            L.marker([0.5143, 35.2698]).addTo(map).bindPopup('Eldoret');
            L.marker([-0.6818, 34.7661]).addTo(map).bindPopup('Kisii');
        })();

        // ---------- RELOCATION FORM ----------
        const relForm = document.getElementById('relocationForm');
        const relSuccess = document.getElementById('relocationSuccess');

        relForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const inputs = this.querySelectorAll('input[required]');
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

            relSuccess.classList.remove('d-none');
            this.reset();
            setTimeout(() => relSuccess.classList.add('d-none'), 6000);
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