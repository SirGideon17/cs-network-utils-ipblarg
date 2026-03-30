FILE_NAME="test.bin"

def to_bin(var):
    print("Writing var to disk in binary format")
    with open(FILE_NAME, "wb") as f:
        f.write(var.to_bytes(2, byteorder='big'))

def from_bin():
    print("Reading binary file to memory")
    with open(FILE_NAME) as f:
        binary = f.read().encode("utf-8")
        return int.from_bytes(binary, byteorder='big')

def main():
    to_bin(11)
    var = from_bin()
    print(var)


if __name__ == "__main__":
    main()
