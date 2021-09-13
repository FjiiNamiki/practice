from typing import Optional
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')
# st.write('Interactive Widgets')
st.write('プログレスバーの表示')
'Start!'
latest_iteration = st.empty ()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.02)
'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input(
#     'あなたの趣味を教えてください',
# )
# condition = st.slider(
#     'あなたの調子は？', 0, 100, 50
# )

# 'あなたのコンディションは', condition, 'です。'
# 'あなたの趣味は、', text, 'です。'

# text = st.text_input(
#     'あなたの趣味を教えてください',
# )
# 'あなたの趣味は、', text, 'です。'

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# if st.checkbox('Shoe Image'):
#     img = Image.open('1621079315146.jpg')
#     st.image(img, caption='エマ', use_column_width=True)
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69, 139.70],
#     columns=['lat','lon']
# )

# st.map(df)

# st.bar_chart(df)


# st.area_chart(df)

# st.line_chart(df)

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })


# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 説
# ### 項



# ```python

# import streamlit as st
# import numpy as np
# import pandas as pd

# ```

# """