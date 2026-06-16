from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

template = "write the email with {tone} to {receiver}"

# Convert the plain template string into a reusable ChatPromptTemplate object.
#
# Think of this as creating a "blueprint" that knows:
#   1. What the template looks like
#   2. Which placeholders need values
#   3. That this template represents a HumanMessage
#
# Conceptually:
#
# ChatPromptTemplate
#        ↓
# Template: "Write an email with a {tone} tone to the {receiver}."
# Variables: ["tone", "receiver"]
# Message type: HumanMessage
#
# Note:
# use `from_template()` where we only have a single HumanMessage template.

prompt_template = ChatPromptTemplate.from_template(template)

# Render the blueprint by replacing the placeholders with actual values.
#
# This produces a ChatPromptValue containing the final chat messages.
# Since we used `from_template()`, the output contains a HumanMessage
# whose content is the fully formatted prompt.
#
# If we had used `from_messages()`, we could define the complete
# conversation structure explicitly (SystemMessage, HumanMessage,
# AIMessage placeholders, chat history, etc.).
#
# Flow:
#
# ChatPromptTemplate
#        ↓ invoke({...})
# Replace placeholders
#        ↓
# ChatPromptValue
#        ↓
# [HumanMessage(...)]
#
# Ready to be passed to llm.invoke(...)
#
# Note:
# prompt is a ChatPromptValue, which internally contains the generated messages.
# ChatPromptValue(
#     messages=[
#         SystemMessage(...)
#         HumanMessage(...)
#     ]
# )

prompt = prompt_template.invoke({
    "tone": "formal",
    "receiver": "HR"
})
 

# now this prompt is the message ready to be passed to an llm
result = model.invoke(prompt)

print(result.content)
