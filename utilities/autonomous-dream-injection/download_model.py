#!/usr/bin/env python3
"""
Automated model download for Autonomous Dream Injection Framework
Downloads Qwen2.5-7B-Instruct-Q5_K_M from HuggingFace
"""

from huggingface_hub import hf_hub_download
import os
import sys

MODEL_REPO = "bartowski/Qwen2.5-7B-Instruct-GGUF"
MODEL_FILE = "Qwen2.5-7B-Instruct-Q5_K_M.gguf"
LOCAL_DIR = "./model"

print("🔥 Autonomous Dream Injection - Model Downloader 🔥\n")
print(f"Repository: {MODEL_REPO}")
print(f"Model: {MODEL_FILE}")
print(f"Size: ~5.4GB\n")

# Set cache location
os.environ['HF_HOME'] = os.path.abspath('./hf_cache')

print("Creating directories...")
os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs('./hf_cache', exist_ok=True)

print("Downloading model (this may take 10-30 minutes)...\n")

try:
    hf_hub_download(
        repo_id=MODEL_REPO,
        filename=MODEL_FILE,
        local_dir=LOCAL_DIR
    )
    print("\n✅ Download complete!")
    print(f"Model saved to: {os.path.abspath(LOCAL_DIR)}/{MODEL_FILE}")
    print("\nReady to run:")
    print("  ./run_threaded.py")
    
except Exception as e:
    print(f"\n❌ Download failed: {e}")
    print("\nTroubleshooting:")
    print("1. Check internet connection")
    print("2. Verify HuggingFace is accessible")
    print("3. Ensure sufficient disk space (~6GB)")
    sys.exit(1)
