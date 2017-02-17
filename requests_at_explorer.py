#! /usr/bin/env python

import requests

source = """#ifdef __clang__
#define C_API __attribute__((annotate("GENERATE_C_API")))
#else
#define C_API
#endif

struct Asset
{
  virtual double PV() const = 0;
  virtual const char* name() const = 0;
  virtual ~Asset() = default;
} C_API;

struct CDO : Asset
{
  CDO() {}

  double PV() const override { return 0.0; }
  const char* name() const override { return "CDO"; }
};
"""

payload = {'module_name': "lad", 'inp_file': source}

r = requests.post(
    "http://127.0.0.1:5000/api/gen_bindings_from_tu", data=payload)
print(r.text)
