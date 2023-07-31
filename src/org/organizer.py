import os

img = ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.jfif', '.raw']
vid = ['.mp4', '.mov', '.avi']
docs = ['.pdf', '.txt', '.doc', '.docx']
edit = ['.psd', '.prproj', '.eps', '.ai', '.svg']

def get_extension(file):
    # file.find(".")
    index = (file.rfind("."))
    extension = file[index:]
    print(extension)
    return extension

def org(dir):

    IMG_DIR = os.path.join(dir, "Imagens")
    VIDEO_DIR = os.path.join(dir, "Vídeos")
    DOCS_DIR = os.path.join(dir, "Documentos")
    EDIT_DIR = os.path.join(dir, "Arquivos Editáveis")
    OTHERS_DIR = os.path.join(dir, "Outros")
    CLONES_DIR = os.path.join(dir, "Duplicados")

    if not os.path.isdir(IMG_DIR):
        os.mkdir(IMG_DIR)
    if not os.path.isdir(VIDEO_DIR):
        os.mkdir(VIDEO_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(EDIT_DIR):
        os.mkdir(EDIT_DIR)
    if not os.path.isdir(OTHERS_DIR):
        os.mkdir(OTHERS_DIR)

    files = os.listdir(dir)
    new_dir = ''

    for file in files:
        if os.path.isfile(os.path.join(dir, file)):

            extension = str.lower(get_extension(file))
            if extension in img:
                new_dir = IMG_DIR
                print("=> Imagens")

            elif extension in vid:
                new_dir = VIDEO_DIR
                print("=> Vídeos")

            elif extension in docs:
                new_dir = DOCS_DIR
                print("=> Documentos")

            elif extension in edit:
                new_dir = EDIT_DIR
                print("=> Arquivos Editáveis")

            else:
                new_dir = OTHERS_DIR
                print("=> Outros")

            try:
                os.rename(os.path.join(dir, file), os.path.join(new_dir, file))

            except FileExistsError:
                print("Erro! Arquivo já existente no Destino.")

                if not os.path.isdir(CLONES_DIR):
                    os.mkdir(CLONES_DIR)
                new_dir = CLONES_DIR

                os.rename(os.path.join(dir, file), os.path.join(new_dir, file))
                print("=> Duplicados")

            print("")
    print("PRESSIONE QUALQUER TECLA PARA ENCERRAR:")
    input("")

if __name__ == '__main__':
    org("")
    # ..\..\..\Downloads
