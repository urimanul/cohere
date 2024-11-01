import streamlit as st

# 初期設定
st.set_page_config(page_title="プロンプト生成", layout="centered")
show_process = True  # 処理中表示を切り替え
show_rag = True      # 引用ボタンの表示切り替え

# 処理中のラベル
if show_process:
    st.markdown("<p style='text-align:center; font-size:24px;'>処理中...</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align:center; font-size:24px;'></p>", unsafe_allow_html=True)

# SelectBox
my_data_source = [
    {"Name": "Option 1", "Value": 1},
    {"Name": "Option 2", "Value": 2},
    {"Name": "Option 3", "Value": 3},
]
selected_value = st.selectbox(
    label="選択",
    options=[item["Name"] for item in my_data_source],
    index=0
)

# プロンプト入力用のTextArea
rag_chain = st.text_area("プロンプトを入力して下さい", value="", height=150)

# 生成ボタン
if st.button("生成"):
    rag_response = "生成結果の例"  # ここで生成した結果を変数に格納します
    st.session_state['rag_response'] = rag_response
    st.session_state['show_process'] = False

# 結果表示用のTextArea
rag_response = st.text_area("結果", value=st.session_state.get('rag_response', ''), height=150, disabled=True)

# 注意ラベル
st.markdown("<p style='text-align:center; font-size:9px; color:darkslategray;'>回答は必ずしも正しいとは限りません。重要な情報は確認するようにしてください。</p>", unsafe_allow_html=True)

# 引用ボタン
if show_rag and st.button("引用"):
    st.write("引用データの表示")  # ここに引用のデータを表示するコードを追加します
