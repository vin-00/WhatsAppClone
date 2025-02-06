
from urlextract import URLExtract

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
    percent = round(df['user'].value_count()/df.shape[0])*100,2).reset_indec()
    return x


