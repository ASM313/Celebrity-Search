from app import client
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.memory import ConversationBufferMemory


st.title("Celeb search")

input_text = st.text_input("Ask me about any celeb")

# Memory

person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')

dob_memory = ConversationBufferMemory(input_key='person', memory_key='dob_history')

events_memory = ConversationBufferMemory(input_key='dob', memory_key='events_history')


# Prompt Template

first_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name}"
)

# Chains

chain1 = LLMChain(llm=client, prompt= first_prompt, verbose=True, output_key='person', memory=person_memory)

# Prompt Template

second_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born"
)

# Chains

chain2 = LLMChain(llm=client, prompt= second_prompt, verbose=True, output_key='dob', memory=dob_memory)

# Prompt Template

third_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events happened around the world on this {dob}"
)

# Chains

chain3 = LLMChain(llm=client, prompt= third_prompt, verbose=True, output_key='events', memory=events_memory)


# Parent Chain

## It only shows last chain output
# parent_chain = SimpleSequentialChain(chains=[chain1,chain2], verbose=True)


parent_chain = SequentialChain(chains=[chain1,chain2, chain3], input_variables=['name'], output_variables=['person', 'dob', 'events'],  verbose=True)

if input_text:
    # st.write(parent_chain.run(input_text))
    
    st.write(parent_chain({'name':input_text}))
    
    with st.expander("Person Name"):
        st.info(person_memory.buffer)
    
    with st.expander("Major Events"):
        st.info(events_memory.buffer)

