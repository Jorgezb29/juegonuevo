let isBoostActive = localStorage.getItem("isBoostActive") === "true";

function activateBoost() {
    if (isBoostActive) {
        alert("El Boost ya está activo.");
        return;
    }

    isBoostActive = true;
    localStorage.setItem("isBoostActive", "true");

    // Desactivar el Boost después de 10 segundos
    setTimeout(() => {
        isBoostActive = false;
        localStorage.setItem("isBoostActive", "false");
        alert("El Boost ha terminado.");
    }, 10000);

    alert("¡Boost activado! Tus puntos se duplicarán por 10 segundos.");
}

document.getElementById("boostButton").addEventListener("click", activateBoost);

function addPoints(points) {
    fetch("/api/points/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ points: points })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("pointsDisplay").textContent = `Puntos: ${data.points}`;
    });
}