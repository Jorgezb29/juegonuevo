from flask import Blueprint, jsonify, request
from .models import db, User, Mission, CompletedMission, Transaction

api = Blueprint('api', __name__)

# Ruta para registrar un usuario
@api.route("/api/user/register", methods=["POST"])
def register_user():
    data = request.json
    telegram_id = data.get("telegram_id")
    username = data.get("username")

    # Verificar si el usuario ya existe
    user = User.query.filter_by(telegram_id=telegram_id).first()
    if user:
        return jsonify({"error": "El usuario ya está registrado."}), 400

    # Crear un nuevo usuario
    new_user = User(telegram_id=telegram_id, username=username)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado correctamente."})

# Ruta para obtener los puntos de un usuario
@api.route("/api/points", methods=["GET"])
def get_points():
    telegram_id = request.args.get("telegram_id")
    user = User.query.filter_by(telegram_id=telegram_id).first()

    if not user:
        return jsonify({"error": "Usuario no encontrado."}), 404

    return jsonify({"points": user.points})

# Ruta para sumar puntos
@api.route("/api/points/add", methods=["POST"])
def add_points():
    data = request.json
    telegram_id = data.get("telegram_id")
    points_to_add = data.get("points", 0)

    user = User.query.filter_by(telegram_id=telegram_id).first()
    if not user:
        return jsonify({"error": "Usuario no encontrado."}), 404

    user.points += points_to_add
    db.session.commit()

    return jsonify({"points": user.points})

# Ruta para obtener las misiones disponibles
@api.route("/api/missions", methods=["GET"])
def get_missions():
    telegram_id = request.args.get("telegram_id")
    user = User.query.filter_by(telegram_id=telegram_id).first()

    if not user:
        return jsonify({"error": "Usuario no encontrado."}), 404

    missions = Mission.query.all()
    missions_data = [{"id": m.id, "name": m.name, "reward": m.reward} for m in missions]

    return jsonify({"missions": missions_data})

# Ruta para completar una misión
@api.route("/api/missions/complete", methods=["POST"])
def complete_mission():
    data = request.json
    telegram_id = data.get("telegram_id")
    mission_id = data.get("mission_id")

    user = User.query.filter_by(telegram_id=telegram_id).first()
    if not user:
        return jsonify({"error": "Usuario no encontrado."}), 404

    mission = Mission.query.get(mission_id)
    if not mission:
        return jsonify({"error": "Misión no encontrada."}), 404

    # Verificar si la misión ya fue completada
    completed = CompletedMission.query.filter_by(user_id=user.id, mission_id=mission.id).first()
    if completed:
        return jsonify({"error": "La misión ya fue completada."}), 400

    # Registrar la misión completada
    completed_mission = CompletedMission(user_id=user.id, mission_id=mission.id)
    db.session.add(completed_mission)

    # Sumar la recompensa al usuario
    user.points += mission.reward

    # Registrar la transacción
    transaction = Transaction(user_id=user.id, type="misión completada", points=mission.reward)
    db.session.add(transaction)

    db.session.commit()

    return jsonify({"points": user.points, "message": "Misión completada."})

# Ruta para activar un boost
@api.route("/api/boost/activate", methods=["POST"])
def activate_boost():
    data = request.json
    telegram_id = data.get("telegram_id")

    user = User.query.filter_by(telegram_id=telegram_id).first()
    if not user:
        return jsonify({"error": "Usuario no encontrado."}), 404

    # Lógica para activar el boost (duplicar puntos durante 10 segundos)
    user.points *= 2
    db.session.commit()

    return jsonify({"message": "Boost activado correctamente.", "points": user.points})

# Ruta para obtener el perfil del usuario
@api.route("/api/user/profile", methods=["GET"])
def get_profile():
    telegram_id = request.args.get("telegram_id")
    user = User.query.filter_by(telegram_id=telegram_id).first()

    if not user:
        return jsonify({"error": "Usuario no encontrado."}), 404

    # Obtener misiones completadas
    completed_missions = CompletedMission.query.filter_by(user_id=user.id).all()
    missions_data = [{"id": m.mission_id, "completed_at": m.completed_at} for m in completed_missions]

    # Obtener transacciones
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    transactions_data = [{"type": t.type, "points": t.points, "created_at": t.created_at} for t in transactions]

    return jsonify({
        "username": user.username,
        "points": user.points,
        "level": user.level,
        "missions": missions_data,
        "transactions": transactions_data
    })