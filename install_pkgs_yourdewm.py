import os

project_dir = os.path.dirname(os.path.abspath(__file__))
dm_file = os.path.join(project_dir, "displaymanager.txt")

packages_list = [
    "base",
    "base-devel",
    "linux",
    "linux-firmware",
    "linux-headers",
    "nano",
    "vim",
    "xorg",
    "konsole",
    "bash-completion",
    "grub",
    "efibootmgr",
    "ttf-ubuntu-font-family",
    "ttf-hack",
    "ttf-dejavu",
    "ttf-opensans",
    "firefox",
    "fastfetch",
    "networkmanager",
]

print(f"There is a list of base packages: {packages_list}")
print(" \n \n")
name_of_display_manager = input("What display-manager(sddm, lxdm) do you want?(type name): ").lower()
user_pkgs = input("Do you want to add some packages? (empty if no) (write with spaces): ")  # example neofetch i3-wm
user_de_wm = input("What DE/WM do you want?: ")
try:
    gpu_is_nvidia = int(input("Is your GPU from Nvidia?(1 - yes, 2 - no): "))
    if gpu_is_nvidia not in [1, 2]:
        print("Invalid input, using default (no NVIDIA drivers)")
        gpu_is_nvidia = 2
except ValueError:
    print("Invalid input, using default (no NVIDIA drivers)")
    gpu_is_nvidia = 2


if gpu_is_nvidia == 1: #если gpu от nvidia, то добавляем драйвера. if gpu from Nvidia, we need to add drivers
    packages_list.extend(["nvidia", "nvidia-utils"])

#сама команда. Command
command = "pacstrap /mnt " + " ".join(packages_list)
command = command + " " + name_of_display_manager
command = command + " " + user_pkgs
command = command + " " + user_de_wm

confirm_command = input(f"Are you sure to start this command?(yes/no): {command}")  #checking, Are user want to execute command.
if confirm_command.lower() == "no":
    print("((( Canceling the command")
    exit()
else:
    #writing user's DM in file for genfstab, arch_chroot_new.py
    with open(dm_file, "w",) as f:
        f.write(name_of_display_manager)
        print(f"Wrote {name_of_display_manager} in displaymanager.txt")

    #выполняем команду. Execute command
    print("Выполняется команда:", command)
    os.system(command)
    print("Yay!")