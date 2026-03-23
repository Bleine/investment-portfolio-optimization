from extract import extract
from transform import transform
from load import load


def main():
    extract()
    transform()
    load()


if __name__ == '__main__':
    main()
