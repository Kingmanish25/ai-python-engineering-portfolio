def retrieve_context(vector_db, query):

    docs = vector_db.similarity_search(query, k=4)

    return docs
