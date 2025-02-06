
from urlextract import URLExtract
from wordcloud import WordCloud

extract = URLExtract()
def fetch_stats(selected_user , df):

    if(selected_user!='Overall'):
        df = df[df['user']==selected_user]
    
    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    # Media
    media = df[(df['message']=='image omitted' )| (df['message']=='video omitted') | (df['message']=='GIF omitted') | (df['message']=='audio omitted') ].shape[0]
    
    # Links
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_messages , len(words) ,media , len(links)

def most_busy_users(df):
    x= df['user'].value_counts().head()
    y = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index()
    return x , y

def create_word_cloud(selected_user,df):
    if(selected_user!='Overall'):
        df = df[df['user']==selected_user]
    
    wc = WordCloud(width=500, height=500 , min_font_size=10 , background_color = 'white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc




