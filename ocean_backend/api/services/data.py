def handle_uploaded_file(f):
    with open("api/services/name.xlsx", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)