import pandas as pd
import numpy as np

np.random.seed(42)

jurusans = ['Sistem Informasi', 'Manajemen', 'Teknik Informatika', 'Akuntansi', 'Ilmu Komunikasi']
jurusan_prob = [0.25, 0.25, 0.20, 0.15, 0.15]

semesters = list(range(1, 9))
semester_prob = [0.18, 0.16, 0.15, 0.14, 0.12, 0.10, 0.08, 0.07]

data = []
for i in range(1000):
    jurusan = np.random.choice(jurusans, p=jurusan_prob)
    semester = int(np.random.choice(semesters, p=semester_prob))
    base_age = 17 + (semester - 1) * 0.6
    usia = int(np.clip(np.random.normal(loc=base_age + 0.8, scale=0.8), 17, 25))
    ipk = round(float(np.clip(np.random.normal(loc=3.35, scale=0.38), 1.80, 4.00)), 2)
    
    data.append({
        'NIM': f"2024{1000 + i}",
        'Jurusan': jurusan,
        'Semester': semester,
        'IPK': ipk,
        'Usia': usia
    })

df = pd.DataFrame(data)
df.to_csv('dataset_mahasiswa_1000.csv', index=False)
print("Data sintesis 1.000 mahasiswa berhasil dibuat!")
