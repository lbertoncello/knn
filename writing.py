#Escreve as classes, cada uma em uma linha
def write_results(file_name, results):
    with open(file_name, 'w') as file:
        file.writelines([str(r) + '\n' for r in results])

#Escreve as classes, cada uma em uma linha
def write_classes(file_name, classes):
    write_results(file_name, classes)

#Escreve um np.array em formato csv
def write_csv(file_name, content, delimiter):
    with open(file_name, 'w') as f:
        for c in content:
            f.write("%s\n" % str(delimiter.join(map(str, c.astype(np.float)))))