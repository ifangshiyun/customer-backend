from flask import Blueprint, request, jsonify
from firebase_config import db
import datetime

orders_bp = Blueprint('orders', __name__)
orders_collection = "orders"

@orders_bp.route('/place_order', methods=['POST'])
def place_order():
    try:
        data = request.get_json()

        # Allow single item to be wrapped as list
        if "menu_id" in data and "quantity" in data and "price" in data and "name" in data:
            data = {
                "items": [
                    {
                        "menu_id": data["menu_id"],
                        "name": data["name"],
                        "price": data["price"],
                        "quantity": data["quantity"]
                    }
                ]
            }

        items = data.get("items")
        if not isinstance(items, list) or not items:
            return jsonify({"error": "items must be a non-empty list"}), 400

        total_price = sum(item["price"] * item["quantity"] for item in items)

        order_data = {
            "items": items,
            "timestamp": datetime.datetime.utcnow(),
            "total_price": total_price
        }

        db.collection(orders_collection).add(order_data)
        return jsonify({"message": "Order placed successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
