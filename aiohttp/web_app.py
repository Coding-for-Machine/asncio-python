from aiohttp import web
import asyncio

# Ma'lumotlarni saqlash uchun vaqtinchalik xotira
users = {}
user_id_counter = 1


# Foydalanuvchilarni ro'yxatdan o'tkazish (POST)
async def register_user(request):
    global user_id_counter
    data = await request.json()
    user_id = user_id_counter
    users[user_id] = {
        "id": user_id,
        "name": data.get("name"),
        "email": data.get("email")
    }
    user_id_counter += 1
    return web.json_response({"message": "User created", "user": users[user_id]}, status=201)


# Foydalanuvchilar ro'yxatini olish (GET)
async def list_users(request):
    return web.json_response({"users": list(users.values())}, status=200)


# Foydalanuvchini yangilash (PUT)
async def update_user(request):
    user_id = int(request.match_info["id"])
    if user_id not in users:
        return web.json_response({"error": "User not found"}, status=404)
    
    data = await request.json()
    users[user_id].update({
        "name": data.get("name", users[user_id]["name"]),
        "email": data.get("email", users[user_id]["email"])
    })
    return web.json_response({"message": "User updated", "user": users[user_id]}, status=200)


# Foydalanuvchini o'chirish (DELETE)
async def delete_user(request):
    user_id = int(request.match_info["id"])
    if user_id not in users:
        return web.json_response({"error": "User not found"}, status=404)
    
    del users[user_id]
    return web.json_response({"message": "User deleted"}, status=200)


# Asosiy serverni sozlash
async def init_app():
    app = web.Application()
    app.add_routes([
        web.post('/users', register_user),
        web.get('/users', list_users),
        web.put('/users/{id}', update_user),
        web.delete('/users/{id}', delete_user)
    ])
    return app


# Dastur ishga tushirish
if __name__ == "__main__":
    web.run_app(init_app())
