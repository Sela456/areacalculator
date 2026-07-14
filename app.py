from flask import Flask, request, jsonify, render_template

from database import create_table, get_connection


app = Flask(__name__)


try:
    create_table()
except Exception as e:
    print("Database initialization failed:", e)


@app.route("/health")
def health():
    return "OK", 200


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

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    connection = get_connection()

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

        if not dimension2:
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

    connection.commit()

    cursor.close()

    connection.close()

    # Return JSON for API clients

    if request.is_json:

        return jsonify({

            "username": username,

            "shape": shape,

            "area": round(area, 2)

        })

    # Return webpage result

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>Area Result</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                text-align: center;
                width: 350px;
            }}

            h1 {{
                color: #333;
            }}

            a {{
                display: inline-block;
                margin-top: 20px;
                background: #007bff;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
            }}

        </style>

    </head>


    <body>

        <div class="container">

            <h1>Calculation Result</h1>

            <p><strong>Name:</strong> {username}</p>

            <p><strong>Shape:</strong> {shape}</p>

            <p><strong>Area:</strong> {round(area, 2)}</p>


            <a href="/">
                Calculate Again
            </a>

        </div>

    </body>

    </html>
    """


# -------------------------
# START APPLICATION
# -------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
