def write_results(file_name, results):
    with open(file_name, 'w') as file:
        file.writelines([r + '\n' for r in results])