import webbrowser, sys, pyperclip

#sys.argv => ['mapit.py','870']

if len(sys.argv)> 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)