import json

# col = open('../../colModel.json')

# colModel = json.load(col)
colModel = json.loads("""[
  {
      "title": "Ship Name",
      "dataIndex": "code",
      "key": "code"
  },
  {
    "title": "Ship Number",
    "dataIndex": "number",
    "key": "number"
  },
  {
    "title": "Embarkation Count",
    "dataIndex": "expected_couch",
    "key": "expected_couch"
  },
  {
    "title": "OCI Count",
    "dataIndex": "oci_completed_core",
    "key": "oci_completed_core"
  },
  {
    "title": "MOCI Count",
    "dataIndex": "moci_completed_core",
    "key": "moci_completed_core"
  },
  {
    "title": "CheckIn Time",
    "dataIndex": "start_date",
    "key": "start_date"
  },
  {
    "title": "OnBoard Time",
    "dataIndex": "end_date",
    "key": "end_date"
  }
]""")