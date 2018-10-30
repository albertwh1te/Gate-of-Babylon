def write_file(file_string, filepath):
    with open(filepath, 'wb+') as destination:
        destination.write(file_string.encode('utf-8'))


def main():
    test_flie_string = ""
    with open('test.py', 'r') as f:
        test_flie_string = f.read()
        print(type(test_flie_string), test_flie_string)
    write_file(test_flie_string, 'test2.py')


if __name__ == '__main__':
    main()
