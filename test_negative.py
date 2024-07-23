from utils import checkout
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

# folder_in = "/home/user/tst"  # Папка с файлами для архивации
# folder_out = "/home/user/out"  # Папка для сохранения архива
# folder_ext = "/home/user/folder1"  # Папка для распаковки файлов
# broken_archive = "corrupted.7z"  # Имя поврежденного архива
class TestNegative:

    def test_step1_negative(self, clear_folders, make_bad_arx):
    # Негативный тест для распаковки поврежденного архива
    # assert checkout(f"cd {folder_out}; 7z e {broken_archive} -o{folder_ext} -y", "Everything is Ok"), "test_step1_negative FAIL"
        assert not checkout('cd {}; 7z e {} -o -y'.format(data['folder_out'], data['broken_archive'], data['folder_ext']), 'test_step1_negative FAIL')

    def test_step2_negative(self, clear_folders, make_bad_arx):
    # Негативный тест для проверки поврежденного архива
    # assert not checkout(f"cd {folder_out}; 7z t {broken_archive}", "Everything is Ok"), "test_step2_negative FAIL"
        assert not checkout('cd {}; 7z t {}'.format(data['folder_out'], data['broken_archive']), "Everything is Ok"), "test_step2_negative FAIL"
