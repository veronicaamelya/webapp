import streamlit as st
from sqlalchemy import text

list_play = ['', 'land', 'watery', 'air']
list_game = ['', 'male', 'female']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://veronicaamelya11:5YA4woemubsX@ep-bold-darkness-61739336.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS PEMESANAN (id serial, play_name varchar, customer_name varchar, gender char(25), \
                                                       game text, handphone varchar, tanggal date);')
    session.execute(query)

st.header('WAHANA LABIRIN ILUSI DATA MANAGEMENT')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM pemesanan ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO pemesanan (play_name, customer_name, gender, game, handphone, waktu, tanggal) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':None, '7':None})
            session.commit()

    data = conn.query('SELECT * FROM pemesanan ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        play_name_lama = result["play_name"]
        customer_name_lama = result["customer_name"]
        gender_lama = result["gender"]
        game_lama = result["game"]
        handphone_lama = result["handphone"]
        waktu_lama = result["waktu"]
        tanggal_lama = result["tanggal"]

        with st.expander(f'a.n. {customer_name_lama}'):
            with st.form(f'data-{id}'):
                play_name_baru = st.selectbox("play_name", list_play, list_play.index(play_name_lama))
                customer_name_baru = st.text_input("customer_name", customer_name_lama)
                gender_baru = st.selectbox("gender", list_game, list_game.index(gender_lama))
                game_baru = st.multiselect("game", ['roller coaster', 'bianglala', 'bombom car', 'bowling', 'ice skating', 'flying fox', 'jetski', 'paralayang', 'snorkling', 'swimming', 'sky diving'], eval(game_lama))
                handphone_baru = st.text_input("handphone", handphone_lama)
                waktu_baru = st.time_input("waktu", waktu_lama)
                tanggal_baru = st.date_input("tanggal", tanggal_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE pemesanan \
                                          SET play_name=:1, customer_name=:2, gender=:3, game=:4, \
                                          handphone=:5, waktu=:6, tanggal=:7 \
                                          WHERE id=:8;')
                            session.execute(query, {'1':play_name_baru, '2':customer_name_baru, '3':gender_baru, '4':str(game_baru), 
                                                    '5':handphone_baru, '6':waktu_baru, '7':tanggal_baru, '8':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM pemesanan WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
