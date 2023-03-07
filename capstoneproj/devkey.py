def decrypt(text):
    decoded = []
    for character in text:
        decoded.append(chr(ord(character) - 3))
    if decoded[-1] == "\x07":
        decoded.pop(-1)
    return "".join(decoded)

def encrypt(text):
    text3 = []
    for character in text:
        text3.append(chr(ord(character) + 3))
    return "".join(text3)

def decrypt_keystore():
    keystore = {}
    with open("keystore.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            keystore[decrypt(lines[i+0])] = [decrypt(lines[i + 1]), decrypt(lines[i + 2])]
        return keystore

def add_to_keystore(original_keystore, names):
    if names[0] == "Q": return original_keystore
    keystore = {}
    for k, v in original_keystore.items():
        keystore[encrypt(k)] = [encrypt(v[0]), encrypt(v[1])]
    for name in names:
        n = name.split()
        keystore[encrypt(n[0])] = [encrypt(n[1]), encrypt(n[2])]
    with open("keystore.txt", "w") as file:
        lines_to_write = []
        for k, v in keystore.items():
            lines_to_write.append(f"{k}\n")
            lines_to_write.append(f"{v[0]}\n")
            lines_to_write.append(f"{v[1]}\n")
        file.writelines(lines_to_write)


if __name__ == "__main__":
    add_to_keystore(decrypt_keystore(), input().split("~"))

