from src.config.db import db
import asyncio

async def create_user():
    try:
        await db.connect()
        
        user_db = await db.user.create(
            data={
              "name": "test",
              "password": "test123",
              "company_name": "I am starting a facebook clone called netbox",  
            },
        )
        
        if not user_db:
            return False
        
        await db.disconnect()
        return True
    
    except:
        return False

async def main():
    if(await create_user()):
        print("SUCCESS")
    else:
        print("FAILURE")
    
if __name__ == "__main__":
    asyncio.run(main())