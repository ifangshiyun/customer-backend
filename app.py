from flask import Flask
from firebase_config import db  # ensure Firebase is initialized
from routes.orders import orders_bp
from routes.menus import menus_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(orders_bp, url_prefix="/orders")
app.register_blueprint(menus_bp, url_prefix="/menus")

@app.route('/')
def index():
    return {"message": "Backend is running."}

if __name__ == '__main__':
    app.run(debug=True)
