# CP77-ModSettings-Translator
[![Support Me on Ko-fi](https://i.imgur.com/7Cm07AZ.png)](https://ko-fi.com/siriusbeck)

Simple tool to make the translation of mods that use ModSettings as little manual as possible, I'm still working on a set of tools for those who create mods for Cyberpunk 2077 but due to lack of time it will take a while to come out a usable version .

Unfortunately I didn't find any way to use ArchiveXL's localization system or Codeware's (which by the way are amazing) together with ModSettings, because it's not possible to pass a variable as one of the `@runtimeProperty` parameters in redscript, which is the way ModSettings works to add items to your mod's menu.

Using this tool, it will still be necessary to install your mod + the translation mod, in case the people who are going to use it don't want to use it in its default language, but it will still make it a lot easier to translate it, even for other people who want to translate your mod's menu.

## How to use
1. First let's prepare our mod and its structure, for that, everything you do related to ModSettings must be done in a separate file, for this example, I created a file called `ModSettings.reds` inside the folder where the files are **.reds** from my mod, the name of this file is irrelevant, I put it like this for organization reasons.

2. Now, inside the same folder where the file we just created is, we will create a folder called `localization` and inside it we will create a json file for each language that we want to have in the mod, I will only use English and Brazilian Portuguese, the name of these files must be according to the game's language code.
   
   | Code    | Language               | Code    | Language             |
   |:------- |:---------------------- |:------- |:-------------------- |
   | `pl-pl` | Polish                 | `ru-ru` | Russian              |
   | `en-us` | English                | `pt-br` | Brazilian Portuguese |
   | `es-es` | Spanish                | `jp-jp` | Japanese             |
   | `fr-fr` | French                 | `zh-tw` | Traditional Chinese  |
   | `it-it` | Italian                | `ar-ar` | Arabic               |
   | `de-de` | German                 | `cz-cz` | Czech                |
   | `es-mx` | Latin American Spanish | `hu-hu` | Hungarian            |
   | `kr-kr` | Korean                 | `tr-tr` | Turkish              |
   | `zh-cn` | Simplified Chinese     | `th-th` | Thai                 |
   
   The folder of our mod, at the moment, looks like this:
   ```
   |→ localization\en-us.json
   |→ localization\pt-br.json
   |→ MyMod.reds
   |→ ModSettings.reds
   ```

3. In place of all the `@runtimeProperty` fields where you would put the text that will be displayed to the player, you will put a brace. Remember that each key needs to be different from the other.
   ```swift
   module ExperienceManager.UI
   
   public class RespecModSettings {
     @runtimeProperty("ModSettings.mod", "Experience Manager")
     @runtimeProperty("ModSettings.category", "em-ms-category-respecCost")
     @runtimeProperty("ModSettings.displayName", "em-ms-displayName-NoRespecCost")
     @runtimeProperty("ModSettings.description", "em-ms-desc-NoRespecCost")
     let freeRespecCost: Bool = false;
   
     @runtimeProperty("ModSettings.mod", "Experience Manager")
     @runtimeProperty("ModSettings.category", "em-ms-category-respecCost")
     @runtimeProperty("ModSettings.displayName", "em-ms-displayName-multRespecCost")
     @runtimeProperty("ModSettings.description", "em-ms-desc-multRespecCost")
     @runtimeProperty("ModSettings.step", "0.5")
     @runtimeProperty("ModSettings.min", "0.5")
     @runtimeProperty("ModSettings.max", "100.0")
     let multiplierRespecCost: Float = 1.0;
   }
   ```
   
   Note that each of the keys is different from each other, their name is irrelevant but I recommend giving them names that make sense of the value they will actually have.

4. Now let's go to the json file, it should follow the following pattern:
   ```json
   {
       "file": "ModSettings.reds",
       "lang": "en-us",
       "entries": [
           {
               "key": "em-ms-category-respecCost",
               "value": "Respec Cost"
           },
           {
               "key": "em-ms-displayName-NoRespecCost",
               "value": "No Respec Cost"
           },
           {
               "key": "em-ms-desc-NoRespecCost",
               "value": "There will be no cost to reset skill points. The value in the multiplier below will be ignored."
           },
           {
               "key": "em-ms-displayName-multRespecCost",
               "value": "Multiplier"
           },
           {
               "key": "em-ms-desc-multRespecCost",
               "value": "The experience gained will be multiplied by the value of this field."
           }
       ]
   }
   ```
   
   Note that in `key` I put the same keys as in the `ModSettings.reds` file and in `value` is the text I want to be displayed.
   
   You will do this for all the languages ​​you want, my tip is to do the `en-us.json` first, and then use the VsCode extension [Coment Translate](https://marketplace.visualstudio.com/items?itemName=intellsmi.comment-translate) to translate the value fields.

5. Now, finally, let's use the tool, this is the easiest part of all, just run the `Translator.exe` file and enter the path to your `ModSettings.reds` file and the [language code](## How to use)
   ![Example 01](https://raw.githubusercontent.com/pySiriusDev/CP77-ModSettings-Translator/main/docs/print_01.png)

6. In the image I used `pt-br`, so, inside the `localization` folder that we created in step 2, a folder was created with the name `pt-br` and, inside it, a new file `ModSettings.reds` translated. The tool will replace all the keys you have placed with the values ​​informed in the json file, as follows:
   
   ```swift
   module ExperienceManager.UI

   public class RespecModSettings {
     @runtimeProperty("ModSettings.mod", "Experience Manager")
     @runtimeProperty("ModSettings.category", "Custo de Respeito")
     @runtimeProperty("ModSettings.displayName", "Sem Custo de Respeito")
     @runtimeProperty("ModSettings.description", "Não haverá custo para redefinir os pontos de habilidade. O valor no multiplicador abaixo será ignorado.")
     let freeRespecCost: Bool = false;

     @runtimeProperty("ModSettings.mod", "Experience Manager")
     @runtimeProperty("ModSettings.category", "Custo de Respeito")
     @runtimeProperty("ModSettings.displayName", "Multiplicador")
     @runtimeProperty("ModSettings.description", "A experiência adquirida será multiplicada pelo valor deste campo.")
     @runtimeProperty("ModSettings.step", "0.5")
     @runtimeProperty("ModSettings.min", "0.5")
     @runtimeProperty("ModSettings.max", "100.0")
     let multiplierRespecCost: Float = 1.0;
   }

   ```
7. Make a copy of the original `ModSettings.reds` file as you will need it whenever you want to translate your mod to a new language, I always use GitHub itself to save my projects and I recommend that you also use it to save all your mod files , this avoids a lot of headaches in the future.

8. Now just replace the original `ModSettings.reds` file with the translated one and your mod is ready to be distributed, the `localization` folder is not necessary for the mod to work and you can delete it if you want.


One tip I gave is that when you post your mod on the Nexus or elsewhere, make the `en-us.json` file available separately so people can download, translate, and re-upload it to you, so you can have your mod in several languages ​​without having to translate it yourself to each existing language. Remember that the mod community is usually united for everyone's fun so don't be different haha, whenever you can, make life easier for other modders just like other modders make yours easier ;), and whenever you use the content from another mod whose permission has been given, leave the credits to the current creator, it's free and a great behavior towards the community that always strives MUCH MORE than the game developers themselves for everyone to always have good hours of fun.