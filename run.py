import pytest

if __name__ == '__main__':
    import os
    import subprocess

    pytest.main()
    current_directory = os.getcwd()
    # print(path_dir)
    xml_path = current_directory + '\\Report\\xml'
    html_path = current_directory + '\\Report\\html'
    report_path = current_directory + "\\Report"

    cmd = "allure generate %s -o %s --clean" % (xml_path, html_path)
    output, errors = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    print(o)

