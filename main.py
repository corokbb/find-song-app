import time
import streamlit as st
import pandas as pd

import base64
import streamlit.components.v1 as stc

st.set_page_config(
    page_title="Find Song App", 
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


file_ = open("resorce/img/u1.gif", "rb")
contents = file_.read()
data_url_u1 = base64.b64encode(contents).decode("utf-8")
file_ = open("resorce/img/u2.gif", "rb")
contents = file_.read()
data_url_u2 = base64.b64encode(contents).decode("utf-8")
file_ = open("resorce/img/nansuka.png", "rb")
contents = file_.read()
data_url_u3 = base64.b64encode(contents).decode("utf-8")

file_.close()

# st.markdown(
#     f'',
#     unsafe_allow_html=True,
#     )

def music_play(file):
    audio_path1 = f'resorce/audio/{file}.wav' 
    audio_placeholder = st.empty()
    file_ = open(audio_path1, "rb")
    contents = file_.read()
    file_.close()

    audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
    audio_html = """
                    <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not support the audio element.
                    </audio>
                """ %audio_str
    audio_placeholder.empty()
    time.sleep(0.1) #これがないと上手く再生されません
    audio_placeholder.markdown(audio_html, unsafe_allow_html=True)




if 'artist_name' not in st.session_state: 
    st.session_state.artist_name = ""

if 'preset' not in st.session_state: 
    st.session_state.preset = ""

if 'syaken' not in st.session_state: 
    st.session_state.syaken = False

if st.session_state.syaken:

    if st.session_state.preset == "ゆにかーる":
        st.markdown(f'<center><img src="data:image/gif;base64,{data_url_u1}" alt="cat gif"><img src="data:image/gif;base64,{data_url_u3}" \
                    alt="cat gif"><img src="data:image/gif;base64,{data_url_u2}" alt="cat gif"></center>', unsafe_allow_html=True)
        music_play("nansuka")

    else:
        st.markdown(f'<center><img src="data:image/gif;base64,{data_url1}" alt="cat gif"><img src="data:image/gif;base64,{data_url3}" \
                    alt="cat gif"><img src="data:image/gif;base64,{data_url2}" alt="cat gif"></center>', unsafe_allow_html=True)


upcol1, upcol2, _ = st.columns([3, 1, 8])
preset = upcol1.selectbox(
    'プリセット',
     ('', 'あっくん', 'Alkome','るぷろん', 'corok-Bb', "kinaphar", "ゆにかーる", 'Sohwe', 'hnxqch', '塩', "dim.", "らばす", "TeIXe", "elli mia", "1 Room Songs", "oblivious", "k-u3k", "かーぼんぶりゅれ",  \
           "人畜無害な人間", "Daiyaki", "高林治紀", "ねこまりもん", "Nettle", "やわらか浪人生",  "ゆせい", "フトンガメ", "Nettle", "ヒマラヤロードレース", "Lem"))
st.session_state.preset = preset

if preset == "あっくん":
    st.session_state.artist_name = "あっくん|usutsuki"
elif preset == "Alkome":
    st.session_state.artist_name = "Alkome|0x63|tukumo99|Temesgen Markos"
elif preset == "るぷろん":
    st.session_state.artist_name = "Chanor|しゃのあ|Luphus|​Pulon|帆立|HTT|筑波変拍子音楽研究会"
elif preset == "corok-Bb":
    st.session_state.artist_name = "corok-Bb|corok-Pp|corok|DJ Ore|Omunifas|Omunifassm|Northbangerz|NAZONO_RAMEN"
elif preset == "kinaphar":
    st.session_state.artist_name = "kinaphar|きなふぁ|rahpanik|Crystarhythm"
elif preset == "ゆにかーる":
    st.session_state.artist_name = "ゆにかーる|unicurl|uni-c|UNIC|古河ユニック|古河気合筋肉|湯西川将吾"
elif preset == "Sohwe":
    st.session_state.artist_name = "Sohwe|SAW|ｙ​ａ​ｓ​ｕ​ｒ​ａ​ｇ​ｉ 🍸 ｄ​ｒ​ｉ​ｎ​ｋ"
elif preset == "hnxqch":
    st.session_state.artist_name = "hnxqch|&2|豚骨"
elif preset == "塩":
    st.session_state.artist_name = "塩|Shion Sakamoto| Shi |Shicom" 
elif preset == "dim.":
    st.session_state.artist_name = "dim.|うんのやすひろ|moyashi17|町​一​番​の​働​き​蜂​|eBANK徳川" 
elif preset == "らばす":
    st.session_state.artist_name = "rabasu" 
elif preset == "TeIXe":
    st.session_state.artist_name = "TeIXe|Piter Robinson"
elif preset == "elli mia":
    st.session_state.artist_name = "elli mia|衿"
elif preset == "1 Room Songs":
    st.session_state.artist_name = "1 Room Songs|Age"
elif preset == "oblivious":
    st.session_state.artist_name = "oblivious|おぶりー|オリビア"
elif preset == "k-u3k":
    st.session_state.artist_name = "k-u3k|くさき"
elif preset == "Daiyaki":
    st.session_state.artist_name = "Daiyaki"
elif preset == "ねこまりもん":
    st.session_state.artist_name = "ねこまりもん|ねこまりも"
elif preset == "Nettle":
    st.session_state.artist_name = "Nettle|うずくま"
elif preset == "やわらか浪人生":
    st.session_state.artist_name = "やわらか浪人生|アメミヤトワ"
elif preset == "人畜無害な人間":
    st.session_state.artist_name = "人畜無害な人間"
elif preset == "かーぼんぶりゅれ":
    st.session_state.artist_name = "かーぼんぶりゅれ"
elif preset == "ゆせい":
    st.session_state.artist_name = "ゆせい"
elif preset == "フトンガメ":
    st.session_state.artist_name = "フトンガメ"
elif preset == "高林治紀":
    st.session_state.artist_name = "高林治紀|Rerohm"
elif preset == "Nettle":
    st.session_state.artist_name = "Nettle|うずくま"
elif preset == "Daiyaki":
    st.session_state.artist_name = "Daiyaki"
elif preset == "ヒマラヤロードレース":
    st.session_state.artist_name = "ヒマラヤロードレース"
elif preset == "Lem":
    st.session_state.artist_name = "Lem"



st.write(f"データ:2024/01/15時点")




col1, col2 = st.columns([3, 1])
text_artist = col1.text_input("アーティスト名(正規表現が使えます)", st.session_state.artist_name)
btn_serach  = col2.button("search", help="検索っちもん")


df = pd.read_csv("csv/musiclist.csv")
df["artist_name"]  = df["artist_name"].fillna("")




def construct(result):

    if text_artist == "UNIC":
        st.session_state.syaken = True

    if st.session_state.syaken:
        if preset == "kinaphar":
            music_play("result2")
        else:
            music_play("result")
            
        time.sleep(3.9)

        if count == 0:
            music_play("unic")


    st.write(f"{count} / {whole}件ヒットしました")
    for row in result.itertuples():
        album_id = row[1]
        track_id = row[4]
        print(album_id, track_id)
        time.sleep(0.1)
        st.markdown(f"""
        <iframe style="border: 0; width: 50%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album={album_id}/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/track={track_id}/transparent=true/" seamless><a href="https://tsukubadtm.bandcamp.com/album/exp80-12-ep"></a></iframe>
        """, unsafe_allow_html=True)






if btn_serach:
    print(text_artist)
    result = df[(df["artist_name"].str.contains(text_artist, case=False)) | (df["music_name"].str.contains(text_artist, case=True))]

    whole = len(df)
    count = len(result)
    if count <= 100:
        
        construct(result)
    else:
        music_play("unic")
        st.write(f"検索結果が100を超えているため表示できません, {count}/{whole}")


# streamlit run d:\Python\find-song-app\main.py

    


