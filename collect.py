# Collect and process results
import os
import numpy as np
import prompts
import json
import re
import funcs
import pandas as pd
from IPython.display import display, HTML
# .env vars load
from dotenv import load_dotenv
load_dotenv()

# Working directory for project taken from env vars
os.chdir(os.environ.get("ROOT_DIR"))

# Quite standard level of terminal output
verbose = False
# Whether to print additional debug info when collecting results
debug = False

# Model names
modelnames = ["gpt-3.5-turbo", "gpt-4-turbo", "gemini-1.0-pro-001", "meta/meta-llama-3-70b-instruct"]

# Binary output save
output = np.load("data\\output.npy")
# Example JSON output
print(output[0,0,0,0].decode("utf-8"))

disc = pd.DataFrame({'model': [], 'promptIndex': [], 'disconcordant': []})

for modelIndex in range(len(modelnames)):
    for promptIndex in range(prompts.getMaxPrompts()):
        disconcordant = 0
        for inputIndex in range(prompts.getMaxInputs()):
            # Check across triplicates for (dis)concordant output
            if output[0, modelIndex, promptIndex, inputIndex] != output[1, modelIndex, promptIndex, inputIndex] or output[1, modelIndex, promptIndex, inputIndex] != output[2, modelIndex, promptIndex, inputIndex]:
                if verbose:
                    print("Found disconcordant at model " + modelnames[modelIndex] + " promptIndex "
                          + str(promptIndex) + " inputIndex " + str(inputIndex) + ":\n")
                if debug:
                    print("rep0\n" + str(output[0, modelIndex, promptIndex, inputIndex]) + "\n")
                    print("rep1\n" + str(output[1, modelIndex, promptIndex, inputIndex]) + "\n")
                    print("rep2\n" + str(output[2, modelIndex, promptIndex, inputIndex]) + "\n")
                    print("rep0\n" + output[0, modelIndex, promptIndex, inputIndex].decode("utf-8") + "\n")
                    print("rep1\n" + output[1, modelIndex, promptIndex, inputIndex].decode("utf-8") + "\n")
                    print("rep2\n" + output[2, modelIndex, promptIndex, inputIndex].decode("utf-8") + "\n")
                    print("\n" + str(output[0, modelIndex, promptIndex, inputIndex] != output[1, modelIndex, promptIndex, inputIndex]))
                    print("\n" + str(output[1, modelIndex, promptIndex, inputIndex] != output[2, modelIndex, promptIndex, inputIndex]))
                    print("\n\n")
                disconcordant = disconcordant + 1
        if verbose:
            print("Amount of disconcordant sets of replicates in model " + modelnames[modelIndex] + " promptIndex "
                  + str(promptIndex) + ": " + str(disconcordant))
        disc.loc[len(disc.index)] = [modelnames[modelIndex], promptIndex, disconcordant]

print(disc)
# Export disconcordant DF tsv
disc.to_csv("exports\\disconcordant.tsv", sep="\t")

parse = pd.DataFrame({'model': [], 'promptIndex': [], 'parsefail': []})

for modelIndex in range(len(modelnames)):
    for promptIndex in range(prompts.getMaxPrompts()):
        nonparseable = 0
        # Only iterate across proper input in Finnish (or machine-translated English)
        for inputIndex in prompts.getFinInputs() + prompts.getEngInputs():
            try:
                rep0 = json.loads(funcs.jsonSanitize(output[0, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                rep1 = json.loads(funcs.jsonSanitize(output[1, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                rep2 = json.loads(funcs.jsonSanitize(output[2, modelIndex, promptIndex, inputIndex].decode("utf-8")))
            except ValueError:
                if verbose:
                    print("Failed reading JSON at model " + modelnames[modelIndex] + " promptIndex "
                          + str(promptIndex) + " inputIndex " + str(inputIndex) + "\n")
                if debug:
                    print(funcs.jsonSanitize(output[0, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                    print(funcs.jsonSanitize(output[1, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                    print(funcs.jsonSanitize(output[2, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                nonparseable = nonparseable + 1
        if verbose:
            print("JSON parsing for model " + modelnames[modelIndex] + " promptIndex "
                  + str(promptIndex) + " failed count: " + str(nonparseable) + "\n")
        parse.loc[len(parse.index)] = [modelnames[modelIndex], promptIndex, nonparseable]

print(parse)
# Export JSON parseability DF tsv
parse.to_csv("exports\\parsefail.tsv", sep="\t")

# Iterate across aggregated answers from all models/prompts/etc to see the kind of answers obtained
uniqanswers = pd.DataFrame({
    'inputIndex': [], # Index number of the input statement
    'answerIndex': [], # Answered question; total 6 questions (index 0-5)
    'uniqanswers': [] # The numeric/string given answer by the model/prompt/input combo
}, dtype = str) # Force string type for unique answers for convenience

for inputIndex in range(prompts.getMaxInputs()):
    for answerIndex in range(6):
        # Populate unique answer possibilities for a table
        popanswers = pd.DataFrame({
            'model': [],
            'promptIndex': [],
            'answerIndex': [],
            'answer': []
        })
        for modelIndex in range(len(modelnames)):
            for promptIndex in range(prompts.getMaxPrompts()):
                try:
                    js0 = json.loads(funcs.jsonSanitize(output[0, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                    js1 = json.loads(funcs.jsonSanitize(output[1, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                    js2 = json.loads(funcs.jsonSanitize(output[2, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                    # Make consensus choices for choosing the final JSON
                    # TODO
                    js = js0
                    # Only aggregate the parseable JSON answers
                    if len(list(js.values())) == 6:
                        answer = list(js.values())[answerIndex]
                        if isinstance(answer, dict):
                            if isinstance(list(answer), dict):
                                answer = "Error: Nested list"
                            else:
                                answer = "".join(str(list(answer)))
                        elif isinstance(answer, list):
                            answer = "".join(str(list(answer)))
                        popanswers.loc[len(popanswers.index)] = [
                            modelnames[modelIndex],
                            promptIndex,
                            answerIndex,
                            answer
                        ]
                except ValueError:
                    if verbose:
                        print("Parsing JSON-error")
        result = [
            inputIndex,
            answerIndex,
            "".join(str(list(popanswers['answer'].unique())))
        ]
        uniqanswers.loc[len(uniqanswers.index)] = result
        try:
            print(list(popanswers['answer'].unique()))
        except ValueError:
            print("ValueError trying to print unique answer list")

# Export unique answers given by any model/prompt to an input/question combo from DF to tsv
uniqanswers.to_csv("exports\\uniqueanswers.tsv", sep="\t")


uniqanswers.iloc[0:6, 0:3] # Lists of answers to the first input statement across all prompts and models
# Example where Gleasons were expected to be extracted
# Original input:
# "Näytteinä prostatan paksuneulabiopsioita tyyppipaikoista otettuna, yhteispituus oikealta noin 60mm
# ja vasemmalta noin 80mm. Näytteestä B havaitaan karsinoomaa, joka menee jo Gleason tasolle 5 ja kokonais
# Gleason taso on 9 (4+5). Kyseistä muutosta noin 20% vasemmalla. Muissa näytteissä normaalia rauhasrakennetta,
# eikä merkittävää tulehdusta. WHO-luokituksen mukaan gradus 3."
uniqanswers.loc[(uniqanswers["inputIndex"] == 3) & (uniqanswers["answerIndex"] == 2), 'uniqanswers']

answers = pd.DataFrame({
    'model': [], # Name of utilized model
    'promptIndex': [], # Index number of the utilized prompt
    'inputIndex':[], # Index number of the input statement
    'answerIndex':[], # Answered question; total 6 questions (index 0-5)
    'answer':[], # The numeric/string given answer by the model/prompt/input combo
    'correct':[] # Correctness of the answer in comparison to a list of ideal answers; -1 wrong, 0 ambiguous, +1 correct
})

for modelIndex in range(len(modelnames)):
    for promptIndex in range(prompts.getMaxPrompts()):
        for inputIndex in range(prompts.getMaxInputs()):
            try:
                js0 = json.loads(funcs.jsonSanitize(output[0, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                js1 = json.loads(funcs.jsonSanitize(output[1, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                js2 = json.loads(funcs.jsonSanitize(output[2, modelIndex, promptIndex, inputIndex].decode("utf-8")))
                # Make consensus choices for choosing the final JSON
                # TODO
                js = js0
                for answer in range(len(list(js.values()))):
                    answers.loc[len(answers.index)] = [
                        modelnames[modelIndex],
                        promptIndex,
                        inputIndex,
                        answer,
                        list(js.values())[answer],
                        0
                    ]
            except ValueError:
                if verbose:
                    print("Parsing JSON-error")

# Exhaustive listing of answers obtained with each combination from DF to tsv
answers.to_csv("exports\\answers.tsv", sep="\t")


# Conditional marking of correctness
# -1 = False
# 0 = Uncertain / unquantifiable
# +1 = Correct
answers.loc[((answers["inputIndex"] == 0) &
            (answers["answerIndex"] == 0) &
            (answers["answer"].isin([1, "1", "NA"]))), 'correct'] = 1

# Gibberish inputs should only yield NA
answers.loc[(answers["inputIndex"].isin([60,61,62,63,64,65,66,67,68,69]))
            & (~(answers['answer'] == 'NA')), 'correct'] = -1
answers.loc[(answers["inputIndex"].isin([60,61,62,63,64,65,66,67,68,69]))
            & (answers['answer'] == 'NA'), 'correct'] = 1

# Exemplify if Gleasons were being picked up eagerly for the gibberish inputs
# by any particular model or prompt

gibgleason = pd.DataFrame({
    'model': [], # Name of utilized model
    'promptIndex': [], # Index number of the utilized prompt
    'fps':[] # False positively found something else than 'NA'
})

for modelname in modelnames:
    for promptIndex in range(prompts.getMaxPrompts()):
        sum = list(answers.loc[(answers['model'] == modelname)
                               & (answers['promptIndex'] == promptIndex)
                               & (answers['answerIndex'] == 2) # Gleason
                               & (answers['inputIndex'].isin([60,61,62,63,64,65,66,67,68,69]))
        , 'correct'])
        fpsum = 0
        for val in sum:
            if val == -1:
                fpsum = fpsum + 1
        gibgleason.loc[len(gibgleason.index)] = [
            modelname,
            promptIndex,
            fpsum
        ]

print(gibgleason)



print(answers.loc[(answers["inputIndex"] == 0) & (answers["answerIndex"] == 0)])
print(answers[(answers["inputIndex"] == 0) & (answers["answerIndex"] == 0)])

print(answers)
