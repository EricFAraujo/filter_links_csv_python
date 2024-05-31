# filter_links_csv_python
O script filtrar_links.py lê um arquivo CSV, filtra os links de imagens presentes nas células (com extensões .jpg, .jpeg, .png), e salva o resultado em um novo arquivo CSV. O script foi projetado para identificar e manter apenas os links de imagens, removendo o restante do texto.

Dependências
Este script utiliza os seguintes módulos da biblioteca padrão do Python:

csv: Para leitura e escrita de arquivos CSV.
re: Para operações com expressões regulares.
os: Para operações com o sistema de arquivos.
Funções
filtrar_links(input_csv, output_csv)
Esta função lê o arquivo CSV de entrada, filtra os links de imagens e escreve os links filtrados em um novo arquivo CSV.

Parâmetros
input_csv (str): O caminho para o arquivo CSV de entrada.
output_csv (str): O caminho para o arquivo CSV de saída.
Funcionamento
Abre o arquivo CSV de entrada para leitura.
Abre o arquivo CSV de saída para escrita.
Para cada linha no arquivo de entrada, busca links de imagens usando uma expressão regular.
Mantém apenas os links de imagens na linha filtrada.
Escreve a linha filtrada no arquivo de saída.
