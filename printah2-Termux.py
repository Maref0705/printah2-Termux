#printah2-Termux.py
import os, sys, time
os.system('clear')
def main (kata):
        for e in kata:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.2)
print ("""
\033[1;91m   _____ _____ ____  __  __ _   ___  __
  |_   _| ____|  _ \|  \/  | | | \ \/ /
    | | |  _| | |_) | |\/| | | | |\  / 
\033[1;37m    | | | |___|  _ <| |  | | |_| |/  \ 
    |_| |_____|_| \_\_|  |_|\___//_/\_\\
                \033[1;33mversi \033[1;92m9.9
""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
main("""
        \033[1;37mSelamat datang Gaess \033[1;92m>_

   \033[1;37mSemoga bermanfaat buat kalian \033[1;92m>_<

""")
print ("\033[1;91m[\033[1;37m=======================================\033[1;91m]")
nama = input('\033[1;34m( \033[1;33mSTAR \033[1;34m) \033[1;92m--> \033[1;91mEnter \033[1;92m: ')
time.sleep(3)
print ('\n')
main('  \033[1;92mLoading\033[1;37m....')
time.sleep(4)
os.system('clear')
print ("""
       \033[1;91m(\033[1;33mAuthor\033[1;91m) \033[1;92m: \033[1;37mM_aref

       \033[1;34m(\033[1;37mYoutub\033[1;34m) \033[1;92m: \033[1;33mThe-X-Cyber
""")
main("""
\033[1;37m======================================
pkg help 
untuk melihat opsi yang disediakan TERMUX pkg package manager
======================================
pkg search
untuk Mencari packages berdasar nama.
======================================
pkg install
untuk menginstall packages.
======================================
pkg uninstall
 untuk menghapus packages.
======================================
pkg reinstall
untuk mereinstall packages
======================================
pkg show
untuk menampilkan informasi detail tentang packages.
======================================
pkg list-installed 
untuk menampilkan daftar packages yang terinstall di termux mu.
======================================
pkg files
untuk melihat lokasi files packages diinstall
======================================
pkg list-all
untuk menampilkan semua package yang disediakan di repositori.
======================================
pkg upgrade 
untuk mengupdate dan upgrade package yang terinstall di termux mu
======================================
clear
Perintah dasar ini digunakan untuk membersihan jendela console
======================================
pwd
pwd (print working directory), digunakan untuk melihat posisis lokasi directory saat ini.
======================================
ls
digunakan untuk melihat /list file dan directory. gunakan ls -la untuk melihat informasi detail dari file dan folder
======================================
cd
Digunakan untuk nevigasi/pindah ke directory lain yang kita inginkan , gunakan cd .. untuk kebali ke 1 tingkat directory , gunakan cd ~ untuk menuju ke home directory
======================================
cp
Digunakan untuk mengkopi/nyalin File dan Folder .
cp -avr /folder-asal /folder-tujuan untuk mengkopi folder dan isinya
======================================
mv
Digunakan Untuk memindahkan file dan folder tau bisa digunakan untuk merename jika file /folder mempunyai asal dan tujuan yang sama
======================================
rm
Digunakan untuk menghapus File.
rm -rf namaFolder untuk menghapus folder dan isinya.
======================================
rmdir
Digunakan untuk menghapus Folder kosong .
rmdir --ignore-fail-on-non-empty namafolder untuk menghapus folder yang tidak kosong
======================================
chmod
Digunakan untuk mengubah File /folder permission/privilage.
chmod +x namaFolder untuk merubah permisin ke 775 atau rwx–x–x
======================================
chsh -s less
untuk Membuat termux logut sendiri atau exit sendiri
======================================
MENGINSTALL *.deb PACKAGES
dpkg -i ./nama_package.deb
======================================
UNINSTALL *.deb PACKAGES
dpkg --remove [nama package]
======================================
MELIHAT APLIKASI *.deb
dpkg -l
======================================
Karena dpkg mempunyai banyak opsi yang berguna, kamu bisa melihat manual via
$ man dpkg.
======================================
""")
time.sleep(4)
os.system("python3 printah2-Termux.py")
