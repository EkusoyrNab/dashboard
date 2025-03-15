from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase の初期化
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# Firestore からデータを取得
@app.route("/api/data", methods=["GET"])
def get_data():
    payments_ref = db.collection("payments").stream()
    tasks_ref = db.collection("tasks").stream()

    payments = [{"項目": p.to_dict().get("項目"), "金額": p.to_dict().get("金額"), "支払日": p.to_dict().get("支払日")} for p in payments_ref]
    tasks = [{"タスク": t.to_dict().get("タスク"), "日付": t.to_dict().get("日付")} for t in tasks_ref]

    return jsonify({"payments": payments, "tasks": tasks})

# Firestore にデータを追加
@app.route("/api/data", methods=["POST"])
def add_data():
    data = request.json
    for payment in data.get("payments", []):
        db.collection("payments").add(payment)
    for task in data.get("tasks", []):
        db.collection("tasks").add(task)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
