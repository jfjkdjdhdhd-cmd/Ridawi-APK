from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

import os
import io
import contextlib


Window.clearcolor = (0.02, 0.02, 0.04, 1)


class IraqCodeStudioSUPREME(App):

    def build(self):

        self.file = "/storage/emulated/0/Iraq_Code_SUPREME.py"

        root = BoxLayout(
            orientation="vertical",
            padding=8,
            spacing=8
        )

        title = Label(
            text="🇮🇶 Iraq Code Studio SUPREME\n👑 إدارة: رضا",
            font_size=26,
            size_hint_y=0.15
        )

        menu = BoxLayout(
            size_hint_y=0.12,
            spacing=5
        )

        run = Button(text="▶️ تشغيل")
        save = Button(text="💾 حفظ")
        open_btn = Button(text="📂 فتح")
        files = Button(text="📁 ملفات")
        examples = Button(text="📚 أمثلة")

        menu.add_widget(run)
        menu.add_widget(save)
        menu.add_widget(open_btn)
        menu.add_widget(files)
        menu.add_widget(examples)


        self.editor = TextInput(
            text="# Python\nprint('مرحبا في SUPREME 👑')",
            font_size=18,
            multiline=True,
            background_color=(0.05,0.05,0.08,1),
            foreground_color=(1,1,1,1)
        )


        self.console = Label(
            text="🖥️ الطرفية جاهزة",
            font_size=18,
            size_hint_y=0.2
        )


        run.bind(on_press=self.run_code)
        save.bind(on_press=self.save_code)
        open_btn.bind(on_press=self.open_code)
        files.bind(on_press=self.show_files)
        examples.bind(on_press=self.example_code)


        root.add_widget(title)
        root.add_widget(menu)
        root.add_widget(self.editor)
        root.add_widget(self.console)

        return root



    def run_code(self, x):

        output = io.StringIO()

        try:
            with contextlib.redirect_stdout(output):
                exec(self.editor.text)

            self.console.text = output.getvalue() or "✅ تم التشغيل"

        except Exception as e:
            self.console.text = "❌ خطأ:\n" + str(e)



    def save_code(self, x):

        with open(self.file, "w", encoding="utf-8") as f:
            f.write(self.editor.text)

        self.console.text = "💾 تم الحفظ"



    def open_code(self, x):

        if os.path.exists(self.file):

            with open(self.file, "r", encoding="utf-8") as f:
                self.editor.text = f.read()

            self.console.text = "📂 تم الفتح"

        else:
            self.console.text = "⚠️ الملف غير موجود"



    def show_files(self, x):

        try:
            files = os.listdir("/storage/emulated/0")

            self.console.text = (
                "📁 الملفات:\n" +
                "\n".join(files[:15])
            )

        except Exception as e:
            self.console.text = str(e)



    def example_code(self, x):

        self.editor.text = (
            "# مثال Python\n\n"
            "name='رضا'\n"
            "print('اهلا '+name)"
        )

        self.console.text = "📚 تم تحميل المثال"



IraqCodeStudioSUPREME().run()
