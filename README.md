# CatGen - a ClanGen Tool
by Nimaereth

CatGen is a [ClanGen](https://github.com/Thlumyn/clangen) tool used to create cats to add to your ClanGen save files.
This tool allows you to generate cats and export their corresponding .json files as well as their sprites as transparent .png files.
Your saved cats and images will be found in the savedcats folder. 


Please do not use generated images for commercial purposes, and do not claim any artwork as your own.

Requirements:
- pygame
- pygame-gui
- ujson

Disclaimer: this tool uses art assets and reuses code from [ClanGen](https://github.com/Thlumyn/clangen).


Steps for adding exported cats to your Clan save:
1. Once you've finished customising your cat, navigate to the export tab click on "export json".
2. Your cat's json will be saved to the savedcats folder with the name [prefix][suffix][ID]json.json
3. Open up this json file (with notepad, for example) and copy it.
4. In your CLANGEN folder, navigate to your current clan's folder and open clan_cats.json
5. Paste in the text you copied at the end of the file (+ Make sure formatting is OK).
6. In your clan's JSON file, add in your customised cat's ID to the list of cats.
7. Run your game.
