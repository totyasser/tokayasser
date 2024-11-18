// Toggle navigation menu on mobile
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('section');

    window.addEventListener('scroll', () => {
        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            if (pageYOffset >= sectionTop) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // Mobile Menu Toggle
    const navContainer = document.querySelector('.nav-links');
    const toggleButton = document.querySelector('.menu-toggle');

    toggleButton.addEventListener('click', () => {
        navContainer.classList.toggle('active');
        toggleButton.classList.toggle('toggle');
    });
});
