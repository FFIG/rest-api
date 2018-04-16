#! /usr/bin/env python3

import difflib
import requests

with open("expected_binding.py") as f:
    expected_binding = f.readlines()


source = """
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

payload = {'module_name': "test", 'inp_file': source,
           "bindings_to_generate": ["py3"]}

r = requests.post(
    "http://127.0.0.1:5000/api/gen_bindings_from_tu", data=payload)
if r.status_code == requests.codes.ok:
    json_resp = r.json()
    d = difflib.Differ()
    res = list(d.compare(json_resp['res'].splitlines(), expected_binding))
    pprint.pprint(res)
    # assert json_resp['res'] == expected_binding
