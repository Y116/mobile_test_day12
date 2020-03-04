"""
Allure报告测试demo
"""
import allure


class Test(object):
    """自定义测试类"""

    @allure.MASTER_HELPER.step(title='测试方法01')
    def test_func01(self):
        print('测试方法01')

    def test_func02(self):
        print('测试方法02')

    def test_func03(self):
        print('测试方法03')
