# Inspect the outputs yourself

Start with [matched comparisons](COMPARE.md). They show the same input under the basic editing request and the general skill, including improvement, unchanged text, and a failure.

The pages below retain actual output wording. All fourteen models have a recorded editing example. Five also have complete fresh-generation-to-edit pairs. Gemini and Mistral's separate generation demonstrations exhausted their token allowances; those failures are visible. Stress-test inputs are ours, not purported examples of the named model's original writing.

The main run used frozen v1 instructions. Claude and ERNIE pages also show the v3 general prompt's smaller follow-up. The earlier v5 has a [two-model paragraph-removal pilot](../benchmark/paragraph-removal-pilot/README.md). [Latest marketing examples](../assets/examples/README.md) use the released instructions. Experimental family-arm outputs remain evidence, without a claim that a family edition is better. [Protocol and limits](../benchmark/README.md).

| Family | Requested model | Displayed stress-test arm | Outputs |
| --- | --- | --- | --- |
| GPT | `openai/gpt-6.1-sol` | general v1 | [Read source and outputs](gpt/README.md) |
| Claude | `anthropic/claude-sonnet-5.5` | general v1 | [Read source and outputs](claude/README.md) |
| Gemini | `google/gemini-3.8-flash` | general v1 | [Read source and outputs](gemini/README.md) |
| Grok | `x-ai/grok-4.7` | general v1 | [Read source and outputs](grok/README.md) |
| DeepSeek | `deepseek/deepseek-v4.1-flash` | general v1 | [Read source and outputs](deepseek/README.md) |
| Qwen | `qwen/qwen3.8-max-0902` | general v1 | [Read source and outputs](qwen/README.md) |
| Llama | `meta-llama/llama-4-maverick` | general v1 | [Read source and outputs](meta/README.md) |
| Mistral | `mistralai/mistral-medium-3-5` | family v1 | [Read source and outputs](mistral/README.md) |
| Gemma | `google/gemma-4-31b-it` | general v1 | [Read source and outputs](gemma/README.md) |
| Kimi | `moonshotai/kimi-k3` | general v1 | [Read source and outputs](kimi/README.md) |
| GLM | `z-ai/glm-5.3-flashx` | family v1 | [Read source and outputs](glm/README.md) |
| Command | `cohere/command-a-plus` | general v1 | [Read source and outputs](command/README.md) |
| ERNIE | `baidu/ernie-4.5-vl-424b-a47b` | general v1 | [Read source and outputs](ernie/README.md) |
| MiniMax | `minimax/minimax-m3` | general v1 | [Read source and outputs](minimax/README.md) |
