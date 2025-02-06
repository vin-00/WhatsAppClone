import streamlit as st
import preprocessor , helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None :
    bytes_data= uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    # Fetch Unique users
    user_list = df['user'].unique().tolist()
    
    group_name = "-1"
    if(len(user_list)>2):
        group_name = user_list.pop(0)
    
    user_list.sort()

    if(group_name!='-1'):
        df = df[df['user']!=group_name]
    
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show Analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        
        num_messages , word ,media ,links= helper.fetch_stats(selected_user, df)
        col1 , col2 , col3 ,col4 = st.columns(4)
        with col1 :    
            st.header("Total Messages")
            st.title(num_messages)

        with col2 :    
            st.header("Total Words")
            st.title(word)

        with col3 :    
            st.header("Media Shared")
            st.title(media)
        with col4 :    
            st.header("Links Shared")
            st.title(links)
        
        #  Busiest users 
        if(selected_user=='Overall'):
            
            st.title("Most Busy Users")
            x , y= helper.most_busy_users(df)
            
            col1 , col2 = st.columns(2)

            with col1 :
                fig , ax = plt.subplots()
                fig.patch.set_facecolor("#0E1117")  # Set entire figure background to black
                ax.set_facecolor("#0E1117")
                ax.bar(x.index, x.values , color='green')
                plt.xticks(rotation='vertical')
                ax.tick_params(colors="white")  # Change axis ticks color
                ax.xaxis.label.set_color("white")  # X-axis label color
                ax.yaxis.label.set_color("white")  # Y-axis label color
                ax.spines["bottom"].set_color("white")  # Make bottom border white
                ax.spines["left"].set_color("white")

                ax.spines["top"].set_visible(False)
                ax.spines["right"].set_visible(False)
                st.pyplot(fig)
            with col2 :
                fig , ax = plt.subplots(facecolor='0E1117')
                fig.patch.set_facecolor("0E1117")  # Set entire figure background
                ax.set_facecolor("0E1117")
                ax.pie(y['count'], labels=y['user'], autopct='%1.1f%%', startangle=140 ,textprops={"color":"white"})
                st.pyplot(fig)
                
        # WordCloud

        st.title("Word Cloud")

        df_wc = helper.create_word_cloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        ax.axis("off")
        st.pyplot(fig) 
