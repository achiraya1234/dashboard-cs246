import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

df = pd.read_csv('https://raw.githubusercontent.com/achiraya1234/dashboard-cs246/main/finalproject%20-%20Form%20Responses%201.csv')

#from google.colab import drive
#drive.mount('/content/drive')

#df = pd.read_csv('/content/drive/MyDrive/CS/CS246/finalproject - Form Responses 1.csv')

df = df.rename(columns={'1. สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1': 'สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1',
                        '2. สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2': 'สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2',
                        '3. สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3': 'สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3'})

df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1']

df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1'].value_counts()

a1 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1'].value_counts()['ด้านการเดินทางและความปลอดภัย']
b1 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1'].value_counts()['ด้านการศึกษา']
c1 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1'].value_counts()['ด้านสุขภาพ']
d1 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1'].value_counts()['ด้านสิ่งแวดล้อม']

a2 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2'].value_counts()['ด้านการเดินทางและความปลอดภัย']
b2 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2'].value_counts()['ด้านการศึกษา']
c2 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2'].value_counts()['ด้านสุขภาพ']
d2 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2'].value_counts()['ด้านสิ่งแวดล้อม']

a3 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3'].value_counts()['ด้านการเดินทางและความปลอดภัย']
b3 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3'].value_counts()['ด้านการศึกษา']
c3 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3'].value_counts()['ด้านสุขภาพ']
d3 = df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3'].value_counts()['ด้านสิ่งแวดล้อม']

#df['สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1'].value_counts()['ด้านการเดินทางและความปลอดภัย']

# สร้าง DataFrame จากข้อมูลของคุณ
data = {
    'Categories': ['การเดินทางและความปลอดภัย', 'การศึกษา', 'สุขภาพ', 'สิ่งแวดล้อม'],
    'Rank 1': [a1, b1, c1, d1],
    'Rank 2': [a2, b2, c2, d2],
    'Rank 3': [a3, b3, c3, d3]
}
df30 = pd.DataFrame(data)

# สร้าง Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df30.set_index('Categories'), cmap='YlGnBu', annot=True, fmt="d", linewidths=.5)
plt.title('Heatmap of Categories by Rank')
plt.xlabel('Rank')
plt.ylabel('Categories')
plt.show()
