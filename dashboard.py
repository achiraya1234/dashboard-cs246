import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

df = pd.read_csv('https://raw.githubusercontent.com/achiraya1234/dashboard-cs246/main/finalproject%20-%20Form%20Responses%201.csv')

df = df.rename(columns={'1. สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1': 'สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 1',
                        '2. สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2': 'สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 2',
                        '3. สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3': 'สวัสดิการและสิ่งอำนวยความสะดวกที่สำคัญอันดับ 3'})

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

######################################
# สร้าง DataFrame
data = {
    'Categories': ['การเดินทางและความปลอดภัย', 'การศึกษา', 'สุขภาพ', 'สิ่งแวดล้อม'],
    'Rank 1': [a1, b1, c1, d1],
    'Rank 2': [a2, b2, c2, d2],
    'Rank 3': [a3, b3, c3, d3]
}
df30 = pd.DataFrame(data)

# สร้าง Heatmap ด้วย Altair
heatmap = alt.Chart(df30).mark_rect().encode(
    x=alt.X('Categories:N', title='Categories'),
    y=alt.Y('Rank:N', title='Rank'),
    color=alt.Color('value:Q', title='Value')
).transform_fold(
    fold=['Rank 1', 'Rank 2', 'Rank 3'],
    as_=['Rank', 'value']
).properties(
    title='Heatmap of Categories by Rank'
).facet(
    column='Rank:N',
    title=None
)

# แสดง Heatmap ใน Streamlit
st.altair_chart(heatmap)
