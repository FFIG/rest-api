from flask import Flask, request, redirect, jsonify, render_template
import sys
import os
import os.path
import pdb
import json
import shutil

""" Flask app that implements a basic front-end on the home page and a rest-api under the /api/ endpoints """

app = Flask(__name__, template_folder=".")

CUR_DIR = os.path.dirname(__file__)


class Args:
    """ Class, which creates a duckly-typed Object
    with same attributes as normal FFIG argparser"""

    def __init__(self, path_to_source, module_name,
                 bindings, output_dir='output', template_dir=None):

        self.inputs = [os.path.abspath(path_to_source)]
        # FFIG.py takes an array of inputs (for future),
        # but currently only uses the 0th
        self.module_name = module_name
        self.bindings = list(bindings)
        if template_dir == None:
            ffig_subfolder = '/home/ffig/ffig/'
            self.template_dir = os.path.join(ffig_subfolder, 'templates')
        self.output_dir = os.path.join(CUR_DIR, output_dir)

    def __repr__(self):
        obj_str = "Module_name: {}, bindings: {}, \
                   template_dir: {}, inputs: {}".format(
            self.module_name, self.bindings, self.template_dir, self.inputs)
        return obj_str


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/api/gen_bindings_from_tu', methods=['POST'])
#@app.after_request
def gen_bindings_from_tu():
    """ Route method that receives a POST request and 
    returns a JSON response with requested bindings in plaintext 
    It writes to a file, because FFIG.py needs a path_to_source file

    """
    mod_name = request.form['module_name']
    inp_file = request.form['inp_file']

    path_to_source = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'headerfile'))
    args = Args(path_to_source, mod_name, ["python"])
    with open(path_to_source, 'w') as f:
        f.write(inp_file)
    # pdb.set_trace()
    FFIG.main(args)

    py2_bind_name = os.path.join(args.output_dir, mod_name, "interop_py2.py")
    py3_bind_name = os.path.join(args.output_dir, mod_name, "interop_py3.py")
    with app.open_resource(py2_bind_name, 'rb') as py2_bd, \
            app.open_resource(py3_bind_name, 'rb') as py3_bd:
        return jsonify(status=200, module_name=mod_name,
                       inp_file=inp_file, py3_bind=py3_bd.read(),
                       py2_bind=py2_bd.read())


if __name__ == '__main__':
    if os.path.exists('/.dockerenv'):
        # check that we are inside a container
        # FIXME runs twice
        import FFIG
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        raise Exception("Build and run a container")
