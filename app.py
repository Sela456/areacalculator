from flask import Flask, request, jsonify

app = Flask(__name__)

# -------------------------
# WEB PAGE (GET)
# -------------------------


@app.route("/", methods=["GET"])
def home():
    return """
    <h2>Area Calculator</h2>

    <label>Shape:</label>
    <input id="shape" placeholder="circle / square / rectangle"><br><br>

    <label>Radius (circle):</label>
    <input id="radius" placeholder="radius"><br><br>

    <label>Length:</label>
    <input id="length" placeholder="length"><br><br>

    <label>Width:</label>
    <input id="width" placeholder="width"><br><br>

    <button onclick="calculate()">Calculate Area</button>

    <h3 id="result"></h3>

    <script>
    async function calculate() {
        const shape = document.getElementById('shape').value;
        const radius = document.getElementById('radius').value;
        const length = document.getElementById('length').value;
        const width = document.getElementById('width').value;

        let data = { shape };

        if (shape === "circle") {
            data.radius = Number(radius);
        }
        else if (shape === "square") {
            data.length = Number(length);
        }
        else if (shape === "rectangle") {
            data.length = Number(length);
            data.width = Number(width);
        }

        const res = await fetch('/area', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        document.getElementById('result').innerText =
            "Result: " + JSON.stringify(result);
    }
    </script>
    """

# -------------------------
# API (POST)
# -------------------------


@app.route("/area", methods=["POST"])
def calculate_area():
    data = request.get_json()

    shape = data.get("shape")

    if shape == "circle":
        radius = data.get("radius")
        if radius is None:
            return jsonify({"error": "radius is required"}), 400
        area = 3.14 * radius * radius
        return jsonify({"shape": "circle", "area": area})

    elif shape == "square":
        length = data.get("length")
        if length is None:
            return jsonify({"error": "length is required"}), 400
        area = length * length
        return jsonify({"shape": "square", "area": area})

    elif shape == "rectangle":
        length = data.get("length")
        width = data.get("width")
        if length is None or width is None:
            return jsonify({"error": "length and width are required"}), 400
        area = length * width
        return jsonify({"shape": "rectangle", "area": area})

    else:
        return jsonify({"error": "invalid shape"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
