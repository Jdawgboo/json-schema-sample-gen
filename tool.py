"""Generate deterministic samples for a small schema subset."""
from __future__ import annotations
def sample(schema:dict):
 if 'enum' in schema:return schema['enum'][0]
 kind=schema.get('type','object')
 if kind=='string':return schema.get('example','example')
 if kind=='integer':return schema.get('minimum',0)
 if kind=='number':return float(schema.get('minimum',0))
 if kind=='boolean':return False
 if kind=='array':return [sample(schema.get('items',{}))]
 if kind=='object':return {key:sample(value) for key,value in schema.get('properties',{}).items() if key in schema.get('required',schema.get('properties',{}))}
 raise ValueError(f'unsupported type: {kind}')
if __name__=='__main__':
 import json,sys;print(json.dumps(sample(json.load(sys.stdin)),indent=2,sort_keys=True))
