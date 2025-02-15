const userId = "user123"; // Este valor debería venir del backend en un proyecto real
const referralLink = `http://127.0.0.1:5000/register?ref=${userId}`;

document.getElementById("inviteLink").querySelector("span").textContent = referralLink;

document.getElementById("copyLink").addEventListener("click", () => {
    navigator.clipboard.writeText(referralLink).then(() => {
        alert("Enlace copiado al portapapeles");
    });
});