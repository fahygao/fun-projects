import sqlite3  # Import sqlite to query sql data

DATABASE = 'ChineseSlangWords.db'  # Initiate database name


def query_word_search(word):
    conn = sqlite3.connect(DATABASE)  # Establish a connection to the SQLite database
    cursor = conn.cursor()  # Create a cursor to retrieve data from the database
    cursor.execute("""
                    SELECT * 
                    FROM slang_long_short
                    WHERE word = ?;
                  """, (word,))  #
    conn.close()  # Close dbase connections
    return [j for i in definitions for j in i]


if __name__ == "__main__":
    while True:
        search = input("你想搜什么梗词？")
        if search:
            print(f'收到，您想搜的梗词为 {search}')
            defi = query_word_search(search.lower())
            if defi:
                print("----------解释如下-------------")
                if defi[2]:
                    if defi[2] != defi[1]:
                        print(f'短释义: {defi[2]} \n长释义: {defi[1]}\n创建时间: {defi[3]}')
                        continue
                print(f'长释义: {defi[1]} \n创建时间: {defi[2]}')
            else:
                print(f'不好意思"{search}"尚未登陆词堂哦~')
        else:
            print("退出成功！")
            break
