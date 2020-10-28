from gendiff import generate_diff


def test_generate_diff():
    result = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True\n}'''
    first_file, second_file = 'gendiff/tests/fixtures/file1.json', 'gendiff/tests/fixtures/file2.json'
    assert generate_diff(first_file, second_file) == result
