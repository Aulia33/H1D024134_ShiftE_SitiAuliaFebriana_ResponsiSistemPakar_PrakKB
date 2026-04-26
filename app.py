from flask import Flask, render_template, request

app = Flask(__name__)


def sistem_pakar(tujuan, kondisi, aktivitas, waktu, preferensi):
    alasan = []

    if tujuan == "turun_berat" and kondisi == "berlebih":
        kategori = "Program Penurunan Berat Badan"
        menu_pagi = "Oatmeal + pisang + air putih"
        menu_siang = "Nasi merah + dada ayam + sayur rebus"
        menu_malam = "Sup sayur + telur rebus / tahu"

        if aktivitas == "rendah":
            olahraga = "Jalan cepat 30 menit, 3–4 kali seminggu."
        else:
            olahraga = "Jogging 30–45 menit + bodyweight workout ringan."

        alasan.append("Tujuan pengguna adalah menurunkan berat badan.")
        alasan.append("Kondisi tubuh berlebih, sehingga menu diarahkan lebih rendah kalori.")

    elif tujuan == "jaga_berat" and kondisi == "normal":
        kategori = "Program Menjaga Berat Badan"
        menu_pagi = "Roti gandum + telur + buah"
        menu_siang = "Nasi + ayam/ikan + sayur"
        menu_malam = "Tumis sayur + tempe/tahu"
        olahraga = "Cardio ringan dan latihan otot 3 kali seminggu."
        alasan.append("Kondisi tubuh normal dan tujuan adalah menjaga berat badan.")

    elif tujuan == "naik_massa" and kondisi == "kurus":
        kategori = "Program Menaikkan Massa Tubuh"
        menu_pagi = "Nasi + telur + susu"
        menu_siang = "Nasi + ayam/ikan + tempe + sayur"
        menu_malam = "Kentang/nasi + protein tinggi + sayur"

        if waktu in ["cukup", "banyak"]:
            olahraga = "Strength training 30–45 menit."
        else:
            olahraga = "Latihan singkat 15–20 menit: push-up, squat, plank."

        alasan.append("Kondisi tubuh kurus dan tujuan adalah menaikkan massa tubuh.")

    elif tujuan == "naik_massa" and preferensi == "tinggi_protein":
        kategori = "Program Tinggi Protein"
        menu_pagi = "Telur + roti gandum + susu"
        menu_siang = "Nasi + dada ayam + tempe + sayur"
        menu_malam = "Ikan/telur + kentang + sayur"
        olahraga = "Latihan beban/bodyweight 4 kali seminggu."
        alasan.append("Preferensi tinggi protein cocok untuk peningkatan massa otot.")

    else:
        kategori = "Program Seimbang"
        menu_pagi = "Oatmeal / roti gandum + telur"
        menu_siang = "Nasi + lauk protein + sayur"
        menu_malam = "Sayur + tahu/tempe + buah"
        olahraga = "Jalan santai, jogging ringan, atau workout 20–30 menit."
        alasan.append("Kombinasi kondisi tidak masuk rule khusus, maka sistem memberi rekomendasi seimbang.")

    if preferensi == "hemat":
        menu_pagi += " (opsi hemat: telur/tempe)"
        menu_siang += " (opsi hemat: tahu/tempe/telur)"
        menu_malam += " (opsi hemat: tahu/tempe)"
        alasan.append("Preferensi hemat membuat sistem memilih bahan yang mudah dan murah.")

    elif preferensi == "tinggi_protein":
        menu_pagi += " + tambahan telur"
        menu_siang += " + tambahan protein"
        menu_malam += " + tambahan tahu/tempe"
        alasan.append("Preferensi tinggi protein membuat sistem menambahkan sumber protein.")

    return {
        "kategori": kategori,
        "menu_pagi": menu_pagi,
        "menu_siang": menu_siang,
        "menu_malam": menu_malam,
        "olahraga": olahraga,
        "alasan": alasan
    }


@app.route("/")
def home():
    return render_template("index.html", page="home", hasil=None)


@app.route("/konsultasi", methods=["GET", "POST"])
def konsultasi():
    hasil = None

    if request.method == "POST":
        hasil = sistem_pakar(
            request.form["tujuan"],
            request.form["kondisi"],
            request.form["aktivitas"],
            request.form["waktu"],
            request.form["preferensi"]
        )

    return render_template("index.html", page="konsultasi", hasil=hasil)


if __name__ == "__main__":
    app.run(debug=True, port=5002)