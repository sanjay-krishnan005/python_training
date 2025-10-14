while True:
    user = input("You:")
    if user.lower() in ["hi", "good morning"]:
        print("chatbot: hi how are you")
    elif user.lower() in ["i am sanjay", "my name is sanjay"]:
        print("chatbot: nice to meet you sanjay")
    elif user.lower() in ["who are you", "who", "what are you", "who is created you"]:
        print("chatbot: i am a simple chatbot created by you")
    elif user.lower() in ["whatv type of programming language did you accept", "coding", "what type of compiler you  use"]:
        print("chatbot: i am running in python")
    elif user.lower() in ["did you make websites", "did you make diagram"]:
        print("chatbot: no, i am currently in chat mode but i will make when you modify me")
    elif user.lower() in ["tell me about yourself"]:
        print("chatbot: i am simple chatbot if you give me input that is presented in this list i am excecuted")
    elif user.lower() in ["did you eat"]:
        print("chatbot: i am a machine i can't eat but i ate eletricity of power")
    elif user.lower() in ["ok good bye", "bye", "end"]:
        print("chatbot: bye, nice meeting you sanjay")
        break
    else:
        print("chatbot: give correct sentence to  talk")
