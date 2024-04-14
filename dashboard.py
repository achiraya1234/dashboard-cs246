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
df = df.rename(columns={' [ด้านการเดินทางและความปลอดภัย]': 'ด้านการเดินทางและความปลอดภัย',
                         ' [ด้านการศึกษา]': 'ด้านการศึกษา',
                         ' [ด้านสุขภาพ]': 'ด้านสุขภาพ',
                         ' [ด้านสิ่งแวดล้อม]': 'ด้านสิ่งแวดล้อม'})

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

counts_5 = []
counts_4 = []
counts_3 = []
counts_2 = []
counts_1 = []

for category_column in ['ด้านการเดินทางและความปลอดภัย', 'ด้านการศึกษา', 'ด้านสุขภาพ', 'ด้านสิ่งแวดล้อม']:
    counts_5.append(df[category_column].value_counts().get(5, 0))
    counts_4.append(df[category_column].value_counts().get(4, 0))
    counts_3.append(df[category_column].value_counts().get(3, 0))
    counts_2.append(df[category_column].value_counts().get(2, 0))
    counts_1.append(df[category_column].value_counts().get(1, 0))

#################################
mean = df[['ด้านการเดินทางและความปลอดภัย', 'ด้านการศึกษา', 'ด้านสุขภาพ', 'ด้านสิ่งแวดล้อม']].mean().round(2)
mean_data = {
    'Categories': ['ด้านการเดินทางและความปลอดภัย', 'ด้านการศึกษา', 'ด้านสุขภาพ', 'ด้านสิ่งแวดล้อม'],
    'Mean': mean
}
df_mean = pd.DataFrame(mean_data)

data_mean = {
    'Categories': ['การเดินทางและความปลอดภัย', 'การศึกษา', 'สุขภาพ', 'สิ่งแวดล้อม'],
    'Satisfaction_5': counts_5,
    'Satisfaction_4': counts_4,
    'Satisfaction_3': counts_3,
    'Satisfaction_2': counts_2,
    'Satisfaction_1': counts_1
}

# สร้าง DataFrame
df1 = pd.DataFrame(data_mean)

# ใช้ pd.melt() เพื่อรวมคอลัมน์ 'Rank 1', 'Rank 2', และ 'Rank 3' เป็นคอลัมน์ 'population'
df_reshaped1 = pd.melt(df1, id_vars=['Categories'], value_vars=['Satisfaction_5','Satisfaction_4','Satisfaction_3','Satisfaction_2','Satisfaction_1'], var_name='Satisfaction', value_name='population')

# แสดง DataFrame ที่ได้
print(df_reshaped1)

########################################
# คำนวณค่าเฉลี่ยของความพึงพอใจในหมวดหมู่การศึกษาตามวิธีที่ระบุ
avg1 = ((df_reshaped1[df_reshaped1['Categories'] == 'การเดินทางและความปลอดภัย']['population'] * df_reshaped1[df_reshaped1['Categories'] == 'การเดินทางและความปลอดภัย']['Satisfaction'].str[-1].astype(int)).sum() / 102).round(2)
avg2 = ((df_reshaped1[df_reshaped1['Categories'] == 'การศึกษา']['population'] * df_reshaped1[df_reshaped1['Categories'] == 'การศึกษา']['Satisfaction'].str[-1].astype(int)).sum() / 102).round(2)
avg3 = ((df_reshaped1[df_reshaped1['Categories'] == 'สุขภาพ']['population'] * df_reshaped1[df_reshaped1['Categories'] == 'สุขภาพ']['Satisfaction'].str[-1].astype(int)).sum() / 102).round(2)
avg4 = ((df_reshaped1[df_reshaped1['Categories'] == 'สิ่งแวดล้อม']['population'] * df_reshaped1[df_reshaped1['Categories'] == 'สิ่งแวดล้อม']['Satisfaction'].str[-1].astype(int)).sum() / 102).round(2)

print(avg1, avg2, avg3, avg4)

average = [avg1, avg2, avg3, avg4]

###############################
data_rank = {
    'Categories': ['การเดินทางและความปลอดภัย', 'การศึกษา', 'สุขภาพ', 'สิ่งแวดล้อม'],
    'Rank 1': [a1, b1, c1, d1],
    'Rank 2': [a2, b2, c2, d2],
    'Rank 3': [a3, b3, c3, d3]
}

# สร้าง DataFrame
df = pd.DataFrame(data_rank)

# ใช้ pd.melt() เพื่อรวมคอลัมน์ 'Rank 1', 'Rank 2', และ 'Rank 3' เป็นคอลัมน์ 'population'
df_reshaped2 = pd.melt(df, id_vars=['Categories'], value_vars=['Rank 1', 'Rank 2', 'Rank 3'], var_name='Ranking', value_name='population')

# แสดง DataFrame ที่ได้
print(df_reshaped2)

###############################
data_scale = pd.DataFrame({
    'Categories': ['การเดินทางและความปลอดภัย', 'การศึกษา', 'สุขภาพ', 'สิ่งแวดล้อม'],
    'average': average
})

# Define color scale for gauge
color_scale = alt.Scale(
    domain=[1.8, 2.6, 3.4, 4.2, 5],
    range=['red', 'orange', 'yellow', 'lightgreen', 'green']
)

legend_data = pd.DataFrame({'value': [5, 4, 3, 2, 1]})
legend_bar = alt.Chart(legend_data).mark_rect().encode(
    y=alt.Y('value:O', axis=alt.Axis(title='Value', titleAnchor='start', titleAngle=0, titleAlign='left'), sort=alt.SortOrder('descending')),
    color=alt.Color('value:Q', scale=color_scale)
)

####################################
with st.sidebar:
    st.title('Satisfaction')

    Categories = list(data_scale.Categories.unique())

    selected_Categories = st.selectbox('Select a Categories', Categories, index=0)
    df_selected_Categories = data_scale[data_scale.Categories == selected_Categories]
    df_selected_Categories_sorted = df_selected_Categories.sort_values(by="average", ascending=False)
    
    st.title('Ranking')

    Ranking = list(df_reshaped2.Ranking.unique())

    selected_Ranking = st.selectbox('Select a Ranking', Ranking, index=0)
    df_selected_Ranking = df_reshaped2[df_reshaped2.Ranking == selected_Ranking]
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
                          #legend=alt.Legend(title=" "),
                          scale=alt.Scale(scheme=input_color_theme)),
          stroke=alt.value('black'),
          strokeWidth=alt.value(0.25),
      ).properties(
          width=350,
          height=250,
      ).configure_axis(
          labelFontSize=12,
          titleFontSize=12
      )

  return heatmap

#################################
# สร้าง donut chart สำหรับ Ranking
def make_donut(input_df, input_population, input_categories):
  donut_chart = alt.Chart(input_df).mark_arc().encode(
      theta=f'{input_population}:Q',
      color=alt.Color(f'{input_categories}:N', scale=alt.Scale(scheme='category20')),
      tooltip=[f'{input_categories}', f'{input_population}']
  ).properties(
      #width=300,
      height=230,
      title=f"{input_df['Ranking'].iloc[0]}"
  )

  return donut_chart

########################################
# Create Gauge Chart using Altair for the selected category
def make_gauge(input_df, input_category, input_average):
    bar_chart_selected = alt.Chart(input_df).mark_bar().encode(
        #y=alt.Y(f'{input_category}'),
        x=alt.X(f'{input_average}', title=None, scale=alt.Scale(domain=(0, 5))),
        color=alt.Color(f'{input_average}:Q', scale=color_scale, legend=None),
        tooltip=[f'{input_category}', f'{input_average}']
    ).properties(
        width=400,
        height=150,
        title=f"{input_df['Categories'].iloc[0]}"
    )

# Add full value text for the selected category
    text_selected = bar_chart_selected.mark_text(
        align='center',
        baseline='bottom',
        dx=20,
        dy=0,  # ระยะห่างจากแท่งกราฟ
        color='black',
        fontSize=14,  # ขนาดตัวอักษร
    ).encode(
        text=alt.Text(f'{input_average}:Q', format='.2f')  # รูปแบบของตัวเลข (ทศนิยม 1 ตำแหน่ง)
    )
    return bar_chart_selected + text_selected

###########################################
col = st.columns((5, 5), gap='medium')
with col[0]:
    st.markdown('#### Mean Satisfaction')
    gauge_chart = make_gauge(df_selected_Categories,'Categories', 'average')
    
    # Combine selected Gauge Chart and Legend
    gauge_chart_with_legend = alt.hconcat(gauge_chart, legend_bar)
    st.altair_chart(gauge_chart_with_legend, use_container_width=True)

    st.markdown('#### Total Ranking')
    heatmap = make_heatmap(df_reshaped2, 'Categories', 'Ranking', 'population', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)

with col[1]:
    st.markdown('#### Ranking')
    donut_chart = make_donut(df_selected_Ranking, 'population', 'Categories')
    st.altair_chart(donut_chart, use_container_width=True)
    
    st.markdown('#### Categories')
    st.dataframe(df_selected_Ranking_sorted,
                 column_order=("Categories", "population"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "Categories": st.column_config.TextColumn(
                        "Categories",
                    ),
                    "population": st.column_config.ProgressColumn(
                        "Population",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_Ranking_sorted.population),
                     )}
                 )
