import os

packages_list = [
    "base",
    "base-devel",
    "linux",
    "linux-firmware",
    "linux-headers",
    "nano",
    "vim",
    "xorg",
    "gnome",
    "gnome-extra"
    "konsole",
    "bash-completion",
    "grub",
    "efibootmgr",
    "ttf-ubuntu-font-family",
    "ttf-hack",
    "ttf-dejavu",
    "ttf-opensans",
    "firefox"
    "fastfetch"
]

gpu_is_nvidia = int(input("Is your GPU from Nvidia?(1 - yes, 2 - no): "))
name_of_display_manager = input("What display-manager(sddm, lxdm) do you want?(type name): ")

if gpu_is_nvidia == 1: #если gpu от nvidia, то добавляем драйвера.
    packages_list.extend(["nvidia", "nvidia-utils"])

#сама команда
command = "pacstrap /mnt " + " ".join(packages_list)
command = command + " " + name_of_display_manager

#выполняем команду
print("Выполняется команда:", command)
os.system(command)