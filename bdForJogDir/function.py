def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def photoInsert(photo):
    emp_photo = convert_to_binary_data(photo)
    return emp_photo

