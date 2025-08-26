from generators.file_generator import generate_file_logs


def test_generate_file_logs(tmp_path):
    access = tmp_path / "access.log"
    error = tmp_path / "error.log"
    generate_file_logs(10, str(access), str(error))
    assert access.exists()
    assert error.exists()
    assert access.read_text().count("\n") == 10
    assert error.read_text().count("\n") == 10
