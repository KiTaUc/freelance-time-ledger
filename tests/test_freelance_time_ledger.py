import importlib.util,json,tempfile,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('x',Path(__file__).parents[1]/'src/freelance_time_ledger.py');x=importlib.util.module_from_spec(s);s.loader.exec_module(x)
class T(unittest.TestCase):
 def test_domain_result(self):
  data=json.loads("[{\"client\":\"A\",\"task\":\"макет\",\"minutes\":45},{\"client\":\"A\",\"task\":\"правки\",\"minutes\":15}]"); result=x.run(data,'2026-08-18',7); self.assertTrue(result is not None)
if __name__=='__main__':unittest.main()
