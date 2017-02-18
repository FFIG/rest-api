from flask import Flask, request, redirect, jsonify, render_template
import sys
import os
import os.path
import pdb


""" Flask app that implements a basic front-end on the home page and a rest-api under the /api/ endpoints """

app = Flask(__name__, template_folder=".")


class Args:
    """ Class, which creates a duckly-typed Object
    with same attributes as normal FFIG argparser"""

    def __init__(self, path_to_source, module_name,
                 bindings, output_dir='output', template_dir=None):
        cur_dir = os.path.dirname(__file__)
        self.inputs = [os.path.abspath(path_to_source)]
        self.module_name = module_name
        self.bindings = list(bindings)
        if template_dir == None:
            self.template_dir = os.path.join(ffig_subfolder, 'templates')
        self.output_dir = os.path.join(cur_dir, output_dir)

    def __repr__(self):
        return "Args. module_name: {}, bindings: {}, template_dir: {}, inputs: {}".format(self.module_name, self.bindings, self.template_dir, self.inputs)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/api/gen_bindings_from_tu', methods=['POST'])
def gen_bindings_from_tu():
    mod_name = request.form['module_name']
    inp_file = request.form['inp_file']

    path_to_source = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'test_write_file'))
    #print(os.path.dirname(__file__), path_to_source)
    with open(path_to_source, 'w') as f:
        f.write(request.form['inp_file'])

    print(os.path.abspath(path_to_source))
    args = Args(path_to_source, mod_name, ["python"])
    print(args)
    FFIG.main(args)
    # f = json.load(os.path.join(Args.output_dir))
    # process the in the response
    return jsonify(status=200, module_name=mod_name, inp_file=inp_file)


if __name__ == '__main__':
    if os.path.exists('/.dockerenv'):
        # check that we are inside a container
        # FIXME runs twice
        ffig_folder = '/home/ffig-master/'
        ffig_subfolder = '/home/ffig-master/ffig/'
        sys.path.extend([ffig_folder, ffig_subfolder])
        from ffig import *

    app.run(host='0.0.0.0', port=5000, debug=False)
