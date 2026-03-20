from ex_01 import log_file

def test_log_file(log_file):
    log_file.write("Benvenuti, Saluton komincanto")

    assert not log_file.closed