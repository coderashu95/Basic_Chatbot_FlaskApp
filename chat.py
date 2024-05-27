from db_call import QASystem
import pandas as pd

def chatbot(input):
    # First try to get a response from the QASystem
    # Initialize the QASystem
    qa = QASystem('test.csv')
    try:
        qa_response = qa.get_response(input)
        print("Try")
    except:
        qa_response = "I can't answer this question."
        print("Except")

        # Save the question and the AI's response to the CSV file
        #df = pd.DataFrame([['"' + input + '"', '"' + reply + '"']], columns=['Questions'])

        # Save the question to the CSV file, so that customer success team can later take a look at it and answer it appropriately
        df = pd.DataFrame(['"' + input + '"'], columns=['Questions'])
        df.to_csv('bank.csv', mode='a', header=False, index=False)

    return qa_response