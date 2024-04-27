# Google Gemini API access
# Refs
# EU does not allow Gemini API, has to be done inside Google Cloud via Vertex AI
# Below is the code used there-in
# First needed in the cloud shell:
# pip3 install "google-cloud-aiplatform>=1.38"

import os
import vertexai
import prompts
import time
from vertexai.generative_models import GenerativeModel, GenerationConfig, HarmCategory, HarmBlockThreshold, FinishReason

vertexai.init(project="speedy-carver-421111", location="europe-north1")
generation_config = GenerationConfig(
    temperature=0.0
)
# Harm blocks appear as a severe hindrance in gemini-1.0-pro-002 but not gemini-1.0-pro-001;
# Falling back to the later release
safety_settings = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE
#    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
#    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
#    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
#    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH
}

# Working directory
os.chdir("~/out/")

try:
    for modelname in ["gemini-1.0-pro-001"]:
        model = GenerativeModel(modelname)
        for promptIndex in range(prompts.getMaxPrompts()):
            for inputIndex in range(prompts.getMaxInputs()):
                print("Model name " + modelname + " prompt index " + str(promptIndex) + " input index " + str(inputIndex) + "\n")
                retries = 1
                while True:
                    prompt = prompts.getPrompt(promptIndex, inputIndex)
                    response = model.generate_content(
                        prompt,
                        generation_config=generation_config,
                        safety_settings=safety_settings,
                        stream=False
                    )
                    # A lot of prompts are getting caught in the safety blocks even when they've been set to NONE? Try iterate
                    # FinishReason.STOP is the response to a run through
                    if response.candidates[0].finish_reason == FinishReason.STOP:
                        break
                    # Run failed, retrying
                    # Appears to be an issue particularly in gemini-1.0-pro-002 ... fallback to older release
                    # even with safety_settings put in
                    else:
                        retries = retries + 1
                        print("Retrying, caught in harm filters likely FinishReason.OTHER...")
                        time.sleep(11)
                f = open("" + modelname + "_promptIndex" + str(promptIndex) + "_inputIndex" + str(inputIndex) + ".out",
                         'w')
                print(response.text, file=f)
                f.close()
                print("\n\n")
                time.sleep(11)
except ValueError as e:
    print("Error: " + e)
