import os
from datetime import datetime

def get_date(file):
    print(file)

    use_date = os.path.getmtime(file)
    use_date = datetime.fromtimestamp(use_date)
    use_date = str(use_date)[:7]

    print(use_date)
    return use_date

def org(dir):
    #print(dir)

    files = os.listdir(dir)

    #print(files)
    new_dir = ''

    for file in files:
        if os.path.isfile(os.path.join(dir, file)):

            use_date = get_date(file)
            new_dir = use_date


            if not os.path.isdir(use_date):
                os.mkdir(use_date)

            os.rename(os.path.join(dir, file), os.path.join(new_dir, file))

if __name__ == '__main__':
    org('.')
