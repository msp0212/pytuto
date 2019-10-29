import os
import os.path
import zipfile

def extract_zip(zip_name, target_path):
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    with zipfile.ZipFile(zip_name) as zf:
        zf.extractall(target_path)


extract_zip('__src.zip', target_path=r'D:\Work\pytest')