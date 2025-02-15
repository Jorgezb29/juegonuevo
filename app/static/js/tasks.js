const missions = [
    { id: 1, name: "Síguenos en Instagram", link: "https://instagram.com/tu_perfil", reward: 50, completed: false },
    { id: 2, name: "Síguenos en X (Twitter)", link: "https://twitter.com/tu_perfil", reward: 50, completed: false },
    { id: 3, name: "Suscríbete a nuestro canal de YouTube", link: "https://youtube.com/tu_canal", reward: 100, completed: false },
    { id: 4, name: "Síguenos en Facebook", link: "https://facebook.com/tu_perfil", reward: 50, completed: false },
    { id: 5, name: "Misión diaria: Mira un anuncio", link: "#", reward: 30, completed: false, isAd: true }
];

function completeMission(mission) {
    if (mission.completed) {
        alert("Esta misión ya fue completada.");
        return;
    }

    if (mission.isAd) {
        alert("Mira un anuncio...");
        setTimeout(() => {
            alert("¡Anuncio completado!");
            finalizeMission(mission);
        }, 3000);
    } else {
        window.open(mission.link, "_blank");
        finalizeMission(mission);
    }
}

function finalizeMission(mission) {
    mission.completed = true;
    let totalPoints = parseInt(localStorage.getItem("totalPoints")) || 0;
    totalPoints += mission.reward;
    localStorage.setItem("totalPoints", totalPoints);
    alert(`¡Has ganado ${mission.reward} puntos!`);
    location.reload();
}
function completeMission(mission) {
    fetch("/api/missions/complete", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mission_id: mission.id })
    })
    .then(response => response.json())
    .then(data => {
        alert(`¡Has ganado ${data.points} puntos!`);
        location.reload();
    });
}