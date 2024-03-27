# Supervised Fine-Tuned DistilGPT2

## Overview

Welcome to the Supervised Fine-Tuned DistilGPT2 Demo App! This web-based application demonstrates the basic functionality of a text generation model, allowing users to input a prompt and retrieve the generated text based on the prompt, max length of output text, and temperature.

## Features

- **Prompt:** User can enter a prompt in the provided prompt section.
- **Max output length:** User can choose the maximum length of generated text. The generated text length will be close to the selected number but never exceeds.
- **Temperature:** User can select temperature from 0.01 to 1 for the text generation. The higher temperature will be more likely to produce a more creative and unpredictable outputs.
- **Submit Button:** User click submit after inputing the prompt. The model will generate the text based on the prompt, max output length, and temperature.
- **Generated Text:** A text will be generated and shown next to the submit button.
- **Dataset:** The pretrained model is [DistilGPT2 model](https://huggingface.co/distilbert/distilgpt2) fine tuned with [Alpaca Dataset](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json).

### Prerequisites

- Ensure you have Python installed

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/thassung/SFT-DistilGPT2.git
   ```

2. Install the required Python dependencies:

   ```bash
   pip install flask torch peft==0.7.1 trl==0.7.4 transformers==4.36.2 pydantic==1.10.9 datasets==2.18.0
   ```

3. Navigate to the app directoty:
   ```bash
   cd SFT-DistilGPT2/app
   ```

4. Start the flask application:
   ```bash
   python main.py
   ```

   You can access the application via http://localhost:8080

The aplication should look like this.


