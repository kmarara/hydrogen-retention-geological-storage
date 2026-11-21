import tempfile
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_ift_csv import profile


class AuditIftCsvTests(unittest.TestCase):
    def test_profiles_comment_lines_and_flags_repeated_measurement_values(self):
        sample = """P_MPa,T_K,Salinity_ppm,IFT_mN_m,Source,Salinity_type
# explanatory comment
10,300,0,70,StudyA,pure_water
10,300,10000,70,StudyA,brine
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text(sample, encoding="utf-8")
            report = profile(path)

        self.assertEqual(report["row_count"], 2)
        self.assertEqual(report["numeric_rows"], 2)
        self.assertEqual(len(report["same_P_T_and_IFT_across_distinct_salinity"]), 1)
        self.assertEqual(report["benchmark_eligibility"], "NOT_CERTIFIED_SOURCE_VERIFICATION_REQUIRED")

    def test_rejects_missing_required_columns(self):
        sample = "P_MPa,T_K\n10,300\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text(sample, encoding="utf-8")
            with self.assertRaises(ValueError):
                profile(path)


if __name__ == "__main__":
    unittest.main()
