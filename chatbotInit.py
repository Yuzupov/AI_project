from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts.prompt import PromptTemplate 
from lanchain.chains.llm import LLMChain 
from langchain.schema import BaseLLMOutputParser

import langchain
lanchain.__version__

pipeline_inst = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    use_cache=True,
    max_new_tokens=100,
    do_sample=True,
    top_k=10,
    repetition_penalty=1.2,
    no_repeat_ngram_size=2,
    temperature=0.01,
    top_p=0.9,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.eos_token_id
)

llm = HuggingFacePipeline(pipeline=pipeline_inst)

template = """[INST]You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.
Your answers should not include any harmful, unethical answers.
Answer the question below from the context below :
Context : {context}
Question : {question}
[/INST]
"""
