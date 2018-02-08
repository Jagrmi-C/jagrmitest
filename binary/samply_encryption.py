# Samply encryption with XOR


def line_to_bin(data_str):
    bytes_object = data_str.encode(encoding='utf-8')
    value_int = int.from_bytes(bytes_object, byteorder='big')
    value_bin = bin(value_int)[2:]
    return value_bin.zfill(8 * ((len(value_bin) + 7) // 8))


def line_to_str(data_bin):
    data_int = int(data_bin, 2)
    lenght = (data_int.bit_length() + 7) // 8
    text = data_int.to_bytes(length=lenght, byteorder='big').decode(encoding='utf-8')
    return text

key = "faust"
initial_text = "Good evening!"

a = line_to_bin(data_str=initial_text)
print(a)
text = line_to_str(a)
print(text)
