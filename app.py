import streamlit as st
import gspread 


creds = {
    "type" : st.secrets['type'],
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["private_key_id"],
    "private_key": st.secrets["private_key"],
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"]

}

st.title('The Wholesome HP Data Capture Project')
st.write("This project is aimed at building a master data from the Harry Potter fanfiction universe based on your, the reader's experiences while reading the story.")
st.write("We are trying to engage as many fans as possible to make a list of fics that can be found regardless of vague summaries and intentional misleading tags on various fanfiction websites. We ask you to please enter the below information to the best you can for the story that you've read.")


st.subheader('Add a new story')

name = st.text_input('Enter the story name')
author = st.text_input('Enter the story author')
link = st.text_input('Enter the story link')

pair = option_pairing = st.selectbox('Select a pairing:', ['Harmony', 'Dramione', 'Haphne', 'Tomione/Volmione', 'Drarry', 'Tomarry', 'No pairing'])

summ = st.text_area("Enter your own detailed summary. Don't worry about any grammatical mistakes or leaving out any inappropriate phrases. Type out what happens in the story like the way you want to remember it in the future. Should be at least 100 words.", 
                        max_chars = 10000, 
                        height=200)


def save_into_csv(name, author, link, pair, summ):
    gc = gspread.service_account_from_dict(creds)

    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CdAMEQKY9nQsPEnFf4AeJSlN5EvCTkdl-t6-j0QzaSU/edit#gid=0')
    worksheet = sh.get_worksheet(0)

    worksheet.append_row([name, author, link, pair, summ])
    st.write('Submitted to database!')

    # last remark
    st.text('This is the start of an honest attempt at building an awesome AI fanfiction search engine.')
    st.text(' It cannot be done without your participation, so thank you. So much!')

    

# save into db
if st.button('Submit'):
    if name.strip() == '' or author.strip() == '' or link.strip() == '' or summ.strip() == '':
        st.error('Please enter all available fields to submit.')
        
    elif len(summ.strip().split(' ')) < 100:
        st.error('Please detail the summary in at least 100 words.')
    else:
        # st.write('OK')
        save_into_csv(name, author, link, pair, summ)


