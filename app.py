# pyrefly: ignore [missing-import]
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
        return jsonify({"error": "Invalid session, please register again"}), 401
        
    data = request.json
    answers = data.get('answers', [])
    
    if len(answers) != 10:
        return jsonify({"error": "Incomplete answer data"}), 400

    # 1. Hitung Total Score PSS-10 Konvensional
    reverse_indices = [3, 4, 6, 7]
    total_score = 0
    adjusted_answers = []

    for i, score in enumerate(answers):
        if i in reverse_indices:
            adjusted_val = 4 - score
            total_score += adjusted_val
            adjusted_answers.append(adjusted_val)
        else:
            total_score += score
            adjusted_answers.append(score)

    # 2. Sistem Pakar Certainty Factor (CF)
    cf_experts = [
        0.41, # PSS 1
        0.54, # PSS 2
        0.46, # PSS 3
        0.33, # PSS 4 (Reverse)
        0.42, # PSS 5 (Reverse)
        0.61, # PSS 6
        0.59, # PSS 7 (Reverse)
        0.72, # PSS 8 (Reverse)
        0.77, # PSS 9
        0.63  # PSS 10
    ]

    gejala_text = [
        "being upset because of something that happened unexpectedly (PSS 1)",
        "feeling unable to control the important things in your life (PSS 2)",
        "feeling nervous and stressed (PSS 3)",
        "lacking confidence in your ability to handle personal problems (PSS 4)",
        "feeling that things were not going your way (PSS 5)",
        "feeling unable to cope with all the things you had to do (PSS 6)",
        "inability to control irritations in your life (PSS 7)",
        "feeling unable to stay on top of things (PSS 8)",
        "being angered because of things outside of your control (PSS 9)",
        "feeling difficulties were piling up so high that you could not overcome them (PSS 10)"
    ]

    cf_combine = 0.0
    max_cf_evidence = -1.0
    dominant_symptom_idx = -1

    for i in range(10):
        # Konversi ke CF User (0-4 -> 0.0 - 1.0)
        cf_user = adjusted_answers[i] / 4.0
        
        # Hitung CF Evidence
        cf_evidence = cf_user * cf_experts[i]

        # Update Gejala Dominan
        if cf_evidence > max_cf_evidence:
            max_cf_evidence = cf_evidence
            dominant_symptom_idx = i

        # CF Kombinasi
        cf_combine = cf_combine + cf_evidence * (1 - cf_combine)

    cf_percentage = round(cf_combine * 100, 2)
    dominant_symptom_text = f"Your dominant symptom is {gejala_text[dominant_symptom_idx]}."

    # Kategori Stres PSS-10
    kategori = ""
    if total_score <= 14:
        kategori = "Low Stress"
    elif total_score <= 26:
        kategori = "Moderate Stress"
    else:
        kategori = "High Stress"

    # Simpan hasil di session
    session['score'] = total_score
    session['category'] = kategori
    session['answers'] = answers
    session['cf_percentage'] = cf_percentage
    session['dominant_symptom'] = dominant_symptom_text

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
    cf_percentage = session.get('cf_percentage')
    dominant_symptom = session.get('dominant_symptom')
    
    return render_template('result.html', name=user_name, score=score, category=category, cf_percentage=cf_percentage, dominant_symptom=dominant_symptom)

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
    cf_percentage = session.get('cf_percentage')
    dominant_symptom = session.get('dominant_symptom')
    
    return render_template('print.html', 
        name=user_name, score=score, category=category, 
        age=user_age, gender=user_gender, date=user_date, answers=answers,
        cf_percentage=cf_percentage, dominant_symptom=dominant_symptom)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
