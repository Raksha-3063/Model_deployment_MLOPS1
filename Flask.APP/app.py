
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h1>Multiplication Table Generator</h1>

    <form method="POST">
        <label>Enter a number:</label>
        <input type="number" name="number" required>
        <button type="submit">Generate Table</button>
    </form>

    {% if table %}
        <h2>Multiplication Table of {{ number }}</h2>
        {% for row in table %}
            <p>{{ row }}</p>
        {% endfor %}
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    table = []
    number = None

    if request.method == "POST":
        number = int(request.form["number"])

        for i in range(1, 11):
            table.append(f"{number} x {i} = {number * i}")

    return render_template_string(
        HTML, table=table, number=number
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
