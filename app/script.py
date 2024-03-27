from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

file_path = '..'
model_path = f'{file_path}/model/checkpoint-625'

model = AutoModelForCausalLM.from_pretrained(
    model_path, device_map = 'auto')

tokenizer = AutoTokenizer.from_pretrained(
    model_path)

text_generator = pipeline(
    task='text-generation',
    model=model,
    tokenizer=tokenizer,
    device_map = 'auto',
    # Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
    pad_token_id = tokenizer.eos_token_id
)

def format_prompt(instruction):
    return f"""
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:


### Output:
""".strip()

	

def generate_text(instruction, max_length, temperature):
    generated_text = text_generator(format_prompt(instruction),
                                    max_length = max_length,
                                    temperature = temperature)
    generated_text = generated_text[0]['generated_text']
    generated_output = generated_text.split('### Output:\n')[-1]
    return generated_output