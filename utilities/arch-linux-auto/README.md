<div align="center">

# Resonant AI Systems TOOLS & UTILITIES

## Arch Linux Auto Installer

### Built by Resonant AI Core
**Research & Development Division of Resonant AI Systems**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-production-brightgreen)
![Scope](https://img.shields.io/badge/scope-infrastructure%20tool-purple)
![Division](https://img.shields.io/badge/division-Resonant%20AI%20Core-black)

**Hardware-specific system deployment for reproducible infrastructure.**

Automated Arch Linux installer optimized for specific hardware configurations. Ships installations from bare metal to functional desktop without manual intervention.
Not a universal installer. Not a GUI wizard. **Hardware-tailored scripts for deterministic deployments.**

</div>

---

## WHAT THIS IS

A collection of hardware-specific Arch Linux installation scripts that automate the full deployment pipeline: partitioning, base system installation, desktop environment configuration, bootloader setup, and post-install tooling.

**Current configurations:**
- **Pinova P1 Edition** - KAMRUI Pinova P1 (Ryzen 3300U, 16GB RAM, 256GB SSD)

Each configuration handles:
- Full disk partitioning and formatting
- Base Arch Linux installation with optimized package selection
- Desktop environment (XFCE4 + LightDM)
- Hardware-specific driver stack (AMD APU, PipeWire audio)
- Network and Bluetooth configuration
- systemd-boot bootloader
- Post-install user creation tooling

This is infrastructure-as-code for bare metal. Wipes the target drive, installs a clean system, produces a reproducible result every time.

---

## WHY IT EXISTS

Manual Arch Linux installations are powerful but time-consuming. Scripted installers exist but often aim for universal compatibility, sacrificing optimization for specific hardware.

This approach prioritizes **hardware-specific optimization** over portability. Each script is tailored to exact hardware specifications, ensuring drivers, firmware, and configurations match the target system perfectly.

**Use cases:**
- Lab environments requiring identical system configurations
- Research infrastructure with specific hardware deployments
- Personal machines where reproducible reinstallation matters
- Testing environments that need clean-slate redeployments

Built for operators who control their hardware and need deterministic system deployments.

---

## FEATURES

### Core Capabilities
- **Fully automated installation** - Boot USB, run script, reboot to functional desktop
- **Hardware-tailored configurations** - Driver selection, firmware, and optimizations for specific machines
- **Deterministic results** - Same script, same hardware, identical installation every time
- **Production-ready defaults** - XFCE desktop, modern audio (PipeWire), full network support

### Safety Features
- **Explicit disk targeting** - Script prompts for target disk, no blind overwrites
- **Pre-install confirmation** - Review selections before destructive operations
- **Post-install documentation** - System-specific README generated with installation details

### Post-Install Tools
- **User creation helper** - Script to create main user account after root login
- **Package manifest** - Full list of installed packages for audit/reproduction
- **Configuration summary** - Hostname, timezone, locale settings documented

---

## REQUIREMENTS

**Hardware:**
- Target system matching an available configuration (currently: KAMRUI Pinova P1)
- 8GB+ USB flash drive for installation media

**Preparation Environment:**
- Windows PC (for USB creation with Rufus)
- Internet connection (for downloading Arch ISO and installer script)

**Installation Environment:**
- Wired internet connection (recommended for package downloads during install)
- UEFI-capable system (legacy BIOS not supported)

---

## INSTALLATION

### Step 1: Prepare Installation Media (Windows)

1. **Download required files**
   - [Rufus](https://rufus.ie) - USB creation tool
   - [Arch Linux ISO](https://archlinux.org/download/) - Latest x86_64 image
   - Installer script for your hardware (from this repository)

2. **Create bootable USB with Rufus**
   - Insert USB drive
   - Open Rufus
   - Select USB device
   - Choose Arch Linux ISO
   - Partition scheme: GPT
   - Target system: UEFI (non-CSM)
   - Click Start

3. **Add installer script to USB**
   - Open USB drive in File Explorer after Rufus completes
   - Copy `arch-auto-pinova-p1.sh` (or relevant script) to USB root
   - Safely eject USB

### Step 2: Boot Target System

1. Insert USB into target machine
2. Power on and enter boot menu (typically F7 or DEL key)
3. Select USB device
4. Choose "Arch Linux install medium (x86_64, UEFI)"
5. Wait for live environment shell

### Step 3: Run Installer

In the live environment shell:

```bash
cd /run/archiso/bootmnt
chmod +x arch-auto-pinova-p1.sh
./arch-auto-pinova-p1.sh
```

Follow prompts:
- Select target disk from detected devices
- Enter hostname for the system
- Confirm configuration

Script handles:
- Disk partitioning (GPT, EFI system partition, root, swap)
- Base system installation
- Package installation (desktop, drivers, utilities)
- Bootloader configuration
- Initial system configuration

### Step 4: Set Root Password

Before rebooting:

```bash
arch-chroot /mnt passwd
```

Set a secure root password.

### Step 5: Reboot

```bash
umount -R /mnt
swapoff -a
reboot
```

Remove USB drive during reboot.

### Step 6: First Boot

1. System boots to LightDM login screen
2. Log in as `root` with password set in Step 4
3. XFCE desktop loads

### Step 7: Create User Account

From the XFCE terminal:

```bash
sudo /usr/local/sbin/create-main-user.sh
```

Enter username and password when prompted.

Log out and log back in as the new user. From this point, use the user account (not root) for normal operations.

---

## USAGE

### Creating a New Hardware Configuration

To add support for different hardware:

1. Copy existing script (e.g., `arch-auto-pinova-p1.sh`)
2. Rename for new hardware (e.g., `arch-auto-framework13.sh`)
3. Modify driver packages:
   - Video drivers (Intel, NVIDIA, AMD)
   - Network firmware
   - Hardware-specific utilities
4. Adjust partition sizes if needed
5. Test thoroughly on target hardware
6. Document hardware specifications in script comments

### Reinstalling a System

The installer is idempotent for the target disk. To reinstall:

1. Boot from USB (same process as initial install)
2. Run installer script
3. Select same disk
4. Script wipes and reinstalls cleanly

Previous data is destroyed. Backup user data before reinstalling.

### Customizing Installations

Modify the script before copying to USB:
- Package selection (add/remove packages in pacstrap command)
- Desktop environment (replace XFCE with KDE, GNOME, etc.)
- Partition sizes (adjust in fdisk commands)
- Locale/timezone (modify configuration section)

Scripts are designed for readability. Customization is encouraged.

---

## STATUS & ROADMAP

**Current Status:** Production

The Pinova P1 installer is battle-tested across multiple installations. Produces stable, functional systems. No known critical issues.

**Supported Hardware:**
- KAMRUI Pinova P1 (Ryzen 3300U, 16GB RAM, 256GB SSD)

**Known Limitations:**
- UEFI-only (no legacy BIOS support)
- Single-disk installations (multi-disk configurations require manual partitioning)
- Wired internet required during installation (offline installation not supported)

**Roadmap:**
- **Additional hardware profiles** - Framework Laptop 13, ThinkPad T series, System76 machines
- **Offline installation support** - Package cache bundled on USB for no-internet deployments
- **Alternative desktops** - Variants for KDE Plasma, GNOME, minimal WM setups
- **Post-install customization scripts** - Automated dotfile deployment, application installation

**Maintenance:** Active. Updated when Arch packaging changes break installations.

---

## TROUBLESHOOTING

### Installer Fails to Detect Disks
- Verify UEFI mode (not legacy BIOS) in firmware settings
- Check USB boot method selected "UEFI" variant in boot menu
- Try different USB port (USB 3.0 sometimes causes issues, use 2.0)

### Package Download Failures
- Confirm wired internet connection active
- Test with `ping archlinux.org` in live environment
- Check firewall/network configuration if on restricted network

### System Won't Boot After Install
- Verify root password was set before reboot
- Check UEFI boot order in firmware (Arch entry should be first)
- Boot USB again and verify systemd-boot installation in EFI partition

### Display Issues After First Boot
- AMD APU driver assumes AMDGPU support (confirm hardware match)
- Check `/var/log/Xorg.0.log` for errors
- For non-AMD hardware, modify script to install appropriate video drivers

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

*Part of the Resonant AI Systems public research toolkit. Built for reproducible infrastructure, local-first deployment, and operator-controlled systems.*
