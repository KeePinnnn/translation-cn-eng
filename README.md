# translation-cn-eng

The purpose of this is to allow user to translate chinese character words into english easier through the use of youdao.com. 

It is painful to make use of online translator such as google translate to translate a large number of words. Thus, I decided to write a quick translator whereby I will only have to add the chinese characters into an excel file and I will be able to translate most of them to english. 

There will be some words that cannot be translated and they will have to be done manually. In the event that there are too many different words relating to one chinese pharse, I have decided to grab all of them and concat them before inputing it back into excel. I will be able to just make use of excel and make the necessary changes instead of going to and fro to some website to translate the chinese words. 

To use the translator, do a 

``` pip install -r requirement.txt ```

This will install all the dependency for this repo. I will strongly encourage you to create a venv so that this will not mess up with your local pip environment. 

Afterwhich, go into the src folder 

``` cd translation-cn-eng/src ```

and run 

``` python3 run.py ```

Make sure that all the chinese words are put into the translation.xlsx so that you will be not have any errors. 

translation.xlsx is located in 

``` translation-cn-eng/src/excel/ ```

