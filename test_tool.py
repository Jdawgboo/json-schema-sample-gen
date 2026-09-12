import unittest
from tool import sample
class SchemaSampleTests(unittest.TestCase):
 def test_types(self):self.assertEqual(sample({'type':'object','properties':{'id':{'type':'integer','minimum':1},'name':{'type':'string'}},'required':['id']}),{'id':1});self.assertEqual(sample({'enum':['a','b']}),'a')
if __name__=='__main__':unittest.main()
