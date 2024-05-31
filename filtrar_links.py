import csv
import re
import os

def filtrar_links(input_csv, output_csv):
    padrao_link_imagem = re.compile(r'(https?://[^\s]+?\.(?:jpg|jpeg|png))[^|]*')
    
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        leitor = csv.reader(infile)
        escritor = csv.writer(outfile)
        
        for linha in leitor:
            linha_filtrada = []
            for celula in linha:
                links_imagem = padrao_link_imagem.findall(celula)
                linha_filtrada.append(';'.join(links_imagem))
            
            escritor.writerow(linha_filtrada)
            
input_csv = r'C:\Users\erics\Program\codigo_p_links.csv\arquivo.csv\planilha.csv.csv'
output_csv = r'C:\Users\erics\Program\codigo_p_links.csv\arquivo.csv\planilha_filtrada.csv'

if not os.path.isfile(input_csv):
    print(f"Erro: O arquivo '{input_csv}' não foi encontrado.")
else:

    filtrar_links(input_csv, output_csv)
    print(f"Arquivo filtrado salvo em '{output_csv}'.")
