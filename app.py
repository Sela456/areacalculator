from flask import Flask, request, jsonify, render_template

from database import create_table, get_connection


app = Flask(__name__)


# Create database table when application starts
create_table()


# -------------------------
# WEB PAGE
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# AREA CALCULATOR API
# -------------------------

@app.route("/area", methods=["POST"])
def calculate_area():
    data = request.get_json()

    # Get database connection
    connection = get_connection()

    # Create cursor
    cursor = connection.cursor()

    username = data.get("username")
    shape = data.get("shape")
    dimension1 = data.get("dimension1")
    dimension2 = data.get("dimension2")

    if not username:
        return jsonify({
            "error": "Username is required"
        }), 400

    if not shape:
        return jsonify({
            "error": "Shape is required"
        }), 400

    try:
        dimension1 = float(dimension1)

    except ValueError:
        return jsonify({
            "error": "Invalid dimension"
        }), 400

    if shape == "circle":
        area = 3.14 * dimension1 * dimension1

    elif shape == "square":
        area = dimension1 * dimension1

    elif shape == "rectangle":

        if dimension2 is None:
            return jsonify({
                "error": "Rectangle requires length and width"
            }), 400

        dimension2 = float(dimension2)

        area = dimension1 * dimension2

    else:
        return jsonify({
            "error": "Invalid shape"
        }), 400

    # Save calculation into PostgreSQL
    cursor.execute(
        """
        INSERT INTO calculations
        (username, shape, dimension1, dimension2, area)

        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            username,
            shape,
            dimension1,
            dimension2,
            area
        )
    )

    # Save changes permanently
    connection.commit()

    # Close database resources
    cursor.close()
    connection.close()

    return jsonify({
        "username": username,
        "shape": shape,
        "area": round(area, 2)
    })


# -------------------------
# START APPLICATION
# -------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
