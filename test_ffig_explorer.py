import os

import unittest

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
        rv = self.app.get("/")
        assert rv.status_code == 200

    def test_api_success(self):
        data = dict(module_name="test", inp_file=header,
                    bindings_to_generate=["py3"])
        rv = self.app.post("api/gen_bindings_from_tu", data=data)
        assert rv.status_code == 200

    def test_api_fails_on_empty_header(self):
        data = dict(module_name="test", inp_file="", bindings_to_generate=[])
        rv = self.app.post("api/gen_bindings_from_tu", data=data)
        assert rv.status_code == 400


if __name__ == '__main__':
    unittest.main(verbosity=10)
