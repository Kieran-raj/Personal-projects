def choose_language():
	lang = input('''Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French\n''')
	word = input('Type the word you want translate:\n')
	print(f'You chose "{lang}" as the language to translate "{word}" to.')

if __name__ == '__main__':
	choose_language()



