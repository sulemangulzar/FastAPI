import sqlite3
from schemas import TaskCreate

class Database():

    def connect_to_db(self):
        self.connection = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                priority TEXT,
                status TEXT
            )""")
        self.connection.commit()
        
    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM task")
        results = self.cursor.fetchall()

        if not results:
            return []

        tasks = []
        for row in results:
            tasks.append({
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "priority": row[3],
                "status": row[4] or "Not Completed",  # ✅ avoid None error
        })

        return tasks
    
    def create_task(self, task : TaskCreate):
        self.cursor.execute("""
            INSERT INTO task (title, description, priority, status)
            VALUES (:title, :description, :priority, :status)
                            """,{
                                **task.model_dump(),
                            })
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_task(self, id : int):
        self.cursor.execute("""
                SELECT * FROM task WHERE id = ?
                            """, (id,))
        result = self.cursor.fetchone()
        
        if result is None:
            return None
        
        return {
            "id" : result[0],
            "title" : result[1],
            "description" : result[2],
            "priority" : result[3],
            "status" : result[4],
        }
        
    def update_status(self,status : str, id : int):
        self.cursor.execute("""
            UPDATE task
            SET status = ?
            WHERE id = ?
                            """,(status, id))
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    
    def delete_task(self, id : int):
        self.cursor.execute("""
                DELETE FROM task WHERE id = ?            
                            """, (id,))
        self.connection.commit()
        return self.cursor.rowcount > 0
        
    
    def close(self):
        self.connection.close()
    
    def __enter__(self):
        self.connect_to_db()
        self.create_table()
        return self
    
    def __exit__(self, *args):
        self.close()
        return self