<div align="center">

# Resonant AI Systems TOOLS & UTILITIES

## ImageGen

### Built by Resonant AI Core
**Research & Development Division of Resonant AI Systems**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-production-brightgreen)
![Scope](https://img.shields.io/badge/scope-creative%20tool-purple)
![Division](https://img.shields.io/badge/division-Resonant%20AI%20Core-black)

**Local-first image generation on hardware you control.**

GPU-accelerated SDXL pipeline with ControlNet, IP-Adapter, and Real-ESRGAN upscaling. Built for professional creators requiring quality, speed, and complete privacy.
Not cloud API calls. Not usage quotas. **Full SDXL stack running locally.**

</div>

---

## WHAT THIS IS

ImageGen is a fully offline SDXL image generation system combining state-of-the-art diffusion models with professional upscaling.

**Core components:**
- SDXL models (Juggernaut XL v9 cinematic, RealVisXL V4 photorealistic)
- ControlNet integration (depth, canny edge detection, pose guidance)
- IP-Adapter for face and style consistency
- Real-ESRGAN 4K AI upscaling (tiled processing for VRAM efficiency)
- Gradio web interface with real-time generation monitoring

**Capabilities:**
- Batch generation with gallery view
- Dynamic model switching without restart
- Advanced prompt weighting and scheduling
- Automatic image preprocessing
- Production-ready 4K export

Designed for offline operation with zero telemetry. All processing local, no cloud dependencies.

---

## WHY IT EXISTS

Professional image generation requires control, consistency, and privacy. Cloud services impose usage limits, privacy concerns, and style restrictions. Running SDXL locally requires extensive configuration.

**Problem solved:**
Setting up SDXL with ControlNet, IP-Adapter, and upscaling involves manual model downloads, dependency management, VRAM optimization, and interface configuration. ImageGen automates the full pipeline.

**Use cases:**
- Character consistency across multiple images (IP-Adapter reference matching)
- Precise composition control (ControlNet pose/depth guidance)
- Style transfer and brand consistency
- Professional 4K output for print and production
- Offline creative workflows without cloud dependencies

Built for creators, studios, and researchers requiring full control over image generation infrastructure.

---

## FEATURES

### Core Generation
- **SDXL models** - Juggernaut XL v9 (cinematic), RealVisXL V4 (photorealistic)
- **Model switching** - Dynamic loading without restart
- **Batch generation** - 4-8 image variations with gallery view
- **Advanced prompting** - Weighted keywords, scheduling, negative prompts

### Precision Control
- **ControlNet** - Depth maps, canny edge detection, pose guidance
- **IP-Adapter** - Face/style consistency from reference images
- **Automatic preprocessing** - Image analysis and conditioning
- **Adjustable influence** - Strength controls for ControlNet and IP-Adapter

### Professional Output
- **Real-ESRGAN** - 4K AI upscaling with tile processing
- **Multiple methods** - LANCZOS (fast), Real-ESRGAN (quality)
- **Automatic models** - Downloads upscaling models on first run (~17MB)
- **Export options** - Production-ready 4K output

### Interface
- **Web-based** - Gradio interface on localhost:7860
- **Real-time monitoring** - System stats, VRAM usage, generation progress
- **Gallery view** - Review batch results, lock seeds
- **Preset management** - Save/load configuration profiles

---

## REQUIREMENTS

**Hardware:**
- NVIDIA RTX 3060+ (12GB+ VRAM recommended)
- 16GB+ system RAM
- 50GB free storage for models

**Software:**
- Linux (tested on Ubuntu 22.04+, Arch Linux)
- Python 3.13+
- CUDA support

**Models (auto-downloaded):**
- SDXL models (~6GB each)
- ControlNet models (~5GB)
- IP-Adapter models (~1.5GB)
- Real-ESRGAN models (~17MB)

---

## INSTALLATION

### Step 1: Clone Repository

```bash
git clone https://github.com/resonantaisystems/RAIS-Tools-and-Utilities.git
cd RAIS-Tools-and-Utilities/utilities/imagegen
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Run Automated Installer

```bash
chmod +x install_complete.sh
./install_complete.sh
```

**Installer handles:**
- PyTorch with CUDA support
- Diffusers, Transformers libraries
- ControlNet and IP-Adapter dependencies
- Real-ESRGAN upscaling libraries
- Gradio web interface

### Step 4: First Launch

```bash
python generate_gui.py
```

Open browser to [http://localhost:7860](http://localhost:7860)

**First run:**
- Real-ESRGAN model downloads automatically (~17MB)
- Interface loads with default settings
- SDXL models download on first generation request (~6GB)

---

## USAGE

### Basic Generation

1. **Launch interface**
   ```bash
   python generate_gui.py
   ```

2. **Enter prompt**
   - Positive prompt: Describe desired image
   - Negative prompt: Exclude unwanted elements
   - Use weighted keywords: `(keyword:1.2)` for emphasis

3. **Configure settings**
   - Model: Juggernaut XL v9 (cinematic) or RealVisXL V4 (photorealistic)
   - Resolution: 2K Standard (1920x1080) recommended
   - Steps: 35-45 for quality
   - Batch count: 4 images for variation testing

4. **Generate**
   - Click "Generate" button
   - Monitor progress in interface
   - Review batch results in gallery

### Professional Workflow

**Development Phase:**
1. Generate 4 variations at 1920x1080
2. Use LANCZOS upscaling for speed (2-3 seconds)
3. Review gallery, select best composition
4. Note seed value from best result

**Production Phase:**
1. Lock seed from best result
2. Refine prompt with sharpness/quality keywords
3. Enable Real-ESRGAN 4K upscaling
4. Generate 1-2 final images (6-8 seconds)
5. Export production-ready output

### ControlNet Usage

**Depth control:**
1. Upload reference image
2. Enable ControlNet Depth
3. Set strength 0.7-0.9
4. Generate with composition guidance

**Canny edge detection:**
1. Upload sketch or edge reference
2. Enable ControlNet Canny
3. Set strength 0.8-0.9
4. Generate precise line-guided image

### IP-Adapter Usage

**Face consistency:**
1. Upload reference portrait
2. Enable IP-Adapter
3. Set strength 0.6-0.7
4. Generate variations with consistent face

**Style transfer:**
1. Upload style reference
2. Enable IP-Adapter
3. Adjust strength for style influence
4. Generate images matching reference style

---

## STATUS & ROADMAP

**Current Status:** Production (v3.1)

ImageGen is stable and used in active production workflows. Generation pipeline optimized for RTX 30/40 series GPUs. Web interface responsive and feature-complete.

**Tested Environments:**
- Ubuntu 22.04 with RTX 3060 (12GB)
- Arch Linux with RTX 4090 (24GB)
- Python 3.13 with CUDA 11.8/12.1

**Known Limitations:**
- Linux only (Windows support possible but untested)
- NVIDIA GPUs only (AMD/Intel not supported)
- Requires 12GB+ VRAM for comfortable operation (8GB works with reduced batch sizes)
- First-run model downloads large (~20GB total)

**Performance Characteristics:**
- RTX 3060 (12GB): 5-7 seconds per image
- RTX 4090 (24GB): 3-4 seconds per image
- Real-ESRGAN upscaling: +2-3 seconds
- LANCZOS upscaling: +0.5 seconds

**Roadmap:**
- **SDXL Turbo support** - Sub-second generation with quality trade-offs
- **Additional ControlNet models** - OpenPose, Normal maps, Segmentation
- **Video generation** - AnimateDiff integration for motion
- **Inpainting/outpainting** - Selective editing and expansion
- **API mode** - REST API for automation and integration
- **Model fine-tuning** - LoRA training interface

**Maintenance:** Active. Updated when new SDXL models or ControlNet versions release.

---

## CONFIGURATION

### Generation Settings

**Models:**
- Juggernaut XL v9: Cinematic, artistic, vibrant colors
- RealVisXL V4: Photorealistic, detailed, accurate lighting

**Schedulers:**
- DPM++ 2M Karras (recommended, balanced)
- Euler A (fast, less detail)
- DDIM (slower, maximum quality)

**Resolution Presets:**
- 2K Standard: 1920x1080 (recommended)
- Ultrawide: 2560x1080 (cinematic)
- Fast Test: 1280x720 (development)

**Steps:**
- 20-30: Fast testing
- 35-45: Production quality (recommended)
- 50+: Diminishing returns

### Control Features

**ControlNet Strength:**
- 0.5-0.6: Subtle guidance
- 0.7-0.9: Strong composition control (recommended)
- 0.9-1.0: Maximum constraint (may reduce creativity)

**IP-Adapter Strength:**
- 0.3-0.5: Style hint
- 0.6-0.7: Face/style consistency (recommended)
- 0.8-1.0: Strong reference matching

### Performance Optimization

**VRAM Management:**
- Automatic pipeline offloading
- Dynamic model loading
- Tiled upscaling for large images

**Speed vs Quality:**
- Development: Fast scheduler, LANCZOS upscale, lower steps
- Production: Quality scheduler, Real-ESRGAN upscale, optimal steps

---

## TROUBLESHOOTING

### Out of Memory Errors

**Solution:**
- Reduce batch size (4 → 2 images)
- Lower resolution (1920x1080 → 1280x720)
- Disable ControlNet/IP-Adapter if not needed
- Use tiled Real-ESRGAN (automatic)

### Slow Generation

**Solution:**
- Verify CUDA installation: `python -c "import torch; print(torch.cuda.is_available())"`
- Check GPU utilization: `nvidia-smi`
- Reduce steps (45 → 35)
- Use LANCZOS upscaling instead of Real-ESRGAN

### Model Download Failures

**Solution:**
- Check internet connection (first run only)
- Verify HuggingFace access (no VPN conflicts)
- Manually download models to `models/` directory
- Re-run installer script

### Poor Image Quality

**Solution:**
- Increase steps (35 → 45)
- Refine prompts (add quality keywords: "highly detailed", "professional photography")
- Adjust negative prompts (add unwanted elements)
- Try different scheduler (DPM++ vs Euler)

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

*Part of the Resonant AI Systems public research toolkit. Built for professional image generation, local-first operation, and privacy-preserving creative workflows.*

---

## Additional Documentation

For advanced configuration, model customization, and development information, see [ADVANCED_README.md](ADVANCED_README.md).
