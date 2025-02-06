def fetch_stats(selected_user , df):
    if(selected_user!='Overall'):
        df = df[df['user']==selected_user]
    
    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    
    return num_messages , len(words)