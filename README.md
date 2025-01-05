# AI_project

For this AI project there is some setup needed. It might take quite some time if you need to train it on your own model. Expect about 1.5 - 2 hours for the training with the dataset used.

## Setup
It is important you create a file within the same directory as the "chatbot.py" file called "apikey.txt" and put your api key in it. Put it plain and don't add quotations around it.
### Packages needed
openai, json, datasets, os.
Use "$ pip install <package-name>" to install them, depending on your environment it may be needed to add "--break-system-packages", making the prompt look like: "$ pip install <package-name> --break-system-packages".

htmx module 28.* is in the current state unusable due to removing a still used method. Therefore you need to downgrade to htmx v. 0.27.2 with "pip install htmx==0.27.2" for the prompts to execute correctly. After installing the potential dependencies, run the setup.py file.
## Using the bot
Run the chatbot.py file to start the bot. Input your prompt to the bot and wait for it to return the response in the terminal window
### If training your own model
If you want to use your own model you need to train it. Currently the modelId that is used in the chatbot is the one trained on a huggingface agile dataset (https://huggingface.co/datasets/nalmeida/agile_dataset_fusionado). If you are training your own model you need to change the modelId in the chatbot.py file to the one matching yours. Then you also need to runthe setup script and change the relevant fields such as dataset used etc.
