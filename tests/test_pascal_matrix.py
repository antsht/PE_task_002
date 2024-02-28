from subprocess import run, PIPE
import os
import os.path
import pytest

B_FILE_PATH = './bin/pascal_matrix'

if os.path.isfile(B_FILE_PATH):
    def test_bin_folder_contains_pascal_matrix():
        assert os.path.isfile(B_FILE_PATH)

    def test_pascal_matrix_not_correct_input_1():
        result = run([B_FILE_PATH], input='-1', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_pascal_matrix_not_correct_input_2():
        result = run([B_FILE_PATH], input='11', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_pascal_matrix_not_correct_input_3():
        result = run([B_FILE_PATH], input='a', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_pascal_matrix_not_correct_input_4():
        result = run([B_FILE_PATH], input='0', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

    def test_pascal_matrix_1():
        result = run([B_FILE_PATH], input='1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1'

    def test_pascal_matrix_2():
        result = run([B_FILE_PATH], input='2', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1\n1 1'

    def test_pascal_matrix_3():
        result = run([B_FILE_PATH], input='3', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1\n1 2 1\n1 3 3'

    def test_pascal_matrix_4():
        result = run([B_FILE_PATH], input='4', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1 1\n2 1 1 3\n3 1 1 4\n6 4 1 1'

    def test_pascal_matrix_5():
        result = run([B_FILE_PATH], input='5', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1 1 2\n1 1 3 3 1\n1 4 6 4 1\n1 5 10 10 5\n1 1 6 15 20'

    def test_pascal_matrix_6():
        result = run([B_FILE_PATH], input='6', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1 1 2 1\n1 3 3 1 1 4\n6 4 1 1 5 10\n10 5 1 1 6 15\n20 15 6 1 1 7\n21 35 35 21 7 1'

    def test_pascal_matrix_7():
        result = run([B_FILE_PATH], input='7', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1 1 2 1 1\n3 3 1 1 4 6 4\n1 1 5 10 10 5 1\n1 6 15 20 15 6 1\n1 7 21 35 35 21 7\n1 1 8 28 56 70 56\n28 8 1 1 9 36 84'

    def test_pascal_matrix_8():
        result = run([B_FILE_PATH], input='8', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1 1 2 1 1 3\n3 1 1 4 6 4 1 1\n5 10 10 5 1 1 6 15\n20 15 6 1 1 7 21 35\n35 21 7 1 1 8 28 56\n70 56 28 8 1 1 9 36\n84 126 126 84 36 9 1 1\n10 45 120 210 252 210 120 45'

    def test_pascal_matrix_9():
        result = run([B_FILE_PATH], input='9', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1 1 2 1 1 3 3\n1 1 4 6 4 1 1 5 10\n10 5 1 1 6 15 20 15 6\n1 1 7 21 35 35 21 7 1\n1 8 28 56 70 56 28 8 1\n1 9 36 84 126 126 84 36 9\n1 1 10 45 120 210 252 210 120\n45 10 1 1 11 55 165 330 462\n462 330 165 55 11 1 1 12 66'

    def test_pascal_matrix_10():
        result = run([B_FILE_PATH], input='10', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout == '1 1 1 1 2 1 1 3 3 1\n1 4 6 4 1 1 5 10 10 5\n1 1 6 15 20 15 6 1 1 7\n21 35 35 21 7 1 1 8 28 56\n70 56 28 8 1 1 9 36 84 126\n126 84 36 9 1 1 10 45 120 210\n252 210 120 45 10 1 1 11 55 165\n330 462 462 330 165 55 11 1 1 12\n66 220 495 792 924 792 495 220 66 12\n1 1 13 78 286 715 1287 1716 1716 1287'

if __name__ == "__main__":
    pytest.main()
