import tkinter as tk


def hex_to_int(hex_str):

    digits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    return digits.index(hex_str[0]) * 16 + digits.index(hex_str[1])


def decode_url(encoded_url):

    byte_array = bytearray()
    i = 0

    while i < len(encoded_url):
        if encoded_url[i] == '%' and i + 2 < len(encoded_url):
            hex_code = encoded_url[i + 1:i + 3]
            byte_array.append(hex_to_int(hex_code))
            i += 3
        else:
            byte_array.extend(encoded_url[i].encode('utf-8'))
            i += 1

    return byte_array.decode('utf-8')


def copy_to_clipboard(text):
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()


def main():
    print("Введіть інтернет-посилання у закодованому форматі:")
    encoded_url = input().strip()

    decoded_url = decode_url(encoded_url)

    print("\nРозкодоване посилання:")
    print(decoded_url)

    copy_to_clipboard(decoded_url)
    print("\nПосилання скопійовано в буфер обміну.")


if __name__ == "__main__":
    main()