// static/js/animations.js

document.addEventListener('DOMContentLoaded', () => {
    // Butterfly animation settings
    const butterflies = document.querySelectorAll('.butterfly');
    const directions = ['120vw', '-120vw']; // Possible horizontal directions

    butterflies.forEach((butterfly, index) => {
        const randomDirection = directions[Math.floor(Math.random() * directions.length)]; // Random direction
        const randomDuration = Math.random() * 10 + 10; // Duration between 10s and 20s
        const randomDelay = Math.random() * 5; // Delay between 0s and 5s
        const randomRotation = Math.random() * 90 - 45; // Rotation between -45deg and 45deg
        const randomYOffset = Math.random() * 40 - 20; // Random vertical offset (-20vh to 20vh)

        gsap.to(butterfly, {
            x: randomDirection,
            y: `${randomYOffset}vh`,
            rotation: randomRotation,
            opacity: 0,
            duration: randomDuration,
            repeat: -1,
            delay: randomDelay,
            ease: 'linear',
        });
    });
});
