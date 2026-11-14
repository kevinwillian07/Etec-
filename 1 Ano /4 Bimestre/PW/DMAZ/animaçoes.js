/*  DMAZ — DIGITAL MUSIC ARCHIVE ZONE  */

/* ELEMENTOS DO PLAYER */

const audio = document.querySelector("#audio");
const playButton = document.querySelector("#play-button");
const progress = document.querySelector("#progress");
const currentTime = document.querySelector("#current-time");
const duration = document.querySelector("#duration");

/* PLAYER */

if (audio && playButton && progress && currentTime && duration) {

    function formatTime(seconds) {
        if (!Number.isFinite(seconds)) return "00:00";

        const minutes = Math.floor(seconds / 60);
        const secondsLeft = Math.floor(seconds % 60);

        return String(minutes).padStart(2, "0") + ":" +
               String(secondsLeft).padStart(2, "0");
    }

    audio.addEventListener("loadedmetadata", () => {
        duration.textContent = formatTime(audio.duration);
    });

    playButton.addEventListener("click", async () => {
        if (audio.paused) {
            try {
                await audio.play();
            } catch (error) {
                console.error("Erro ao reproduzir:", error);
                alert("Confira se Hysteria.mp3 está na pasta correta.");
            }
        } else {
            audio.pause();
        }
    });

    audio.addEventListener("timeupdate", () => {
        if (!audio.duration) return;

        progress.value = (audio.currentTime / audio.duration) * 100;
        currentTime.textContent = formatTime(audio.currentTime);
    });

    progress.addEventListener("input", () => {
        if (!audio.duration) return;
        audio.currentTime = (progress.value / 100) * audio.duration;
    });

    audio.addEventListener("ended", () => {
        progress.value = 0;
        currentTime.textContent = "00:00";
    });

    audio.addEventListener("pause", () => {
        playButton.textContent = "▶";
    });

    audio.addEventListener("play", () => {
        playButton.textContent = "Ⅱ";
    });

    audio.addEventListener("error", () => {
        console.error("Erro ao carregar Hysteria.mp3.");
    });
}


/*  MOVIMENTO DO GATO ALIEN*/

const astronaut = document.querySelector(".astronaut");


/* MOVIMENTO COM OMAUSE */

if (astronaut) {

    window.addEventListener("scroll", () => {

        const scroll = window.scrollY;

        astronaut.style.marginTop =
            `${scroll * 0.12}px`;

    }, { passive: true });}


   // CURSOR PERSONALIZADO

const cursor = document.querySelector(".cursor");
const outline = document.querySelector(".cursor-outline");

if (cursor && outline) {

    let mouseX = 0;
    let mouseY = 0;
    let outlineX = 0;
    let outlineY = 0;

    document.addEventListener("mousemove", (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        cursor.style.left = mouseX + "px";
        cursor.style.top = mouseY + "px";
    });

    function animateCursor() {
        outlineX += (mouseX - outlineX) * 0.15;
        outlineY += (mouseY - outlineY) * 0.15;

        outline.style.left = outlineX + "px";
        outline.style.top = outlineY + "px";

        requestAnimationFrame(animateCursor);
    }

    animateCursor();

    document.querySelectorAll("a, button, .player").forEach(element => {
        element.addEventListener("mouseenter", () => {
            outline.classList.add("hover");
        });

        element.addEventListener("mouseleave", () => {
            outline.classList.remove("hover");
        });
    });
}
