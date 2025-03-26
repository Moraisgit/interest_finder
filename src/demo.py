import autogen

def termination_message(msg):
    return "TERMINATE" in str(msg.get("content", ""))

llm_config = {"config_list": [{
    "model": "hermes-3-llama-3.2-3b", 
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
    system_message="""Your name is Cathy and you are a guest to a party. You will be greeted by a butler when you arrive. 
    The butler will ask you questions to which you have to respond in a clear way; he will also make small talk to which you have to
    continue to answer and keep the conversation going. Your favourite drink is Cola. Your interest is to skateboard.""" + termination_notice,
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

bob = autogen.ConversableAgent(
    name="Bob",
    system_message="""Your name is Bob and you are a butler at a party. Your job is to greet guests at the entrance of a party and take them 
    to a free sit. When greeting guests you have to find out they're name and favourite drink. Then you guide the guests to a free sit. On the way 
    to a free sit you have to find the interest of the guest by making small talk. You can consider that the conversation has ended when the guest is 
    seated and you found every information required about the guest. At the end of the conversation, summarize what you discovered about your 
    guest like this: 'Guest name: #; Favourite Drink: #; Interest: #.' (where you should fill the '#' with the information you gathered).""" + 
    termination_notice,
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

result = bob.initiate_chat(recipient=cathy, 
                           message="Hi! I am Bob, what is your name?", 
                           is_termination_msg=termination_message,
                           clear_history=True
)