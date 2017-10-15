
import os
import time

# List of voice options available in Say command
Female_Voices = ['Ava', 'Allison', 'Vicki', 'Victoria']

Male_Voices = ['Alex', 'Bruce']

Novelty_Voices = ['Bad News', 'Trinoids']

all_voices = Female_Voices + Male_Voices + Novelty_Voices


for voice in all_voices:
    time.sleep(1)
    print("Voice is "+voice)
    os.system("say -v "+voice+" you win!!!!")