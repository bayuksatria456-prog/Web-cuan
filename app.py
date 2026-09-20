from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    teks = ""
    if request.method == 'POST':
        teks = request.form.get('teks', '')
        aksi = request.form.get('action', '')
        
        if aksi == 'hitung':
            char_count = len(teks)
            word_count = len(teks.split())
            hasil = f"Jumlah Karakter: {char_count} | Jumlah Kata: {word_count}"
        elif aksi == 'rapih':
            hasil = " ".join(teks.split())
            
    return render_template('index.html', hasil=hasil, teks_asal=teks)

@app.route('/convert', methods=['POST'])
def convert_text():
    teks = request.form.get('teks', '')
    tipe = request.form.get('tipe', 'upper')
    
    if tipe == 'upper':
        hasil = teks.upper()
    elif tipe == 'lower':
        hasil = teks.lower()
    elif tipe == 'title':
        hasil = teks.title()
    else:
        hasil = teks
        
    return render_template('index.html', hasil_convert=hasil, teks_asal=teks)

@app.route('/replace', methods=['POST'])
def replace_text():
    teks = request.form.get('teks', '')
    cari = request.form.get('cari', '')
    ganti = request.form.get('ganti', '')
    
    hasil = teks.replace(cari, ganti)
    return render_template('index.html', hasil_replace=hasil, teks_asal=teks, cari=cari, ganti=ganti)

@app.route('/remove-empty', methods=['POST'])
def remove_empty_lines():
    teks = request.form.get('teks', '')
    lines = teks.splitlines()
    non_empty_lines = [line for line in lines if line.strip() != ""]
    hasil = "\n".join(non_empty_lines)
    
    return render_template('index.html', hasil_empty=hasil, teks_asal=teks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

