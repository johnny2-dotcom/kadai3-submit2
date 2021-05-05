import pandas as pd
import eel


# @eel.expose
def kimetsu_search(word,csv_name):
    df_name = pd.read_csv('./{}'.format(csv_name))
    names = df_name['0'].tolist()

    if word == "":
        print('検索ワードを入力してください。')
        eel.view_log_js('検索ワードを入力してください。')
    else:
        if word in names:
            # df_names = pd.DataFrame(word)
            # df_names.to_csv('source.csv')
            print('{}が見つかりました。'.format(word))
            eel.view_log_js('{}が見つかりました。'.format(word))
        else:
            print('{}が見つかりません。'.format(word))
            names.append(word)
            df_names = pd.DataFrame(names)
            df_names.to_csv('source.csv')
            print('{}を追加しました。'.format(word))
            eel.view_log_js('{}が見つかりません。'.format(word))
            eel.view_log_js('{}を追加しました。'.format(word))

# eel.init("html")
# eel.start("index.html")
# if __name__ == "__main__":
#     search_write_name()