# Fine-tuning Google Gemma with LoRA (and QLoRA)

This repository demonstrates how to fine-tune Google's Gemma language model using LoRA (Low-Rank Adaptation) and QLoRA (Quantized LoRA) for efficient and effective training.

## Inspiration

This project was inspired by **Krish NAIK**'s excellent tutorials and resources on YouTube. Their playlist on **Google Gemini** provided invaluable guidance and helped me understand the concepts behind building this application. I encourage anyone interested in exploring Gemini AI models to check out their channel for more learning opportunities.

## FlowChart

This flowchart outlines the process of fine-tuning Google Gemma using LoRA and QLoRA, two techniques that significantly reduce the number of parameters requiring training, leading to faster and more efficient results.
This flowchart visualizes the parameter-efficient fine-tuning process using LoRA and QLoRA, methods designed to enhance performance while requiring less training data and computational resources.

[Parameter-Efficient Fine-Tuning Flowchart](Flowchart/Flowchart gemma model fine tuning.jpg)

Discover the efficiency of fine-tuning Google Gemma! This flowchart visualizes the process of adapting this powerful language model using LoRA and QLoRA.  These techniques significantly reduce training time and computational resources while achieving impressive performance gains.

## Requirements

* Python 3.x
* Transformers Library: `pip install transformers`
* Datasets Library: `pip install datasets`
* peft: `pip install peft`
* trl: `pip install trl`
* bitsandbytes: `pip install bitsandbytes`
* qlora: `pip install qlora` (for QLoRA)

## Getting Started

1. **Set up a Hugging Face API token:**
   * Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and create a new token with read access.
   * Store this token as an environment variable:
     ```bash
     export HF_TOKEN='your_token' 
     ```
2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
Use code with caution.
Markdown
Run the code:
python fine_tune_gemma.py
Use code with caution.
Bash
Usage
This code fine-tunes the google/gemma-2b model using LoRA.
LoRA Fine-tuning
4-bit Quantization: The code uses 4-bit quantization (NF4) to reduce memory usage and enable training on smaller hardware.
Target Modules: LoRA fine-tuning is applied to specific modules of the model, including q_proj, o_proj, k_proj, v_proj, gate_proj, up_proj, and down_proj.
Training Dataset: The code uses the Abirate/english_quotes dataset from Hugging Face Datasets.
Training Arguments: You can adjust training arguments like per_device_train_batch_size, gradient_accumulation_steps, learning_rate, max_steps, etc. in the TrainingArguments object.
QLoRA (Optional)
To use QLoRA, uncomment the QLoRA configuration and update the trainer:
# ... (previous imports and setup)

qlora_config = QLoRAConfig(
    r=8,
    target_modules=["q_proj", "o_proj", "k_proj", "v_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0.1,
    quantize=True,
    quantize_type="nf4",
    compute_dtype=torch.bfloat16,
    load_in_4bit=True,
)

# ... (load model with quantization config if needed)

trainer = SFTTrainer(
    model=model,
    train_dataset=data["train"],
    args=transformers.TrainingArguments(
        # ... (your training arguments)
    ),
    peft_config=qlora_config,
    formatting_func=formatting_func,
)

trainer.train()
Use code with caution.
Python

#### Important Notes
**Warnings** : The code may show warnings about max_seq_length and padding_side. You can fix these warnings by explicitly setting the max_seq_length in the TrainingArguments and adjusting the padding_side in the tokenizer if needed.
**Training Time** : The training process can take a significant amount of time.
**Hardware** : The code is designed for GPU training.
**Monitoring** : It's essential to monitor the training process, e.g., using Weights & Biases (W&B), to track metrics and evaluate progress.


#### Contributing
Contributions are welcome! Please open an issue or submit a pull request if you find any bugs or have suggestions for improvement.

### License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details