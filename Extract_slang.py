import pandas as pd
from datetime import date
import sqlite3


def extract_concat_df(filenames):
    """Extract and concat cleaned data
    filenames: csv to look for
    return:
    allSlang_df: dataframe that contains all unique words, long definitions, short definitions and date.
    """
    allSlang_df = pd.DataFrame()
    for filename in filenames:
        df = pd.read_csv(f'{filename}.csv')

        # data cleaning
        if '解释+出处：' in df.columns:
            df = df.rename(columns={'解释+出处：': 'long_definition'})
        if '长释义' in df.columns:
            df = df.rename(columns={'长释义': 'long_definition'})
        if 'long-definition' in df.columns:
            df = df.rename(columns={'long-definition': 'long_definition'})
        if '短释义' in df.columns:
            df = df.rename(columns={'短释义': 'short_definition'})
        if 'short-definition' in df.columns:
            df = df.rename(columns={'short-definition': 'short_definition'})

        df = df[['word', 'long_definition', 'short_definition']]
        df = df.dropna(subset=['word', 'long_definition'])
        if not len(allSlang_df):
            allSlang_df = df
        else:
            allSlang_df = pd.concat([allSlang_df, df], ignore_index=True)

        # create date
        allSlang_df['date'] = date.today()
        allSlang_df = allSlang_df.drop_duplicates(subset=['word']).reset_index(drop=True)
    return allSlang_df


def upload_to_sqlite(df, table_name, conn):
    """Upload a dataframe to SQLite database.
    df: the dataframe to upload.
    table_name: the name of the table to create in the database.
    conn: SQLite database connection.
    """
    df.to_sql(table_name, conn, if_exists='replace', index=False)


def main():
    filenames = ["google_form_slangs", "google_form_slangs2", "google_form_slangs3", "lark_slangs"]
    dbname = "ChineseSlangWords"
    concat_df = extract_concat_df(filenames)

    # Upload dataframes to SQLite
    conn = sqlite3.connect(f"{dbname}.db")
    try:
        upload_to_sqlite(concat_df, 'slang_long_short', conn)
        print("Data uploaded successfully.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
