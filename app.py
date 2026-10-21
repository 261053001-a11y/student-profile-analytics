import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Dashboard Profil Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# 2. Load Data Sintesis
@st.cache_data
def load_data():
    df = pd.read_csv('dataset_mahasiswa_1000.csv')
    return df

df = load_data()

# 3. Sidebar Filter
st.sidebar.title("🔍 Filter Profil Mahasiswa")

jurusan_list = ["Semua"] + list(df['Jurusan'].unique())
selected_jurusan = st.sidebar.selectbox("Pilih Jurusan", jurusan_list)

semester_list = ["Semua"] + sorted(list(df['Semester'].unique()))
selected_semester = st.sidebar.selectbox("Pilih Semester", semester_list)

# Filtering Data
filtered_df = df.copy()

if selected_jurusan != "Semua":
    filtered_df = filtered_df[filtered_df['Jurusan'] == selected_jurusan]

if selected_semester != "Semua":
    filtered_df = filtered_df[filtered_df['Semester'] == int(selected_semester)]

# 4. Header & Identitas
st.title("🎓 Dashboard Analisis Profil Mahasiswa")
st.caption("Bedah Kasus 2: Dataset Profil Mahasiswa (1.000 Data) | HUDZAIFAH AINI& 261053001	")
st.markdown("---")

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

total_mhs = len(filtered_df)
avg_ipk = filtered_df['IPK'].mean() if total_mhs > 0 else 0
avg_usia = filtered_df['Usia'].mean() if total_mhs > 0 else 0
total_jurusan = filtered_df['Jurusan'].nunique()

col1.metric("Total Mahasiswa", f"{total_mhs:,} Orang")
col2.metric("Rata-Rata IPK", f"{avg_ipk:.2f}")
col3.metric("Rata-Rata Usia", f"{avg_usia:.1f} Tahun")
col4.metric("Jumlah Jurusan", f"{total_jurusan}")

st.markdown("---")

# 5. Visualisasi Data (Sesuai Karakteristik Tipe Data)
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📊 Distribusi Mahasiswa per Semester")
    st.caption("Kategorik (Ordinal): Bar Chart Berurutan (1 -> 8)")
    df_sem = filtered_df.groupby('Semester')['NIM'].count().reset_index()
    df_sem.columns = ['Semester', 'Jumlah Mahasiswa']
    df_sem = df_sem.sort_values(by='Semester')
    fig_sem = px.bar(
        df_sem, 
        x='Semester', 
        y='Jumlah Mahasiswa',
        text='Jumlah Mahasiswa',
        title='Jumlah Mahasiswa per Tingkat Semester',
        color_discrete_sequence=['#2b5c8f']
    )
    fig_sem.update_xaxes(type='category')
    fig_sem.update_layout(template='plotly_white')
    st.plotly_chart(fig_sem, use_container_width=True)

with row1_col2:
    st.subheader("🍰 Proporsi Mahasiswa per Jurusan")
    st.caption("Kategorik (Nominal): Pie Chart")
    df_jur = filtered_df.groupby('Jurusan')['NIM'].count().reset_index()
    df_jur.columns = ['Jurusan', 'Jumlah Mahasiswa']
    fig_jur = px.pie(
        df_jur, 
        names='Jurusan', 
        values='Jumlah Mahasiswa',
        hole=0.4,
        title='Persentase Mahasiswa Berdasarkan Jurusan',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_jur.update_layout(template='plotly_white')
    st.plotly_chart(fig_jur, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("🔔 Distribusi IPK Mahasiswa")
    st.caption("Numerik (Kontinu): Histogram")
    fig_hist_ipk = px.histogram(
        filtered_df, 
        x='IPK', 
        nbins=20,
        title='Distribusi Nilai IPK',
        color_discrete_sequence=['#41b6c4']
    )
    fig_hist_ipk.update_layout(template='plotly_white')
    st.plotly_chart(fig_hist_ipk, use_container_width=True)

with row2_col2:
    st.subheader("📦 Sebaran & Outlier Usia dan IPK")
    st.caption("Numerik (Kontinu): Box Plot")
    tab1, tab2 = st.tabs(["Box Plot IPK", "Box Plot Usia"])
    with tab1:
        fig_box_ipk = px.box(
            filtered_df, 
            y='IPK', 
            x='Jurusan',
            color='Jurusan',
            title='Box Plot Distribusi IPK per Jurusan'
        )
        fig_box_ipk.update_layout(template='plotly_white')
        st.plotly_chart(fig_box_ipk, use_container_width=True)
    with tab2:
        fig_box_usia = px.box(
            filtered_df, 
            y='Usia', 
            x='Semester',
            color_discrete_sequence=['#e6550d'],
            title='Box Plot Sebaran Usia per Semester'
        )
        fig_box_usia.update_xaxes(type='category')
        fig_box_usia.update_layout(template='plotly_white')
        st.plotly_chart(fig_box_usia, use_container_width=True)

# 6. Tabel Data Interaktif
st.markdown("---")
st.subheader("📄 Raw Data Profil Mahasiswa")
st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "NIM": st.column_config.TextColumn("NIM"),
        "Jurusan": st.column_config.TextColumn("Jurusan"),
        "Semester": st.column_config.NumberColumn("Semester", format="%d"),
        "IPK": st.column_config.NumberColumn("IPK", format="%.2f"),
        "Usia": st.column_config.NumberColumn("Usia (Thn)", format="%d Thn")
    }
)