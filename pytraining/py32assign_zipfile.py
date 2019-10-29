import zipfile
import glob

def make_archive(archive_name, *args):
    with zipfile.ZipFile(archive_name, mode='w') as zf:
        for file_name in args:
            zf.write(file_name)
            print(f'{file_name} added')

make_archive('__src.zip', *glob.glob('*.py'))