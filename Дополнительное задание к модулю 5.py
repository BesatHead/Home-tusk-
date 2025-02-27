import time
import hashlib

class User:

    def __init__ (self, nickname, password, age):
        self.name = None
        self.nickname = nickname
        # self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        self.age = age

    def __hash__(self):
        return hash((self.age, self.name))

    def __str__ (self):
        return f"В данный момент активный пользователь: {self.nickname}"

class Video:

    def __init__ (self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:

    def __init__ (self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in (self, nickname, password):
        password_hash = int (hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                return
        print ("Неверный логин или пароль")

    def register (self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print (f"Пользователь {nickname} уже существует")
                return

        new_user = User (nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print (f"Пользователь {nickname} успешно зарегистрирован")

    def log_out (self):
        self.current_user = None

    def add (self, *videos):
        for video in videos:
            if not any (v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos (self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print ("Войдите в аккаунт, чтобы смотреть видео")
            return

        video_found = None
        for video in self.videos:
            if video.title == title:
                video_found = video
                break

        if video_found is None:
            return

        if video_found.adult_mode and self.current_user.age < 18:
            print ("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for i in range (video_found.time_now, video_found.duration):
            print (f"Просмотр секунды: {i+1}")
            time.sleep(0.5)  # Время просмотра
        video_found.time_now = 0
        print ("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

        # Добавление видео

ur.add(v1, v2)

        # Проверка поиска

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

        # Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

        # Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print (ur.current_user)

        # Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')