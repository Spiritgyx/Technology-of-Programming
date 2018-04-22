import S_Z, shifr_c1
from Aes import aesNew


def main():
    while True:
        mode = input('Select mode:\nz - S_Z crypt\nc - Cezar\' crypt\na - AES\nq - quit\nMODE: ').lower()
        if mode == 'z':
            S_Z.main()
        elif mode == 'c':
            shifr_c1.main()
        elif mode == 'a':
            aesNew.main()
        elif mode == 'q':
            break
        else:
            print('Incorrect mode')
    pass


if __name__ == '__main__':
    main()
