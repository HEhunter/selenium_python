# coding: utf-8

import unittest

import HTMLTestRunner_cn
# HTMLTestReportCN

casePath = "D:\\pz\\testone\\case"
discover = unittest.defaultTestLoader.discover(casePath,"test*.py") # 匹配规则
print(discover)


# runer = unittest.TextTestRunner()
# runer.run(discover)  # 运行所有测试用例

reportPath = "D:\\pz\\testone\\report\\" + "result.html"

fp = open(reportPath, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(fp,verbosity=2,
                                         title="测试报告",
                                         description="报告描述")
runner.run(discover)
fp.close()