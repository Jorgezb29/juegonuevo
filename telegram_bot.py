import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests
from decouple import config

# Configuración del bot
TELEGRAM_TOKEN = '7031570425:AAGUtn2x7ihd4KNkmjph4QG1OgulNXBlWso'  # <-- Reemplaza con tu token real

# Comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "¡Bienvenido al juego! Usa /play para empezar a jugar."
    )

# Comando /play
async def play(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    await update.message.reply_text(
        f"¡Hola! Tu ID de usuario es {user_id}. Usa /tap para ganar puntos."
    )

# Comando /tap
async def tap(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    # Llamar a la API para sumar puntos
    response = requests.post(
        "http://127.0.0.1:5000/api/points/add",
        json={"telegram_id": user_id, "points": 10}  # Sumar 10 puntos por cada tap
    )

    if response.status_code == 200:
        points = response.json().get("points", 0)
        await update.message.reply_text(
            f"¡Has ganado 10 puntos! Ahora tienes {points} puntos."
        )
    else:
        await update.message.reply_text(
            "Hubo un error al sumar puntos. Inténtalo de nuevo."
        )

# Manejar mensajes no reconocidos
async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text("Lo siento, no reconozco ese comando.")

# Función principal para iniciar el bot
def main():
    # Crear la aplicación del bot
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Registrar manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("tap", tap))

    # Manejar mensajes no reconocidos
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    # Ejecutar el bot en un bucle asíncrono
    asyncio.run(main())