# WhatsApp Chat Analyzer

A powerful and interactive WhatsApp Chat Analyzer built with **Streamlit** that provides deep insights into your exported chat data. It supports both **Android** and **iOS** chat exports and offers a comprehensive analysis of group and individual statistics.
![image](https://github.com/user-attachments/assets/144131bc-55b5-4989-8374-388af94c46ef)
![image](https://github.com/user-attachments/assets/72e03620-6dc3-4675-a158-5efbd352713a)

## 📊 Features

- **Multi-Platform Support**: Works with both Android and iOS exported chat files.
- **User Activity Insights**: Identify the most active user, busiest months, and days.
- **Message Statistics**: Total messages, words, links, and media shared.
- **User Activity Chart**: Visualize when users are most active during the day.
- **Emoji & Word Analysis**: Find the most used emojis and visualize chat trends using a word cloud.
- **Longest Streak**: Discover the longest consecutive messaging streak.
- **User-Level Insights**: Analyze data for the whole group or focus on individual members.

## 📁 Supported Input

- Exported **WhatsApp** chat files:
  - Android: `txt` format (without media option)
  - iOS: `txt` format (without media)

## 🛠️ Tech Stack

- **Streamlit**: For building the interactive web app.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For generating visual charts and graphs.
- **re**: For regular expression-based text extraction.
- **urlExtract**: For detecting and counting URLs.
- **WordCloud**: For generating a word cloud visualization.

## 📊 Insights You Can Explore

1. **General Statistics**
   - Total messages, words, links, and media shared
   - Most active user
2. **Time-Based Analysis**
   - Busiest month and day
   - Hourly activity heatmap (when users are most active)
3. **User-Level Analysis**
   - Filter data for specific members
4. **Engagement Patterns**
   - Longest messaging streak
   - Most used words and emojis
5. **Visual Representations**
   - Interactive charts for user activity
   - Word cloud of frequently used words

## 🚀 How to Run the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/whatsapp-chat-analyzer.git
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\\Scripts\\activate'
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

5. **Upload your exported WhatsApp chat** and start exploring the insights!

## 📷 Screenshots

- **User Activity Heatmap**: When are users most active?
- ![image](https://github.com/user-attachments/assets/9b473ddc-9993-4806-8474-94389e4560b0)

- **Word Cloud**: Visualize the most common words.
- ![image](https://github.com/user-attachments/assets/3f653ad4-97d8-4987-937f-026dc72e78ff)

## 📌 Future Enhancements

- Sentiment analysis of messages
- Multi-chat comparison
- More advanced filters and queries


## 📧 Contact

For any questions or feedback, reach out via [vinaykhatri292@gmail.com](mailto:your-email@example.com).

---

⭐ If you find this project helpful, give it a star on GitHub!

