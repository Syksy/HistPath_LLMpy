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

# Working directory for project taken from env vars
os.chdir(os.environ.get("ROOT") + "out\\")

for rep in range(3):  # Run multiple repeats of the same setup to assess determinism
    for modelname in ["meta/meta-llama-3-70b-instruct"]:
        for promptIndex in range(prompts.getMaxPrompts()):
            for inputIndex in range(prompts.getMaxInputs()):
                filename = "" + re.sub("meta/", "", modelname) + "_promptIndex" + str(promptIndex) \
                             + "_inputIndex" + str(inputIndex) + "_rep" + str(rep) + ".out"
                # Run only if the existing output file doesn't exist yet
                if not os.path.isfile(os.path.realpath(filename)):
                    print("Model name " + modelname + " prompt index " + str(promptIndex) + " input index "
                      + str(inputIndex) + " repeat " + str(rep) + "\n")
                    print("Provided input: " + prompts.getInput(inputIndex) + "\n")
                    prompt = prompts.getPrompt(promptIndex, inputIndex)
                    input = {
                        "prompt": prompt,
                        "temperature": 0.0
                    }
                    # Write output to a suitable file
                    f = open(filename, 'w', encoding="utf-8")
                    for iterator in replicate.run(
                            modelname,
                            input=input
                    ):
                        print("".join(iterator), end="", file=f)
                    f.close()
                    print("\n\n")
                    time.sleep(2)
