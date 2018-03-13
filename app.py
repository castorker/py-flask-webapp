from flask import Flask, render_template, redirect, url_for, request
from quibble import Quibble
from quibble_data_service import QuibbleDataService

app = Flask(__name__)

data_service = QuibbleDataService()


@app.route("/", methods=["GET", "POST"])
def quibbles_page():
    if request.method == "POST":
        new_quibble_text = request.form.get("text", "")
        new_quibble_category = request.form.get("category", "")
        new_quibble = Quibble(text=new_quibble_text, category=new_quibble_category)
        data_service.create(new_quibble)

        return redirect(url_for("quibbles_page"))

    return render_template("index.html", quibbles=data_service.get_all())


if __name__ == "__main__":
    app.run(debug=True)
