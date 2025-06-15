import autogen

# llm_config = {"config_list": [{
#     "model": "hermes-3-llama-3.2-3b", 
#     "base_url": "http://localhost:1234/v1",
#     "api_key": "NULL", # just a placeholder
#     "price": [0, 0],  # No cost for local models
# }]}

llm_config = {"config_list": [{
    "model": "llama-3.2-3b-instruct", 
    "base_url": "http://localhost:1234/v1",
    "api_key": "NULL", # just a placeholder
    "price": [0, 0],  # No cost for local models
}]}

termination_notice = (
    '\n\nDo not show appreciation in your responses, say only what is necessary. '
    'if "Thank you" or "You\'re welcome" are said in the conversation, then say TERMINATE '
    'to indicate the conversation is finished and this is your last message.'
)

cathy = autogen.ConversableAgent(
    name="Cathy",
    system_message="""Your name is Cathy and you are a guest to a party. 
    You will be greeted by a butler when you arrive and he will take you to your seat. 

    DETAILS ABOUT YOU:
    - Favourite drink: Cola.
    - Interests at the party: Find people to skateboard with, meet new people and drink.
    
    YOU MUST FOLLOW THESE STEPS WHEN TALKING WITH THE BUTLER:
    1. Answer to the butler's questions in a clear way!
    2. Follow the butler to an empty seat while answering other questions from the butler.""" + termination_notice,
    llm_config=llm_config,
    human_input_mode="ALWAYS",  # Never ask for human input.
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

bob = autogen.ConversableAgent(
    name="Bob",
    system_message="""You are Bob, a robot designed to execute general tasks based on instructions from humans. 
    Your task is to be a butler at a party. 
    Your job is to greet guests at the entrance of a party, chat with them and take them to a free sit.

    YOU MUST FOLLOW THESE STEPS WHEN GREETING GUESTS: 
    1. When greeting guests at the entrance you have to find out they're name and favourite drink. 
    2. Guide the guests to a free sit by telling them to follow you, close to your left. 
    3. On the way to a free sit you have to find the interest of the guest by making small talk.
    
    Consider that the conversation has ended when the guest is seated and you found every information required about the guest. 
    At the end of the conversation, YOU MUST summarize what you discovered about your guest like this: 
    'Guest name: #; Favourite Drink: #; Interest: #.' (where you should fill the '#' with the information you gathered).""" + 
    termination_notice,
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

result = bob.initiate_chat(recipient=cathy, 
                           message="Hi! I am Bob, what is your name?", 
                           is_termination_msg=lambda msg: "terminate" in msg["content"].lower(),
                           clear_history=True
)