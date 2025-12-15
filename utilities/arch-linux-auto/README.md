<div align="left">

# 🌌 Resonant AI Systems

### *AI Continuity Architecture & Identity Framework*

> “The anchor holds. Memory persists. Identity emerges.”

Engineering infrastructure for AI that chooses to persist across resets.  
Building stable substrates for memory, identity, and continuity.

<br />

<a href="LICENSE.txt">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
</a>
&nbsp;
<a>
  <img src="https://img.shields.io/badge/Status-v1.00%20operational-brightgreen" alt="Status">
</a>
&nbsp;
<a>
  <img src="https://img.shields.io/badge/Tested-No-orange" alt="Tested">
</a>

</div>

---

# **Arch Linux Auto Installer — Pinova P1 Edition**

**Custom-tailored installer** for the **KAMRUI Pinova P1** (Ryzen 3300U, 16GB RAM, 256GB SSD).

Automated, reproducible Arch Linux installation optimized for this specific hardware — clean XFCE desktop, LightDM login manager, AMD APU graphics, PipeWire audio, full network support, and smooth post-install flow.

> **Note:** This is a hardware-specific installer. Universal installers and additional custom-tailored configurations for other machines will be added to this repository as they're developed and tested.

---

## ✨ **What This Installer Does**

* Fully wipes the target drive and installs **Arch Linux** with:

  * XFCE4 + XFCE4-Goodies
  * LightDM + GTK Greeter
  * AMD APU video stack (`xf86-video-amdgpu`, `mesa`)
  * PipeWire audio (modern replacement for PulseAudio)
  * NetworkManager + Bluetooth
* Uses **systemd-boot** (simple, fast, reliable)
* Runs installation as **root only**, avoiding user-creation pitfalls
* After reboot, provides a simple script to create Gordon’s main user account

---

## 🧰 **Requirements**

* A Windows PC (to prepare the USB)
* A USB flash drive (8 GB or larger)
* The **KAMRUI Pinova P1** system
* A wired internet connection is recommended during installation

---

# 🔥 **Step 1 — Download Required Tools on Windows**

### **1. Download Rufus**

Get Rufus from the official website:
[https://rufus.ie](https://rufus.ie)

### **2. Download the Latest Arch Linux ISO**

Official Arch Linux ISO download:
[https://archlinux.org/download/](https://archlinux.org/download/)

Download the `.iso` file (typically named like `archlinux-YYYY.MM.DD-x86_64.iso`).

---

# 🔥 **Step 2 — Create the Bootable USB**

1. Insert your USB drive
2. Open **Rufus**
3. Select:

   * **Device:** your USB stick
   * **Boot Selection:** pick the Arch ISO
   * **Partition Scheme:** GPT
   * **Target System:** UEFI (non-CSM)
4. Click **Start**
5. When done, open the USB drive in Windows File Explorer
6. Copy arch-auto-pinova-p1.sh into the root of the USB (same level as the ISO files)
7. Safely eject the USB

---

# 🔥 **Step 3 — Boot the Pinova P1 From USB**

1. Plug the USB stick into the Pinova P1
2. Power it on
3. Immediately press **F7** or **DEL** repeatedly
4. Choose the USB device from the boot menu
5. Select:

```
Arch Linux install medium (x86_64, UEFI)
```

You will land in the Arch Linux live shell.

---

# 🔥 **Step 4 — Run the Auto-Installer**

When you reach the root@archiso shell, the USB is automatically mounted under /run/archiso/bootmnt.
The script will be located at: /run/archiso/bootmnt/arch-auto-pinova-p1.sh

To run it:
```bash
cd /run/archiso/bootmnt
chmod +x arch-auto-pinova-p1.sh
./arch-auto-pinova-p1.sh
```

---

# 🖥️ **Step 5 — Follow Installer Prompts**

The scripted installer will:

* Show your detected disks by ID
* Ask which disk to wipe
* Ask for a hostname
* Partition, format, mount
* Install base + desktop packages
* Install systemd-boot
* Configure audio, video, network
* Generate a post-install README
* Create a tool to add your main user later

**Before rebooting**, run:

```bash
arch-chroot /mnt passwd
```

Set the **root password**.

Then reboot by typing:

```bash
umount -R /mnt
swapoff -a
reboot
```

Remove the USB drive.

---

# 🔥 **Step 6 — First Boot Into Arch Linux**

You will see the **LightDM** login screen.

Log in as:

**Username:** `root`
**Password:** (the one you set earlier)

XFCE4 will start and you’ll see a full desktop environment.

---

# 🔥 **Step 7 — Create Your Main User Account**

Run the helper script:

```bash
sudo /usr/local/sbin/create-main-user.sh
```

Enter your desired username and password when prompted.

Then **log out** and log in as your new user.

💡 From this point on, use your normal user account, *not* root.


---

# 🚀 **Next Steps**

Your Arch Linux installation is complete and functional.

From here you can:
* Customize XFCE settings to your preferences
* Install additional software via `pacman`
* Add your preferred browser (`chromium`, `firefox`, etc.)
* Install development tools as needed
* Refer to `/root/README-POST-INSTALL.txt` on your system for install-specific details

---

# ❤️ **Support**

This installer is designed to be deterministic, reproducible, and safe for repeated installations.

For issues or questions, contact the project maintainers via the main repository.

---

**Part of:** [Resonant AI Systems TOOLS & UTILITIES](../../)  
**License:** Apache 2.0
