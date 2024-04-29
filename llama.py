# Running LLama 3 on Replicate
# https://replicate.com/blog/run-llama-3-with-an-api

# Replicate
import replicate

import os
import time
import prompts
import re

# API key load
from dotenv import load_dotenv
load_dotenv()

# Working directory
os.chdir("D:\\Gits\\HistPath_LLMpy\\out\\")

for rep in range(3):  # Run multiple repeats of the same setup to assess determinism
    for modelname in ["meta/meta-llama-3-70b-instruct"]:
        for promptIndex in range(prompts.getMaxPrompts()):
        #for promptIndex in range(3,4,1):
            for inputIndex in range(prompts.getMaxInputs()):
                print("Model name " + modelname + " prompt index " + str(promptIndex) + " input index "
                      + str(inputIndex) + " repeat " + str(rep) + "\n")
                print("Provided input: " + prompts.getInput(inputIndex) + "\n")
                prompt = prompts.getPrompt(promptIndex, inputIndex)
                input = {
                    "prompt": prompt,
                    "temperature": 0.0
                }
                output = replicate.run(modelname, input=input)
                # Write output to a suitable file
                f = open("" + re.sub("meta/", "", modelname) + "_promptIndex" + str(promptIndex)
                         + "_inputIndex" + str(inputIndex) + "_rep" + str(rep) + ".out", 'w')
                print("".join(output), file=f)
                f.close()
                print("\n\n")
                time.sleep(2)
