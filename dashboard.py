import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Dashboard",
    #page_icon="",
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

###############################
data = {
    'Categories': ['การเดินทางและความปลอดภัย', 'การศึกษา', 'สุขภาพ', 'สิ่งแวดล้อม'],
    'Rank 1': [a1, b1, c1, d1],
    'Rank 2': [a2, b2, c2, d2],
    'Rank 3': [a3, b3, c3, d3]
}

# สร้าง DataFrame
df = pd.DataFrame(data)

# ใช้ pd.melt() เพื่อรวมคอลัมน์ 'Rank 1', 'Rank 2', และ 'Rank 3' เป็นคอลัมน์ 'population'
df_reshaped = pd.melt(df, id_vars=['Categories'], value_vars=['Rank 1', 'Rank 2', 'Rank 3'], var_name='Ranking', value_name='population')

# แสดง DataFrame ที่ได้
print(df_reshaped)

###############################
with st.sidebar:
    st.title('Ranking')

    Ranking = list(df_reshaped.Ranking.unique())

    selected_Ranking = st.selectbox('Select a Ranking', Ranking, index=0)
    df_selected_Ranking = df_reshaped[df_reshaped.Ranking == selected_Ranking]
    df_selected_Ranking_sorted = df_selected_Ranking.sort_values(by="population", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    print(df_selected_Ranking_sorted)

##################################
alt.themes.enable("dark")

def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
  heatmap = alt.Chart(input_df).mark_rect().encode(
          y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Categories", titleFontSize=16, titlePadding=15, titleFontWeight=900, labelAngle=0)),
          x=alt.X(f'{input_x}:O', axis=alt.Axis(title="Ranking", titleFontSize=16, titlePadding=15, titleFontWeight=900, labelAngle=0)),
          color=alt.Color(f'max({input_color}):Q',
                          legend=alt.Legend(title=" "),
                          scale=alt.Scale(scheme=input_color_theme)),
          stroke=alt.value('black'),
          strokeWidth=alt.value(0.25),
          #tooltip=[
          #    alt.Tooltip('year:O', title='Year'),
          #    alt.Tooltip('population:Q', title='Population')
          #]
      ).properties(width=900
      #).configure_legend(orient='bottom', titleFontSize=16, labelFontSize=14, titlePadding=0
      #).configure_axisX(labelFontSize=14)
      ).configure_axis(
      labelFontSize=12,
      titleFontSize=12
      )

  return heatmap

#################################
# สร้าง donut chart สำหรับ Ranking
# สร้าง donut chart สำหรับ Ranking
def make_donut(input_df, input_population, input_categories):
  donut_chart = alt.Chart(input_df).mark_arc().encode(
      theta=f'{input_population}:Q',
      color=alt.Color(f'{input_categories}:N', scale=alt.Scale(scheme='category20')),
      tooltip=[f'{input_categories}', f'{input_population}']
  ).properties(
      width=500,
      height=500,
      title='Ranking'
  )

  return donut_chart

################################################
def format_number(num):
    if num > 100:
        if not num % 100:
            return f'{num // 100} M'
        return f'{round(num / 100, 1)} M'
    return f'{num // 10} K'

###########################################
col = st.columns((5.5, 4.5), gap='medium')
with col[0]:
    st.markdown('#### Ranking')
    donut_chart = make_donut(df_selected_Ranking, 'population', 'Categories')
    st.altair_chart(donut_chart)

with col[1]:
    st.markdown('#### Total Ranking')
    
    heatmap = make_heatmap(df_reshaped, 'Categories', 'Ranking', 'population', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)
