from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os

app = Flask(__name__)
# Gunakan secret_key agar fitur session Flask bisa bekerja (untuk menyimpan nama tanpa database)
app.secret_key = os.urandom(24) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            session['user_name'] = name
            session['user_age'] = request.form.get('age')
            session['user_gender'] = request.form.get('gender')
            session['user_date'] = request.form.get('date')
            return redirect(url_for('test'))
    return render_template('register.html')

@app.route('/test')
def test():
    # Pastikan user sudah registrasi
    if 'user_name' not in session:
        return redirect(url_for('register'))
    return render_template('test.html')

@app.route('/api/calculate-score', methods=['POST'])
def calculate_score():
    if 'user_name' not in session:
        return jsonify({"error": "Sesi tidak valid, silakan registrasi ulang"}), 401
        
    data = request.json
    answers = data.get('answers', [])
    
    if len(answers) != 10:
        return jsonify({"error": "Data jawaban tidak lengkap"}), 400

    # Pertanyaan ke-4, 5, 7, 8 adalah pertanyaan positif (perlu di-reverse)
    # Index array mulai dari 0, jadi item ke-4 adalah index 3
    reverse_indices = [3, 4, 6, 7]
    total_score = 0

    for i, score in enumerate(answers):
        if i in reverse_indices:
            # Skoring terbalik: 0 jadi 4, 1 jadi 3, 2 jadi 2, 3 jadi 1, 4 jadi 0
            total_score += (4 - score)
        else:
            total_score += score

    # Kategori Stres PSS-10
    kategori = ""
    if total_score <= 13:
        kategori = "Rendah"
    elif total_score <= 26:
        kategori = "Sedang"
    else:
        kategori = "Tinggi"

    # Simpan hasil di session
    session['score'] = total_score
    session['category'] = kategori
    session['answers'] = answers

    # Berikan respons ke client bahwa sukses dan URL untuk redirect
    return jsonify({
        "success": True, 
        "redirect_url": url_for('result')
    })

@app.route('/result')
def result():
    if 'score' not in session or 'user_name' not in session:
        return redirect(url_for('register'))
        
    # Ambil data dari session untuk di-render di HTML
    user_name = session.get('user_name')
    score = session.get('score')
    category = session.get('category')
    
    return render_template('result.html', name=user_name, score=score, category=category)

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/print')
def print_page():
    # Menampilkan hasil saat halaman di-print
    if 'score' not in session or 'user_name' not in session:
        return redirect(url_for('register'))
        
    user_name = session.get('user_name')
    score = session.get('score')
    category = session.get('category')
    user_age = session.get('user_age')
    user_gender = session.get('user_gender')
    user_date = session.get('user_date')
    answers = session.get('answers')
    
    return render_template('print.html', 
        name=user_name, score=score, category=category, 
        age=user_age, gender=user_gender, date=user_date, answers=answers)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
