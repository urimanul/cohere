import streamlit as st
import requests

# 初期設定
st.set_page_config(page_title="プロンプト生成", layout="centered")

# SelectBox
my_data_source = [
    {"Name": "韓国の首都は", "Value": "韓国の首都は"},
    {"Name": "日本の首都は", "Value": "日本の首都は"},
    {"Name": "米国の首都は", "Value": "米国の首都は"},
]

# コールバック関数の定義
def update_rag_chain():
    selected_item = next(item for item in my_data_source if item["Name"] == st.session_state.selected_value)
    st.session_state.rag_chain = selected_item["Value"]

# セッションステートの初期化
if 'rag_chain' not in st.session_state:
    st.session_state.rag_chain = ""
if 'selected_value' not in st.session_state:
    st.session_state.selected_value = my_data_source[0]["Name"]

# SelectBoxの作成
selected_value = st.selectbox(
    label="選択",
    options=[item["Name"] for item in my_data_source],
    index=0,
    key='selected_value',
    on_change=update_rag_chain
)

# プロンプト入力用のTextArea（valueを直接指定しない）
rag_chain = st.text_area("プロンプトを入力して下さい", height=150, key="rag_chain")



if st.button("生成"):
    # Cohere API設定
    API_URL = 'https://api.cohere.com/v1/chat'
    MODEL = 'command-r-plus'
    API_KEY = 'GqsxZlKmcBzSultkVOfKPf7kVhYkporXvivq9KHg'
    maxTokens = 4096
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        'model': MODEL,
        'max_tokens': maxTokens,
        'messages': rag_chain,
        'connectors': [{"id": "authryh-wfc54k"},{"id": "o365schedule-e4baaa"},{"id": "web-search"}]
    }
        
    # リクエストの送信
    response = requests.post(f'{API_URL}chat/completions', headers=headers, json=data)
    rag_response = response.json()['data']['text']
        
    #rag_response = "生成結果の例"  # ここで生成した結果を変数に格納します
    st.session_state['rag_response'] = rag_response
    st.session_state['show_process'] = False  # ボタンが押されたらshow_processをFalseに設定

# 結果表示用のTextArea
st.text_area("結果", value=st.session_state.get('rag_response', ''), height=150, disabled=True)

# 注意ラベル
st.markdown("<p style='text-align:center; font-size:9px; color:darkslategray;'>回答は必ずしも正しいとは限りません。重要な情報は確認するようにしてください。</p>", unsafe_allow_html=True)

# 引用ボタン
#if show_rag and st.button("引用"):
    #st.write("引用データの表示")  # ここに引用のデータを表示するコードを追加します
