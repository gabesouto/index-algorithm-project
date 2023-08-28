def exists_word(word, queue_instance):
    search_results = []

    for index in range(len(queue_instance)):
        file_info = queue_instance.search(index)
        lines_with_word = []

        for line_number, line in enumerate(file_info['linhas_do_arquivo'], start=1):
            if word.lower() in line.lower(): 
                lines_with_word.append({"linha": line_number})

        if lines_with_word:
            result = {
                "palavra": word,
                "arquivo": file_info['nome_do_arquivo'],
                "ocorrencias": lines_with_word
            }
            search_results.append(result)

    return search_results

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
