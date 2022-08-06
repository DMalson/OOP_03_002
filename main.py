from ya_disk import YandexDisk

TOKEN = ''

if __name__ == '__main__':
    file_to_load = 'test1.txt'
    token = TOKEN
    ya = YandexDisk(token=token)
    ya.upload_file_to_disk('Netology/' + file_to_load,file_to_load)
    