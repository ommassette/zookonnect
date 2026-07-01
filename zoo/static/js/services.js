    // ---------- PLAN TOGGLES ----------
    const toggleHome = document.getElementById('toggleHome');
    const toggleBusiness = document.getElementById('toggleBusiness');
    const allPlans = document.querySelectorAll('.plan-card');

    function showPlans(type) {
        allPlans.forEach(plan => {
            if (plan.dataset.plan === type) {
                plan.classList.remove('hidden');
                plan.style.opacity = '1';
                plan.style.transform = 'translateY(0)';
            } else {
                plan.classList.add('hidden');
            }
        });
        // Update active toggle button
        document.querySelectorAll('.plan-toggle-btn').forEach(btn => btn.classList.remove('active'));
        if (type === 'home') {
            toggleHome.classList.add('active');
        } else {
            toggleBusiness.classList.add('active');
        }
    }

    toggleHome.addEventListener('click', function() {
        showPlans('home');
    });
    toggleBusiness.addEventListener('click', function() {
        showPlans('business');
    });

    // Show Home plans by default
    showPlans('home');

    // ---------- (Optional) Navbar scroll, smooth scroll, active link – already in base ----------
    // We'll rely on base template's scripts, but if you want to keep the dropdown toggle,
    // you can add it here or keep it in base.
    // The base already has the dropdown toggle logic.