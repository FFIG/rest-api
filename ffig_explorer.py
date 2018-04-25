from flask import Flask, request, redirect, jsonify, render_template
import sys
import os
import os.path
import pdb
import json
import shutil

import ffig.FFIG

""" Flask app that implements a basic front-end on the home page and a rest-api under the /api/ endpoints """

app = Flask(__name__, template_folder=".")


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/api/gen_bindings_from_tu', methods=['POST'])
def gen_bindings_from_tu():
    """ Route method that receives a POST request and 
    returns a JSON response with requested bindings in plaintext 
    It writes to a file, because FFIG.py needs a path_to_source file

    """
    mod_name = request.form['module_name']
    inp_file = request.form['inp_file']
    bindings_requested = request.form["bindings_to_generate"]

    # local re-write/copy of ffig functionality
    ffig_subfolder = '../ffig/ffig/'
    template_dir = os.path.join(ffig_subfolder, 'templates')

    env = ffig.FFIG.set_template_env(template_dir)

    template = env.get_template("py3.tmpl")

    m = ffig.FFIG.build_model_from_source(
        "filename.hpp", mod_name, [("filename.hpp", inp_file)])
    classes = m.classes
    api_classes = ffig.FFIG.collect_api_and_obj_classes(classes, 'FFIG:EXPORT')
    output_string = ffig.generators.render_api_and_obj_classes(
        mod_name, api_classes, template)
    return jsonify(status=200,
                   module_name=mod_name,
                   res=output_string)


if __name__ == '__main__':
    if os.path.exists('/.dockerenv'):
        # check that we are inside a container

        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        raise Exception("Build and run a container")
