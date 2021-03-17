from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def main_page():
    return render_template("MainPage.html")


@app.route('/3')
def result_page(input_value):
    return render_template("ResultPage.html", result=3)


print(__name__)
if __name__ == '__main__':
    app.run(debug=True)
