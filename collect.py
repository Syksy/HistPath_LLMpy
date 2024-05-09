# Collect and process results
import os
import numpy as np
import prompts
import json
import re
import funcs
import pandas as pd
from IPython.display import display, HTML

# Working directory for project
os.chdir("D:\\Gits\\HistPath_LLMpy\\")

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
