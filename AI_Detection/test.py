import pandas as pd
import io

# Carica il CSV in un DataFrame
df = pd.read_csv('final_result.csv')

# Funzione per convertire la stringa di un DataFrame in un vero DataFrame
def convert_to_dataframe(df_string):
    return pd.read_csv(io.StringIO(df_string.strip()), sep='\s{2,}', engine='python')

abstract_df_string = df.loc[1, 'abstract_sentence']
abstract_df = convert_to_dataframe(abstract_df_string)

print(abstract_df['label'])


