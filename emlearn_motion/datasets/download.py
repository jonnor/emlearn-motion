
import os.path

from . import uci_har, pamap2

DOWNLOADERS={
    'uci_har': uci_har.download_and_pack,
    'pamap2': pamap2.download_and_pack,
}

def download_dataset(name, raw_path, processed_path):

    packed_path = os.path.join(processed_path, f'{name}.parquet')
    if os.path.exists(packed_path):
        print(f'Packed file already exists: {packed_path}')
        return False

    download = DOWNLOADERS[name]
    download(raw_path, packed_path)

    return True

def parse():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', default=None, required=True)
    parser.add_argument('--raw-path', default='data/raw/')
    parser.add_argument('--processed-path', default='data/processed/')

    args = parser.parse_args()
    return args

def main():
    args = parse()
    download_dataset(args.dataset, args.raw_path, args.processed_path)


if __name__ == '__main__':
    main()
