import difflib
import json
import unittest

import sys
print(sys.path)

import ffig_explorer


header = """
#include "ffig/attributes.h"

struct FFIG_EXPORT Asset
{
  virtual FFIG_EXPORT_NAME(value) double PV() const = 0;
  virtual FFIG_PROPERTY_NAME(name) const char* id() const = 0;
};
  virtual ~Asset() = default;

struct FFIG_NAME(CDO) CollateralisedDebtObligation : Asset
{
  CollateralisedDebtObligation() {}

  double PV() const override { return 99.99; }
  const char* id() const override { return "CDO"; }
};
"""


class FFIGExplorerTestCase(unittest.TestCase):

    def setUp(self):
        import ffig.FFIG
        self.app = ffig_explorer.app.test_client()
        self.app.testing = True

    def test_home(self):
        flask_resp = self.app.get("/")
        assert flask_resp.status_code == 200

    def test_api_success(self):
        data = dict(module_name="test", inp_file=header,
                    bindings_to_generate=["py3"])
        flask_resp = self.app.post("api/gen_bindings_from_tu", data=data)
        assert flask_resp.status_code == 200

    def test_api_generated_good_binding(self):
        with open("expected_binding.py") as f:
            # remove \n from end of each line
            expected_binding = [line.rstrip() for line in f]
        payload = {'module_name': "test", 'inp_file': header,
                   "bindings_to_generate": ["py3"]}

        flask_resp = self.app.post("http://127.0.0.1:5000/api/gen_bindings_from_tu",
                                   data=payload)
        assert flask_resp.status_code == 200
        # returns Flask.Response object, with .data attribute
        # load the byte string into json and index into it
        generated_code = json.loads(flask_resp.data)['res']
        differ = difflib.Differ()
        binding_from_api = generated_code.splitlines()
        res = list(differ.compare(binding_from_api, expected_binding))
        for line in res:
            # Each line of a Differ delta begins with a two-letter code.
            # '  '  represents a line common to both sequences.
            assert line[0:2] == '  '

    def test_api_fails_on_empty_header(self):
        data = dict(module_name="test", inp_file="", bindings_to_generate=[])
        flask_resp = self.app.post("api/gen_bindings_from_tu", data=data)
        assert flask_resp.status_code == 400


if __name__ == '__main__':
    unittest.main(verbosity=10)
