from datetime import datetime

def sample_response(input_text):
    user_message= str(input_text).lower()

    if user_message in ("hello","hi","sup",):
        return "Hey Buddy! How can I help You?"
    if user_message in ("who are you","who are you?"):
        return "I am Elthra!I can able to answer some questions related to machine learning"
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    if user_message in ("what is machine learning", "machine learning","what is machine learning?"):
        return "Machine learning (ML) is a type of artificial intelligence (AI) that allows software applications to become more accurate at predicting outcomes without being explicitly programmed to do so."
    if user_message in ("types?","types","types of machine learning"):
        return "supervised, unsupervised, and reinforcement learning."
    if user_message in ("examples","examples?"):
        return "1. Hey Siri · 2. Yelp's Photo Classifier · 3. Facebook · 4. Twitter · 5. Google Maps · 6. Pinterest . etc..."
    if user_message in ("dataset","where can i get the dataset?","where can i get the dataset"):
        return "Kaggle,UCI Machine Learning Repository,Datasets via AWS,Google's Dataset Search Engine."
    if user_message in ("Advantages","advantages"):
        return "It is automatic.It is used in various fields.It can handle varieties of data."
    if user_message in ("Disadvantages", "disadvantages"):
        return "Chances of error or fault are more.Data requirement is more.Time-consuming and more resources required."
    if user_message in ("Imporatnce","importance"):
        return "Machine Learning is a subfield of Artificial Intelligence. From predicting the spread of the COVID-19 virus to supporting cutting-edge cancer research, AI & ML can disrupt and transform every single segment of society. Naturally, it is hard to imagine a future without machine learning in our lives today."
    if user_message in ("Thank you","thanks","thank you"):
        return "you are always welcome."
    return "I don't understand you."
