import streamlit as st
from analyzer import TextAnalyzer

def main():
    # UI Guidelines: Simple and clean single-page interface
    st.set_page_config(page_title="Text Insight Pro", layout="centered")
    st.title("Text File Analyzer")
    st.write("Upload a text file to get instant insights and statistics.")

    # 1. File Uploading (File Handling Requirement)
    uploaded_file = st.file_uploader("Choose a .txt file", type=['txt'])

    if uploaded_file is not None:
        try:
            # Error Handling: Check if the file is empty or unreadable
            stringio = uploaded_file.getvalue().decode("utf-8")
            
            if not stringio.strip():
                st.warning("The uploaded file is empty. Please upload a file with content.")
                return

            # Instantiate our OOP class
            analyzer = TextAnalyzer(stringio)

            # 2. Display Metrics (UI Layout)
            st.subheader("Key Statistics")
            col1, col2, col3 = st.columns(3)
            
            col1.metric("Words", analyzer.get_word_count())
            col2.metric("Characters", analyzer.get_char_count())
            col3.metric("Sentences", analyzer.get_sentence_count())

            # 3. Optional Features (Frequency Analysis)
            st.divider()
            st.subheader("Most Frequent Words")
            freq_data = analyzer.get_frequent_words()
            
            for word, count in freq_data:
                st.write(f"**{word}**: {count} times")

            # 4. Preview Section
            with st.expander("View Raw Text"):
                st.text(stringio)

        except Exception as e:
            # Error Handling: Catch decoding errors or unexpected crashes
            st.error(f"An error occurred while processing the file: {e}")

if __name__ == "__main__":
    main()