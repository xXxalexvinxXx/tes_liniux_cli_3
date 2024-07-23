import subprocess

def checkout(cmd, text):
    """
        Функция для выполнения командной строки и проверки выходного текста положительный сценарий.

        Параметры:
        cmd (str): Команда для выполнения.
        text (str): Текст, который должен присутствовать в выходных данных для успешного выполнения.

        Возвращает:
        bool: True, если команда выполнена успешно и текст найден в выходных данных, иначе False.
        """
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def getout(cmd):
    #return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout