from transformers import pipeline

pipe = pipeline("image-text-to-text" , model="goggle/gemma-3-4b-it")


message = [
    {
        "role":"user",
        "content":[
            {"type":"image" , "url":"https://huggingface.co/datasets/huggingface/pet/resolve/main/1.jpg"},
            {"type":"text" , "text":"a cat"}
        ]
    }
]