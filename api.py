from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import skimage
import tensorflow as tf
import numpy as np

app = Flask(__name__)

interpreter = tf.lite.Interpreter(model_path="./modeling/mnist.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


@app.get("/")
def index():
    ans = request.args.get('ans')
    prob = request.args.get('prob')

    if prob:
        prob = float(prob)*100


    return render_template("index.html", ans=ans, prob=prob)

@app.post("/process")
def handle_input():
    img_input = request.files['image']
    img_input.save("./server/tmp/img.jpg")

    input_data = skimage.io.imread("./server/tmp/img.jpg")
    input_data = input_data.astype(input_details[0]['dtype'])
    input_data = np.expand_dims(input_data, axis=0)

    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])

    out_as_list = output[0].tolist()

    ans = out_as_list.index(max(out_as_list))
    prob = max(out_as_list)

    return redirect(url_for('index', ans=ans, prob=prob))

