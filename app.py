import streamlit as st
from langchain import PromptTemplate
from langchain_openai import OpenAI


#LLM and key loading function
def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm


#Page title and header
st.set_page_config(
    page_title="Blog Post Generator",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://genaiexpertise.com/contact/",    
        "Report a bug": "https://github.com/genaiexpertise/RAGApps/issues",
        "About": "https://genaiexpertise.com",
    },
)



st.header("Blog Post Generator")


#Intro: instructions
col1, col2 = st.columns(2)

# with col1:
#     st.markdown("Blog Post Generator")

with col2:
    st.write("Contact with [GenAIExpertise](https://genaiexpertise.com) to build your AI Projects")



#Input OpenAI API Key
def get_openai_api_key():
    st.sidebar.markdown("## Enter Your OpenAI API Key")
    input_text = st.sidebar.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input", type="password")
    return input_text

openai_api_key = get_openai_api_key()


#

def generate_response(topic):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    As experienced startup and generative AI Engineers,
    generate a 400-word blog post about {topic}
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return st.write(response)

topic_text = st.text_input("Enter topic: ")
if st.button("Generate Blog"):
    if not openai_api_key.startswith("sk-"):
        st.warning("openai_api_key not found. Please add it to the sidebar.")
    if openai_api_key.startswith("sk-") and topic_text:
        generate_response(topic_text)
        