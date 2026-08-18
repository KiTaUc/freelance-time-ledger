import importlib.util,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('x',Path(__file__).parents[1]/'src/freelance_time_ledger.py');x=importlib.util.module_from_spec(s);s.loader.exec_module(x)
class T(unittest.TestCase):
 def test_domain_workflow(self):
  r=x.run([{'client':'A','task':'x','minutes':15},{'client':'A','task':'y','minutes':20}],'2026-08-18',7); self.assertTrue(r=={'A':35})
if __name__=='__main__':unittest.main()
