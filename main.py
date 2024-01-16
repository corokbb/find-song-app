import streamlit as st
import pandas as pd

import base64
import streamlit.components.v1 as stc

st.set_page_config(
    page_title="モ　ン　チ　ー　チ　ー　チ　ー　ア　プ　リ", 
    layout="wide", 
)

file_ = open("resorce/img/y1.gif", "rb")
contents = file_.read()
data_url1 = base64.b64encode(contents).decode("utf-8")
file_ = open("resorce/img/y2.gif", "rb")
contents = file_.read()
data_url2 = base64.b64encode(contents).decode("utf-8")
file_ = open("resorce/img/logo.png", "rb")
contents = file_.read()
data_url3 = base64.b64encode(contents).decode("utf-8")
file_.close()

# st.markdown(
#     f'',
#     unsafe_allow_html=True,
#     )
st.markdown(f'<center><img src="data:image/gif;base64,{data_url1}" alt="cat gif"><img src="data:image/gif;base64,{data_url3}" \
            alt="cat gif"><img src="data:image/gif;base64,{data_url2}" alt="cat gif"></center>', unsafe_allow_html=True)

if 'artist_name' not in st.session_state: 
    st.session_state.artist_name = ""

upcol1, upcol2, _ = st.columns([3, 1, 8])
preset = upcol1.selectbox(
    'プリセット',
     ('', 'Alkome','るぷろん', 'corok-Bb', "kinaphar", "ゆにかーる", 'Sohwe', 'hnxqch', '塩'))

if preset == "Alkome":
    st.session_state.artist_name = "Alkome|0x63|tukumo99|Temesgen Markos"
elif preset == "るぷろん":
    st.session_state.artist_name = "Chanor|Luphus|​Pulon|帆立|HTT|筑波変拍子音楽研究会"
elif preset == "corok-Bb":
    st.session_state.artist_name = "corok-Bb|corok-Pp|corok|DJ Ore|Omunifas|Omunifassm|ラ​ー​メ​ン​パ​ラ​ダ​イ​ス​オ​ー​ケ​ス​ト​ラ"
elif preset == "kinaphar":
    st.session_state.artist_name = "kinaphar|きなふぁ|rahpanik|Crystarhythm"
elif preset == "ゆにかーる":
    st.session_state.artist_name = "ゆにかーる|unicurl|uni-c|UNIC|古河ユニック|古河気合筋肉|湯西川将吾"
elif preset == "Sohwe":
    st.session_state.artist_name = "Showe|SAW|ｙ​ａ​ｓ​ｕ​ｒ​ａ​ｇ​ｉ 🍸 ｄ​ｒ​ｉ​ｎ​ｋ|"
elif preset == "hnxqch":
    st.session_state.artist_name = "野獣先輩"
elif preset == "塩":
    st.session_state.artist_name = "塩"

st.write(f"データ:2024/01/15時点")

col1, col2 = st.columns([3, 1])
text_artist = col1.text_input("アーティスト名(正規表現が使えます)", st.session_state.artist_name)
btn_serach  = col2.button("search", help="検索っちもん")


df = pd.read_csv("csv/musiclist.csv")
df["artist_name"]  = df["artist_name"].fillna("")

def construct(result):
    for row in result.itertuples():
        album_id = row[1]
        track_id = row[4]
        print(album_id, track_id)

        st.markdown(f"""
        <iframe style="border: 0; width: 50%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album={album_id}/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/track={track_id}/transparent=true/" seamless><a href="https://tsukubadtm.bandcamp.com/album/exp80-12-ep"></a></iframe>
        """, unsafe_allow_html=True)


if btn_serach:
    print(text_artist)
    result = df[(df["artist_name"].str.contains(text_artist, case=False)) | (df["music_name"].str.contains(text_artist, case=True))]

    whole = len(df)
    count = len(result)
    if count <= 100:
        st.write(f"{count} / {whole}件ヒットしました")
        construct(result)
    else:
        st.write(f"検索結果が100を超えているため表示できません, {count}/{whole}")





