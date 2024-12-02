import requests
import json

# Bosh URL (mahalliy server yoki boshqa manzil)
BASE_URL = "http://127.0.0.1:8080"

# Foydalanuvchilarni boshqaruvchi sinf
class UserManager:
    def __init__(self, base_url):
        self.base_url = base_url

    # GET: Barcha foydalanuvchilarni olish
    def get_users(self):
        response = requests.get(f"{self.base_url}/users")
        if response.status_code == 200:
            print("Foydalanuvchilar ro'yxati:")
            print(json.dumps(response.json(), indent=4))
        else:
            print(f"Xatolik ({response.status_code}): {response.text}")

    # POST: Yangi foydalanuvchi yaratish
    def create_user(self, name, email):
        data = {"name": name, "email": email}
        response = requests.post(f"{self.base_url}/users", json=data)
        if response.status_code == 201:
            print("Yangi foydalanuvchi qo'shildi:")
            print(json.dumps(response.json(), indent=4))
        else:
            print(f"Xatolik ({response.status_code}): {response.text}")

    # PUT: Foydalanuvchini yangilash
    def update_user(self, user_id, name=None, email=None):
        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email
        response = requests.put(f"{self.base_url}/users/{user_id}", json=data)
        if response.status_code == 200:
            print("Foydalanuvchi yangilandi:")
            print(json.dumps(response.json(), indent=4))
        else:
            print(f"Xatolik ({response.status_code}): {response.text}")

    # DELETE: Foydalanuvchini o'chirish
    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        if response.status_code == 200:
            print("Foydalanuvchi o'chirildi.")
        else:
            print(f"Xatolik ({response.status_code}): {response.text}")


# Asosiy menyu funksiyasi
def main():
    manager = UserManager(BASE_URL)

    while True:
        print("\nTanlovni bajaring:")
        print("1. Foydalanuvchilarni ko'rish")
        print("2. Yangi foydalanuvchi qo'shish")
        print("3. Foydalanuvchini yangilash")
        print("4. Foydalanuvchini o'chirish")
        print("5. Chiqish")

        choice = input("Tanlov: ")
        if choice == "1":
            manager.get_users()
        elif choice == "2":
            name = input("Foydalanuvchi ismi: ")
            email = input("Foydalanuvchi email: ")
            manager.create_user(name, email)
        elif choice == "3":
            user_id = int(input("Foydalanuvchi ID: "))
            name = input("Yangi ism (bo'sh qoldirsa, o'zgarmaydi): ")
            email = input("Yangi email (bo'sh qoldirsa, o'zgarmaydi): ")
            manager.update_user(user_id, name=name if name else None, email=email if email else None)
        elif choice == "4":
            user_id = int(input("O'chiriladigan foydalanuvchi ID: "))
            manager.delete_user(user_id)
        elif choice == "5":
            print("Chiqmoqda...")
            break
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()
