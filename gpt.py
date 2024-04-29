# GPT-4 API access
import os
import openai
import time
from openai import OpenAI
import prompts

# API key load
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Working directory
os.chdir("D:\\Gits\\HistPath_LLMpy\\out\\")

# Try-catch some of the most common errors
try:
    for rep in range(3): # Run multiple repeats of the same setup to assess determinism
        for modelname in ["gpt-4-turbo", "gpt-3.5-turbo"]:
            for promptIndex in range(prompts.getMaxPrompts()):
                for inputIndex in range(prompts.getMaxInputs()):
                    print("Model name " + modelname + " prompt index " + str(promptIndex) + " input index "
                        + str(inputIndex) + " repeat " + str(rep) + "\n")
                    prompt = prompts.getPrompt(promptIndex, inputIndex)
                    # Run the actual prompt itself
                    response = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": prompt,
                            }
                        ],
                        model=modelname,
                        response_format={"type": "json_object"},
                        temperature=0.0
                    )
                    # Write output to a suitable file
                    f = open("" + modelname + "_promptIndex" + str(promptIndex) + "_inputIndex" + str(inputIndex)
                             + "_rep" + str(rep) + ".out", 'w')
                    print(response.choices[0].message.content, file=f)
                    f.close()
                    print("\n\n")
                    time.sleep(2) # Sleep 2 seconds
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
