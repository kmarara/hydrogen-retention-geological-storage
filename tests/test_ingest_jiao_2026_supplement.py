"""Tests for the Jiao et al. supplementary workbook ingestion."""
from pathlib import Path
import sys, tempfile, unittest
from openpyxl import Workbook
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from ingest_jiao_2026_supplement import extract

class TestJiaoSupplementIngestion(unittest.TestCase):
    def make_workbook(self,path):
        book=Workbook(); sheet=book.active; sheet.title="Experiment data from literature"
        sheet.append(["No.","p","T","NaCl","KCl","CaCl2","MgCl2","CH4","CO2","Method","IFT","Ref"])
        sheet.append([""]*12)
        for i in range(1,451):
            study=min(9,((i-1)//50)+1)
            marker=f"[{study}]" if i==1 or (i-1)%50==0 else None
            sheet.append([i,1.0,298.15,0.,0.,0.,0.,0.,0.,i%2,70.+i/100,marker])
        book.save(path)
    def test_extracts_all_rows_and_keeps_unverified_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"fixture.xlsx"; self.make_workbook(path); frame,_=extract(path)
            self.assertEqual(len(frame),450)
            self.assertEqual(frame.observation_no.tolist(),list(range(1,451)))
            self.assertEqual(frame.source_excel_row.iloc[0],3)
            self.assertEqual(frame.source_excel_row.iloc[-1],452)
            self.assertTrue((frame.provenance_status=="unknown").all())
            self.assertFalse(frame.benchmark_eligible_primary.any())
            self.assertEqual(set(frame.method_label),{"Pendant Drop","Sessile Drop"})
    def test_rejects_missing_required_values(self):
        import pandas as pd
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"fixture.xlsx"; self.make_workbook(path)
            raw=pd.read_excel(path,sheet_name="Experiment data from literature",header=None)
            raw.iloc[2,10]=None
            with pd.ExcelWriter(path,engine="openpyxl") as writer:
                raw.to_excel(writer,sheet_name="Experiment data from literature",header=False,index=False)
            with self.assertRaises(ValueError): extract(path)

if __name__=="__main__": unittest.main()
