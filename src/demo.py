import autogen

llm_config = {"config_list": [{
    "model": "hermes-3-llama-3.2-3b", 
    "base_url": "http://localhost:1234/v1",
    "api_key": "NULL", # just a placeholder
}]}

cathy = autogen.ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = autogen.ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=6)


# import autogen

# llm_config = {"config_list": [{
#     "model": "hermes-3-llama-3.2-3b", 
#     "base_url": "http://localhost:1234/v1"
# }]}

# bob = autogen.AssistantAgent(
#     name="Bob",
#     system_message=""""
#       You love telling jokes. After Alice feedback improve the joke. 
#       Say 'TERMINATE' when you have improved the joke.
#     """,
#     llm_config=llm_config
# )

# alice = autogen.AssistantAgent(
#     name="Alice",
#     system_message="Criticise the joke.",
#     llm_config=llm_config
# )

# def termination_message(msg):
#     return "TERMINATE" in str(msg.get("content", ""))

# user_proxy = autogen.UserProxyAgent(
#     name="user_proxy",
#     code_execution_config={"use_docker": False},
#     is_termination_msg=termination_message,
#     human_input_mode="NEVER"
# )

# groupchat = autogen.GroupChat(
#     agents=[bob, alice, user_proxy],
#     speaker_selection_method="round_robin",
#     messages=[]
# )

# manager = autogen.GroupChatManager(
#     groupchat=groupchat, 
#     code_execution_config={"use_docker": False},
#     llm_config=llm_config_local,
#     is_termination_msg=termination_message
# )

# user_proxy.initiate_chat(
#     manager, 
#     message="Tell a joke"
# )