# Discord management tools

## Requirements

You need to have a Discord token either in a file called `.env` in the
current working directory containing `DISCORD_TOKEN=xxx` or export this
variable before running the scripts.

Install the required libraries via:

```shell
pip install -r requirements.txt
```

## match_names.py

Based on an Excel sheet containing the participants' names, try to match
those to the Discord server's user names (who are not facilitators).

## create_channels.py

Create a participant and a facilitator role for each exercise as well as
a corresponding category that then contains 5 voice and text channels.

## assign_roles.py

Assign roles to participants based on a Google spreadsheet.
