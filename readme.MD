# Bookyway Automation
by Davide Ponzini

## Requirements
The following programs are needed to run these scripts:
* Python3
* Chromedriver (https://chromedriver.chromium.org/)
* All packages listed in `requirements.txt`

## Configuration
Write your Bookyway credentials in `secret.py`.

## Usage
Run `main.py` from command line. Argoments are as follows:
* `username`: full name of the person(s) to edit
* `credits`: new credit balance for each person selected with `username`
* `reason`: note to be added to each transaction

### Notes
* An incomplete username can select multiple persons; e.g. *"dav"* can select both *"Dave"* and *"David"*.
  * This feature also works with usernames.
* An empty username will select **everyone**.
