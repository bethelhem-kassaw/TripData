from flask import Flask , request, jsonify
import asyncio
from insert_to_db import insert_group
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')


# Define the Telethon client
client = TelegramClient('Travel', api_id, api_hash)

# Define the asynchronous function for login
async def login(phone, password, code):
    try:
        await client.start()
    except SessionPasswordNeededError:
        await client.start(phone=lambda: phone, password=lambda: password, code=lambda: code)



async def login(phone):
    try:
        await client.start(phone=lambda: phone)
    except SessionPasswordNeededError:
        pass  # Do nothing as we'll handle password in the next step

async def enter_password(password, code):
    try:
        await client.start(password=lambda: password, code=lambda: code)
    except Exception as e:
        return str(e)


async def scapeGroupData(name):
    async with client:
        # Fetch the entity using the group identifier
        entity = await client.get_entity(name)
        
        # Extract and return the desired information
        group_info = {
            "name": entity.title,
            "tgname": entity.username,
            "members_count": entity.participants_count,
            
        }
        return group_info

@app.route('/login', methods=['POST'])
def login_api():
    data = request.json
    phone = data.get('phone')

    # Step 1: Login with phone number
    asyncio.run(login(phone))
    
    # Step 2: Enter password and code
    password = data.get('password')
    code = data.get('code')
    error = asyncio.run(enter_password(password, code))

    if error:
        return jsonify({"message": f"Login failed: {error}"}), 401
    else:
        return jsonify({"message": "Login successful."})
    

# 
@app.route('/addGroup', methods=['POST'])
async def addgroup():
    data = request.json
    name = data.get('name')
    info = await scapeGroupData(name)
    print(info)
    insert_group(info['name'], info['tgname'], info['members_count'], "Null")
    
    return jsonify({"message": "Group added successfully."})


if __name__ == '__main__':
    app.run(debug=True)
    