from src.config.db import db
import src.global_vars

async def login_func(username:str, password:str):
    try:
        await db.connect()
        
        user_db = await db.user.find_first(
            where={
                "name": username,
            },
        )
        
        if not user_db:
            return False
        
        if password != user_db.password:
            return False
        
        await db.disconnect()
        
        src.global_vars.loggedInUser = username
        src.global_vars.loggedInUserCompany = user_db.company_name
        
        return True
    
    except:
        return False