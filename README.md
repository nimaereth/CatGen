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



# Adding the JSON file to your Clan
Steps for adding exported cats to your Clan save:
1. Once you've finished customising your cat, navigate to the export tab click on "export json".
![image](https://user-images.githubusercontent.com/127260133/223848788-9b0ec56b-46a1-479f-8ab7-3704f1d4e24f.png)

2. Your cat's json will be saved to the savedcats folder with the name [prefix][suffix][ID]json.json
![image](https://user-images.githubusercontent.com/127260133/223848969-420a784d-5323-4c71-b91d-325c13e71caa.png)

3. Open up this json file (with notepad, for example) and copy the text.

4. In your CLANGEN folder, navigate to your current clan's folder and open clan_cats.json
![image](https://user-images.githubusercontent.com/127260133/223849160-18ab7166-7296-40bd-a1fb-5bd0733d9b89.png)

5. Paste in the text you copied at the end of the file (+ Make sure formatting is OK).

6. In your clan's JSON file, add in your customised cat's ID to the list of cats.
![image](https://user-images.githubusercontent.com/127260133/223849396-fa2b8d90-32ae-48fd-8a14-c166ebecfad3.png)
![image](https://user-images.githubusercontent.com/127260133/223849432-cb0c749a-de09-477a-bfba-962a7f1738a0.png)

7. Run your game.
