from aiohttp import web
from app.models import User
from app.validators import validate_username, validate_email, validate_street, validate_city, validate_username_max
from app.validators import AsyncValidator


async def create_user(request):
    # Ma'lumotlarni olish
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400)

    # Validatsiya qoidalarini yozamiz
    rules = {
        "username": [validate_username, validate_username_max],
        "email": validate_email,
        "street": validate_street,
        "city": validate_city
    }

    # Validatsiya jarayoni
    validator = AsyncValidator(data)
    try:
        validated_data = await validator.validate(rules)
    except ValueError as e:
        return web.json_response({"errors": e.args[0]}, status=400)

    # `validated_data`ni tekshirish
    if not validated_data:
        return web.json_response({"error": "Validated data is empty or invalid."}, status=400)

    # Foydalanuvchini saqlash
    try:
        user = await User.create(**validated_data)
        return web.json_response({"id": user.id, "message": "User created successfully!"}, status=201)
    except Exception as e:
        return web.json_response({"error": f"Failed to create user: {str(e)}"}, status=500)


# get data
async def get_user(request):
    data = await User.all()
    return web.json_response([user.to_dict() for user in data])

# Marshrutlarni ro'yxatga olish
def setup_routes(app):
    app.router.add_post("/users", create_user)
    app.router.add_post("/user", get_user)

