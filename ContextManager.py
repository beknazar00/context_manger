# import psycopg2


# db_params = {
#     'database': 'lesson',
#     'user': 'postgres',
#     'password': '1',
#     'host': 'localhost',
#     'port': '5432'
# }
       
# class DBConnect:
#     def __init__(self,db_params):
#         self.db_params = db_params

#     def __enter__(self):
#         self.conn = psycopg2.connect(**db_params)
#         return self.conn, self.cur
    
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         if self.conn:
#             self.conn.close()

# with DBConnect(db_params) as conn:
#     cursor = conn.cursor()
#     select_query = ''' selct * from book; '''
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     print(rows)

#     def create(cls, title, author):
#         next_id = cls.get_next_id()
#         new_book = cls(next_id, title, author)
#         with open(cls.db_file, 'a') as file:
#             file.write(f"{new_book.id},{new_book.title},{new_book.author}\n")
        
#         return new_book
    
#     def read(cls, book_id):
#         with open(cls.db_file, 'r') as file:
#             for line in file:
#                 id, title, author = line.strip().split(',')
#                 if int(id) == book_id:
#                     return cls(int(id), title, author)
        
#         return None