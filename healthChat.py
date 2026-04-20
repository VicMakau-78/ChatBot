import pandas as pd

# load your data into a dataframe
df = pd.read_csv("health_data.csv")

# print(df)

print("HealthBot: Hello there, I am your health Assistance Bot. Ask me about any symptoms")

while True:
    # 1. Get the user input and store the same into a variable
    user_text = input("\n You: ").lower()

    # print("user entered: ", user_text)
    # break

    # 2. Check if the users want to exit
    if user_text == "quit":
        print("HealthBot: Goodbye! Nice to have been of service to you. Stay Healthy.")
        break

    # Create a variable that will store the details structured in the CSV file
    found_answer = False

    # Come up with a loop that loops through the entire data frame created before
    for index, row in df.iterrows():
        # clean up the keywords from the CSV row
        keywords_list = str(row['Keywords']).split(',')

        # print("The words inside of the variable keywords_list are: ",keywords_list)
        # Below we check every keyword in that given row (Keywords)
        # lower is for lowercase

        for word in keywords_list:
            clean_word = word.strip().lower()  # strip removes the space before or after a given word
            # if the keyword is inside of the user's interface
            if clean_word in user_text:
                print("HealthBot:", row["Response"])
                found_answer = True
                break #stop looking for at other keywords
        
        if found_answer:
            break #Stop looking at other answers since we already found a match

    # 4. If we went through the entire/whole CSV file and never found ay match of the keyword, we need to display a message to the user

    if not found_answer:
        print("HealthBot: Sorry, I don't know that one, Try asking for something else.")


