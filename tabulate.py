# Tabulate and collect results in a suitable format across all output files
import os
import re

import numpy

import prompts
import numpy as np

# Working directory for output files
os.chdir("D:\\Gits\\HistPath_LLMpy\\")

modelnames = ["gpt-3.5-turbo", "gpt-4-turbo", "gemini-1.0-pro-001", "meta/meta-llama-3-70b-instruct"]

output = np.chararray(
    shape=(
        # 3 repeats
        3,
        # Number of tested models
        len(modelnames),
        # Maximum number of run prompt variation wrapping the statement
        prompts.getMaxPrompts(),
        # Maximum number of statements
        prompts.getMaxInputs()
    ),
    itemsize=1000
)

# Iterate over models
for modelIndex in range(len(modelnames)):
    # Iterate over prompts
    for promptIndex in range(prompts.getMaxPrompts()):
        # Iterate over inputs
        for inputIndex in range(prompts.getMaxInputs()):
            # Iterate over replicates
            for rep in range(3):
                # Aggregate into a multidim array
                filename = ("out\\" + re.sub("meta/", "", modelnames[modelIndex]) + "_promptIndex"
                            + str(promptIndex) + "_inputIndex" + str(inputIndex) + "_rep" + str(rep) + ".out")
                print("Processing filename " + filename)
                if os.path.isfile(filename):
                    file = open(filename, 'r', encoding="utf-8")
                    lines = file.readlines()
                    start = 0
                    end = len(lines)
                    # Sanitize; extract {JSON} part from  ...```json {JSON} -- ```...
                    # or ... ``` {JSON} ```
                    for i in range(len(lines)):
                        if lines[i].strip() == "```json" or lines[i].strip() == "```":
                            start = i+1
                            break
                    # The ending to ``` sequence if one was detected; starting sequence from prior start point
                    for j in range(start, len(lines)):
                        if lines[j].strip() == "```":
                            end = j
                            break
                    # Grab the JSON part
                    lines = lines[start:end]
                    lines = "".join(lines).strip()
                    file.close()
                else:
                    lines = "Error; file not present or model call failed."
                print("-- Found content:\n" + lines + "\n--\n")
                print("Finished rep " + str(rep) + " modelIndex " + str(modelIndex) + " promptIndex "
                      + str(promptIndex) + " inputIndex " + str(inputIndex))

                output[rep, modelIndex, promptIndex, inputIndex] = lines.encode("utf-8")

print("\n\nExample output: \n")
print(output[0,0,0,0].decode("utf-8"))
print("\n\nDimensions and shape of output: \n")
print(str(output.ndim) + "\n")
print(str(output.shape) + "\n")

# Write out the 4-dim np char array as binary file
file = open("data\\output.npy", 'wb')
numpy.save(file=file, arr=output)
file.close()
