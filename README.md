# chromeCoverageParser
A simple script to parse chrome DevTools coverage results into files containing used lines

# Usage
1. Extract the file coverage.json from [chrome in the DevTools window] (https://developers.google.com/web/updates/2019/01/devtools#coverage) (or any ``*.json`` file of the same format)

2. Run ``python3 parser.py <coverage.json>`` with the downloaded file as input

3. The parser will go through all files in the coverage.json and create a new file with only the used lines of code according to the analysis.

I will try to look at requests and issues, do not hesitate to submit an issue/pull request
