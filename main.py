import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex


class UserProfileApp(App):
    def build(self):
        self.title = "Мой профиль"

        # Устанавливаем тёмный фон
        Window.clearcolor = get_color_from_hex('#121212')  # Тёмный фон

        # Главный layout с фоном
        main_layout = BoxLayout(orientation='vertical', padding=25, spacing=20)

        # Добавляем тёмный фон для main_layout
        with main_layout.canvas.before:
            Color(*get_color_from_hex('#121212'))  # Основной тёмный фон
            self.rect = Rectangle(size=main_layout.size, pos=main_layout.pos)

        # Заголовок в современном стиле
        title_label = Label(
            text="Мой Профиль",
            font_size='26sp',
            bold=True,
            size_hint_y=None,
            height=70,
            color=get_color_from_hex('#FFFFFF'),  # Белый текст
            text_size=(None, None),
            halign='center'
        )
        # Фон для заголовка
        with title_label.canvas.before:
            Color(*get_color_from_hex('#1E1E1E'))  # Чуть светлее основного
            Rectangle(size=title_label.size, pos=title_label.pos)

        main_layout.add_widget(title_label)

        # Контейнер для аватарки с тёмным фоном
        avatar_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=280,
            padding=20,
            spacing=15
        )
        with avatar_container.canvas.before:
            Color(*get_color_from_hex('#1E1E1E'))  # Тёмный фон контейнера
            Rectangle(size=avatar_container.size, pos=avatar_container.pos)

        # Аватарка
        self.avatar = Image(
            source='',
            size_hint=(None, None),
            size=(180, 180),
            pos_hint={'center_x': 0.5}
        )
        avatar_container.add_widget(self.avatar)

        # Текст под аватаркой
        avatar_text = Label(
            text="Нажми 'Сменить аватарку'\nчтобы добавить фото",
            font_size='14sp',
            size_hint_y=None,
            height=50,
            color=get_color_from_hex('#888888'),  # Серый текст
            text_size=(None, None),
            halign='center'
        )
        avatar_container.add_widget(avatar_text)
        main_layout.add_widget(avatar_container)

        # Кнопка смены аватарки в современном стиле
        change_btn = Button(
            text='Сменить аватарку',
            size_hint=(None, None),
            size=(220, 50),
            pos_hint={'center_x': 0.5},
            background_color=get_color_from_hex('#BB86FC'),  # Фиолетовый акцент
            background_normal='',
            color=get_color_from_hex('#000000'),  # Чёрный текст
            font_size='16sp',
            bold=True
        )
        change_btn.bind(on_press=self.change_avatar)
        main_layout.add_widget(change_btn)

        # Контейнер для информации с тёмным фоном
        info_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=200,
            padding=20,
            spacing=12
        )
        with info_container.canvas.before:
            Color(*get_color_from_hex('#1E1E1E'))  # Тёмный фон
            Rectangle(size=info_container.size, pos=info_container.pos)

        # Информация о пользователе
        self.name_label = Label(
            text='[b]Имя:[/b] Софья',
            font_size='18sp',
            markup=True,
            color=get_color_from_hex('#FFFFFF'),  # Белый текст
            text_size=(None, None),
            halign='left'
        )
        info_container.add_widget(self.name_label)

        self.age_label = Label(
            text='[b]Возраст:[/b] 18 лет',
            font_size='16sp',
            markup=True,
            color=get_color_from_hex('#E0E0E0'),  # Светло-серый
            text_size=(None, None),
            halign='left'
        )
        info_container.add_widget(self.age_label)

        self.city_label = Label(
            text='[b]Город:[/b] Москва',
            font_size='16sp',
            markup=True,
            color=get_color_from_hex('#E0E0E0'),  # Светло-серый
            text_size=(None, None),
            halign='left'
        )
        info_container.add_widget(self.city_label)

        main_layout.add_widget(info_container)

        # Кнопка обновления информации
        update_btn = Button(
            text='Обновить информацию',
            size_hint=(None, None),
            size=(220, 50),
            pos_hint={'center_x': 0.5},
            background_color=get_color_from_hex('#03DAC6'),  # Бирюзовый акцент
            background_normal='',
            color=get_color_from_hex('#000000'),  # Чёрный текст
            font_size='16sp',
            bold=True
        )
        update_btn.bind(on_press=self.update_info)
        main_layout.add_widget(update_btn)

        return main_layout

    def change_avatar(self, instance):
        """Открывает стандартный диалог Windows для выбора файла"""
        try:
            from tkinter import filedialog, Tk
            root = Tk()
            root.withdraw()  # Скрываем главное окно
            root.attributes('-topmost', True)  # Поверх всех окон

            file_path = filedialog.askopenfilename(
                title="Выберите аватарку",
                filetypes=[
                    ("Изображения", "*.png *.jpg *.jpeg *.bmp *.gif"),
                    ("Все файлы", "*.*")
                ]
            )

            if file_path:
                # Проверяем расширение файла
                valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
                file_ext = os.path.splitext(file_path)[1].lower()

                if file_ext in valid_extensions:
                    self.avatar.source = file_path
                    self.avatar.color = (1, 1, 1, 1)
                    self.show_message("Успех!", "Аватарка загружена! 🎉")
                else:
                    self.show_message("Ошибка", "Выберите файл изображения\n(PNG, JPG, BMP, GIF)")

            root.destroy()

        except Exception as e:
            self.show_message("Ошибка", f"Не удалось открыть диалог выбора файла")

    def update_info(self, instance):
        """Обновляет информацию о пользователе"""
        self.name_label.text = '[b]Имя:[/b] Софья '
        self.age_label.text = '[b]Возраст:[/b] 19 год ✨'
        self.city_label.text = '[b]Город:[/b] Санкт-Петербург '
        self.show_message("Успех!", "Информация обновлена!")

    def show_message(self, title, message):
        """Простой вариант с белым фоном и чёрным текстом"""
        content = BoxLayout(orientation='vertical', spacing=15, padding=20)

        # Белый фон для контраста
        with content.canvas.before:
            Color(1, 1, 1, 1)  # Белый фон
            Rectangle(size=content.size, pos=content.pos)

        # Текст сообщения
        message_label = Label(
            text=message,
            color=get_color_from_hex('#FFFFFF'),  # Чёрный текст
            font_size='16sp',
            bold=True,
            text_size=(None, None),
            halign='center'
        )
        content.add_widget(message_label)

        # Кнопка OK
        ok_btn = Button(
            text='OK',
            size_hint_y=0.4,
            background_color=get_color_from_hex('#BB86FC'),
            background_normal='',
            color=get_color_from_hex('#FFFFFF'),
            bold=True
        )
        content.add_widget(ok_btn)

        # Используем стандартный белый фон попапа
        popup = Popup(
            title=title,  # Без цвета - будет чёрный на белом
            title_size='18sp',
            content=content,
            size_hint=(0.5, 0.3)
            # Убираем background='' чтобы использовать стандартный фон
        )

        ok_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    UserProfileApp().run()