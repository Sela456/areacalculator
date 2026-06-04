from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route("/app/<shape>")
def area(shape):
    if shape == "circle":
        radius = float(request.args.get("radius"))
        area = 3.14 * radius * radius
        return jsonify ({"shape": "circle", "area": area})
    
    elif shape == "square":
        length = float(request.args.get("length"))
        area = length * length
        return jsonify ({"shape": "square", "area": area})
    
    elif shape == "rectangle":
        length = float(request.args.get("length"))
        width = float(request.args.get("width"))
        area = length * width
        return jsonify ({"shape": "rectangle", "area": area})
    
    else:
        return jsonify ({"error": "unknown shape"})
    

    if __name__ == "__main__":
        app.run(debug=True)

