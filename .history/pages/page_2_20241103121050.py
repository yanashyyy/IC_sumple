import streamlit as st
import datetime

st.title('回収報告')

col1, col2 = st.columns(2)

with col1:
    with st.form(key='profile_form'):
        st.header('回収入力フォーム')
        #テキストボックス
        name = st.text_input('名前')
        address = st.text_input('住所')
        
        #ラジオボタン※selectboxでプルダウンセレクトも可能。
        collction_documents = st.radio(
            '回収書類',
            ('契約書','借受証','覚書','口座振替用紙','その他'))
        
        #複数選択
        hobby = st.multiselect(
            '回収書類 複数ver',
            ('契約書','借受証','覚書','口座振替用紙','その他'))
        #チェックボックス
        mail_subscribe = st.checkbox('メールマガジンを購読する。')

        #スライダー
        height = st.slider('身長',min_value=110, max_value=210)

        #日付
        start_date = st.date_input(
            '開始日',
            datetime.date.today())

        #ボタン
        submit_btn2 = st.form_submit_button('送信')
        cancel_btn1 = st.form_submit_button('キャンセル')
        #print(f'submit_btn2:{submit_btn2}')
        #print(f'cancel_btn1:{cancel_btn1}')
        if submit_btn2:
            st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
            st.text(f'回収書類 :{collction_documents}')
            st.text(f'複数の回収書類 :{", ". join(hobby)}')
            st.text(f'回収日 :{start_date}')

            if mail_subscribe == True:
                st.text(f'メルマガ : 購入する')
            else:
                st.text(f'メルマガ : 購入しない')

with col2:
    with st.form(key='profile_form'):
        st.header('回収入力フォーム')
        #テキストボックス
        name = st.text_input('名前')
        address = st.text_input('住所')
        
        #ラジオボタン※selectboxでプルダウンセレクトも可能。
        collction_documents = st.radio(
            '回収書類',
            ('契約書','借受証','覚書','口座振替用紙','その他'))
        
        #複数選択
        hobby = st.multiselect(
            '回収書類 複数ver',
            ('契約書','借受証','覚書','口座振替用紙','その他'))
        #チェックボックス
        mail_subscribe = st.checkbox('メールマガジンを購読する。')

        #スライダー
        height = st.slider('身長',min_value=110, max_value=210)

        #日付
        start_date = st.date_input(
            '開始日',
            datetime.date.today())

        #ボタン
        submit_btn1 = st.form_submit_button('送信')
        cancel_btn1 = st.form_submit_button('キャンセル')
        #print(f'submit_btn1:{submit_btn1}')
        #print(f'cancel_btn1:{cancel_btn1}')
        if submit_btn1:
            st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
            st.text(f'回収書類 :{collction_documents}')
            st.text(f'複数の回収書類 :{", ". join(hobby)}')
            st.text(f'回収日 :{start_date}')

            if mail_subscribe == True:
                st.text(f'メルマガ : 購入する')
            else:
                st.text(f'メルマガ : 購入しない')