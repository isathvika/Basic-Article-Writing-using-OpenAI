from openai import OpenAI
import streamlit as st

clt = OpenAI(
  #defaults to os.environ.get("OPENAI_API_KEY")
  api_key = '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'

def main():
  st.title("Article Writer")
  notes = st.text_area("Enter Topic Information:")
  content = "I want you to write shortliterature review on topic" +notes
  if st.button("Generating Article"):
    with st.spinner("Generating Article...."):
      response = clt.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{'role':'user','content':content}]
      )
    description=response.choices[0].message.content
    st.subhead("Generated Writeup:")
    st.write(description)
