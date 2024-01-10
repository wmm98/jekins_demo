import pytest


class TestDep:
    dep_id = None

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.run(order=1)
    def test_add_dep(self):
        print("11111111111111111")
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_get_dep(self):
        print("222222222222222222222")
        assert 1 == 1

    @pytest.mark.run(order=3)
    def test_update_dep(self):
        print("33333333333333333333333")
        assert 0 == 0


