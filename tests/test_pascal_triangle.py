from subprocess import run, PIPE
import os
import os.path
import pytest

B_FILE_PATH = './bin/pascal_triangle'

def test_bin_folder_contains_pascal_triangle():
    assert os.path.isfile(B_FILE_PATH)

def test_pascal_triangle_not_correct_input_1():
    result = run([B_FILE_PATH], input='-1', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_pascal_triangle_not_correct_input_2():
    result = run([B_FILE_PATH], input='31', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_pascal_triangle_not_correct_input_3():
    result = run([B_FILE_PATH], input='a', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_pascal_triangle_not_correct_input_4():
    result = run([B_FILE_PATH], input='0', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_pascal_triangle_1():
    result = run([B_FILE_PATH], input='1', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1'

def test_pascal_triangle_2():
    result = run([B_FILE_PATH], input='2', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 1'

def test_pascal_triangle_3():
    result = run([B_FILE_PATH], input='3', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 2 1'

def test_pascal_triangle_4():
    result = run([B_FILE_PATH], input='4', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 3 3 1'

def test_pascal_triangle_5():
    result = run([B_FILE_PATH], input='5', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 4 6 4 1'

def test_pascal_triangle_6():
    result = run([B_FILE_PATH], input='6', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 5 10 10 5 1'

def test_pascal_triangle_7():
    result = run([B_FILE_PATH], input='7', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 6 15 20 15 6 1'

def test_pascal_triangle_8():
    result = run([B_FILE_PATH], input='8', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 7 21 35 35 21 7 1'

def test_pascal_triangle_9():
    result = run([B_FILE_PATH], input='9', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 8 28 56 70 56 28 8 1'

def test_pascal_triangle_10():
    result = run([B_FILE_PATH], input='10', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 9 36 84 126 126 84 36 9 1'

def test_pascal_triangle_11():
    result = run([B_FILE_PATH], input='11', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 10 45 120 210 252 210 120 45 10 1'

def test_pascal_triangle_12():
    result = run([B_FILE_PATH], input='12', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 11 55 165 330 462 462 330 165 55 11 1'

def test_pascal_triangle_13():
    result = run([B_FILE_PATH], input='13', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 12 66 220 495 792 924 792 495 220 66 12 1'

def test_pascal_triangle_14():
    result = run([B_FILE_PATH], input='14', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 13 78 286 715 1287 1716 1716 1287 715 286 78 13 1'

def test_pascal_triangle_15():
    result = run([B_FILE_PATH], input='15', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 14 91 364 1001 2002 3003 3432 3003 2002 1001 364 91 14 1'

def test_pascal_triangle_16():
    result = run([B_FILE_PATH], input='16', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 15 105 455 1365 3003 5005 6435 6435 5005 3003 1365 455 105 15 1'

def test_pascal_triangle_17():
    result = run([B_FILE_PATH], input='17', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 16 120 560 1820 4368 8008 11440 12870 11440 8008 4368 1820 560 120 16 1'

def test_pascal_triangle_18():
    result = run([B_FILE_PATH], input='18', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 17 136 680 2380 6188 12376 19448 24310 24310 19448 12376 6188 2380 680 136 17 1'

def test_pascal_triangle_19():
    result = run([B_FILE_PATH], input='19', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 18 153 816 3060 8568 18564 31824 43758 48620 43758 31824 18564 8568 3060 816 153 18 1'

def test_pascal_triangle_20():
    result = run([B_FILE_PATH], input='20', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 19 171 969 3876 11628 27132 50388 75582 92378 92378 75582 50388 27132 11628 3876 969 171 19 1'

def test_pascal_triangle_21():
    result = run([B_FILE_PATH], input='21', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 20 190 1140 4845 15504 38760 77520 125970 167960 184756 167960 125970 77520 38760 15504 4845 1140 190 20 1'

def test_pascal_triangle_22():
    result = run([B_FILE_PATH], input='22', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 21 210 1330 5985 20349 54264 116280 203490 293930 352716 352716 293930 203490 116280 54264 20349 5985 1330 210 21 1'

def test_pascal_triangle_23():
    result = run([B_FILE_PATH], input='23', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 22 231 1540 7315 26334 74613 170544 319770 497420 646646 705432 646646 497420 319770 170544 74613 26334 7315 1540 231 22 1'

def test_pascal_triangle_24():
    result = run([B_FILE_PATH], input='24', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 23 253 1771 8855 33649 100947 245157 490314 817190 1144066 1352078 1352078 1144066 817190 490314 245157 100947 33649 8855 1771 253 23 1'

def test_pascal_triangle_25():
    result = run([B_FILE_PATH], input='25', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 24 276 2024 10626 42504 134596 346104 735471 1307504 1961256 2496144 2704156 2496144 1961256 1307504 735471 346104 134596 42504 10626 2024 276 24 1'

def test_pascal_triangle_26():
    result = run([B_FILE_PATH], input='26', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 25 300 2300 12650 53130 177100 480700 1081575 2042975 3268760 4457400 5200300 5200300 4457400 3268760 2042975 1081575 480700 177100 53130 12650 2300 300 25 1'

def test_pascal_triangle_27():
    result = run([B_FILE_PATH], input='27', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 26 325 2600 14950 65780 230230 657800 1562275 3124550 5311735 7726160 9657700 10400600 9657700 7726160 5311735 3124550 1562275 657800 230230 65780 14950 2600 325 26 1'

def test_pascal_triangle_28():
    result = run([B_FILE_PATH], input='28', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 27 351 2925 17550 80730 296010 888030 2220075 4686825 8436285 13037895 17383860 20058300 20058300 17383860 13037895 8436285 4686825 2220075 888030 296010 80730 17550 2925 351 27 1'

def test_pascal_triangle_29():
    result = run([B_FILE_PATH], input='29', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 28 378 3276 20475 98280 376740 1184040 3108105 6906900 13123110 21474180 30421755 37442160 40116600 37442160 30421755 21474180 13123110 6906900 3108105 1184040 376740 98280 20475 3276 378 28 1'

def test_pascal_triangle_30():
    result = run([B_FILE_PATH], input='30', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 29 406 3654 23751 118755 475020 1560780 4292145 10015005 20030010 34597290 51895935 67863915 77558760 77558760 67863915 51895935 34597290 20030010 10015005 4292145 1560780 475020 118755 23751 3654 406 29 1'

if __name__ == "__main__":
    pytest.main()
