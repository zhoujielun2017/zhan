# coding:utf-8
import os
import unittest

# 用例路径
case_path = os.path.join(os.getcwd())
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")


def all_case():

    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="*_test.py",
                                                   top_level_dir=None)
    return discover


if __name__ == "__main__":
    os.remove(report_path)
    with open(report_path, "a") as report:
        runner = unittest.TextTestRunner(stream=report, verbosity=2)
        runner.run(all_case())
