adb reboot bootloader
fastboot oem hw dualsim false
fastboot erase modemst1 erase modemst2
fastboot oem config carrier $1
fastboot -w
fastboot erase frp
fastboot reboot