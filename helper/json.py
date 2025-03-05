import json

def convert_to_json(file):
    if file is not None:
        extrated_texts = []
        
        # 📌 Python List Comprehension ile JSON İçinden "text" Alanlarını Çekme
        
        # if "data" in file:
            # extrated_texts = [tweet["text"] for tweet in file["data"] if "text" in tweet]
        if "data" in extrated_texts:
            for tweet in file["data"]:
                if "text" in tweet:
                    extrated_texts.append(tweet["text"])
        
            
        with open('helper/data.json', 'w', encoding='utf-8') as f:
            json.dump(extrated_texts, f, ensure_ascii=False, indent=4)
        return True
    
    return False
    
    # status = json.loads(tweets_as_json)
    # print(status['status'], status)