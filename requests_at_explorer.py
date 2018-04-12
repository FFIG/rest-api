#! /usr/bin/env python3

import requests

source = """
#include "ffig/attributes.h"

struct FFIG_EXPORT Asset
{
  virtual FFIG_EXPORT_NAME(value) double PV() const = 0;
  virtual FFIG_PROPERTY_NAME(name) const char* id() const = 0;
  virtual ~Asset() = default;
};

struct FFIG_NAME(CDO) CollateralisedDebtObligation : Asset
{
  CollateralisedDebtObligation() {}

  double PV() const override { return 99.99; }
  const char* id() const override { return "CDO"; }
};
"""

payload = {'module_name': "test", 'inp_file': source}

r = requests.post(
    "http://127.0.0.1:5000/api/gen_bindings_from_tu", data=payload)
if r.status_code == 200:
    print(r.text)
else:
    print("Request failed")
