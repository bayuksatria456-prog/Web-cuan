from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FormatTools - Multi Web Utilities</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 20px; }
        .container { max-width: 750px; margin: 0 auto; }
        .ad-space { background-color: #e9ecef; border: 2px dashed #adb5bd; text-align: center; padding: 15px; margin-bottom: 20px; color: #495057; border-radius: 6px; font-weight: bold; font-size: 14px; }
        .card { background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; border: 1px solid #e1e4e8; }
        .section-title { border-left: 5px solid #28a745; padding-left: 10px; color: #212529; margin-bottom: 15px; }
        textarea { width: 100%; box-sizing: border-box; padding: 12px; border: 1px solid #ced4da; border-radius: 6px; font-family: monospace; font-size: 14px; margin-bottom: 10px; resize: vertical; }
        button { background-color: #28a745; color: white; border: none; padding: 12px 20px; font-size: 14px; font-weight: bold; border-radius: 6px; cursor: pointer; }
        button:hover { background-color: #218838; }
        .hasil-box { padding: 15px; background-color: #e8f4fd; border: 1px solid #bee5eb; color: #0c5460; border-radius: 6px; font-family: monospace; margin-top: 15px; font-size: 14px; word-break: break-all; }
        .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 15px; }
        .info-stat { background: #e9ecef; padding: 10px; border-radius: 6px; text-align: center; font-weight: bold; }
        .info-box { background: #fff; padding: 15px; border-radius: 8px; border: 1px solid #e1e4e8; font-size: 13px; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="container">
        <!-- TEMPAT IKLAN ATAS -->
        <div class="ad-space">
            <!-- Taruh Script Iklan Kamu Di Sini Nanti -->
            Iklan Sponsor / Google AdSense (Banner Atas)
        </div>

        <div class="card">
            <h3 class="section-title">Fitur 1: Penghitung Kata & Karakter</h3>
            <form method="POST" action="/">
                <textarea name="teks_hitung" rows="4" placeholder="Ketik atau tempel teks di sini...">{{ inputan_hitung }}</textarea>
                <button type="submit" name="aksi" value="hitung">Hitung Sekarang</button>
            </form>
            {% if kata or karakter %}
            <div class="info-grid" style="margin-top: 15px;">
                <div class="info-stat">Total Kata: {{ kata }}</div>
                <div class="info-stat">Total Karakter: {{ karakter }}</div>
            </div>
            {% endif %}
        </div>

        <div class="card">
            <h3 class="section-title">Fitur 2: Perapih Teks (Text Formatter)</h3>
            <form method="POST" action="/">
                <textarea name="teks_rapi" rows="4" placeholder="Contoh: teks    berantakan   banyak    spasi...">{{ inputan_rapi }}</textarea>
                <button type="submit" name="aksi" value="rapikan">Rapikan Teks</button>
            </form>
            {% if hasil_rapi %}
            <div class="hasil-box" style="background-color: #d4edda; border-color: #c3e6cb; color: #155724;">
                <strong>Hasil Rapi:</strong><br><br>{{ hasil_rapi }}
            </div>
            {% endif %}
        </div>

        <!-- TEMPAT IKLAN BAWAH -->
        <div class="ad-space">
            <!-- Taruh Script Iklan Kamu Di Sini Nanti -->
            Iklan Sponsor / Google AdSense (Banner Bawah)
        </div>

        <div class="info-box">
            <strong>Halaman Informasi:</strong><br>
            <b>Tentang Kami:</b> Web multi-utilitas format data gratis.<br>
            <b>Kebijakan Privasi:</b> Data aman & langsung diproses tanpa disimpan.<br>
            <b>Hubungi Kami:</b> support@formattools.id
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    kata = karakter = hasil_rapi = ""
    inputan_hitung = inputan_rapi = ""
    if request.method == 'POST':
        aksi = request.form.get('aksi')
        if aksi == 'hitung':
            inputan_hitung = request.form.get('teks_hitung', '')
            kata = len(inputan_hitung.split())
            karakter = len(inputan_hitung)
        elif aksi == 'rapikan':
            inputan_rapi = request.form.get('teks_rapi', '')
            hasil_rapi = " ".join(inputan_rapi.split())
    return render_template_string(HTML, kata=kata, karakter=karakter, inputan_hitung=inputan_hitung, hasil_rapi=hasil_rapi, inputan_rapi=inputan_rapi)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

