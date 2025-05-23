from flask import Blueprint, jsonify

menus_bp = Blueprint('menus', __name__)

@menus_bp.route("/", methods=["GET"])
def get_menus():
    return jsonify([
        { "name": "原味紅豆餅", "price": 15, "imgUrl": "./images/redbean.png" },
        { "name": "奶油餅", "price": 15, "imgUrl": "./images/cream.png" },
        { "name": "芝士餅", "price": 15, "imgUrl": "./images/cream.png"  },
        { "name": "巧克力餅", "price": 20, "imgUrl": "./images/choco.png" },
        { "name": "OREO奶酥油餅", "price": 20, "imgUrl": "./images/cream.png"  },
        { "name": "可可奶酥白餅", "price": 20, "imgUrl": "./images/cream.png"  },
        { "name": "紅豆抹醬餅", "price": 20, "imgUrl": "./images/cream.png"  },
        { "name": "抹茶麻糬餅", "price": 20, "imgUrl": "./images/cream.png"  },
        { "name": "黑芝麻奶酥油餅", "price": 20, "imgUrl": "./images/cream.png"  },
        { "name": "珍珠抹奶酥油餅", "price": 20, "imgUrl": "./images/cream.png"  }
    ])
