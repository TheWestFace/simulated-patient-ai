<div align="center"> <h2><b> SimPatient AI </b></h2> </div> 

# Overview

A Python-based interactive system that simulates patients for mental health clinician training.  
Users can speak to AI-simulated patients with specific mental health conditions (e.g., depression), and the AI responds naturally with audio output.

## Repo Structure

```
simulated-patient-ai/
├── src/
    ├── audio/                                # Handles all audio functionality
        ├── record.py/                          # records user speech
        ├── speech_to_test.py/                  # converts audio to text
        ├── text_to_speech.py/                  # converts AI text to audio
    ├── patient/                              # Core AI patient simulation
        ├── gemini_config.py/                   # configuration for gemini genai
        ├── simulator.py/                       # patient simulator
        ├── test_patient.py/                    # testing patient and gemini call
    ├── prompts/                              # Stores prompts for patient personas
        ├── depression.txt/                     
    ├── main.py/                              # SimPatient Interface
├── README.md
├── environmental.yml
```

## Getting Started

1. **Create the Conda Environment**
    ```
    conda env create -f environment.yml
    ```

2. **Activate the Environment**
    ```
    conda activate patient-ai
    ```

3. **Set Up Environment Variables**
   Create a `.env` file at the root of the project and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the Simulation**
    ```
    python src/main.py
    ```
    - Press *ENTER* to start talking to the simulated patient.
    - Type *Q* and press *ENTER* anytime to quit.