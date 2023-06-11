#!/usr/bin/env python
# coding: utf-8

# In[1]:


elemen = []


def create():
  if len(elemen) >= 4:
    print("Batas maksimum elemen tercapai.")
  else:
    for i in range(4):
      item = input("Masukkan Elemen baru: ")
      elemen.append(item)
    print("Data telah ditambahkan.")

def read():
  if not elemen:
    print("Tidak ada elemen yang tersedia.")
  else:
    print("Data yang tersimpan:")
    for item in elemen:
      print(item)

def update():
  if not elemen:
    print("Tidak ada elemen yang tersedia.")
  else:
    print("Data yang tersimpan:")
    for index, item in enumerate(elemen):
      print(f"{index+1}. {item}")

    choice = input("Pilih nomor elemen yang akan diubah: ")
    if choice.isdigit() and int(choice) <= len(elemen):
      new_item = input("Masukkan Elemen baru: ")
      elemen[int(choice) - 1] = new_item
      print("Data berhasil diubah.")
    else:
      print("Nomor elemen tidak valid.")


def delete():
  if not elemen:
    print("Tidak ada elemen yang tersedia.")
  else:
    print("Data yang tersimpan:")
    for index, item in enumerate(elemen):
      print(f"{index+1}. {item}")

    choice = input("Pilih nomor elemen yang akan dihapus: ")
    if choice.isdigit() and int(choice) <= len(elemen):
      del elemen[int(choice) - 1]
      print("Data berhasil dihapus.")
    else:
      print("Nomor elemen tidak valid.")


def display_menu():
  print("=======================")
  print("=== Program Elemen ====")
  print("=======================")
  print("1. Insert Elemen")
  print("2. Show Elemen")
  print("3. Update Elemen")
  print("4. Delete Elemen")
  print("5. Exit")
  print("\n")


def main():
  while True:
    display_menu()
    choice = input("Pilih menu (1-5): ")

    if choice == '1':
      create()
      print("\n")
    elif choice == '2':
      read()
      print("\n")
    elif choice == '3':
      update()
      print("\n")
    elif choice == '4':
      delete()
      print("\n")
    elif choice == '5':
      print("Terima kasih! Program selesai.")
      break
    else:
      print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")


if __name__ == '__main__':
  main()


# In[ ]:




