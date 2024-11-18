document.addEventListener('DOMContentLoaded', () => {
    // Scroll Navigation Highlighting
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('section');

    window.addEventListener('scroll', () => {
        let current = '';

        // Determine the current section in view
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100; // Adjust offset for fixed header
            if (pageYOffset >= sectionTop) {
                current = section.getAttribute('id');
            }
        });

        // Highlight the active link
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // Mobile Menu Toggle
    document.getElementById('mobile-menu').addEventListener('click', function() {
        const navLinks = document.querySelector('.nav-links');
        const menuToggle = document.getElementById('mobile-menu');
        navLinks.classList.toggle('active'); // Toggle the active class to show/hide the menu
        menuToggle.classList.toggle('toggle'); // Toggle the bar rotation for menu button
    });
    
    // Logo Name Toggle
    const logo = document.getElementById('logo');
    const logoName = document.getElementById('logo-name');

    if (logo && logoName) {
        logo.addEventListener('click', (e) => {
            e.preventDefault();
            logoName.classList.toggle('hidden'); // Show/hide logo name
        });
    }
});
