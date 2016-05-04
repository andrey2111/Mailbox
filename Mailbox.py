input_file_name = 'unix.mailbox'
opened_files = {} #словарь открытых файлов {email: объект файла с этим email}

inf = open(input_file_name, 'r')
opened_files[input_file_name] = inf #открытие входного файла на чтение и добавление его в словарь

for line in inf:
    if line.startswith("From "): #Если строка начинается с From
        email = line.split(maxsplit=2)[1] #email отправителя
        if email not in opened_files: #если файл с именем email не открыт, его необходимо открыть
            ouf = open(email, 'w')
            opened_files[email] = ouf #добавляем открытый файл в словарь

    opened_files[email].write(line) #запись строки в соответствующий файл

for file in opened_files.values():
    file.close() #закрытие всех открытых файлов
