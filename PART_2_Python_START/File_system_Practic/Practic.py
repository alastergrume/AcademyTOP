def pars_bad_word():
    """
    ��� ��������� ����. ���������� ������� ����� ����
    ����� �� ���� ��� ������������ �����. ������ ������������ ���� ��������� � ������ �����.

    1. ������� file_1 �� ������
    2. �������� �� ���� ������
    2.1 ��������� i � ����������
    3. ��� ����������� ���������� i c ���������� � ����� bad_words �������
    4. ������������ ��������� ���� ������ �������
    """
    with open("file_1.txt", 'r') as new_file_1:
        content = new_file_1.read()
        print(content)

    

if __name__ == "__main__":
    pars_bad_word()