from flask import Flask, render_template, request, send_from_directory
import os
import csv
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')  # Alterado para 'upload.html'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = 'planilha.csv'
        file_path = os.path.join(app.root_path, 'uploads', filename)
        file.save(file_path)
        filtered_file_path = os.path.join(app.root_path, 'processed', 'planilha_filtrada.csv')
        filtrar_links(file_path, filtered_file_path)
        return send_from_directory(directory=os.path.join(app.root_path, 'processed'), path='planilha_filtrada.csv', as_attachment=True)

def filtrar_links(input_csv, output_csv):
    padrao_link_imagem = re.compile(r'https.*?(?:\.jpg|\.jpeg|\.png)')
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        leitor = csv.reader(infile)
        escritor = csv.writer(outfile)
        for linha in leitor:
            linha_filtrada = []
            for celula in linha:
                links_imagem = padrao_link_imagem.findall(celula)
                linha_filtrada.append(';'.join(links_imagem))
            escritor.writerow(linha_filtrada)

if __name__ == '__main__':
    app.run(debug=True)
