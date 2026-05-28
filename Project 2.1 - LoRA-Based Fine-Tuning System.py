from transformers import AutoModelForCausalLM

model_id = "your-target-LLM-identifier"

# Fix: Explicitly load the weights into memory first
base_model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

model = get_peft_model(base_model, lora_config)
