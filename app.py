import streamlit as st
import requests

# 初期設定
st.set_page_config(page_title="プロンプト生成", layout="centered")

# セッションステートでshow_processの初期値を設定
if 'show_process' not in st.session_state:
    st.session_state['show_process'] = True  # 処理中表示の初期状態

show_rag = True  # 引用ボタンの表示切り替え

# 処理中のラベル
if st.session_state['show_process']:
    st.markdown("<p style='text-align:center; font-size:24px;'>処理中...</p>", unsafe_allow_html=True)

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
    # APIキーを設定
    apikey = 'GqsxZlKmcBzSultkVOfKPf7kVhYkporXvivq9KHg'  # ここにAPIキーを入力

    # URLとヘッダーの設定
    url = 'https://api.cohere.com/v1/chat'
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Content-Type': 'application/json'
    }

    # POSTデータを設定
    data = {
        "model": "command-r-plus",
        "message": rag_chain,  # chainPromptは事前に設定
        "connectors": [{"id": "authryh-wfc54k"}, {"id": "o365schedule-e4baaa"}, {"id": "web-search"}]
    }


    # POSTリクエストを送信
    response = requests.post(url, headers=headers, json=data)

    # レスポンスの確認
    if response.status_code == 200:
        st.text_area("結果", value="response", height=150, disabled=True)
    else:
        print("エラー:", response.status_code, response.text)
        
    rag_response = "生成結果の例"  # ここで生成した結果を変数に格納します
    st.session_state['rag_response'] = "seiko"
    st.session_state['show_process'] = False  # ボタンが押されたらshow_processをFalseに設定

# 結果表示用のTextArea
rag_response = st.text_area("結果", value=st.session_state.get('rag_response', ''), height=150, disabled=True)

# 注意ラベル
st.markdown("<p style='text-align:center; font-size:9px; color:darkslategray;'>回答は必ずしも正しいとは限りません。重要な情報は確認するようにしてください。</p>", unsafe_allow_html=True)

# 引用ボタン
if show_rag and st.button("引用"):
    st.write("引用データの表示")  # ここに引用のデータを表示するコードを追加します
