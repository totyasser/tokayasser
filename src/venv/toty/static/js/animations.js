// static/js/animations.js

document.addEventListener('DOMContentLoaded', () => {
    gsap.to('.butterfly1', {
        x: '120vw',
        y: '-20vh',
        rotation: 45,
        opacity: 0,
        duration: 15,
        repeat: -1,
        delay: 0,
        ease: 'linear'
    });

    gsap.to('.butterfly2', {
        x: '-120vw',
        y: '20vh',
        rotation: -45,
        opacity: 0,
        duration: 20,
        repeat: -1,
        delay: 5,
        ease: 'linear'
    });

    gsap.to('.butterfly3', {
        x: '120vw',
        y: '-20vh',
        rotation: 45,
        opacity: 0,
        duration: 18,
        repeat: -1,
        delay: 10,
        ease: 'linear'
    });
});
