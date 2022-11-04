# Steps taken to gather data

## Step 1:
> Create a new Google cloud project, with following apis enabled:  
>- Custom Search API  
>- Google Sheets API  
>- Google Cloud Storage API  
>
> Create an api key for the Custom Search API and a service account .  

## Step 2:
> Install Dendencies: pip install google-ap-client
> Run CreateFileStructure.py to created data file structure

## Step 3:  

>  Now the src folder contains the following files:  
>-  GetData.py: This file contains the code to get the data from the Custom Search API.
>- GoogleSheets.py: This file contains the code to write the data to Google Sheets.
>- main.py: This file contains the code to run the above two files.

## Limitaions:
> One account has 12 project(api-keys).
> 1 project(api-key) can give 1000 images per day.
> I have 4 project running, so in total 48 api keys.
> We can collect 48,000 images/day.
> We have in total 528 keywords https://ads-keyword-visualisation.herokuapp.com/
> On average per keyword we can collect 90 images.
