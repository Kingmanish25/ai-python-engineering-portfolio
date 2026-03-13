def filter_documents(docs, year=None, doc_type=None):

    filtered = []

    for d in docs:

        if year and d.metadata.get("year") != year:
            continue

        if doc_type and d.metadata.get("type") != doc_type:
            continue

        filtered.append(d)

    return filtered
