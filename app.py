<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import base64
=======
from flask import flask, render_template, request, redirect, url_for, Flask

>>>>>>> 1cf48c4e4f93fd4f2635d931a6cb49c85c9af872
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def main_page():
    return render_template("MainPage.html")


@app.route('/3', methods = ['POST'])
def result_page():
    draw = request.form.get("url")
    draw = draw[21:]
    # Decoding
    draw_decoded = base64.b64decode(draw)
    image = np.asarray(bytearray(draw_decoded), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    # Show Image, uncomment to see image
    # cv2.imshow('img', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return render_template("ResultPage.html", result=3)


print(__name__)
if __name__ == '__main__':
    app.run(debug=True)
