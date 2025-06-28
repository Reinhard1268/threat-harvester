from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Helper: Load enriched IOCs from JSON file
def load_iocs():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "enriched_iocs.json")
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    iocs = load_iocs()
    query = request.args.get("q", "").strip().lower()

    if query:
        filtered = []
        for ioc in iocs:
            # Match across all fields
            if any(query in str(value).lower() for value in ioc.values()):
                filtered.append(ioc)
        return render_template("stats.html", iocs=filtered, query=query)
    
    return render_template("stats.html", iocs=iocs, query="")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
