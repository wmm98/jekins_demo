import pytest
# import requests
# from api.login import Login
# import config




class TestLogin:
    def setup(self):
        print("*********这是开始****************")
        # self.api_login = Login()
        # self.session = requests.Session()

    def teardown(self):
        print("*********这是结束****************")

    @pytest.mark.run(order=0)
    def test_login(self):
        print("***********登录成功**************8")
        assert 1 == 1


if __name__ == '__main__':
    import os
    pytest.main()
    # pytest.main(["-v"])
    cmd = "allure generate xml -o html --clean"
    # cmd = 'allure generate %s -o %s --clean' % ("../Report/xml", "../Report/html")
    # os.system(cmd)

