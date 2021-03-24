# FollowbackChecker
Github crosschecker for those who follow me and who I should follow. Automatically runs on schedule and creates an issue when a change is detected.

## Features
1. Checks if you need to follow back someone or if someone has unfollowed you
2. Creates and assigns an issue to yourself containing the warning
3. Runs on a schedule via a cron job

## How to use
1. Fork this repo
2. Enable `Issues` in the `Settings` of the forked repo
3. Modify `check.py` and update the github profile link to your own.
4. Modify `needf.md` and `notf.md` inside `/.github`, change the assignee to your github username

### Modifying the check frequency
1. You may change the frequency to your own liking
2. Change the `schedule` on /.github/workflow/ci.yml, the default is every 4 hours

Note: The first run will trigger 4 hours after you set this up
