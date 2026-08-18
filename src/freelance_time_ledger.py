import argparse,json
from datetime import date
from pathlib import Path

def run(entries,today='',days=0):
 totals={}
 for entry in entries: totals[entry['client']]=totals.get(entry['client'],0)+int(entry['minutes'])
 return totals

def main():
 parser=argparse.ArgumentParser(description='Локальный отраслевой инструмент')
 parser.add_argument('command')
 parser.add_argument('file',type=Path)
 parser.add_argument('--today',default='')
 parser.add_argument('--days',type=int,default=0)
 args=parser.parse_args()
 data=json.loads(args.file.read_text(encoding='utf-8'))
 print(json.dumps(run(data,args.today,args.days),ensure_ascii=False,indent=2))
if __name__=='__main__': main()
