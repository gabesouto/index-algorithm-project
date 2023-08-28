from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    lines = txt_importer(path_file)
    is_not_in_file = True

    for file in instance.qeue:
        if path_file == file["nome_do_arquivo"]:
            is_not_in_file = False

    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    if is_not_in_file:
        instance.enqueue(file_dict)

    print(file_dict)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso",
          file=sys.stdout)


def file_metadata(instance, index):
    if 0 <= index < len(instance):
        metadata = instance.search(index)
        print(metadata)
    else:
        print("Posição inválida", file=sys.stderr)
