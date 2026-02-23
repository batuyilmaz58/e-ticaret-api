def get_error_message(e):
    if hasattr(e, 'detail'):
        if isinstance(e.detail, list):
            return str(e.detail[0])    
        elif isinstance(e.detail, dict):
            # values() içindeki ilk elemanı al ama karakterine bölme!
            first_value = next(iter(e.detail.values()))
            # Eğer değer bir liste ise (Django hata mesajları genelde listedir) ilk elemanını al
            if isinstance(first_value, list):
                return str(first_value[0])
            return str(first_value)
        else:
            return str(e.detail)
        
    return str(e)