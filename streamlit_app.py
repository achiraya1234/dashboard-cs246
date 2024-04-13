import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Ranking",
    page_icon="🏫",
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

    Ranking = list(df_reshaped.Ranking.unique())[::-1]

    selected_Ranking = st.selectbox('Select a Ranking', Ranking, index=len(Ranking)-1)
    df_selected_Ranking = df_reshaped[df_reshaped.Ranking == selected_Ranking]
    df_selected_Ranking_sorted = df_selected_Ranking.sort_values(by="population", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    print(df_selected_Ranking_sorted)

##################################
alt.themes.enable("dark")

heatmap = alt.Chart(df_reshaped).mark_rect().encode(
        y=alt.Y('Categories:O', axis=alt.Axis(title="Categories", titleFontSize=16, titlePadding=15, titleFontWeight=900, labelAngle=0)),
        x=alt.X('Ranking:O', axis=alt.Axis(title="Ranking", titleFontSize=16, titlePadding=15, titleFontWeight=900)),
        color=alt.Color('max(population):Q',
                         legend=alt.Legend(title=" "),
                         scale=alt.Scale(scheme="blueorange")),
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

heatmap

#################################
# สร้าง donut chart สำหรับ Ranking 1
donut_chart_rank1 = alt.Chart(df_reshaped[df_reshaped['Ranking'] == 'Rank 1']).mark_arc().encode(
    theta='population:Q',
    color=alt.Color('Categories:N', scale=alt.Scale(scheme='category20')),
    tooltip=['Categories', 'population']
).properties(
    width=200,
    height=200,
    title='Ranking 1'
)

# สร้าง donut chart สำหรับ Ranking 2
donut_chart_rank2 = alt.Chart(df_reshaped[df_reshaped['Ranking'] == 'Rank 2']).mark_arc().encode(
    theta='population:Q',
    color=alt.Color('Categories:N', scale=alt.Scale(scheme='category20')),
    tooltip=['Categories', 'population']
).properties(
    width=200,
    height=200,
    title='Ranking 2'
)

# สร้าง donut chart สำหรับ Ranking 3
donut_chart_rank3 = alt.Chart(df_reshaped[df_reshaped['Ranking'] == 'Rank 3']).mark_arc().encode(
    theta='population:Q',
    color=alt.Color('Categories:N', scale=alt.Scale(scheme='category20')),
    tooltip=['Categories', 'population']
).properties(
    width=200,
    height=200,
    title='Ranking 3'
)

# แสดง donut charts ทั้ง 3 กราฟ
donut_chart_rank1 | donut_chart_rank2 | donut_chart_rank3

################################################
def calculate_population_difference(input_df, input_Ranking):
  selected_Ranking_data = input_df[input_df['Ranking'] == input_Ranking].reset_index()
  previous_Ranking_data = input_df[input_df['Ranking'] == input_Ranking - 1].reset_index()
  selected_Ranking_data['population_difference'] = selected_Ranking_data.population.sub(previous_Ranking_data.population, fill_value=0)
  return pd.concat([selected_Ranking_data.states, selected_Ranking_data.id, selected_Ranking_data.population, selected_Ranking_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)

  print(df_Ranking_difference_sorted)

#################################################
def make_donut(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']

  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })

  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)

  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text

################################################
def format_number(num):
    if num > 100:
        if not num % 100:
            return f'{num // 100} M'
        return f'{round(num / 100, 1)} M'
    return f'{num // 10} K'

###########################################
col = st.columns((1.5, 4.5, 2), gap='medium')
