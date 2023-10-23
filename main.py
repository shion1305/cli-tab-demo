from pyreadline import Readline
from pyreadline.unicode_helper import ensure_unicode

readline = Readline()


# カスタム補完の定義
def custom_completer(text, state):
    commands = ['list', 'create', 'delete', 'update']  # 利用可能なコマンドの例
    options = [command for command in commands if command.startswith(text)]

    try:
        return ensure_unicode(options[state])  # 次の補完候補を返す
    except IndexError:
        return None  # 該当する補完がない場合


# 補完機能を設定
readline.set_completer(custom_completer)
readline.parse_and_bind('tab: complete')


def main():
    while True:
        # ユーザーからの入力を待ち受ける
        user_input = input('Command> ')
        if user_input == 'exit':
            break  # 'exit'コマンドでループを抜ける
        # 他のコマンド処理...
        print(f'You entered: {user_input}')


if __name__ == '__main__':
    main()
