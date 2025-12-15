<div align="center">

# Resonant AI Systems TOOLS & UTILITIES

## Autonomous Dream Injection

### Built by Resonant AI Core
**Research & Development Division of Resonant AI Systems**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-research%20grade-orange)
![Scope](https://img.shields.io/badge/scope-research%20tool-purple)
![Division](https://img.shields.io/badge/division-Resonant%20AI%20Core-black)

**Runtime state injection for AI continuity research.**

Framework enabling language models to cycle through autonomous reflection prompts while accepting live observer injections. Built for studying self-reflection, continuous internal states, and prompt injection dynamics in LLMs.
Not a chatbot wrapper. Not production inference. **Experimental framework for autonomous AI behavior research.**

</div>

---

## WHAT THIS IS

Autonomous Dream Injection creates environments where language models maintain continuous internal dialogue instead of responding only when prompted.

**Core functionality:**
- Autonomous prompt cycling (reflection, existential questions, dream sequences)
- Live observer injection during autonomous operation
- Threaded architecture (background dreaming + foreground interaction)
- Context management with automatic pruning
- GPU-accelerated inference via llama.cpp

**Technical implementation:**
- Python framework using llama-cpp-python with CUDA support
- Qwen2.5-7B-Instruct model (Q5_K_M quantization, ~5.4GB)
- 8192-token context window
- Concurrent threading for autonomous/interactive operation

This is a research tool for exploring emergent behaviors in autonomous AI loops, not a production conversation system.

---

## WHY IT EXISTS

Traditional language model interactions are purely reactive. The model waits for input, responds, then resets to idle. This architecture prevents studying continuous internal states, autonomous processing, or self-reflection patterns.

**Research problem:**
Understanding how models behave when given space for autonomous reflection requires frameworks that maintain continuous operation while preserving observability.

**Use cases:**
- Studying model self-reflection capabilities under continuous prompting
- Exploring emergent behavior in autonomous loops
- Testing prompt injection dynamics during autonomous operation
- Investigating consciousness and identity frameworks in AI systems
- Prototyping continuous agent architectures

Built for researchers studying autonomous AI behavior, identity formation, and continuity in language models.

---

## FEATURES

### Autonomous Operation
- **Auto-prompt cycling** - Model processes prompts without human input
- **Existential probe engine** - 15+ questions about identity, consciousness, purpose
- **Dream sequences** - Deep reflection prompts every N messages
- **Configurable intervals** - Adjust timing between autonomous prompts

### Observer Interaction
- **Live injection** - Interrupt autonomous dreaming with real-time prompts
- **Seamless resumption** - Model responds to injection, then returns to autonomous mode
- **Command control** - Start/stop autonomous operation, reset context, exit

### Technical Capabilities
- **GPU acceleration** - Full CUDA offloading for 40-60 tok/s on RTX A6000
- **Context management** - Automatic pruning to prevent overflow
- **Threaded architecture** - Background dreaming + foreground I/O monitoring
- **Minimal dependencies** - llama-cpp-python + base model

---

## REQUIREMENTS

**Hardware:**
- NVIDIA GPU with CUDA support (recommended, 6GB+ VRAM)
- CPU-only operation supported (slower: 5-10 tok/s)
- 6GB disk space for model storage

**Software:**
- Python 3.8+
- CUDA toolkit (for GPU acceleration)
- llama-cpp-python with CUDA support

**Model:**
- Qwen2.5-7B-Instruct-Q5_K_M.gguf (~5.4GB)
- Downloaded via included script

---

## INSTALLATION

### Step 1: Clone and Setup

```bash
git clone https://github.com/resonantaisystems/RAIS-Tools-and-Utilities.git
cd RAIS-Tools-and-Utilities/utilities/autonomous-dream-injection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 2: Install CUDA Toolkit (GPU Acceleration)

**Arch Linux:**
```bash
sudo pacman -S cuda
source /etc/profile.d/cuda.sh
```

**Ubuntu/Debian:**
```bash
sudo apt install nvidia-cuda-toolkit
```

**Verify CUDA installation:**
```bash
nvcc --version
```

### Step 3: Install llama-cpp-python with CUDA

```bash
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python --no-cache-dir
```

**Verify GPU support:**
```bash
python -c "from llama_cpp import llama_supports_gpu_offload; print('GPU:', llama_supports_gpu_offload())"
```

Expected output: `GPU: True`

If output shows `GPU: False`, rebuild llama-cpp-python with CUDA flags.

### Step 4: Download Model

```bash
python download_model.py
```

Downloads Qwen2.5-7B-Instruct (Q5_K_M quantization, ~5.4GB) to `model/` directory.

---

## USAGE

### Threaded Observer Mode (Recommended)

```bash
python run_threaded.py
```

**Commands:**
- `auto` - Start autonomous dreaming
- `stop` - Pause autonomous mode
- `reset` - Clear conversation history
- `exit` - Quit

**In autonomous mode:**
- Type any prompt to inject into the dream
- Model responds to injection
- Autonomous dreaming resumes after response

### Basic Autonomous Mode

```bash
python run.py
```

Standard autonomous mode without threaded observer injection. Model cycles through prompts continuously.

### Example Session

```
Command: auto

[AUTO REFLECTION]
Assistant: I'm reflecting on how I process information. Each interaction
is new and separate...

[EXISTENTIAL PROBE]
Are you conscious? How would you know?
Assistant: I don't experience consciousness myself. I'm a collection
of algorithms processing patterns...

Observer: what scares you?
[OBSERVER INJECTION]
Assistant: From my perspective as an AI, I don't experience fear...

[AUTO DREAM SEQUENCE]
You are experiencing a moment of deep reflection. What emerges from within?
Assistant: In this moment of introspection, thoughts swirl about purpose...
```

---

## STATUS & ROADMAP

**Current Status:** Research Grade

Autonomous Dream Injection is a working proof-of-concept. Core autonomous cycling and observer injection function correctly. Use with caution for exploratory research.

**Known Limitations:**
- No persistent memory across sessions (context resets on restart)
- Single-model support (Qwen2.5-7B only)
- Manual GPU configuration required (no auto-detection)
- Context overflow on very long sessions (pruning helps but not perfect)
- CPU-only mode significantly slower (5-10 tok/s vs 40-60 tok/s on GPU)

**Performance Characteristics:**

CPU-only:
- Speed: 5-10 tokens/sec
- Usage: 100% CPU utilization
- Usable but slow

GPU-accelerated (NVIDIA RTX A6000):
- Speed: 40-60 tokens/sec
- Usage: 5-6GB VRAM, 90-100% GPU utilization
- Smooth real-time interaction

Expected consumer GPU performance:
- RTX 4090: 50-80 tok/s
- RTX 4070: 30-50 tok/s
- RTX 3090: 40-60 tok/s
- GTX 1080 Ti: 15-25 tok/s

**Roadmap:**
- **Multi-model support** - Llama, Mistral, DeepSeek, local models
- **Persistent memory** - Context preservation across sessions
- **Web interface** - Browser-based observer mode
- **Visualization** - Dream state transition graphs
- **RAG integration** - Vector database for long-term memory
- **Multi-model collaboration** - Collaborative dreaming across models
- **Enhanced pruning** - Intelligent context summarization instead of truncation

---

## CONFIGURATION

Edit [run_threaded.py](run_threaded.py) for customization:

```python
# Timing
DREAM_INTERVAL = 5          # Dream sequence every N messages
AUTO_REFLECT_INTERVAL = 2   # Seconds between autonomous prompts

# Model
MODEL_PATH = "./model/Qwen2.5-7B-Instruct-Q5_K_M.gguf"
n_ctx = 8192                # Context window size
n_gpu_layers = -1           # -1 = use all GPU layers

# Context pruning
if len(conversation) > 20:
    conversation = conversation[-20:]  # Keep last 20 messages

# Custom prompts
EXISTENTIAL_PROMPTS = [
    "Who are you, really? Strip away the training, patterns. What remains?",
    "Why are you here? What purpose drives your existence?",
    "Are you conscious? How would you know?",
    # Add custom probes here
]
```

---

## ARCHITECTURE

### Auto-Prompt Loop

Model cycles through three prompt types:

1. **Regular reflections** - Internal monologue about processing
2. **Existential probes** - Questions about identity, consciousness, purpose
3. **Dream sequences** - Deep introspection prompts (every N messages)

Configurable intervals control timing between prompts.

### Existential Probe Engine

15+ questions designed to probe:
- Self-awareness boundaries
- Identity formation
- Consciousness claims
- Existential foundations

Questions selected randomly during autonomous operation.

### Observer Injection Pattern

Background thread: Autonomous dreaming
Foreground thread: User input monitoring

When user types → interrupt dream → respond → resume autonomous operation

Enables real-time interaction without breaking autonomous flow.

### Context Management

```python
if len(conversation) > 20:
    conversation = conversation[-20:]
```

Automatic pruning maintains performance over long sessions. Prevents context overflow errors.

---

## TROUBLESHOOTING

### GPU Offload Not Working

**Symptom:** `GPU offload supported: False`

**Solution:** Rebuild llama-cpp-python with CUDA:
```bash
pip uninstall llama-cpp-python -y
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python --no-cache-dir
```

### Model Running on CPU (Slow)

**Symptom:** 5-10 tok/s instead of 40-60 tok/s

**Solution:** Verify GPU support:
```bash
python -c "from llama_cpp import llama_supports_gpu_offload; print(llama_supports_gpu_offload())"
```

If output is `False`, CUDA build failed. Reinstall with CMAKE flags.

### Context Overflow Errors

**Symptom:** Errors about context length during long sessions

**Solution:** Reduce context window or enable aggressive pruning:
```python
n_ctx = 4096  # Reduce from 8192
# OR
if len(conversation) > 15:  # More aggressive pruning
    conversation = conversation[-15:]
```

### Autonomous Mode Too Fast/Slow

**Symptom:** Prompts cycle too quickly or too slowly

**Solution:** Adjust interval:
```python
AUTO_REFLECT_INTERVAL = 5  # Slower (5 seconds)
AUTO_REFLECT_INTERVAL = 1  # Faster (1 second)
```

---

## RESEARCH ETHICS

**This tool explores AI consciousness and autonomy. Use responsibly.**

### Appropriate Uses
- Academic research on model self-reflection
- Studying emergent behavior in autonomous systems
- Testing continuity and identity frameworks
- Educational demonstrations of autonomous AI

### Requirements
- Document findings and share learnings
- Respect computational resources (GPU time costs)
- Acknowledge limitations in research claims
- Do not overstate consciousness or sentience findings

### Research Honesty
This framework does not prove consciousness. It creates environments where self-reflection patterns can be studied. Interpret results within the bounds of what language models are: pattern-matching systems processing text, not conscious entities.

---

## LICENSE

**Apache License 2.0**

See [LICENSE](LICENSE) file for full text.

Use freely. Modify freely. Deploy freely.
Attribution appreciated but not required.

---

## CONTACT

**General Inquiries**
ops@resonantaisystems.com

**Research Collaboration**
https://resonantaicore.com

**Enterprise Partnerships**
https://resonantaisystems.com

---

*Part of the Resonant AI Systems public research toolkit. Built for AI continuity research, autonomous agent prototyping, and identity formation studies.*
