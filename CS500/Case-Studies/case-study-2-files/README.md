Build Raspberry Pi
============
This github addresses these problems:
- provide some instructions, build and environmental contents so you can  start building your Raspberry Pi kernels and modules
- solves the case studies of the CS500 class.

*Note: The content of this repository is based on the materials and instructions taught in module [CS500-SVUCA](http://class.svuca.edu/~sau/class/CS500/), taught by professor Jerry Shiao.*

Prerequisites
-------------
- **Hardware**:
  - **Raspberry Pi**: You should have a Raspberry Pi and a SD memory card (or microSD for RPI v2). I'm using RPi v1 (model B) for testing. In theory, this should work for RPi v1 model A, or RPi v2.
  - Optionally, you can get a **WIFI USB dongle** so you can ssh into your RPI wirelessly. I'm using the nano Wifi dongle called Edimax EW-7811Un (I will also provide instructions to compile this module into your RPI kernel)
- **Software**:
  - **Kernel Source**: I've included kernel source v3.12 (folder `kernel-3.12`) in this repository.
    - Optionally, I've included the driver source from Realtek website for the Edimax EW-7811Un Wifi USB Dongle (`8192cu`)
  - **Kernel Config file**: file `dot_config`.
  - **Build tools**: folder `tools`
  - **Build environment setup**: file `envSetup.bash`
  - Build OS: I'm using Ubuntu to cross compile the RPI kernel and modules. I'm suggesting you to use Ubuntu and have these packages installed before hand: `sudo apt-get build-essential gcc-arm-linux-gnueabi lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6 bc`

Prepare your RPI SD Card
--------------
  * Download the Raspbian Wheezy 2014-12-24 ([direct link](http://director.downloads.raspberrypi.org/raspbian/images/raspbian-2014-12-25/2014-12-24-wheezy-raspbian.zip), or  [torrent](http://downloads.raspberrypi.org/raspbian/images/raspbian-2014-12-25/2014-12-24-wheezy-raspbian.zip.torrent)) and `unzip 2014-12-24-wheezy-raspbian.zip`
  * `dd` the wheezy Raspbian image to your SD Card: `sudo dd bs=4M if=2014-12-24-wheezy-raspbian.img |pv|sudo dd of=/dev/sdb` (Note: `/dev/sdb` is where my SDCard located, you can find out about yours by `sudo fdisk -l`)


Compile your RPI Kernel
--------------
  Assuming you already clone this repository and currently at top directory.

  1. Prepare your compile environment

       * Edit file `envSetup.bash` and change `BUILD_RPI_DIR` to the folder where you clone the repository into. (i.e. this folder contains file `dot_config`, folder `kernel-3.12`, `tools`, etc.)
       * `chmod u+x envSetup.bash`
       * `source envSetup.bash`

  2. Prepare your kernel config file

    * Copy the dot_config file into kernel folder: `cp dot_config kernel-3.12/.config`
    * `chmod u+w kernel-3.12/.config`
    * [CS500 Student only] Edit `.config` file, search for `CONFIG_LOCALVERSION`, add your student ID such as this example: `CONFIG_LOCALVERSION=”-150200300-CS500Linux”`

  3. Compile the Raspberry Pi Kernel

    * Switch to kernel directory: `cd kernel-3.12`
    * Remove old Kernel Image before compiling:
      * `rm arch/arm/boot/Image`
      * `make clean` - *Notes: if you are building modules, **do not execute this statement**, it will **reset module drivers** (if you are just building your pure kernel, go ahead with this statement)*
      * `make ARCH=arm CROSS_COMPILE=$CCPREFIX`
    * After compilation, the Kernel image, file `Image`, is placed in `kernel-3.12/arch/arm/boot` directory. Make sure the date is current and the size is around 6.44 Mbytes.

  4. Copy kernel file to the SD Card

    * Plugin your SD card and mount your SD Card into Ubuntu, example:
      * create a local mount point `mkdir sd`
      * mount: `sudo mount -t auto /dev/sdb1 sd`)
    * Copy the `Image` file produced in step (3) to the SD Card and rename to `kernel.img` (overwrite existing `kernel.img` file before you do this)

Now you can boot up your RPI with the SD Card and to check if this is the kernel you've built: `uname -a`, it should show your student ID configured in `CONFIG_LOCALVERSION` in step (2).

Compile your RPI Modules
--------------
In this section, I'm giving an example of compiling the popular `Realtek 8192cu` chip driver used in many USB WIFI Dongle (Edimax EW-7811un, GMYLE Wireless N/G, ...)

  * Load environment variables in main folder: `source envSetup.bash`
  * Switch to module build directory: `cd ${BUILD_RPI_DIR}/ext-modules/RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911/driver/rtl8188C_8192C_usb_linux_v4.0.2_9000.20130911`
  * Edit `include/autoconf.h`
    * Find this line `#define DBG     0`
    * Comment off all lines below that line, for example `//#define CONFIG_DEBUG_RTL819X`
    * basically, we do not want any debugging feature ON.
  * execute `make ARCH=arm CROSS_COMPILE=$CCPREFIX -C ${BUILD_RPI_DIR}/kernel-3.12/ modules`
  * Once done, your driver object files should have be copied to the drivers directory of the kernel 3.12, you can verify the modified date `ls -ls ${BUILD_RPI_DIR}/kernel-3.12/drivers/net/wireless/rtl8192cu/`
  * Now you just need to repeat steps in "Compile your RPI Kernel" (except `make clean`) and copy new kernel (`Image` file) into the SD Card as per instructions above.
  * To verify if wlan0 is loaded, in RPI, execute `ifconfig -a`. If you found wlan0 listed, it means the driver has been compiled correctly.
