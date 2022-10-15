## Confessions Image Creator

![preview image](https://github.com/UnidentifiedX/Confessions-Image-Creator/blob/master/images/preview.png?raw=)

### Running the program
First, install the required dependencies

`pip install -r requirements.txt`

You may then run the program through the command line. Create an excel file, and name a column the same as the confession question, e.g. if your confession question is "Enter your confession:", the excel column header should be "Enter your confession:".

Place the excel file in `./src/files`. Or, you may reference the file in other directories using the flags listed below. 

The default html file to reference is `mimic.html`. The default output folder is in `/runs`. Do note that every time you run the program, images generated from previous runs will be overwritten.


**CLI Flags**
|Flag|Expected Input|Remarks|
|---|---|---|
|`--file`, `-f`|`str`, A file path|Path of referenced excel file|
|`--question`, `-q`|`str`|Set question for the form; do note that this has to be the same as the column name in the excel file to work|
|`--save-path`, `-s`, `-o`|`str`, A file path|Output path for image(s)|
|`--model`, `-m`|`str`, A file path|Path to model HTML file|