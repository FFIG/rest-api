import os

import unittest
import tempfile

import ffig_explorer


class FFIGExplorerTestCase(unittest.TestCase):

    def setUp(self):
        import ffig.FFIG
        ffig_explorer.app.testing = True
        self.app = ffig_explorer.app.run()

    def tearDown(self):
        pass

    def test_recieve_json():
        data = dict(module_name="test", inp_file="", bindings_to_generate=[])
        rv = self.app.post("api/gen_bindings_from_tu", data=data)
        assert rv.status_code == 400

if __name__ == '__main__':
    unittest.main()
