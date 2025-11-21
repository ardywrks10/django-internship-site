document.addEventListener('DOMContentLoaded', () => {
    const text = "WELCOME";
    const speed = 150;
    const deleteSpeed = 100;
    const delay = 1000;

    let index = 0;
    let isDeleting = false;
    const element = document.getElementById("welcomeText");

    if (!element) {
        console.log("typing.js: #welcomeText not found");
        return;
    }
    function typeEffect() {
        if (!isDeleting) {
            element.textContent = text.slice(0, index + 1);
            index++;

            if (index === text.length) {
                isDeleting = true;
                setTimeout(typeEffect, delay);
                return;
            }
        } else {
            element.textContent = text.slice(0, index - 1);
            index--;

            if (index === 0) {
                isDeleting = false;
            }
        }
        setTimeout(typeEffect, isDeleting ? deleteSpeed : speed);
    }
    typeEffect();
});

document.addEventListener("DOMContentLoaded", () => {
    const slider = document.getElementById("techSlider");
    const wrapper = document.querySelector(".tech-slider-wrapper");

    const clone = slider.cloneNode(true);
    slider.appendChild(clone);

    let speed = 2.2;
    let pos = 0;

    function loop() {
        pos -= speed;

        const totalWidth = slider.scrollWidth / 2;

        if (Math.abs(pos) >= totalWidth) {
            pos = 0;
        }

        slider.style.transform = `translateX(${pos}px)`;

        fadeIcons();
        requestAnimationFrame(loop);
    }

    function fadeIcons() {
        const wrapperRect = wrapper.getBoundingClientRect();
        const centerX = wrapperRect.left + wrapperRect.width / 2;

        document.querySelectorAll(".tech-icon").forEach(icon => {
            const rect = icon.getBoundingClientRect();
            const iconCenter = rect.left + rect.width / 2;

            const dist = Math.abs(centerX - iconCenter);
            if (dist < 120) {
                icon.classList.add("visible");
            } else {
                icon.classList.remove("visible");
            }
        });
    }

    loop();
});

document.addEventListener("DOMContentLoaded", function () {
    const track = document.querySelector(".slider-track");
    const images = document.querySelectorAll(".slider-image");
    const dotsContainer = document.querySelector(".slider-dots"); 
    let index = 0;
    const total = images.length;
    const firstClone = images[0].cloneNode(true);
    track.appendChild(firstClone);

    const dots = [];
    for (let i = 0; i < total; i++) {
        const dot = document.createElement("div");
        dot.classList.add("slider-dot");
        if (i === 0) dot.classList.add("active");
        dotsContainer.appendChild(dot);
        dots.push(dot);
        dot.addEventListener("click", () => {
            index = i;
            updateSlide();
        });
    }

    function updateDots() {
        dots.forEach((d, idx) => {
            d.classList.toggle("active", idx === index);
        });
    }

    function updateSlide() {
        track.style.transition = "transform 0.7s ease-in-out";
        track.style.transform = `translateX(-${index * 100}%)`;
        updateDots();
    }

    setInterval(() => {
        index++;

        updateSlide();

        if (index === total) {
            setTimeout(() => {
                track.style.transition = "none";
                track.style.transform = "translateX(0%)";
                index = 0;
                updateDots();
            }, 700);
        }

    }, 4000);
});


