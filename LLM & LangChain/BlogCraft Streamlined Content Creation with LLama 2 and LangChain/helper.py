## Import the Necessary Modules.
 
from langchain_community.llms import CTransformers          ## Imports CTransformers class specifically designed to work with Llama 2 models from the Hugging Face Transformers library.
from langchain.prompts import PromptTemplate                ## Imports PromptTemplate class which helps structure the prompt to be fed to the Llama 2 model.


## Function to get Response fom LLama 2 model

def get_llama_reponse(input_text, no_words, blog_style):                    ## The function get_llama_reponse takes three arguments:
## input_text: The topic of the blog post.
## no_words: The desired number of words in the generated blog post.
## blog_style: The style of the blog post (e.g., informative, humorous, persuasive).    


    ## Call LLama2 model from local, for that only we specifically using Ctransformers

    llm = CTransformers(model = "model\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type = "llama",
                        config={"max_new_tokens":256,        
                                "temperature":0.01})

## CTransformers: This line instantiates a CTransformers object, loading the specified Llama 2 model.
## model: The path to the Llama 2 model file is provided here, if not provide config paramaters it will take as default ones
## model_type: This specifies the type of model, which is "llama" in this case.
## config: This dictionary defines additional parameters for the model:
        ## max_new_tokens: Limits the length of the generated text to 256 tokens.
        ## temperature: Controls the randomness of the generated text (lower values mean more deterministic and focused output).    


    ## Promp Template
    template = """Write a blog for {blog_style} job profile for topic {input_text} with in {no_words} words."""

    prompt = PromptTemplate(input_variables = ["blog_style", "input_text", "no_words"],
                            template = template)

## template: This string defines the structure of the prompt that will be given to the Llama 2 model. It includes placeholders for the blog style, topic, and desired word count.
## PromptTemplate: This creates a PromptTemplate object with the specified template and input variables. This helps organize and format the prompt before sending it to the model.    


    ## Generate the response from LLama 2 model
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words = no_words))
    print(response)
    return response

## prompt.format: This fills in the placeholders in the template with the actual values provided as function arguments.
## llm(): The formatted prompt is passed to the Llama 2 model, which generates the text for the blog post.
## print(response): The generated text is printed to the console.
## return response: The generated text is returned by the function for further use.