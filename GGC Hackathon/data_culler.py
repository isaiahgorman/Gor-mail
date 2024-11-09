import pandas as pd

df = pd.read_csv(r"C:\Users\isaia\OneDrive\GGC Hackathon\500 emailss.csv")
print(df.columns)
df.columns = df.columns.str.strip()

#only take out email subject and message and get rid of the rest
df_cleaned = df[['email', 'subject', 'message']]

#no whitespace
df_cleaned['subject'] = df_cleaned['subject'].str.strip()
df_cleaned['message'] = df_cleaned['message'].str.strip()

#get rd of empty rows
df_cleaned = df_cleaned.dropna(subset=['email', 'subject', 'message'])

# Save it to a new CSV
df_cleaned.to_csv(r"C:\Users\isaia\Downloads\cleaned_email_data_with_messages.csv", mode= 'a', index=False)


